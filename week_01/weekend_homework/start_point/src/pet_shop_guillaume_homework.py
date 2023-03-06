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

# does not work, for loop doe snot check correct information
# def get_pets_by_breed(pet_shop, animal_breed):
#     breeds_in_stock = []
#     pet_shop = pet_shop["pets"]
#     breed_type = animal_breed
#     for pet in pet_shop:
#               if breed_type == pet["breed"]:
#                 breeds_in_stock.append(breed_type)
#     return breeds_in_stock

# does not work
# def find_pet_by_name(shop, pet_name):
#     pet_in_shop = {}
#     for pet_info in shop["pets"]:
#         if pet_name in pet_info["name"]:
#             pet_in_shop.update(pet_info)
#         else:
#             pet_in_shop = None
#     return pet_in_shop

def find_pet_by_name(shop, pet_name):
    # pet_in_shop = None #assigning None for future test and for empty results
    # for pet_info in shop["pets"]: #pet_info refers to each pet's dictionnary
    #     if pet_name in pet_info["name"]:
    #         pet_in_shop = {} #change variable to a dict
    #         pet_in_shop.update(pet_info) #update dict with the pet's dict
            # can also be pet_in_shop = pet_info, as pet_info is already a dictionary
    # return pet_in_shop
    for pet in shop["pets"]:
        if pet_name in pet["name"]:
            return pet

# find the dict containing the pet name and remove it
def remove_pet_by_name(shop, pet_name):
    for pet_info in shop["pets"]:
        if pet_name in pet_info["name"]:
            shop["pets"].remove(pet_info)

# add new pet to the shop list, testing with previous function
def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

# using index of customer in list provided, find cash value
def get_customer_cash(customer):
    return customer["cash"]

# removing amount of cash from desiganted customer
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

# get the current number of pets for the designated customer
def get_customer_pet_count(customer):
    return len(customer["pets"])

# adding the new pet dict to the customer's pet list
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

# call previous function to get cash amount and compare to pet price
def customer_can_afford_pet(customer, new_pet):
    # works, but other complicated
    # enough_dough = False
    # if get_customer_cash(customer) >= new_pet["price"]:
    #     enough_dough = True
    # return enough_dough
    return customer["cash"] >= new_pet["price"]
# operators automatically check if operation is true/false


def sell_pet_to_customer(shop, pet, customer):
    if  pet != None and customer_can_afford_pet(customer, pet) == True:
    # also works with pet != None and customer_can_afford_pet(customer, pet):,
    # true is implied in result of can_afford_pet function
        remove_pet_by_name(shop, pet["name"])
        add_pet_to_customer(customer, pet)
        increase_pets_sold(shop,1)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(shop, pet["price"])