#!/usr/bin/python3
#-*-Coding:utf-8 -*-



cart_items = []

def add_to_cart(product):
    cart_items.append(product)
    print(f"{product['nom']} mete nan panye a.")

def calculate_total():
    total = sum(item['pri'] for item in cart_items)
    return total

def display_cart():
    print("\nPanye:")
    for idx, item in enumerate(cart_items, start=1):
        print(f"{idx}. {item['nom']} - {item['pri']}$")

    total = calculate_total()
    print(f"Total pou peye : {total}$")
