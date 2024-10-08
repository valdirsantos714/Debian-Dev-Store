import os

class Dev:

    def __init__(self):
        """
        Inicializa a loja com uma lista de funcionalidades e de executadores.
        """

        self.funcionalidades = ['1 - Criar Projeto NodeJs', "2 - Criar projeto React Native", "3 - Criar Projeto React", "4 - Criar Projeto Angular ", "5 - Sair"]

        self.executadores = ["", self.nodejs_project, self.react_native_project, self.react_project, self.angular_project]


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
░██████╗░█████╗░███████╗████████╗░██╗░░░░░░░██╗░█████╗░██████╗░███████╗
██╔════╝██╔══██╗██╔════╝╚══██╔══╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝
╚█████╗░██║░░██║█████╗░░░░░██║░░░░╚██╗████╗██╔╝███████║██████╔╝█████╗░░
░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░░░████╔═████║░██╔══██║██╔══██╗██╔══╝░░
██████╔╝╚█████╔╝██║░░░░░░░░██║░░░░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║███████╗
╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝

██████╗░███████╗██╗░░░██╗███████╗██╗░░░░░░█████╗░██████╗░███╗░░░███╗███████╗███╗░░██╗████████╗
██╔══██╗██╔════╝██║░░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝████╗░██║╚══██╔══╝
██║░░██║█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░██║░░██║██████╔╝██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
██║░░██║██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░██║░░██║██╔═══╝░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
██████╔╝███████╗░░╚██╔╝░░███████╗███████╗╚█████╔╝██║░░░░░██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚══════╝░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░""")
            
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

        print("\nBem vindo a Loja Software Development!\n")
        print("Escolha uma das opções abaixo:")

        for f in self.funcionalidades:
            print(f)   


    def executar_comando(self, comando):
        """
        Executa um comando no terminal.
        :param comando: O comando a ser executado.
        """
        os.system(comando)


    def nodejs_project(self):
        """
        Automatiza o processo de criação de projetos Node.js.

        Esta função permite ao usuário criar um projeto Node.js utilizando dois 
        frameworks diferentes: Express (JavaScript) e Fastify (TypeScript). O usuário 
        pode escolher o caminho do projeto, o nome do projeto e a tecnologia desejada. 
        Após coletar as informações, a função gera e executa os comandos necessários 
        para criar o projeto, inicializar um repositório Git e instalar as dependências.
        """
        try:
            # Perguntas iniciais
            caminho_absoluto = input("Digite o caminho absoluto (ex: /home/user/Documentos/coisas_uteis) onde você deseja criar o seu projeto: ")
            nome_projeto = input("Digite o nome do projeto que você deseja criar: ")

            # Escolha de linguagem e framework
            print("Escolha a linguagem e framework:")
            print("1 - JavaScript + Express")
            print("2 - TypeScript + Fastify")
            opcao = input("Digite o número da sua escolha: ")

            self.executar_comando("cd")
            os.chdir(caminho_absoluto)

            # Comandos padrão (vão se adaptando conforme a escolha)
            comandos_basicos = [
                f"mkdir {nome_projeto}",
                f"cd {nome_projeto}",
                "npm init -y",
                "echo 'node_modules/' > .gitignore",
                "git init"
            ]

            # Comandos específicos para TypeScript + Fastify
            comandos_typescript_fastify = [
                "npm i typescript -D",
                "npm i fastify",
                "npm i tsx -D",
                "npm i @types/node tsx -D",
                "npm i postgres",
                "npx tsc --init",
                "npm i zod drizzle-orm",
                "npm i drizzle-kit -D",
                """echo '{
                "$schema": "https://json.schemastore.org/tsconfig",
                "_version": "20.1.0",
                "compilerOptions": {
                    "lib": ["es2023"],
                    "module": "node16",
                    "target": "es2022",
                    "strict": true,
                    "esModuleInterop": true,
                    "skipLibCheck": true,
                    "moduleResolution": "node16"
                }
            }' > tsconfig.json""",
                """echo 'import { defineConfig } from "drizzle-kit"
            export default defineConfig({
                schema: "./schema.ts",
                dialect: "postgresql",
                dbCredentials: {
                    url: process.env.DB_URL,
                },
                verbose: true,
                strict: true,
            })' > drizzle.config.ts""",
                """echo 'version: "3.8"
            services:
            db:
                image: postgres:latest
                container_name: postgres_db
                environment:
                POSTGRES_USER: postgres
                POSTGRES_PASSWORD: nodejs
                POSTGRES_DB: database
                volumes:
                - db_data:/var/lib/postgresql/data
                ports:
                - "5433:5432"
            volumes:
            db_data:' > docker-compose.yml""",
                "mkdir src",
                """echo 'import fastify from "fastify"
            const app = fastify()
            app.get("/", () => {
                return "Foi"
            })
            app.listen({ port: 3333 }).then(() => {
                console.log("Server running")
            })' > src/server.ts""",
                """echo 'DB_URL="postgresql://postgres:nodejs@localhost:5433/database"' > .env"""
            ]

            # Comandos para JavaScript + Express
            comandos_javascript_express = [
                "npm i express",
                "mkdir src",
                """echo 'const express = require("express");
            const app = express();
            app.get("/", (req, res) => {
                res.send("Foi");
            });
            app.listen(3333, () => {
                console.log("Server running on port 3333");
            });' > src/server.js"""
            ]

            # Execução dos comandos

            self.executar_comando(comandos_basicos[0])
            os.chdir(caminho_absoluto + f"/{nome_projeto}")
            for i in range(2, len(comandos_basicos)):
                self.executar_comando(comandos_basicos[i])  # Executa os comandos básicos

            
            # Escolha das opções
            if opcao == "1":  # JavaScript + Express
            
                for c in comandos_javascript_express:
                    self.executar_comando(c)

            elif opcao == "2":  # TypeScript + Fastify
                for c in comandos_typescript_fastify:
                    self.executar_comando(c)
            
            print("Projeto criado com sucesso!")
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def react_native_project(self):
        """
        Automatiza o processo de criação de projetos React Native.
        
        Esta função solicita ao usuário informações necessárias para criar um projeto 
        React Native usando o Expo. Ela permite que o usuário escolha entre JavaScript 
        e TypeScript como linguagem, além de perguntar se deseja usar o NativeWind 
        para estilização. Após coletar as informações, a função gera e executa os 
        comandos necessários para criar o projeto e instalar as dependências.
        """
        try:
            caminho_absoluto = input("Digite o caminho absoluto (ex: /home/user/Documentos/coisas_uteis) onde você deseja criar o seu projeto: ")

            nome_projeto = input("Digite o nome do projeto que você deseja criar: ")

            # Escolha de linguagem
            print("Escolha a linguagem:")
            print("1 - JavaScript")
            print("2 - TypeScript")
            linguagem = input("Digite o número da sua escolha: ")

            # Pergunta se o usuário deseja usar NativeWind
            usar_nativewind = input("Deseja usar NativeWind para estilização? (s/n): ")

            # Base do comando para criar o projeto
            if linguagem == "1":
                comando_criar_projeto = f"npx create-expo-app {nome_projeto} --template expo-template-blank"
            elif linguagem == "2":
                comando_criar_projeto = f"npx create-expo-app {nome_projeto} --template expo-template-blank-typescript"
            else:
                print("Opção inválida.")

            # Lista de comandos a serem executados
            lista_comandos = [comando_criar_projeto, "npm i"]

            if usar_nativewind.lower() == 's':
                lista_comandos += [
                    "npm i nativewind",
                    "npm i --save-dev tailwindcss@3.3.2",
                    "npx tailwindcss init",
                    """echo '
    module.exports = function (api) {
    api.cache(true);
    return {
        presets: ['babel-preset-expo'],
        plugins: ['nativewind/babel'],
    };
    };' > babel.config.js""",
                    """echo '
    module.exports = {
    content: ['./src/**/*.{js,jsx,ts,tsx}'],
    theme: {
        extend: {},
    },
    plugins: [],
    };' > tailwind.config.js"""
                ]

            # Executa os comandos
            self.executar_comando(f"cd {caminho_absoluto}")
            os.chdir(caminho_absoluto)
            self.executar_comando(lista_comandos[0])

            os.chdir(caminho_absoluto + f"/{nome_projeto}")
            self.executar_comando(lista_comandos[1])

            if usar_nativewind.lower() == 's':
                for i in (range(2, len(lista_comandos))):
                    self.executar_comando(lista_comandos[i])

            print(f"Projeto React Native '{nome_projeto}' criado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def react_project(self): 
        """
        Automatiza o processo de criação de projetos React.

        Esta função permite ao usuário criar um projeto React utilizando o Vite como 
        bundler. O usuário pode escolher entre várias opções, incluindo JavaScript, 
        TypeScript e a adição de React Router Dom. Após coletar as informações, a 
        função gera e executa os comandos necessários para criar o projeto e 
        instalar as dependências.
        """

        try:
            print("Deseja Criar Projeto React com:")
            print("\n1-Javascript, \n2-Typescript, \n3 - Javascript + React Router Dom, \n4 - Typescript + React Router Dom")
            opcao = int(input("\nDigite a opção desejada: "))

            caminho_absoluto = input("Digite o caminho absoluto (ex: /home/user/Documentos/coisas_uteis) aonde vc deseja criar o seu projeto: \n")

            nome_projeto = input("Digite o nome do projeto que vc deseja criar : ")
            os.system("cd") # cd
            os.chdir(caminho_absoluto) # Entra no caminho especificado

            lista_comandos = []

            if opcao == 1:
                lista_comandos = ["cd", f"npm create vite@latest {nome_projeto} -- --template react", "npm install"]
                os.system(lista_comandos[1])

                os.system(lista_comandos[0]) # cd
                os.chdir(caminho_absoluto + f"/{nome_projeto}")

                for i in range(2,len(lista_comandos)):
                    os.system(lista_comandos[i])

            elif opcao == 2:
                lista_comandos = ["cd", f"npm create vite@latest {nome_projeto} -- --template react-ts", "npm install"]
                os.system(lista_comandos[1])

                os.system(lista_comandos[0]) # cd
                os.chdir(caminho_absoluto + f"/{nome_projeto}")

                for i in range(2,len(lista_comandos)):
                    os.system(lista_comandos[i])
            
            elif opcao == 3:
                lista_comandos = ["cd", f"npm create vite@latest {nome_projeto} -- --template react", "npm install", "npm install react-router-dom"]
                os.system(lista_comandos[1])

                os.system(lista_comandos[0]) # cd
                os.chdir(caminho_absoluto + f"/{nome_projeto}")

                for i in range(2,len(lista_comandos)):
                    os.system(lista_comandos[i])
            
            elif opcao == 4:
                lista_comandos = ["cd", f"npm create vite@latest {nome_projeto} -- --template react-ts", "npm install", "npm install react-router-dom"]
                os.system(lista_comandos[1])

                os.system(lista_comandos[0]) # cd
                os.chdir(caminho_absoluto + f"/{nome_projeto}")

                for i in range(2,len(lista_comandos)):
                    os.system(lista_comandos[i])
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def angular_project(self):
        """
        Automatiza o processo de criação de projetos Angular.

        Esta função permite ao usuário criar um projeto Angular usando a CLI do Angular. 
        O usuário pode escolher entre JavaScript e TypeScript como linguagem, além de 
        decidir se deseja incluir Tailwind CSS, Angular Material e RxJS. Após coletar 
        as informações, a função gera e executa os comandos necessários para criar 
        o projeto e instalar as dependências.
        """
        try:
            caminho_absoluto = input("Digite o caminho absoluto (ex: /home/user/Documentos/coisas_uteis) onde você deseja criar o seu projeto: ")

            nome_projeto = input("Digite o nome do projeto que você deseja criar: ")

            # Escolha de linguagem
            print("Escolha a linguagem:")
            print("1 - JavaScript")
            print("2 - TypeScript (Recomendado)")
            linguagem = input("Digite o número da sua escolha: ")

            # Pergunta se o usuário deseja usar Tailwind CSS
            usar_tailwind = input("Deseja usar Tailwind CSS para estilização? (s/n): ")

            # Pergunta se deseja incluir Angular Material
            incluir_material = input("Deseja incluir Angular Material? (s/n): ")

            # Pergunta se deseja incluir RxJS
            incluir_rxjs = input("Deseja incluir RxJS? (s/n): ")

            # Base do comando para criar o projeto Angular
            if linguagem == "1":
                comando_criar_projeto = f"npx -p @angular/cli ng new {nome_projeto} --skip-install --style css --routing true --strict false"
                os.chdir(caminho_absoluto)
                self.executar_comando(comando_criar_projeto)
                os.chdir(caminho_absoluto + f"/{nome_projeto}")
                
            elif linguagem == "2":
                comando_criar_projeto = f"npx -p @angular/cli ng new {nome_projeto} --skip-install --style css --routing true --strict true"
                os.chdir(caminho_absoluto)
                self.executar_comando(comando_criar_projeto)
                os.chdir(caminho_absoluto + f"/{nome_projeto}")
            
            else:
                print("Opção inválida.")
                return

            # Lista de comandos a serem executados
            lista_comandos = [comando_criar_projeto, f"cd {nome_projeto}", "npm install"]

            # Comandos para instalar e configurar Tailwind CSS, se desejado
            if usar_tailwind.lower() == 's':
                lista_comandos += [
                    "npm install -D tailwindcss@latest postcss@latest autoprefixer@latest",
                    "npx tailwindcss init",
                    """echo 'module.exports = {
    content: ["./src/**/*.{html,ts}"],
    theme: {
        extend: {},
    },
    plugins: [],
    };' > tailwind.config.js""",
                    """echo '@tailwind base;
    @tailwind components;
    @tailwind utilities;' >> src/styles.css"""
                ]

            # Comandos para incluir Angular Material, se desejado
            if incluir_material.lower() == 's':
                lista_comandos.append("ng add @angular/material")

            # Comandos para incluir RxJS, se desejado
            if incluir_rxjs.lower() == 's':
                lista_comandos.append("npm install rxjs")

            lista_comandos.append("ng serve --open")

            for i in range(2,len(lista_comandos)):
                self.executar_comando(lista_comandos[i])

            print(f"Projeto Angular '{nome_projeto}' criado com sucesso!")
        
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

