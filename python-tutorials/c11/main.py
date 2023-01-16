from c11.electric_vehicle import ElectricVehicle

if __name__ == '__main__':
    # v = Vehicle("mazda", "3", "white", 1999)
    # print(v.get_manufacturer())
    # print(v._model)
    # print(v.__dict__)
    # print(v._Vehicle__manufacturer)
    ev = ElectricVehicle('tesla', 'model 3', 'white', 2022, 103, 4)
    ev.drive(100)
    print("bye")