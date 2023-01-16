from water import db

if __name__ == '__main__':
    print(db['users_data']['ziv'])
    db['users_data']['ziv']['details']['1.1.2022'] = 1
    print(db['users_data']['ziv'])