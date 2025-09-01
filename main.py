import os
from lib import *

if __name__ == "__main__":
    init_input = int(input("insira um valor para iniciar: "))
    fila = Fila.new_fila(init_input)

    while(True):
        print(
            "\ndigite a operação que deseja realizar\n" \
            "\n\"1\" para inserir" \
            "\n\"2\" para remover" \
            "\n\"3\" para imprimir fila"
        )
        option = int(input())
        
        if option == 1:
            input_value = input("\ninsira o valor: ")
            fila.push(input_value)
            option = input("")
            os.system("cls")
        elif option == 2:
            fila.pop()
            option = input("")
            os.system("cls")
        elif option == 3:
            fila.print_fila()
            option = input("")
            os.system("cls")
        else:
            option = input("\ninsira um valor válido")
            os.system("cls")