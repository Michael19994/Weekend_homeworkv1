# WRITE YOUR FUNCTIONS HERE
from email.errors import NoBoundaryInMultipartDefect
from operator import index
from pickle import APPEND


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, plus10):
    pet_shop["admin"]["total_cash"] += plus10
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash_remove(pet_shop, minus10):
    pet_shop["admin"]["total_cash"] - minus10
    return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, two):
    pet_shop["admin"]["pets_sold"] += two
    return pet_shop["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_input):
    breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_input:
           breed_list.append(pet)
    
    return breed_list

def get_pets_by_breed(pet_shop, breed_input):
    breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_input:
            breed_list.append(pet)

    return breed_list

def find_pet_by_name(pet_shop,name):
    name_list = []
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            name_list = pet
    
    return name_list

def find_pet_by_name(pet_shop,name):
    name_list = None
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            name_list = pet

    return name_list

def remove_pet_by_name(pet_shop,remove_name):
    for index, pet in enumerate(pet_shop["pets"]):
        if pet["name"] == remove_name:
            pet_shop["pets"].pop(index)

def add_pet_to_stock(pet_shop,new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers,num100):
    customers["cash"] -= num100

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers,num1):
    customers["pets"].append(num1)

def customer_can_afford_pet(customer,new_pet):
    return True

def customer_can_afford_pet(customer,new_pet):
    return customer["cash"] >= new_pet["price"]

def customer_can_afford_pet_exact(customer,new_pet):
    return customer["cash"] == new_pet["price"]
        

    