#!/usr/bin/python3
#-*-Coding:utf-8 -*-


import products
import cart

def main():
    print("Byenvini nan boutik an liy nou an !")
    while True:
        print("\nMeni:")
        print("1. Chache pwodwi")
        print("2. We panye ak pri total yo")
        print("3. Femen")
        
        choice = input("Chwazi yon opsyon : ")
        
        if choice == "1":
            products.display_products()
        elif choice == "2":
            cart.display_cart()
        elif choice == "3":
            print("Mesi paskew te itilize boutik an liy nou an !")
            break
        else:
            print("Opsyon sa pa valide. Svp chwazi yon opsyon ki valide.")

if __name__ == "__main__":
    main()
