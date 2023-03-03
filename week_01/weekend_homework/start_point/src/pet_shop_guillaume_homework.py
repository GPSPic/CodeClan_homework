# WRITE YOUR FUNCTIONS HERE

# get the name of the shop
def get_pet_shop_name(shop):
    return shop["name"]

# get the current cash balance for the shop
def get_total_cash(shop):
    return shop["admin"]["total_cash"]

# add or remove from shop cash balance
def add_or_remove_cash(shop, transaction_amount):
    shop["admin"]["total_cash"] += transaction_amount

# get the number of pets sold
def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

# add to the number of pet sold for the shop
def increase_pets_sold(shop, number_of_sales):
    shop["admin"]["pets_sold"] += number_of_sales

# get the number of pets currently in the shop for sale
def get_stock_count(shop):
    return len(shop["pets"])

# get a list with all the pets in the shop matching the breed
def get_pets_by_breed(shop, searching_for_breed):
    pets_matching_the_breed = []
    for pet_info in shop["pets"]:
        # if pet_info["breed"].count(searching_for_breed) == 1:
        if searching_for_breed in pet_info["breed"]:
            pets_matching_the_breed.append(pet_info)
    return pets_matching_the_breed

# def find_pet_by_name(shop, pet_name):
#     pet_in_shop = {}
#     for pet_info in shop["pets"]:
#         if pet_name in pet_info["name"]:
#             pet_in_shop.update(pet_info)
#         else:
#             pet_in_shop = None
#     return pet_in_shop

def find_pet_by_name(shop, pet_name):
    pet_in_shop = None #assigning None for future test and for empty results
    for pet_info in shop["pets"]: #pet_info refers to each pet's dictionnary
        if pet_name in pet_info["name"]:
            pet_in_shop = {} #change variable to a dict
            pet_in_shop.update(pet_info) #update dict with the pet's dict
    return pet_in_shop

# find the dict containing the pet name and remove it
def remove_pet_by_name(shop, pet_name):
    for pet_info in shop["pets"]:
        if pet_name in pet_info["name"]:
            shop["pets"].remove(pet_info)

# add new pet to the shop list, testing with previous function
def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

# using index of customer in list provided, find cash value
def get_customer_cash(customer_index):
    return customer_index["cash"]

