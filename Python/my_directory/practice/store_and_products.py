class Store:
    def __init__(self, name, product_list):
        self.name = name
        self.product_list = product_list
        self.product_list = []

    def add_product(self, new_product, price, category):
        self.product_list.append(Product(new_product, price, category))

    def sell_product(self, index):
        self.product_list[index].print_info()
        self.product_list.remove(index)

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

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change)
        if not is_increased:
            self.price -= (self.price * percent_change)

    def print_info(self):
        print("Name: ", self.name, "Category: ", self.category, "Price: ", self.price, sep="\n")

def main():
    sale_store = Store("sale store", stock)


if __name__ == "__main__":
    main()
