import os
from devops.devops import Devops
from software_development.developer import Dev
from essential_tools.essential_tools import EssentialTools 

def logo():
    print("""

██████╗░███████╗██████╗░██╗░█████╗░███╗░░██╗  ██████╗░███████╗██╗░░░██╗
██╔══██╗██╔════╝██╔══██╗██║██╔══██╗████╗░██║  ██╔══██╗██╔════╝██║░░░██║
██║░░██║█████╗░░██████╦╝██║███████║██╔██╗██║  ██║░░██║█████╗░░╚██╗░██╔╝
██║░░██║██╔══╝░░██╔══██╗██║██╔══██║██║╚████║  ██║░░██║██╔══╝░░░╚████╔╝░
██████╔╝███████╗██████╦╝██║██║░░██║██║░╚███║  ██████╔╝███████╗░░╚██╔╝░░
╚═════╝░╚══════╝╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝  ╚═════╝░╚══════╝░░░╚═╝░░░

░██████╗████████╗░█████╗░██████╗░███████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝""")

def apresentacao():
    """
    Exibe o logo e apresenta as opções de áreas disponíveis.
    """

    logo()
    print('\nBem vindo o que vc deseja fazer está relacionada a que área?')
    areas = ["1 - Devops", "2 - Software Development", "3 - Essential Tools", "4 - Sair"]

    for a in areas:
      print(a)

def opcoes():
    """
    Exibe o menu de opções e processa a escolha do usuário.
    """

    opcao = 0

    while opcao != 4:
        apresentacao()

        try:
            opcao = int(input('\nDigite um número: '))
            print("\n")

            if opcao == 4:
                print("Programa finalizado!")
            elif opcao == 1:
                devop = Devops()
                devop.inicio()
            elif opcao == 2:
                dev = Dev()
                dev.inicio()
            elif opcao == 3:
                tools = EssentialTools()
                tools.inicio()
        except ValueError:
            print("Por favor, digite um número válido.")

opcoes()