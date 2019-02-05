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

option = 0
while option == 9:
    print("Seleccione la opción: \n1.Crear Libro \n2.Mostrar Libros")
