# 🔐 Gerenciador de Credenciais — Python

Um sistema simples de armazenamento de credenciais desenvolvido em **Python**, utilizando criptografia para proteger as senhas armazenadas localmente.

O projeto foi desenvolvido com finalidade de **aprendizagem**, com o objetivo de estudar conceitos de criptografia, manipulação de arquivos, gerenciamento de chaves e tratamento de exceções em Python.

---

## 📌 Sobre o projeto

A aplicação permite armazenar credenciais localmente em um arquivo de texto, utilizando uma chave criptográfica para proteger as senhas antes de serem armazenadas.

O fluxo básico da aplicação é:

```text
Título + Senha
      ↓
Criptografia Fernet
      ↓
Arquivo local
      ↓
Senha criptografada
```

Quando o usuário solicita a listagem das credenciais, a aplicação utiliza a chave armazenada localmente para descriptografar os dados.

---

## ⚙️ Funcionalidades

* 🔑 Geração de chave criptográfica
* 🔐 Criptografia das senhas utilizando Fernet
* 💾 Armazenamento local das credenciais
* 🔓 Descriptografia das senhas para consulta
* ⚠️ Tratamento de chaves inválidas
* 📁 Manipulação de arquivos
* 🖥️ Interface através do terminal

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **Cryptography**
* **Fernet**
* **OS / File System**
* **Git / GitHub**

### Biblioteca externa

O projeto utiliza a biblioteca:

```text
cryptography
```

Instalação:

```bash
pip install cryptography
```

Ou, utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 📦 Estrutura do projeto

```text
Password_Saver/
│
├── systm.py
├── requirements.txt
├── README.md
└── .gitignore
```

Durante a execução, a aplicação utiliza arquivos locais para armazenar a chave e as credenciais:

```text
ky.key
arqpss.txt
```

Esses arquivos **não devem ser enviados ao GitHub**.

---

## 🔐 Como funciona a criptografia?

O projeto utiliza o **Fernet**, disponibilizado pela biblioteca `cryptography`.

A chave criptográfica é gerada através de:

```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
```

A senha fornecida pelo usuário é então criptografada:

```python
encrypted_password = cipher.encrypt(password.encode())
```

O resultado criptografado é armazenado localmente.

Para recuperar a senha, a aplicação utiliza a mesma chave:

```python
password = cipher.decrypt(encrypted_password).decode()
```

### ⚠️ Importante

O sistema utiliza **criptografia simétrica**.

Isso significa que a mesma chave utilizada para criptografar os dados é necessária para descriptografá-los.

Portanto:

> **A perda da chave significa a perda do acesso às credenciais criptografadas.**

---

## 🔑 Segurança da chave

A chave criptográfica é um dos componentes mais importantes da aplicação.

O arquivo:

```text
ky.key
```

**não deve ser publicado no GitHub.**

Da mesma forma, o arquivo contendo as credenciais:

```text
arqpss.txt
```

também não deve ser versionado.

### ⚠️ Por que isso é importante?

A criptografia protege os dados enquanto a chave permanece secreta.

Se uma pessoa obtiver:

```text
ky.key
```

e:

```text
arqpss.txt
```

ela poderá utilizar a chave para descriptografar as credenciais.

Por esse motivo, esses arquivos devem ser protegidos e adicionados ao `.gitignore`.

Exemplo:

```gitignore
ky.key
arqpss.txt

__pycache__/
*.pyc

.venv/
venv/

.env
```

---

## 🚀 Executando o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Gilson2/Password_Saver.git
```

### 2. Entre no diretório

```bash
cd Password_Saver
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual no Windows

```bash
.venv\Scripts\activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute a aplicação

```bash
python systm.py
```

---

## 🖥️ Exemplo de utilização

Ao executar a aplicação:

```text
Sistema de armazenamento de Credenciais

1 - Salvar Nova Senha
2 - Listar Senhas
9 - Criar Nova Chave
0 - Sair
```

Ao salvar uma credencial:

```text
Digite o título da senha: GitHub
Digite a senha:
Senha 'GitHub' salva com sucesso
```

A senha não é armazenada em texto puro.

Um exemplo conceitual do arquivo de armazenamento:

```text
GitHub|gAAAAAB...
Email|gAAAAAB...
Sistema|gAAAAAB...
```

O conteúdo após `|` representa o valor criptografado.

---

## ⚠️ Aviso importante

Este projeto foi desenvolvido para **fins educacionais e de demonstração**.

Embora utilize criptografia para proteger as credenciais armazenadas, ele **não deve ser considerado um gerenciador de senhas profissional ou uma solução de segurança para ambientes de produção**.

Um sistema de gerenciamento de credenciais destinado à produção precisaria implementar outras medidas de segurança, como:

* Proteção adequada da chave criptográfica
* Controle de acesso
* Autenticação
* Proteção contra ataques locais
* Armazenamento seguro
* Auditoria
* Backup seguro
* Gerenciamento adequado de segredos

---

## 📚 Objetivos de aprendizagem

Este projeto foi desenvolvido para praticar conceitos de:

* Programação em Python
* Funções
* Estruturas condicionais
* Manipulação de arquivos
* Tratamento de exceções
* Criptografia simétrica
* Gerenciamento de chaves
* Organização de projetos
* Gerenciamento de dependências
* Git e GitHub

---

## 🔮 Próximas melhorias

Algumas funcionalidades que podem ser implementadas futuramente:

* [ ] Interface gráfica
* [ ] Geração automática de senhas fortes
* [ ] Pesquisa de credenciais
* [ ] Edição de credenciais
* [ ] Exclusão de credenciais
* [ ] Confirmação de identidade do usuário
* [ ] Banco de dados
* [ ] Melhor gerenciamento da chave criptográfica
* [ ] Testes automatizados
* [ ] Logs de operações
* [ ] Empacotamento da aplicação

---

## 👨‍💻 Autor

**Gilson Calixto Neves**

Projeto desenvolvido como parte do processo de aprendizagem e aprimoramento em **desenvolvimento de software, Python e segurança da informação**.
