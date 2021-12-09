import random


class Store:
    def __init__(self, name):
        self.name = name
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def sell_product(self, upc):
        for item in self.product_list:
            if item.u_id == upc:
                item.print_info()
                print(item.name, "sold for", item.price)
                del item

    def inflation(self, percentage):
        for item in self.product_list:
            item.update_price(percentage, True)

    def clearance(self, percentage):
        for item in self.product_list:
            item.update_price(percentage, False)


class Product:
    def __init__(self, name, price, category="uncategorized"):
        self.name = name
        self.price = price
        self.category = category
        self.u_id = random.randint(1000, 9999)

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change)
        if not is_increased:
            self.price -= (self.price * percent_change)

    def print_info(self):
        print("Name: ", self.name, "\n", "Category: ", self.category, "\n", "Price: ", self.price, "\n", "UPC: ",
              self.u_id, sep="")


def main():
    sale_store = Store("sale store")
    carrots = Product("carrots", 4.00, "veggie")
    cereal = Product("cereal", 5.00, "breakfast")
    sale_store.add_product(carrots)
    sale_store.add_product(cereal)
    sale_store.inflation(.5)
    sale_store.clearance(.1)
    for item in sale_store.product_list:
        item.print_info()
    sale_store.sell_product(int(input("UPC: ")))


if __name__ == "__main__":
    main()
