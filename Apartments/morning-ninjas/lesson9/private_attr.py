import pprint


class Car:
    def __init__(self, manufacturer: str, model: str, color: str,
                 fuel_consumption: float, fuel_tank_capacity: float):
        self.manufacturer: str = manufacturer
        self.__model: str = model
        self.__color: str = color
        self._fuel_consumption = fuel_consumption
        self.fuel_tank_capacity = fuel_tank_capacity
        self.__km: int = 0
        self.fuel: float = 0

    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__color = new_color

    def __str__(self):
        return f"{self.manufacturer} | Model: {self.__model} |  km: {self.__km} | fuel: {self.fuel}"

    def fill_tank(self, amnt: float) -> bool:
        if amnt <= 0:
            return False
        if amnt + self.fuel > self.fuel_tank_capacity:
            return False

        self.fuel += amnt
        return True

    def drive(self, kms_driven: int):
        if (self.fuel_consumption / 100) * kms_driven <= self.fuel:
            self.__km += kms_driven
            self.fuel -= (self.fuel_consumption / 100) * kms_driven
            return True
        else:
            return False



if __name__ == '__main__':
    car_mazda: Car = Car('Mazda', '3', 'white', 20, 60)
    car_toyota = Car('Toyota', 'Yaris', 'red', 25, 45)
    # ret_val = car_mazda.drive(30)
    # print(ret_val)
    print(car_mazda.__dir__())
    print(car_mazda._Car__km)
    # car_mazda._Car__km = 30
    # car_mazda.km = 60
    print(car_mazda.get_color())
    # print(car_mazda._fuel_consumption)
    # print(car_mazda.__km)
