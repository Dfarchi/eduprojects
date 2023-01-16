from c11.vehicle import Vehicle


class ElectricVehicle(Vehicle):

    def __init__(self, manufacturer: str, model: str, color: str, year: int,
                 battery_capacity: int, km_per_kw: int, km: int = 0):

        super().__init__(manufacturer, model, color, year, km)

        self._km_per_kw = km_per_kw
        self._battery_capacity = battery_capacity
        self._current_charge = 0

    def has_enough_resource(self, km):
        return self._current_charge / self._km_per_kw >= km

    def update_resource(self, km):
        self._current_charge -= km / self._km_per_kw


    def charge(self, kw):
        pass
