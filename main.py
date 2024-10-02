import os
from devops import Devops
from developer import Dev

def logo():
    print("""
██╗░░░██╗██████╗░██╗░░░██╗███╗░░██╗████████╗██╗░░░██╗  ██████╗░███████╗██╗░░░██╗
██║░░░██║██╔══██╗██║░░░██║████╗░██║╚══██╔══╝██║░░░██║  ██╔══██╗██╔════╝██║░░░██║
██║░░░██║██████╦╝██║░░░██║██╔██╗██║░░░██║░░░██║░░░██║  ██║░░██║█████╗░░╚██╗░██╔╝
██║░░░██║██╔══██╗██║░░░██║██║╚████║░░░██║░░░██║░░░██║  ██║░░██║██╔══╝░░░╚████╔╝░
╚██████╔╝██████╦╝╚██████╔╝██║░╚███║░░░██║░░░╚██████╔╝  ██████╔╝███████╗░░╚██╔╝░░
░╚═════╝░╚═════╝░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░  ╚═════╝░╚══════╝░░░╚═╝░░░

░██████╗████████╗░█████╗░██████╗░███████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝""")

def apresentacao():
    logo()
    print('\nBem vindo o que vc deseja fazer está relacionada a que área?')
    areas = ["1 - Devops, 2 - Development, 5 - Sair"]

    for a in areas:
      print(a)

def opcoes():
    opcao = 0

    while opcao != 5:
        apresentacao()
        opcao = int(input('\nDigite um número: '))
        print("\n")

        if opcao == 5:
            print("Programa finalizado!")
        elif opcao == 1:
            devop = Devops()
            devop.inicio()
        elif opcao == 2:
            dev = Dev()
            dev.inicio()

opcoes()