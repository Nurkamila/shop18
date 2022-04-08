# класс методы, статик методы и инстанс методы

# class SomeClass:
#     def __init__(self, a, b) -> None:
#         self.a = a
#         self.b = b

#     def func(self):
#         pass

#     @classmethod
#     def func_two(cls):
#         pass

#     @staticmethod # напрямую не меняет состояние класса или объекта
#     def func_three():
#         pass

# SomeClass().func()

# DELIVERY_PRICE = 120
# class Order:
#     orders = []

#     def __init__(self, name, address, product, price, count) -> None:
#         self.name = name
#         self.address = address
#         self.product = product
#         self.price = price
#         self.count = count

#     def create_order(self):
#         order = {
#             'name': self.name,
#             'address': self.address,
#             'product': self.product,
#             'price': self.price,
#             'count': self.count,
#             'delivery': self.set_delivery(self.count, DELIVERY_PRICE)
#         }
#         self.orders.append(order)

#     @staticmethod
#     def set_delivery(count, price):
#         return price * count / 2

# order1 = Order(
#     "john", "California", 'ice-cream', 250, 5
# )
# order1.create_order()
# print(order1.orders)

# order2 = Order(
#     'Raychel', "LA", 'ice-cream', 250, 10
# )
# order2.create_order()
# print(Order.orders)


class Pizza:
    def __init__(self, name, radius, *ingredients):
        self.name = name
        self.radius = radius
        self.ingredients = ingredients
        self.create_pizza()

    def create_pizza(self):
        print(f'Created Pizza -> {self.name} with radius {self.radius} ingredients {self.ingredients}')

    @classmethod
    def create_pepperoni(cls, radius):
        name ='Pepperoni'
        ingredients = ('sausage', 'cheese', "dough", 'origano')
        return cls(name, radius, *ingredients)

    @classmethod
    def create_margarita(cls, radius):
        name ='Margarita'
        ingredients = ('tomatos', 'cheese', "dough", 'origano')
        return cls(name, radius, *ingredients)

    @classmethod
    def create_four_cheese(cls, radius):
        name ='Margarita'
        ingredients = ('cheese another', 'cheese', "dough", 'origano')
        return cls(name, radius, *ingredients)

# pizza = Pizza('Pepperoni', 30, 'sausage', 'cheese', "dough", 'origano')
# pizza.create_pizza()
Pizza.create_margarita(30)
Pizza.create_pepperoni(40)
Pizza.create_four_cheese(20)