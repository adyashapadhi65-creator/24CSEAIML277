# Q3. Supermarket Product Management using class

class Product:
    def __init__(self, pid, name, price, quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def display(self):
        print("Product ID:", self.pid)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Amount:", self.calculate_total())


p = Product(1, "Milk", 50, 4)
p.display()