from os import system, name
from time import sleep

list_of_book = []

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

print("-----------------------------------------")
print("Bienvenidos a la Biblioteca de Alejandria")
print("-----------------------------------------\n\n")

