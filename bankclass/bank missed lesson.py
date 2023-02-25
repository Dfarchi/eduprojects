import psycopg2
from flask import Flask, request, jsonify

app = Flask("bank_web_app")

# bank REST api
# get /customers
# get /customers/id

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="bankfun",
    user="postgres",
    password="morbella12")


# @app.route("/api/v1/customers/<int:customer_id>", methods=['GET'])
# def get_customer(customer_id):
#     print(f"called /customers/customer_id/{customer_id}")
#     with conn:
#         with conn.cursor() as cur:
#             sql = "SELECT * FROM customers WHERE id = %s"
#             cur.execute(sql, (customer_id,))
#             result = cur.fetchone()
#             if result:
#                 ret_data = {
#                     'id': result[0],
#                     'passport_num': result[1],
#                     'name': result[2],
#                     'address': result[3]
#                 }
#                 # option I
#                 response = app.response_class(
#                     response=json.dumps(ret_data),
#                     status=200,
#                     mimetype='application/json'
#                 )
#                 return response
#
#                 # option II
#                 # return jsonify(ret_data)
#             else:
#                 return app.response_class(
#                     status=404
#                 )

# @app.route("/api/v1/customers/<int:passport_num>", methods=['GET'])
# def get_customer_by_pass(passport_num):
#     print(f"called /customers/passport_num/{passport_num}")
#     with conn:
#         with conn.cursor() as cur:
#             sql = "SELECT * FROM passport_num WHERE id = %s"
#             cur.execute(sql, (passport_num,))
#             result = cur.fetchone()
#             if result:
#                 ret_data = {
#                     'id': result[0],
#                     'passport_num': result[1],
#                     'name': result[2],
#                     'address': result[3]
#                 }
#                 # option I
#                 # response = app.response_class(
#                 #     response=json.dumps(ret_data),
#                 #     status=200,
#                 #     mimetype='application/json'
#                 # )
#                 # return response
#
#                 # option II
#                 return jsonify(ret_data)
#             else:
#                 return app.response_class(
#                     status=404
#                 )
#
# @app.route("/api/v1/customers/<int:customer_id>", methods=['PUT'])
# def update_customer(customer_id):
#     new_data = request.form
#     updates_str_list = []
#     for field in new_data:
#         updates_str_list.append(f"{field}={new_data[field]}")
#     sql = f"UPDATE customers SET {','.join(updates_str_list)} WHERE id=%s"
#     with conn:
#         with conn.cursor() as cur:
#             cur.execute(sql, tuple(new_data.keys()) + tuple([customer_id]))
#             if cur.rowcount == 1:
#                 # update succeeded
#                 return app.response_class(status=200)
#     return app.response_class(status=500)

# @app.route("/customers", methods=['GET'])
# def get_customers():
#     return 'get customers'


# running from commandline or code
# debugging
@app.route('/api/v1/customers', methods=['GET', 'POST'])
def get_all_customers_wet():
    if request.method == 'GET':
        results_per_page = request.args.get('rpp') or 20
        page_num = request.args.get('page') or 0
        passport_num = request.args.get('passportnum')
        acc_name = request.args.get('acc_name')
        acc_address = request.args.get('acc_address')

        try:
            page_num, results_per_page = int(page_num), int(results_per_page)
            if page_num < 0 or results_per_page < 0:
                return jsonify({'Error': 'page num and results per page must be positive'}), 404
        except ValueError:
            return jsonify({'Error': 'page num and results per page must be integers'}), 404

        query = "SELECT customers.id, customers.passportnum, acc_address, acc_name, account_num FROM customers " \
                "LEFT JOIN cus_acc ON customers.id = cus_acc.id"

        conditions = list()
        params = list()

        if request.args.get('passportnum'):
            conditions.append("passportnum::text ILIKE %s")
            params.append(f"%{passport_num}%")

        if request.args.get('acc_name'):
            conditions.append("acc_name ILIKE %s")
            params.append(f"%{acc_name}%")

        if request.args.get('acc_address'):
            conditions.append("acc_address ILIKE %s")
            params.append(f"%{acc_address}%")

        offset = page_num * results_per_page - results_per_page if page_num != 0 else 0
        limit = results_per_page

        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += f" LIMIT {limit} OFFSET {offset}"

        with conn:
            with conn.cursor() as curs:
                curs.execute(query, params)
                result = curs.fetchall()
                if result:
                    ret_data = dict()
                    for item in result:
                        if item[1] not in ret_data:
                            ret_data[item[1]] = {
                                "customers id": item[0],
                                "passport": item[1],
                                "address": item[2],
                                "name": item[3],
                                "accounts number": [item[4]]
                            }
                        else:
                            ret_data[item[1]]['account_id'].append(item[4])

                    ret_data = {
                        "passport_num": ret_data
                    }
                    return jsonify(ret_data), 200
                else:
                    return jsonify({'Error': 'No customer found with given filter params'}), 404

    if request.method == 'POST':
        if {"passport_num", "acc_name", "acc_address"} != request.form.keys():
            return jsonify({"Error": "Invalid form data params"}), 400

        passport_num = request.form['passport_num']
        acc_name = request.form['acc_name']
        acc_address = request.form['acc_address']

        try:
            passport_num = int(passport_num)
        except ValueError:
            return jsonify({"Error": "Passport number must be an integer"}), 400

        if not acc_name or not acc_address:
            return jsonify({"Error": f"To add a customer, "
                                     f"you must specify all params {passport_num, acc_name, acc_address}"}), 400

        query = f"INSERT INTO customers (passport_num, acc_name, acc_address)" \
                f" VALUES (%s, %s, %s)"

        with conn:
            with conn.cursor() as curs:
                curs.execute(query, (passport_num, acc_name, acc_address))
                if curs.rowcount == 1:
                    return jsonify({"Success": f"Added customer: {passport_num, acc_name, acc_address}"}), 200
                else:
                    return jsonify({'Error': 'Failed to add a customer'}), 400




if __name__ == '__main__':
    app.run(debug=True)
