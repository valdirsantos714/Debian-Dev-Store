import os

class EssentialTools:
    
    def __init__(self):
        """
        Inicializa a loja com uma lista de funcionalidades e de executadores.
        """

        self.funcionalidades = ['1 - Instalar Git', "2 - Instalar Docker ", "3 - Instalar OpenSSH Server", "4 - Instalar VS Code", "5 - Sair", "6 - Instalar Terminator (Terminal Com autocomplete)", "7 - Instalar Node JS"]

        self.executadores = ["", self.install_git, self.install_docker, self.install_openssh, self.install_vscode, "", self.install_terminator, self.install_nodejs]


    def inicio(self):
        """
        Inicia o menu principal da loja, permitindo ao usuário escolher uma 
        funcionalidade.

        Esta função limpa a tela, exibe o cabeçalho da loja e apresenta 
        as opções disponíveis. O usuário pode escolher uma opção 
        digitando o número correspondente. A função continua 
        executando até que o usuário escolha a opção para sair.
        """

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
        """
        Executa a função correspondente à opção escolhida pelo usuário.

        Este método chama a função associada ao número fornecido, que 
        representa uma das funcionalidades disponíveis. Após a execução, 
        imprime o nome da função executada.

        Parâmetros:
        numero (int): O número da opção escolhida pelo usuário.
        """

        self.executadores[numero]()
        print(f"{self.executadores[numero]}")

    def mostra_funcionalidade(self):
        """
        Exibe as funcionalidades disponíveis na loja.

        Esta função imprime uma mensagem de boas-vindas e lista as opções disponíveis 
        que o usuário pode escolher. Cada funcionalidade é mostrada em uma linha 
        separada, permitindo que o usuário saiba quais ações podem ser realizadas.
        """

        print("\nBem vindo a Loja Essential Tools!\n")
        print("Escolha uma das opções abaixo:")

        for f in self.funcionalidades:
            print(f)   

    def install_git(self):
        """
        Instala o Git no sistema usando comandos de terminal.

        Este método atualiza os pacotes do sistema, instala o Git e 
        verifica a versão instalada.
        """
        try:
            lista_comandos = ["sudo apt update", "sudo apt install git", "git --version"]

            for c in lista_comandos:
                os.system(c)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")


    def install_docker(self):
        """
        Instala o Docker no sistema.

        Este método baixa e executa o script de instalação do Docker.
        """
        try:
            lista_comandos = ["curl -fsSL https://get.docker.com -o get-docker.sh", "sudo sh get-docker.sh"]

            for c in lista_comandos:
                os.system(c)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    
    def install_openssh(self):
        """
        Instala o OpenSSH Server no sistema.

        Este método atualiza os pacotes do sistema, instala o OpenSSH, 
        inicia o serviço SSH e o habilita para iniciar na inicialização. 
        """
        
        try:
            lista_comandos = ["sudo apt update", "sudo apt install openssh-server", "sudo systemctl status ssh", "sudo systemctl start ssh", "sudo systemctl enable ssh"]

            for c in lista_comandos:
                os.system(c)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    
    def install_vscode(self):
        """
        Instala o Visual Studio Code no sistema.

        Este método configura o repositório do VS Code e instala o editor.
        """
        try:
            lista_comandos = ["sudo apt update", "sudo apt install apt-transport-https curl", "curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/vscode.gpg", "echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/vscode.gpg] https://packages.microsoft.com/repos/code stable main' | sudo tee /etc/apt/sources.list.d/vscode.list", "sudo apt update", "sudo apt install code"]

            for c in lista_comandos:
                os.system(c)
                
        except Exception as e:
            print(f"Ocorreu um erro: {e}")



    def install_terminator(self):
        """
        Instala o Terminator, Zsh e configura o Oh My Zsh no sistema.

        Este método instala o Terminator, o shell Zsh e algumas 
        personalizações, incluindo plugins e temas.
        """
        try:
            lista_comandos = ["sudo apt-get install terminator", "sudo apt-get install zsh", "chsh -s $(which zsh)", "sh -c '$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)'", "sudo apt-get install fonts-powerline", "git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions", "git clone https://github.com/zsh-users/zsh-syntax-highlighting.git", "echo 'source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh' >> ${ZDOTDIR:-$HOME}/.zshrc", "sudo apt install git zsh zsh-autosuggestions zsh-syntax-highlighting fzf -y", "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k"]

            for c in lista_comandos:
                os.system(c)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    
    def install_nodejs(self):
        """
        Instala o Node.js no sistema.

        Este método atualiza o sistema, configura o repositório do Node.js 
        e instala a versão LTS do Node.js e do NPM.
        """
        try:
            lista_comandos = ["sudo apt update && sudo apt upgrade -y", "curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -", "sudo apt-get install -y nodejs", "node -v",  "npm -v"]

            for c in lista_comandos:
                os.system(c)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
