class BusCompany:

    def __init__(self):
        self.lines = []
        # self.lines = {}


    def add_route(self, line_num, stops: list[str]) -> None:
        pass

    def report_delay(self, line_num):
        pass

    def get_all_lines(self) -> list:
        return list(self._lines.values())

    def add_ride(self, line_num, ride_details):
        # find the relevant line
        # line.add_ride(ride_details)
        pass

class Route:
    pass

class BusRoute(Route):
    pass

class TrainRoute(Route):
    pass



if __name__ == '__main__':
    company = BusCompany()
    # for line in company.lines:
    #     print(line.number)
    # print(company.lines)

    lines = company.get_all_lines()
    for line in lines:
        print(line.number)