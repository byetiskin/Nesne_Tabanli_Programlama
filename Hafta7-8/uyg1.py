from datetime import datetime

class Customer:
    def __init__(self, id: int, name: str, address: str, phone: str):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone

    def add(self):
        print(f"Customer '{self.name}' added to the system.")

    def edit(self):
        print(f"Customer '{self.name}' information updated.")

    def delete(self):
        print(f"Customer '{self.name}' removed from the system.")


class Product:
    def __init__(self, id: int, price: float, type: str):
        self.id = id
        self.price = price
        self.type = type

    def add(self):
        print(f"Product '{self.type}' with ID {self.id} added to the catalog.")

    def modify(self, id: int):
        print(f"Product with ID {id} has been modified.")

    def select(self, id: int):
        print(f"Product with ID {id} has been selected.")


class Stock:
    def __init__(self, product: Product, quantity: int, no: int):
        self.product = product  # Composition relationship with Product
        self.quantity = quantity
        self.no = no

    def add(self):
        print(f"Stock entry for Product ID {self.product.id} added with quantity {self.quantity}.")

    def modify(self, product_id: int):
        print(f"Stock entry for Product ID {product_id} has been modified.")

    def select(self, product_id: int):
        print(f"Stock entry for Product ID {product_id} has been selected.")


class Order:
    def __init__(self, id: int, customer: Customer, product: Product, amount: int, date: datetime):
        self.id = id
        self.customer = customer  # Association with Customer
        self.product = product  # Aggregation relationship with Product
        self.amount = amount
        self.date = date

    def newOrder(self):
        print(f"New order created for Customer '{self.customer.name}' with Product ID {self.product.id} on {self.date}.")

    def edit(self, id: int):
        print(f"Order {id} has been updated.")


# Example usage of the classes and their relationships

# Creating a customer
customer = Customer(1, "John Doe", "123 Main St", "555-1234")
customer.add()

# Creating a product
product = Product(101, 19.99, "Book")
product.add()

# Creating a stock entry for the product
stock = Stock(product, 50, 1)
stock.add()

# Creating an order for the customer with the product
order = Order(1001, customer, product, 2, datetime.now())
order.newOrder()
order.edit(1001)
