import os

class EssentialTools:
    
    def __init__(self):
        self.funcionalidades = ['1 - Instalar Git', "2 - Instalar Docker ", "3 - Instalar OpenSSH Server", "4 - Instalar VS Code", "5 - Sair", "6 - Instalar Terminator (Terminal Com autocomplete)", "7 - Instalar Node JS"]

        self.executadores = ["", self.install_git, self.install_docker, self.install_openssh, self.install_vscode, "", self.install_terminator, self.install_nodejs]


    def inicio(self):
        os.system("clear")
        opcao = 0

        while opcao != 5:
            print("""

███████╗░██████╗░██████╗███████╗███╗░░██╗████████╗██╗░█████╗░██╗░░░░░  ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
██╔════╝██╔════╝██╔════╝██╔════╝████╗░██║╚══██╔══╝██║██╔══██╗██║░░░░░  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
█████╗░░╚█████╗░╚█████╗░█████╗░░██╔██╗██║░░░██║░░░██║███████║██║░░░░░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
██╔══╝░░░╚═══██╗░╚═══██╗██╔══╝░░██║╚████║░░░██║░░░██║██╔══██║██║░░░░░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
███████╗██████╔╝██████╔╝███████╗██║░╚███║░░░██║░░░██║██║░░██║███████╗  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
╚══════╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░""")
            
            self.mostra_funcionalidade()
            opcao = int(input('\nDigite a opção desejada: '))

            print("\n")

            if opcao == 5:
                os.system("clear")
            else:
                self.executa_funcoes(opcao)

    def executa_funcoes(self, numero):

        self.executadores[numero]()
        print(f"{self.executadores[numero]}")

    def mostra_funcionalidade(self):
        print("\nBem vindo a Loja Essential Tools!\n")
        print("Escolha uma das opções abaixo:")

        for f in self.funcionalidades:
            print(f)   

    def install_git(self):
        lista_comandos = ["sudo apt update", "sudo apt install git", "git --version"]

        for c in lista_comandos:
            os.system(c)

    def install_docker(self):
        lista_comandos = ["curl -fsSL https://get.docker.com -o get-docker.sh", "sudo sh get-docker.sh"]

        for c in lista_comandos:
            os.system(c)
    
    def install_openssh(self):
        lista_comandos = ["sudo apt update", "sudo apt install openssh-server", "sudo systemctl status ssh", "sudo systemctl start ssh", "sudo systemctl enable ssh"]

        for c in lista_comandos:
            os.system(c)
    
    def install_vscode(self):
        lista_comandos = ["sudo apt update", "sudo apt install apt-transport-https curl", "curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/vscode.gpg", "echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/vscode.gpg] https://packages.microsoft.com/repos/code stable main' | sudo tee /etc/apt/sources.list.d/vscode.list", "sudo apt update", "sudo apt install code"]

        for c in lista_comandos:
            os.system(c)


    def install_terminator(self):
        lista_comandos = ["sudo apt-get install terminator", "sudo apt-get install zsh", "chsh -s $(which zsh)", "sh -c '$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)'", "sudo apt-get install fonts-powerline", "git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions", "git clone https://github.com/zsh-users/zsh-syntax-highlighting.git", "echo 'source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh' >> ${ZDOTDIR:-$HOME}/.zshrc", "sudo apt install git zsh zsh-autosuggestions zsh-syntax-highlighting fzf -y", "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k"]

        for c in lista_comandos:
            os.system(c)
    
    def install_nodejs(self):
        lista_comandos = ["sudo apt update && sudo apt upgrade -y", "curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -", "sudo apt-get install -y nodejs", "node -v",  "npm -v"]

        for c in lista_comandos:
            os.system(c)