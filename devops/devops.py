import os

class Devops:

    def __init__(self):
        self.funcionalidades = ['1 - Instalar docker', "2 - Instalar Ansible", "3 - Instalar Terraform", "4 - Executar Prometheus", "5 - Sair", "6 - Instalar Jenkins", "7 - Instalar Kubernates"]

        self.executadores = ["", self.install_docker, self.install_ansible, self.install_terraform, self.prometheus, "", self.install_jenkins, self.install_kubernates]


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
                os.system("clear")
            else:
                self.executa_funcoes(opcao)

        
    def mostra_funcionalidade(self):
        print("\nBem vindo a Loja Devops!\n")
        print("Escolha uma das opções abaixo:")

        for f in self.funcionalidades:
            print(f)   

    def executa_funcoes(self, numero):

        self.executadores[numero]()
        print(f"{self.executadores[numero]}")

    def install_docker(self):
        lista_comandos = ["curl -fsSL https://get.docker.com -o get-docker.sh", "sudo sh get-docker.sh"]

        for c in lista_comandos:
            os.system(c)

    def install_ansible(self):
        lista_comandos = ["sudo apt update", "sudo apt-get install -y software-properties-common", "sudo add-apt-repository --yes --update ppa:ansible/ansible", "sudo apt update", "sudo apt-get install ansible", "ansible --version"]

        for c in lista_comandos:
            os.system(c)

    def install_terraform(self):
        lista_comandos = ["wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg", "echo 'deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main' | sudo tee /etc/apt/sources.list.d/hashicorp.list", "sudo apt update && sudo apt install terraform"]

        for c in lista_comandos:
            os.system(c)

    def prometheus(self):
        lista_comandos = ["docker run -d -p 9090:9090 prom/prometheus"]

        for c in lista_comandos:
            os.system(c)
    
    def install_jenkins(self):
        lista_comandos = ["sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key echo 'deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]' \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null", "sudo apt-get update", "sudo apt-get install jenkins"]
        
        for c in lista_comandos:
            os.system(c)
        
    
    def install_kubernates(self):
        lista_comandos = ["curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg", "echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list", "sudo apt update", "sudo apt install kubeadm kubelet kubectl", "sudo apt-mark hold kubeadm kubelet kubectl", "kubeadm version"]

        for c in lista_comandos:
            os.system(c)
