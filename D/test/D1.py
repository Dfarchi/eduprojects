import os.path
from csv import DictReader, DictWriter

import datetime


# def csv_details(path):
#     if not os.path.exists(path):
#         return False
#
#     file2deteils: dict[str: list] = {}
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             if file.endswith(".csv"):
#                 path_file = os.path.join(root, file)
#                 with open(path_file) as fh:
#                     clu = fh.readline()
#                     clu = clu.split(";")
#                     count_linse = 0
#                     for line in fh:
#                         count_linse += 1
#                 file2deteils[file] = [f"Amount of columns: {len(clu)}", f"amount of rows: {count_linse}"]
#
#     return file2deteils


# path = 'C:\\Users\\user\\Desktop\\check'
# pprint(csv_details(path))
#
# Year,  Avg Price, Min Price, Max Price, Avg Volume, Min Volume, Max Volume

# def reargnges(path):
#
#     with open(path) as csv:
#         aada = DictReader(csv)
#         newdata = {}
#         for cul in aada:
#             newdata.update({cul['Date'][6:20]: [cul['Low'], cul['High']]})
#
#     print(newdata)
#


#     with open('files\PL.csv', "a") as csv_f:
#         writer = csv.DictWriter(csv_f, ['Year', 'Avg Volume', 'Min Volume', 'Max Volume'])
#         writer.writeheader()
#         new_row = {'Year': date_year, 'Avg Volume': sum_volume / counter, 'Min Volume': low, 'Max Volume': high}
#         writer.writerow(new_row)
#


path = 'C:\\Users\\user\\Desktop\\eduprojects\\ebook\\AAPL.csv'


def reargnges(path):
    counter = 0
    vol = []
    high_price = []
    low_price = []
    line_in_csv = []
    with open(path) as csv_file:
        reader = DictReader(csv_file)

        for item in reader:        # Inserts the date of each row
            item['Date'] = datetime.date.year
            # date = datetime.datetime.strptime(date, "%d-%m-%Y")

            # enter the first year in variable
            if counter == 0:
                date_year = datetime.date.year

            if datetime.date.year == date_year:
                vol.append(float(item['Volume']))
                high_price.append(float(item['High']))
                low_price.append(float(item['Low']))
                counter = 1
            else:
                # When we come to a new year, we enter all the details and reset the variables for the next year
                line_in_csv.append({'Year': date_year,
                                    'Avg Price': (sum(high_price) + sum(low_price)) / (
                                            len(high_price) + len(low_price)),
                                    'Min Price': min(low_price), 'Max Price': max(high_price),
                                    'Avg Volume': sum(vol) / len(vol), 'Min Volume': min(vol), 'Max Volume': max(vol)})
                high_price = []
                low_price = []
                vol = []
                date_year = datetime.date.year

    with open('C:\\Users\\user\\Downloads\\PL.csv', "w") as csv_f:
        writer = DictWriter(csv_f, ['Year', 'Avg Price', 'Min Price', 'Max Price', 'Avg Volume',
                                    'Min Volume', 'Max Volume'])
        writer.writeheader()
        for row in line_in_csv:
            writer.writerow(row)

reargnges(path)
# with open('C:\\Users\\user\\Downloads\\PL.csv', 'r') as f:
#     print(f)
#
# reargnges()