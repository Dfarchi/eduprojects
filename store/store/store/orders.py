from store import store
from store.store import Product


class Shipment:
    STATUSES = ('processing', 'shipped', 'delivered')
    counter = 0

    def __init__(self, address):
        self.address = address
        self.status = 0
        Shipment.counter += 1

    def change_status_to_next(self) -> bool:
        if self.status == len(Shipment.STATUSES) - 1:
            print('Bad status')
            return False
        self.status += 1
        return True


class Order:

    def __init__(self, customer: store.Customer):
        self.neworder = []
        self.customer = customer
        self.price = 0

    def add_to_order(self, product: Product):
        if product.qty == 0:
            print('out of stock')
            return False
        else:
            self.neworder.append([product.sku, product.price])
            return self.neworder

    def sahac_price(self, neworder):
        sahac = 0
        for item in neworder:
            sahac += item.price
        self.price = sahac
        return sahac
