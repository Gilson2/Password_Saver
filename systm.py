
import os
from cryptography.fernet import Fernet
import systm
from cryptography.fernet import InvalidToken

arq = 'arqpss.txt'
kyloc = 'ky.key' 
A = 10


def executar(nome):
    print(f"executando o arquivo {nome}")

def console_menu():
    while A < 20:
        print ("Sistema de armazenamento de Credencial")
        opção = input("1- Salvar Nova Senha. \n2- Para listar Senhas\n")
        if opção == "1":
            if not kyloc or not os.path.exists(kyloc):
                return print("Erro: arquivo de chave vazio/Não encontrado")

            titulo = input("Digite o título da senha: ")
            senha = input("Digite a senha: ")
            resultado = salvar_senha(titulo, senha)
            print(resultado)

        if opção == "2":
            try:
                # carrega a chave
                with open(kyloc, 'rb') as f:
                    key = f.read().strip()
                    if not kyloc or not key:
                        print("Erro: arquivo de chave vazio/Não encontrado")
                        return
                    
                sh = Fernet(key)

                # lê o arquivo de senhas
                with open(arq, "r") as f:
                    for line in f:
                        titulo, encrypted_senha = line.strip().split("|")
                        senha = sh.decrypt(encrypted_senha.encode()).decode()
                        print(f"Título: {titulo}, Senha: {senha}")

                    
            except FileNotFoundError:
                print("Erro: arquivo de chave ou de senhas não encontrado")

            except InvalidToken:
                print("Erro: chave inválida")


        if opção == "9": #PARA CRIAR UM ARQUIVO KEY NOVO
            key = Fernet.generate_key()

            with open(kyloc, 'wb') as f:
                if os.path.exists(kyloc):
                    print("Arquivo de chave já existe. Não será criado um novo.")
                    deseja = input("Deseja substituir a chave existente? (s/n): ")
                    if deseja.lower() == 's':
                        f.write(key)
                        print(f"Nova Key criada:{key}")
                        deseja = input("Devido a alteração da key, todas as senhas salvas anteriormente não poderão ser recuperadas. Deseja apagar o arquivo de senhas? (s/n): ")
                        if deseja.lower() == 's':
                            if os.path.exists(arq):
                                os.remove(arq)
                                print("Arquivo de senhas apagado.")
                            else:
                                print("Arquivo de senhas não encontrado.")

                        sh = Fernet(key)

def salvar_senha(titulo: str, senha: str) -> str:
    try:
        # carrega a chave
        with open(kyloc, 'rb') as f:
            key = f.read().strip()
        if not kyloc or not key:
            return "Erro: arquivo de chave vazio/Não encontrado"
        sh = Fernet(key)

        encrypted_senha = sh.encrypt(senha.encode()).decode()

        # salva no arquivo
        with open(arq, "a") as f:
            f.write(f"{titulo}|{encrypted_senha}\n")

        return f"Senha '{titulo}' salva com sucesso"

    except FileNotFoundError:
        return "Erro: arquivo de chave não encontrado"

    except InvalidToken:
        return "Erro: chave inválida"


## INFORMAÇÕES IMPORTANTES: OS ARQUIVOS AQUI PRESENTES SÃO EXEMPLOS E NÃO DEVEM SER USADOS EM AMBIENTES DE PRODUÇÃO. ESTE CÓDIGO É APENAS PARA FINS EDUCACIONAIS E DE TESTE. NÃO É RECOMENDADO ARMAZENAR SENHAS EM TEXTO SIMPLES OU USAR CHAVES FIXAS EM APLICAÇÕES REAIS.


console_menu()

if __name__ == "__main__":
    console_menu()