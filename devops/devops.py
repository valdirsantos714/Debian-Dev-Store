import os

class Devops:

    def __init__(self):
        """
        Inicializa a loja com uma lista de funcionalidades e de executadores.
        """

        self.funcionalidades = ['1 - Instalar Docker', "2 - Instalar Ansible", "3 - Instalar Terraform", "4 - Executar Prometheus", "5 - Sair", "6 - Instalar Jenkins", "7 - Instalar Kubernates"]

        self.executadores = ["", self.install_docker, self.install_ansible, self.install_terraform, self.prometheus, "", self.install_jenkins, self.install_kubernates]


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
                os.system("clear")
            else:
                self.executa_funcoes(opcao)

        
    def mostra_funcionalidade(self):
        """
        Exibe as funcionalidades disponíveis na loja.

        Esta função imprime uma mensagem de boas-vindas e lista as opções disponíveis 
        que o usuário pode escolher. Cada funcionalidade é mostrada em uma linha 
        separada, permitindo que o usuário saiba quais ações podem ser realizadas.
        """

        print("\nBem vindo a Loja Devops!\n")
        print("Escolha uma das opções abaixo:")

        for f in self.funcionalidades:
            print(f)   

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

    def install_ansible(self):
        """
        Instala o Ansible no sistema.

        Este método atualiza os pacotes do sistema, instala as dependências necessárias, 
        adiciona o repositório do Ansible e instala o Ansible.
        """

        try:

            lista_comandos = ["sudo apt update", "sudo apt-get install -y software-properties-common", "sudo add-apt-repository --yes --update ppa:ansible/ansible", "sudo apt update", "sudo apt-get install ansible", "ansible --version"]

            for c in lista_comandos:
                os.system(c)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def install_terraform(self):
        """
        Instala o Terraform no sistema.

        Este método configura o repositório do Terraform e instala a ferramenta.
        """

        try:
            lista_comandos = ["wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg", "echo 'deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main' | sudo tee /etc/apt/sources.list.d/hashicorp.list", "sudo apt update && sudo apt install terraform"]

            for c in lista_comandos:
                os.system(c)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def prometheus(self):
        """
        Instala o Prometheus utilizando o Docker.

        Este método executa o container do Prometheus na porta 9090. 
        """

        try:

            lista_comandos = ["docker run -d -p 9090:9090 prom/prometheus"]

            for c in lista_comandos:
                os.system(c)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def install_jenkins(self):
        """
        Instala o Jenkins no sistema.

        Este método baixa a chave do repositório do Jenkins, adiciona o repositório e 
        instala o Jenkins. 
        """

        try:

            lista_comandos = ["sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
    https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key echo 'deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]' \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null", "sudo apt-get update", "sudo apt-get install jenkins"]
            
            for c in lista_comandos:
                os.system(c)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    
    def install_kubernates(self):
        """
        Instala o Kubernetes no sistema.

        Este método adiciona a chave do repositório do Kubernetes, configura o repositório e 
        instala os componentes kubeadm, kubelet e kubectl.
        """

        try:

            lista_comandos = ["curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg", "echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list", "sudo apt update", "sudo apt install kubeadm kubelet kubectl", "sudo apt-mark hold kubeadm kubelet kubectl", "kubeadm version"]

            for c in lista_comandos:
                os.system(c)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
