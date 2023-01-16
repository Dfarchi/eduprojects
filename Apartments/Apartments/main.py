class Apartment:
    states = ['for sale', 'open for rent', 'rented', 'sold']

    def __init__(self, adress, parking, rooms: int, size: int, tax):
        self.address = adress
        self.parking_type = parking
        self.rooms_num = rooms
        self.size_in_sq_meters = size
        self.balcony = False
        self.penthouse = False
        self.villa = False
        self.deal_state = None
        self.monthly_municipal_tax = tax

    def __str__(self):
        return self.address

    def is_villa(self):
        self.villa = True
        return self.villa

    def has_balcony(self):
        self.balcony = True
        return self.balcony

    def is_penthouse(self):
        self.penthouse = True
        return self.penthouse

    def get_agency_fee(self):
        if self is Sale and self.close_deal() == 'sold':
            agency_fee = 0.02 * sale.sale_price
            return agency_fee
        elif self is Rent and self.close_deal() == 'rented':
            agency_fee = rent.rent_price_per_month
            return agency_fee

    def get_annual_municipal_tax(self):
        return self.monthly_municipal_tax * 12

    def close_deal(self):
        if self.deal_state == 'for sale':
            self.deal_state = 'sold'
        elif self.deal_state == 'for rent':
            self.deal_state = 'rented'


class Sale(Apartment):

    def __init__(self, price, adress, parking, rooms: int, size: int, tax):
        super().__init__(adress, parking, rooms, size, tax)
        self.deal_state = self.is_for_sale()
        self.sale_price = price

    def is_for_sale(self):
        self.deal_state = 'for sale'

        return self.deal_state


class Rent(Apartment):

    def __init__(self, price, adress, parking, rooms: int, size: int, tax):
        super().__init__(adress, parking, rooms, size, tax)
        self.rent_price_per_month = price
        self.deal_state = self.is_for_rent()


    def is_for_rent(self):
        self.deal_state = 'for rent'
        return self.deal_state

    def get_annual_rent_price(self):
        print(f'annual rent is {self.rent_price_per_month * 12} NIS')


a = Rent(5000, 'tel aviv', 1, 3, 90, 200,)
print(a.rent_price_per_month)
a.is_for_rent()
print(a, a.deal_state)
a.get_annual_rent_price()
# a.is_penthouse()
# a.is_villa()
a.get_annual_rent_price()
a.close_deal()
print(a, a.deal_state)
a = Sale(100, 'ASDF', 3, 12, 244,1000)
print(a)