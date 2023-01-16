from numbergenerator import taz_generator



class Client:
    def __init__(self, password: str, name: str, address: str, clientid:str):
        self.name = name
        self.adress = address
        self.password = password
        self.clientid = clientid


    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
