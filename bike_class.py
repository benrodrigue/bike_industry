#! /usr/bin/env python3

class Customer:
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund

        """Add a return function to print out the customers funds?"""

class Bicycle:
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

    def __repr__(self):
        template = "The {} weighs {}lbs and costs ${}."
        return template.format(self.model, self.weight, self.cost)

class BikeShop: 
    def __init__(self, name, margin, bikes):
        self.name = name
        self.margin = margin
        self.bikes = bikes

        self.profit = 0
        self.inventory = {}

        for bike in bikes:
            bike.markup = int((bike.cost / 100.0) * self.margin)
            bike.price = bike.cost + bike.markup
            self.inventory[bike.model] = bike # I don't understand what is happening here.




    def __repr__(self):

        template = "\n{0} (${1} profit)\n{2}\n"
        bikes = "\n".join( str(bike) for bike in self.inventory.values() )
        return template.format(self.name, self.profit, bikes)

    def filter(self, budget):

        bikes = self.inventory.values()
        return [ bike for bike in bikes if bike.price <= budget ]

    def sell(self, bike, customer):

        customer.bike = bike
        customer.fund -= bike.price
        self.profit += bike.markup
        del self.inventory[bike.model]