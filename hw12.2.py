class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"

    def __repr__(self):
        return f"Item({self.name!r}, {self.price}, {self.description!r}, {self.dimensions!r})"

    def __hash__(self):
        return hash((self.name, self.price, self.description, self.dimensions))

    def __eq__(self, other):
        return isinstance(other, Item) and (self.name, self.price, self.description, self.dimensions) == \
               (other.name, other.price, other.description, other.dimensions)


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        self.products[item] = cnt  

    def get_total(self):
        return sum(item.price * qty for item, qty in self.products.items())

    def __str__(self):
        result = f"User: {self.user}\nItems:\n"
        for item, qty in self.products.items():
            result += f"{item.name}: {qty} pcs.\n"
        return result.strip()


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'

cart.add_item(apple, 10) 
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""
assert cart.get_total() == 40
