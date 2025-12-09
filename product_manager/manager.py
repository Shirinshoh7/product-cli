from .models import Product

class ProductManager:
    def __init__(self, filename):
        self.filename = filename
        self.products = self.load_products()

    def load_products(self):
        products = {}
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    if "—" in line:
                        name, price = line.strip().split("—")
                        products[name.strip()] = float(price.strip())
        except FileNotFoundError:
            pass
        return products

    def save_products(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            for name, price in self.products.items():
                f.write(f"{name} — {price}\n")

    def add_product(self, name, price):
        self.products[name] = price
        self.save_products()

    def edit_product(self, name, price):
        if name in self.products:
            self.products[name] = price
            self.save_products()

    def delete_product(self, name):
        if name in self.products:
            del self.products[name]
            self.save_products()

    def total_sum(self):
        return sum(self.products.values())
