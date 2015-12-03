#! /usr/bin/env python3

import random
from bicycles import Bicycle, BikeShop, Customer

# First create a list of Bikes, then create a BikeShop, stocking it
# with the Bikes...

bikes = [
    Bicycle("Super Speed", 75, 100), Bicycle("Mama Jama", 70, 150),
    Bicycle("Jumper Jack", 50, 250), Bicycle("Red Racer", 90, 350),
    Bicycle("Mud Muncher", 65, 100), Bicycle("Blastoff", 75, 550)
    ]

shop = BikeShop("Eddies Bike Shop", 20, bikes)

# Now, create a list of Customers, then iterate over them, printing
# the Customer's name and the Bikes that they can afford...

customers = [Customer("Walter White", 200), Customer("Jesse Pinkman", 500), Customer("Hank Schrader", 1000)]

for customer in customers:

    bikes = ", ".join( bike.model for bike in shop.filter(customer.fund) )
    print(customer.name, "|", bikes) # should this be printing the customers name and fund??

# Print the BikeShop before making any sales...

print(shop)

# Iterate over the customers, selling each a Bike, then using a template,
# print who the customer is, what they bought, what it cost, and how much
# they have left over...

template = "{0} bought the {1} at ${2}, and they have ${3} left over."

for customer in customers:
    
    affordables = shop.filter(customer.fund)
    shop.sell(random.choice(affordables), customer)
    
    print(template.format(
        customer.name, customer.bike.model,
        customer.bike.price, customer.fund
        ))

# Print the BikeShop again, now it's made a few sales...

print(shop)

