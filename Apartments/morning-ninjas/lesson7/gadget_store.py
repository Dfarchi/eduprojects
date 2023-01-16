class Customer:
    def __init__(self, name, address, phone, email=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"<Customer>\n" \
               f"Name: {self.name}\n" \
               f"Address: {self.address}\n" \
               f"Phone: {self.phone}"

    def __repr__(self):
        return f"<Customer> {self.name}"


class Product:
    def __init__(self, sku: str, category: str, brand: str,
                 qty: float, price: float,
                 model: str = None,
                 warranty_months: int = None):
        if price <= 0:
            pass
            # error
            # return None
        self.sku = sku
        self.category = category
        self.price = price
        self.qty = qty

    def update_qty(self, diff: float):
        if diff + self.qty < 0:
            # error
            return None
        self.qty += diff

    def update_price(self, new_price):
        if new_price <= 0:
            # error
            return None
        self.price = new_price

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        return self.sku == other.sku


# c = Customer('adv', 'sdfs', 'sdfs')
# c.phone = '054-342342'

#
# d1 = {
#     'address':'sdfs'
# }
#
# c1 = Customer()

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.customers: dict[str: Customer] = {}
        self.inventory: {str: Product} = {}
        self.inventory_by_name: dict[str: Product] = {}
        # customers
        # inventory
        # order_product
        # orders
        # shipments

    def add_customer(self, name, address, phone, email=None):
        new_customer = Customer(name, address, phone, email)
        self.customers[name] = new_customer

    def add_product_to_inventory(self, sku: str, category: str, brand: str,
                                 qty: float, price: float,
                                 model: str = None,
                                 warranty_months: int = None):
        new_product = Product(sku, category, brand,
                              qty, price, model, warranty_months)
        self.inventory[sku] = new_product
        self.inventory_by_name[brand+model] = new_product

    def add_qty(self, sku:str, qty: float):
        self.inventory[sku].update_qty(qty)

    def add_items(self, skus: list, quantities: list):
        for sku, qty in zip(skus, quantities):
            self.add_qty(sku, qty)

    def get_products_by_brand(self, brand) -> list[Product]:
        ret_val = list()
        for product in self.inventory.values():
            if product.brand == brand:
                ret_val.append(product)
        return ret_val

    def get_out_of_stock(self):
        pass

    def add_order(self):
        pass

