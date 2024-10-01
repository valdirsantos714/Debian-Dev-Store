import os

def nodejs_typescript_postgres():
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

def install_docker():
    lista_comandos = ["curl -fsSL https://get.docker.com -o get-docker.sh", "sudo sh get-docker.sh"]

    for c in lista_comandos:
        os.system(c)


funcionalidades = ["1 - Criar Projeto NodeJs + Typescript + PostgreSQL + Docker Compose", "2 - Instalar docker", "3", "4", "5 - Sair"]
executadores = ["", nodejs_typescript_postgres, install_docker, "", "", ""]

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

def funcoes():
    for i in range(len(funcionalidades)):
        print(f"{funcionalidades[i]}")

def executa_funcoes(numero):
    executadores[numero]()
    print(f"{executadores[numero]}")

def opcoes():
    logo()
    print('\nBem vindo o que vc deseja fazer?')
    funcoes()

    opcao = 0

    while opcao != 5:
        opcao = int(input('\nDigite um número: '))
        print("\n")
        if opcao == 5:
            print("Programa finalizado!")
        else:
            executa_funcoes(opcao)




opcoes()
