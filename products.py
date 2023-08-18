#!/usr/bin/python3
#-*-Coding:utf-8 -*-

import cart


products_list = [
    {"nom": "Pwodwi A", "pri": 10.99, "kantite": 5},
    {"nom": "Pwodwi B", "pri": 24.99, "kantite": 8},
    {"nom": "Pwodwi C", "pri": 5.99, "kantite": 12}
]

def display_products():
    print("\nPwodwi ki disponib yo :")
    for idx, product in enumerate(products_list, start=1):
        print(f"{idx}. {product['nom']} - {product['pri']}$")




    choice = int(input("Rantre nimewo Pwodwi ou chwazi an : ")) - 1
    if 0 <= choice < len(products_list):
        selected_product = get_product_by_index(choice)
        cart.add_to_cart(selected_product)
    else:
        print("Nimewo Pwodwi an pa bon.")



def get_product_by_index(index):
    return products_list[index]

