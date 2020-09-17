# Desafio técnico da Atados

Este código trata-se da resolução para o desafio proposto pela Atados.
O desafio proposto baseia-se na construção de uma API que comporte a 
inclusão de voluntários e ações sociais.


## Getting Started

Para iniciar, realiza-se a clonagem do projeto na máquina local.
Após baixar o projeto, para executá-lo basta rodar o comando
```
docker-compose up
``` 
e então aguardar que o container docker suba, que logo então todas as 
rotas e acessos da api estarão disponíveis para uso.

### Pré-requisitos

- Docker
- Python 3

### Instalação

Para executar o projeto, basta rodar o comando
```
docker-compose up
``` 
e então aguardar que o container docker suba. 
Após o container subir, todas as rotas da aplicação se tornarão disponíveis
para acesso e testes, conforme suas próprias regras.

## Executanto os testes

Para executar os testes, antes é preciso acessar o bash do Docker 
referente a api. Para isso, com o container ainda rodando em outra janela, 
basta executar o comando 
```
docker exec -it api_atados bash
``` 
que com isso terá acesso ao bash da api. Feito isso, 
acessa-se a pasta **src** pelo terminal e após isso tem-se acesso aos 
testes que podem ser executados das seguintes maneiras 
seguindo de base os exemplos:

* **Todos disponíveis -** _python manage.py test --pattern="test\_*.py"_
* **Por módulo -** _python manage.py test tests.autenticacao_
* **Individual -** _python manage.py test tests.autenticacao.test_api_

### Explicação dos testes

Os testes feitos tem como base avaliar o CRUD geral das 
rotas da aplicação, também verificando se as regras e políticas de 
cada uma delas está sendo seguida devidamente.


## Deployment

Para testa o sistema de forma local, realiza-se primeiro a clonagem 
do projeto na máquina local.
Após baixar o projeto, para executá-lo basta rodar o comando
```
docker-compose up
``` 
e então aguardar que o container docker suba, que logo então todas as 
rotas e acessos da api estarão disponíveis para uso, que são:

* **/api/v1/criar-usuario/ -** Para criar usuário que será utilizado 
em fins de adição de novas instâncias de ação e voluntário no sistema.
* **/api/v1/acoes/ -** Para ter acesso ao CRUD geral de ação.
* **api/v1/voluntarios/ -** Para ter acesso ao CRUD geral de voluntário.

Para mais informações sobre as rotas, acesse a documentação do sistema pelo
[Postman](https://documenter.getpostman.com/view/4328408/TVKA5eVv).

## Feito com

* [Django](https://www.djangoproject.com/) - Framework web escolhido para realização do desafio
* [Docker](https://www.docker.com/) - Forma de containerização
* [Python](https://www.python.org/) - Linguagem de programação utilizada

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
