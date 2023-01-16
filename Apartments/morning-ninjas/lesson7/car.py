from pprint import pprint

# my_car = {
#     'manufacturer': 'Mazda',
#     'model': '3',
#     'color': 'white',
#     'license_plate': '1234567',
#     'year': 2015,
#     'fuel': 50,
#     'km': 102000,
#     'fuel_consumption': 20
# }
#
# def add_fuel(car, liters):
#     car['fuel'] += liters
#
# def drive(car, km):
#     car['km'] += km
#
#
#
# if __name__ == '__main__':
#     add_fuel(my_car, 2)
#     drive(my_car, 100)
#     drive(my_car, -300)
#     pprint(my_car)


# what should we do if we also want to update info about fuel left?



# We want something like (pseudocode - will not run!):

# Create an object, it has internal state
# car = Car(manufacturer='Mazda', model='3', fuel=50,...)

# "Use" the object bu applying actions on it - and internal state will change accordingly
# (increas km), add/reduce fuel, etc...
# car.add_fuel(liters=20)
# car.drive(km=200)
# car.get_fuel_left()
# car.is_out_of_fuel()
# ...

# Cars “remember” things about their current state
# Cars functions (methods) that can change that state
# We can manage each car separately


class Car:
    def __init__(self, manufacturer: str, model: str,
                 color: str, fuel_consumption: float,
                 fuel_tank_capacity: float,
                 year: int = None):
        print(f"Inside __init__ of {manufacturer}")
        self.manufacturer: str = manufacturer
        self.model: str = model
        self.color: str = color
        self.fuel_consumption = fuel_consumption
        self.fuel_tank_capacity = fuel_tank_capacity
        self.km: int = 0
        self.fuel: float = 0
        self.year: int = year
        self.maintenance = {}

    def __str__(self):
        print("Inside __str__")
        return f"{self.manufacturer} | Model: {self.model} | Year: {self.year}"

    def display_dashboard(self):
        print(f"Dashboard for {self.manufacturer} {self.model}")
        print('====================')
        print(f"Fuel left: {self.fuel}")
        print(f"Km: {self.km}")
        print('====================')

    def fill_tank(self, amnt: float) -> bool:
        print(f"Inside fill_tank, amount: {amnt}")
        if amnt <= 0:
            print("Non-positive amnt is not allowed")
            return False
        if amnt + self.fuel > self.fuel_tank_capacity:
            print(f"Cannot fill more than the tank capacity."
                  f"Current capacity is: {self.fuel_tank_capacity}")
            return False

        self.fuel += amnt
        return True

    def fill_to_full(self):
        self.fuel = self.fuel_tank_capacity
        # return None

    def drive(self, kms_driven: int):
        if (self.fuel_consumption / 100) * kms_driven <= self.fuel:
            self.km += kms_driven
            self.fuel -= (self.fuel_consumption / 100) * kms_driven
            return True
        else:
            print("error")
            return False

    def add_maintenance(self, date, description):
        m_list = self.maintenance.get(date, [])
        m_list.append(description)
        self.maintenance[date] = m_list
        # self.maintenance[date] = description
        print("maintenance added")

    def display_all_maintenance(self):
        pprint(self.maintenance)


    def get_all_maintenance(self):
        return self.maintenance



# car_mazda: Car = Car('Mazda', '3', color='white')
# car_toyota = Car('Toyota', 'Yaris', 'red', 2020)
# print(car_mazda)
# print(car_toyota)
# print(isinstance(car_mazda, Car))
# print(car_mazda is Car)
# my_car = car_mazda
# print(car_mazda is my_car)

# l = list()
# s = set([3,4,3,5])


# car1 = Car()
# Car.__init__()
# print(car.manufacturer, car.model, car.color)
# print(car.__init__)
# print(car)

# print(Car)
# print(str)


mazda_car = Car('Mazda', '3 Spirit', 'white',
                fuel_consumption=20, fuel_tank_capacity=60, year=2015)

toyota_car = Car('Toyota', 'Yaris', 'red',
                 fuel_consumption=25, fuel_tank_capacity=40, year=2022)

mazda_car.display_dashboard()
# mazda_car.fill_tank()
# Car.fill_tank(mazda_car)

is_success = mazda_car.fill_tank(20)
mazda_car.display_dashboard()

mazda_car.display_dashboard()
is_success = mazda_car.fill_tank(10)
mazda_car.display_dashboard()
# while not is_success:
#     is_success = mazda_car.fill_tank(20)

mazda_car.add_maintenance('23.11.2022', '10000 maintenance')
mazda_car.display_all_maintenance()
mazda_car.add_maintenance('23.11.2022', 'new maint')
mazda_car.display_all_maintenance()
mazda_car.add_maintenance('24.11.2022', 'fix after crash')
mazda_car.display_all_maintenance()
maintenance_dict = mazda_car.get_all_maintenance()
print(mazda_car)








