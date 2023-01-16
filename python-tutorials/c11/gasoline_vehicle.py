from c11.vehicle import Vehicle


class GasolineVehicle(Vehicle):


    def __init__(self, manufacturer: str, model: str, color: str, year: int,
                 tank_capacity: int, fuel_consumption: int, fuel_type: str,
                 km: int = 0):

        super().__init__(manufacturer, model, color, year, km)
        self._fuel_type = fuel_type
        self._tank_capacity = tank_capacity
        self._fuel_consumption = fuel_consumption
        self._curr_fuel = 0


    def has_enough_resource(self, km):
        return self._curr_fuel / self._fuel_consumption >= km

    def update_resource(self, km):
        self._curr_fuel -= km / self._fuel_consumption


    def add_fuel(self, liters):
        pass