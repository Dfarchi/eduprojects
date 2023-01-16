from lesson7.gadget_store import Store, Customer

if __name__ == '__main__':
    # my_store = Store('Gadgets')
    # my_store.add_customer('Ziv Attias', 'Tel Aviv-Yaffo', '054-4444444')
    # my_store.add_customer('Nehorai Tubul', 'Ashkelon', '054-444555544')
    # print(my_store.customers)
    # print(my_store.customers['Ziv Attias'])

    c1 = Customer('Ziv Attias', 'Tel Aviv-Yaffo', '054-4444444')
    print(c1) # __str__
    l1 = [c1]
    print(l1) # __repr__
