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
<p>
Adicionar no arquivo .env:
<br>SECRET_KEY=<SECRET_KEY_DJANGO_PROJECT>
<br>DEBUG=<True>
<br><br>DATABASE_NAME=<NOME_BANCO>
<br>DATABASE_USER=<USUARIO_BANCO>
<br>DATABASE_PASSWORD=<SENHA_BANCO>
<br>DATABASE_HOST=<HOST_BANCO>
<br>DATABASE_PORT=<PORTA_BANCO>
<br><br>LANGUAGE_CODE=pt-BR
<br>TIME_ZONE=America/Sao_Paulo
</p>


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

Criar super usuário para usar na autenticação
```bash
$ python3 manage.py createsuperuser
```

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
<br> Authorization = Bearer <Token_JWT>
</p>

## Endpoints da API

Foi utilizado o Postman para gerar uma documentação:<br />
[Documentação da API](https://documenter.getpostman.com/view/2628786/SWE29LLE?version=latest)