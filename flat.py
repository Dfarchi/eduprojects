
class Bathroom:

    def __init__(self, name: str, size: float, toilet: int, sink: int, bath: int, shower: int):
        self.name = name
        self.size = size
        self.elements = [toilet*'toilet', sink*'sinks', bath*'bath', shower*'shower']


class Apartment:

    def __init__(self, country: str, city: str, street: str, house_num: int, flat_num: int, floor: int, floors: int,
                 kitchen: float, balconi=0):
        self.address = [country, city, street, f'house number -{house_num}', f' flat number- {flat_num}']
        self.floor = floor
        self.floors = floors
        self.rooms = [kitchen, balconi]
        self.size = sum(self.rooms)


    def add_bathromm(self, name: str, size: float, toilet: int, sink: int, bath: int, shower: int):
        one = Bathroom(name, size, toilet, sink, bath, shower)
        self.rooms.append(one.size)

    def get_size(self):
        print(sum(self.rooms))
