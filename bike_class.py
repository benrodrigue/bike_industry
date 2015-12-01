#! /usr/bin/env python3

class Bicycle(object):
    def __init__(self, model_name, model_weight, cost_to_produce):
        self.model_name = model_name
        self.model_weight = model_weight
        self.cost_to_produce = cost_to_produce
        
    def __repr__(self):
        return "\nThe {0} model weighs {1}lbs and costs ${2} to produce".format(self.model_name, self.model_weight, self.cost_to_produce)

class BikeShop(object):
    def __init__(self, shop_name, shop_inventory, shop_margin):
        self.shop_name = shop_name
        self.shop_inventory = shop_inventory
        self.shop_margin = shop_margin
        
    def __repr(self):
        return "\nThe shop charges a margin of {} for the bikes.".format(self.shop_margin)

class Customer(object):
    def __init__(self, customer_name, customer_fund):
        self.customer_name = customer_name
        self.customer_fund = customer_fund

    def __repr__(self):
        return"\n{0} has ${1} to spend on a bike.".format(self.customer_name, self.customer_fund)
"""      

        
    def shop_inventory(self, quantity):
        self.quantity = quantity
        print("The shop has {} bicycles in inventory".format(quantity))
        
    def sales_price(self, cost):
            super(Bike_Shops, self).__init__()
            self.production_cost = cost
            margin = 1.2
            sales_price = cost * margin
        
    def profit(self):
        #for every bike sold take the sales price and divide by 20% 
        #need to come up with how many bikes have been sold first
        print("The bike shop has made {} so far".format(profit()))
        
        
class Customer(object):
    def __init__(self, name):
        self.name = customer_name
        
    def bike_fund(self):
        self.bike_fund = bike_fund 
        
    def buy_bicycle():
        print("{0} just purchased a new {1} bike".format(customer_name, Bike(name)))
        
Steve = Customer.customer_name

"""