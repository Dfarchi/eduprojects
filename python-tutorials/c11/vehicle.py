from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, manufacturer: str, model: str, color: str,
                 year: int, km: int = 0):
        self._year = year
        self._model = model
        self._manufacturer = manufacturer
        self._colors = [color]
        self._km = km

    def get_manufacturer(self):
        return self._manufacturer

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_color(self):
        return self._colors[-1]

    def set_color(self, new_color):
        self._colors.append(new_color)

    def get_original_color(self):
        return self._colors[0]

    def get_km(self):
        return self._km

    @abstractmethod
    def has_enough_resource(self, km):
        pass

    @abstractmethod
    def update_resource(self, km):
        pass

    def drive(self, km):
        if self.has_enough_resource(km):
            self._km += km
            self.update_resource(km)



