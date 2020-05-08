# import sys
# sys.path.append(
#     '../CS/Intro-Python-I/src/15_classes.py')
from classes import latLong
# Design a store using OOP methadologies

# what does this store look like?
# what are attributes we care about?
# a name
# location
# department of products

# a store need product

# product class


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} cost ${self.price}"

# deapartment section
    # products will be a list of touples with signature (String, int)


class Department:
    def __init__(self, name, products=[]):
        self.name = name
        # * = spread this, name, price
        self.products = products  # [Product(*p) for p in products]
        # ↳ Product(p[0],p[1])

    def __str__(self):
        return f"Welcome to the {self.name} department"

    def add_product(self, product, price):
        self.products.append(Product(product, price))

    def print_products(self):
        for p in self.products:
            print(p)


class Store:
    def __init__(self, name, lat, lon, department):
        self.name = name
        self.location = latLong(lat, lon)
        # self.department = department
        self.department = [Department(department_name, department_products)
                           for department_name, department_products in department.items()]  # have them in a list

    # add a __str__ method so that can observe our Store instance

    def __str__(self):
        return f"Store {self.name}, {self.location}, {self.department}"

    def print_products(self):
        for d in self.department:
            d.print_products()

    def print_departments(self):
        for d in self.department:
            print(d)


products_and_departments = {
    "produce": [Product("Zucchini", 20)],
    "clothing": [Product("Coat", 90), Product("Blouse", 25)],
    "Books": [Product("Game of Thrones", 2), Product("Witcher", 10)],
    "Sporting Goods": [Product("Canoe", 2000), Product("Gloves", 20), Product("Baseball", 20)]
}

store = Store("LabmdaStore: ", 44.052137, -121.41556, products_and_departments)

# alternative 2 ↴
# store = Store("LabmdaStore: ", 44.052137, -121.41556,
#               [Department("produce"), Department("clothing"), Department("Books"), Department("Sporting Goods")])
store.department[1].add_product("Zucchini", 2.00)
store.department[3].add_product("coat", 25.00)

store.print_products()
store.print_departments()
# print(store)

# we want to add departments
# let's take input from the user and have them specify departments
# index in the department list
while True:
    selection = input(
        'Select the number of a department or type "exit" to leave : ')

    if selection == "exit":
        print("Thanks for shopping with us!")
        break
    # return the id of the store departments
    # print('The user selected ' + store.department[int(selection)])

    # add error handling so that whena  user inuts a department for a non existent
    # department, we'll notify them that that department doesn't exist

    # this part handles flow for getting user input, printing back what they've selected.
    # Until the user decides to exit
    try:
        # casting migh cause an error
        # if anything breaks, fall back on except
        selection = int(selection)
        if selection >= len(store.department):
            print("That's not a valid department")
        elif selection >= 0 and selection < len(store.department):
            # print('The user selected ' + store.department[selection])
            print(store.department[selection])

        else:
            print('Department numbrs are positive')

    except ValueError:  # TypeError: the user gave us something that can not be typed and doesnt match the type we want not the value
        # the user didnt give us a value that could be cast to a number
        print('Please enter your choice as a number')

    # when should we break out of this loop?
    # lets let the user type "exit" into the selection to have them leave

    # research exception error
