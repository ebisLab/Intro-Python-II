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

# deapartment section


class Department:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"No products available in the {self.name}"


class Store:
    def __init__(self, name, lat, lon, department):
        self.name = name
        self.location = latLong(lat, lon)
        # self.department = department
        self.department = [Department(d)
                           for d in department]  # have them in a list

    # add a __str__ method so that can observe our Store instance

    def __str__(self):
        return f"Store {self.name}, {self.location}, {self.department}"


store = Store("LabmdaStore: ", 44.052137, -121.41556,
              ["produce", "clothing", "Books", "Sporting Goods"])
# print(store)

# we want to add departments
# let's take input from the user and have them specify departments
# index in the department list

selection = input(
    'Select the number of a department or type "exit" to leave : ')
# return the id of the store departments
# print('The user selected ' + store.department[int(selection)])

# add error handling so that whena  user inuts a department for a non existent
# department, we'll notify them that that department doesn't exist

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

except ValueError:
    # the user didnt give us a value that could be cast to a number
    print('Please enter your choice as a number')

    # when should we break out of this loop?
    # lets let the user type "exit" into the selection to have them leave
