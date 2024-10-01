import os

class Devops:

    funcionalidades = ['1 - Instalar docker', "2 - Hello world Docker", "3 - ", "4 - ", "5 - Sair"]

    def inicio(self):
        os.system("clear")
        opcao = 0

        while opcao != 5:
            print("""
██████╗░███████╗██╗░░░██╗░█████╗░██████╗░░██████╗
██╔══██╗██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔════╝
██║░░██║█████╗░░╚██╗░██╔╝██║░░██║██████╔╝╚█████╗░
██║░░██║██╔══╝░░░╚████╔╝░██║░░██║██╔═══╝░░╚═══██╗
██████╔╝███████╗░░╚██╔╝░░╚█████╔╝██║░░░░░██████╔╝
╚═════╝░╚══════╝░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═════╝░""")
            
            self.mostra_funcionalidade()
            opcao = int(input('\nDigite a opção desejada: '))

            print("\n")

            if opcao == 5:
                print("Programa finalizado!")
            else:
                self.executa_funcoes(opcao)

        
    def mostra_funcionalidade(self):
        print("Bem vindo a Loja de ferramenta Devops!\n")
        print("Escolha uma das opções abaixo:")

        for f in self.funcionalidades:
            print(f)   

    def executa_funcoes(self, numero):

        executadores = ["", self.install_docker, self.hello_world_docker]
        executadores[numero]()
        print(f"{executadores[numero]}")

    def hello_world_docker(self):
        os.system("sudo docker run hello-world")

    def install_docker(self):
        lista_comandos = ["curl -fsSL https://get.docker.com -o get-docker.sh", "sudo sh get-docker.sh"]

        for c in lista_comandos:
            os.system(c)

