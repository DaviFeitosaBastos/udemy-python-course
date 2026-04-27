"""  
Faça uma lista de comprar com listas o usuario deve ter a responsabilidade de inserir, apagar e listar valores da sua lista, nao permita que o programa quebre com erros de indices inexistentes na lista
"""
import os
from time import sleep

shopping_list = []
VALID_OPTIONS = ('i', 'd', 'l')

def clear():
    os.system("clear" if  os.name == "posix" else "cls")

while True:
    clear()

    print(f"Select an option:")
    option = input(f"[i]nsert [d]elet [l]ist: ").lower()

    if option not in VALID_OPTIONS:
        print("Invalid option!")
        sleep(0.8)
        continue

    match option:

        case 'i':
            insert = input(f"Name: ")
            if insert in shopping_list:
                print("It's already added")
                sleep(0.8)
                continue
            shopping_list.append(insert)
        case 'd':
            while True:
                if not shopping_list :
                    print("Empty list")
                    sleep(0.8)
                    break
                clear()
                print("Select the ID to delete from your list")

                for indice, item in enumerate(shopping_list, start=1):
                    print(f"{indice} - {item} |", end=" ")

                try:
                    choice = int(input('\nType here: '))

                    if choice < 1 or choice > len(shopping_list):
                        print(f"ID doesn't exist: {choice}")
                        sleep(0.8)
                        continue

                    shopping_list.pop(choice - 1)  # pop() use indice, -1 for start=1
                    input("Press to return to main menu: ")
                    break

                except ValueError:
                    print("Error: expected integer number")
                    sleep(0.8)

            
        case 'l':
            if not shopping_list:
                print("You haven't added anything yet")
                sleep(0.8)
                continue
            for indice, item in enumerate(shopping_list, start=1):
                print(f"{indice} - {item}")

            input("Press to return to main menu: ")
                


