import os

class Dev:

    def __init__(self):
        self.funcionalidades = ['1 - Criar Projeto NodeJs + Typescript + PostgreSQL', "2 - ", "3 - ", "4 - ", "5 - Sair"]

        self.executadores = ["", self.nodejs_typescript_postgres]


    def inicio(self):
        os.system("clear")
        opcao = 0

        while opcao != 5:
            print("""

██████╗░███████╗██╗░░░██╗███████╗██╗░░░░░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔════╝██║░░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░██║█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░██║░░██║██████╔╝█████╗░░██████╔╝
██║░░██║██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░██║░░██║██╔═══╝░██╔══╝░░██╔══██╗
██████╔╝███████╗░░╚██╔╝░░███████╗███████╗╚█████╔╝██║░░░░░███████╗██║░░██║
╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚══════╝░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝""")
            
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
        print("Bem vindo a Loja de ferramenta Devops!\n")
        print("Escolha uma das opções abaixo:")

        for f in self.funcionalidades:
            print(f)   


    def nodejs_typescript_postgres(self):
        lista_comandos = ["cd", "mkdir", "npm init -y", "npm init -y", "npm i typescript -D", "npm i fastify", "npm i tsx -D", "npm i @types/node tsx -D", "npm i postgres", "npx tsc --init", "npm i zod drizzle-orm", "npm i drizzle-kit -D", "echo 'node_modules/' > .gitignore", "git init","""echo '{
    '$schema': 'https://json.schemastore.org/tsconfig',
    '_version': '20.1.0',

    'compilerOptions': {
        'lib': ['es2023'],
        'module': 'node16',
        'target': 'es2022',

        'strict': true,
        'esModuleInterop': true,
        'skipLibCheck': true,
        'moduleResolution': 'node16'
    }
    }
    ' > tsconfig.json""", 
    """echo 'import { defineConfig } from 'drizzle-kit'
    export default defineConfig({
    schema: "./schema.ts",
    dialect: 'postgresql',
    dbCredentials: {
        url: process.env.DB_URL,
    },
    verbose: true,
    strict: true,
    })' > drizzle.config.ts""", """echo '
    version: '3.8'

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
    db_data:

    ' > docker-compose.yml""", "mkdir src", """echo '
    import fastify from 'fastify'

    const app = fastify()

    app.get('/', () => {
    return 'Foi'
    })

    app
    .listen({
        port: 3333,
    })
    .then(() => {
        console.log('Server running')
    })

    ' > server.ts""", """echo '
    DB_URL="postgresql://postgres:nodejs@localhost:5433/database"
    ' > .env"""]

        caminho = "/home/valdir/Documentos/z_coisas_uteis"
        #caminhoAbsoluto = input("Digite o caminho absoluto (ex: /home/user/Documentos/coisas_uteis) aonde vc deseja criar o seu projeto: ")

        nome_projeto = input("Digite o nome do projeto que vc deseja criar : ")
        os.system(lista_comandos[0]) # cd
        os.chdir(caminho) # Entra no caminho especificado
        os.system(lista_comandos[1] + f" {nome_projeto}") # Cria pasta
        os.system(lista_comandos[0]) # cd
        os.chdir(caminho + f"/{nome_projeto}")

        for i in range(2,len(lista_comandos)):
            os.system(lista_comandos[i])

