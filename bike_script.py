#! /usr/bin/env python3

from bike_class import Bicycle, BikeShop, Customer

if __name__ == '__main__':
    
    """Create 6 different bicycle models"""
    first_bike = Bicycle("Speedy", 20, 100)
    second_bike = Bicycle("Blazer", 40, 150)
    third_bike = Bicycle("Hip", 35, 650)
    fourth_bike = Bicycle("Downhill", 20, 720)
    fifth_bike = Bicycle("Racer", 35, 625)
    sixth_bike = Bicycle("Pinky", 25, 245)

    """Create a bicycle shop that has six different bicycle models in stock"""
inventory_list = [
    first_bike, second_bike, third_bike, fourth_bike, fifth_bike, sixth_bike
]

bike_shop = BikeShop("Eddies Bike Shop", inventory_list, .2)
print("\nShop name: {0}.".format(bike_shop.shop_name))

"""Print the initial inventory of the bike shop for each bike it carries."""
print("\nInventory")
print("-" * 20)

for bike in inventory_list:
    bike_msrp = bike.cost_to_produce * bike_shop.shop_margin + bike.cost_to_produce
    print("{} and the msrp is ${}.".format(bike, bike_msrp))
    
"""Create a customer and their bike budget"""
first_customer = Customer("Walter White", 200)
second_customer = Customer("Jesse Pinkman", 500)
third_customer = Customer("Hank Schrader", 1000)

customer_list = [first_customer, second_customer, third_customer]

print('\nCustomers')
print('-' * 20)

for customer in range(len(customer_list)):
    print(customer_list[customer])

#parsing inventory_list and customer list for bikes that customers can afford   
print('\nWhich bikes can they afford?')

for customer in range(len(customer_list)):
    print("-" * 20)
    for bike in range(len(inventory_list)):
        if inventory_list[bike].cost_to_produce <= customer_list[customer].customer_fund:
            print("{0} can afford the {1}".format(customer_list[customer].customer_name,inventory_list[bike].model_name))
print('-' * 20)