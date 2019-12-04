# API - Cashback

<p>Foi criada uma API para realizar cashback para revendedores de produtos.</p>

## Como executar a API

### Clonar repositório

Clone o repositório no seu computador:
```bash
$ cd pasta-desejada
$ git clone https://github.com/franciellyferreira/api-cashback.git
```

### Banco de dados

<p>
Crie um banco de dados MySQL para esse projeto
</p>

### .Env

Crie um arquivo para armazenar as variáveis de ambiente sensíveis
```bash
$ cd cashback
$ touch .env
```

Adicionar no arquivo .env:
```
SECRET_KEY="Adicionar Secret Key do Projeto Django"
DEBUG="True ou False"

DATABASE_NAME="Nome do Banco de Dados"
DATABASE_USER="Usuário do Banco de Dados"
DATABASE_PASSWORD="Senha do Banco de Dados"
DATABASE_HOST="Host do Banco de Dados"
DATABASE_PORT="Porta do Banco de Dados"

LANGUAGE_CODE=pt-BR
TIME_ZONE=America/Sao_Paulo
```


### Virtualenv

Se você não tiver instalado, faça a instalação do Virtualenv:
```bash
$ pip3 install virtualenv
```

### Ambiente virtual

Criar o ambiente virtual dentro do projeto com Virtualenv:
```bash
$ cd ..
$ virtualenv venv -p python3
```

Ativar o ambiente virtual:
```bash
$ source venv/bin/activate 
```

Instalar as dependências:
```bash
$ pip3 install -r requirements.txt
```

### Migrations

Criar as migrations
```bash
$ cd cashback
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

Criar super usuário para usar na Autenticação JWT
```bash
$ python3 manage.py createsuperuser
```

<p>
Caso você tenha algum problema para instalar a dependência *mysqlclient* que consta no arquivo requirements.txt, tente instalar as seguintes bibliotecas:
```bash
$ sudo apt-get install libssl-dev libffi-dev
```
</p>


### Executar Testes

Executar os testes da aplicação
```bash
$ python3 manage.py test
```

### Executar Servidor

Executar o servidor da aplicação
```bash
$ python3 manage.py runserver
```

### Abrir projeto

[API - Cashback](http://127.0.0.1:8000)

### Autenticação JWT

<p>
Para utilizar os endpoints da API é necessário autenticar
e obter o Token que será usado no cabeçalho dessa forma:
<br> Authorization = Bearer "Token JWT"
</p>

## Documentação - Endpoints da API

Foi utilizado o Postman para gerar uma documentação:<br />
[Documentação da API](https://documenter.getpostman.com/view/2628786/SWE29LLE?version=latest)