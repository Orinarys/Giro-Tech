Giro.Tech - Desafio Técnico Backend
Este repositório contém a solução para o desafio técnico proposto pela Giro.Tech, que consiste em desenvolver uma API RESTful para gerenciar moedas, taxas de câmbio, investidores e investimentos. A aplicação foi desenvolvida utilizando Flask e SQLAlchemy, com um banco de dados SQLite para armazenamento dos dados.

Introdução
O objetivo deste desafio é demonstrar habilidades no desenvolvimento de APIs RESTful, com foco na manipulação eficiente e estruturada de dados. A aplicação implementa operações CRUD (Create, Read, Update, Delete) para as entidades descritas no modelo de banco de dados, além de incluir regras de negócio específicas e testes automatizados.

Modelo de Banco de Dados
O banco de dados relacional é composto pelas seguintes tabelas:

Currency (Moeda):

id: Identificador único da moeda.

name: Nome da moeda.

type: Tipo da moeda (ex: USD, EUR).

ExchangeRate (Taxa de Câmbio):

id: Identificador único da taxa de câmbio.

date: Data da taxa de câmbio.

daily_variation: Variação diária da taxa.

daily_rate: Taxa diária.

currency_id: Chave estrangeira para a tabela Currency.

Investor (Investidor):

id: Identificador único do investidor.

name: Nome do investidor.

email: E-mail do investidor (único).

InvestmentHistory (Histórico de Investimento):

id: Identificador único do investimento.

initial_amount: Valor inicial do investimento.

months: Período do investimento em meses.

interest_rate: Taxa de juros aplicada.

final_amount: Valor final do investimento.

currency_id: Chave estrangeira para a tabela Currency.

investor_id: Chave estrangeira para a tabela Investor.

Funcionalidades Implementadas
1. Inserção de Dados
POST /currencies: Cadastra uma nova moeda.

Exemplo de entrada:

json
Copy
{
  "name": "Dólar Americano",
  "type": "USD"
}
Exemplo de saída:

json
Copy
{
  "id": 1,
  "name": "Dólar Americano",
  "type": "USD"
}
POST /exchange-rates: Cadastra uma nova taxa de câmbio.

Exemplo de entrada:

json
Copy
{
  "date": "2025-02-01",
  "daily_variation": 0.5,
  "daily_rate": 5.25,
  "currency_id": 1
}
Exemplo de saída:

json
Copy
{
  "id": 1,
  "date": "2025-02-01",
  "daily_variation": 0.5,
  "daily_rate": 5.25,
  "currency_id": 1
}
POST /investors: Cadastra um novo investidor.

Regra: Não é possível cadastrar um investidor com um e-mail já existente.

Exemplo de entrada:

json
Copy
{
  "name": "João Silva",
  "email": "joao@email.com"
}
Exemplo de saída:

json
Copy
{
  "id": 1,
  "name": "João Silva",
  "email": "joao@email.com"
}
POST /investments: Cadastra um novo investimento.

Exemplo de entrada:

json
Copy
{
  "initial_amount": 10000,
  "months": 12,
  "interest_rate": 5.5,
  "currency_id": 1,
  "investor_id": 1
}
Exemplo de saída:

json
Copy
{
  "id": 1,
  "initial_amount": 10000,
  "months": 12,
  "interest_rate": 5.5,
  "final_amount": 10550,
  "currency_id": 1,
  "investor_id": 1
}
2. Consultas
GET /currencies: Lista todas as moedas cadastradas.

Exemplo de saída:

json
Copy
[
  {
    "id": 1,
    "name": "Dólar Americano",
    "type": "USD"
  },
  {
    "id": 2,
    "name": "Euro",
    "type": "EUR"
  }
]
GET /exchange-rates/recent: Retorna as taxas de câmbio dos últimos 7 dias.

Exemplo de saída:

json
Copy
[
  {
    "id": 1,
    "date": "2025-02-01",
    "daily_variation": 0.5,
    "daily_rate": 5.25,
    "currency_name": "Dólar Americano",
    "currency_type": "USD"
  }
]
3. Atualização de Dados
PUT /exchange-rates/{id}: Atualiza a taxa de câmbio de uma moeda específica.

Exemplo de entrada:

json
Copy
{
  "daily_variation": 0.8,
  "daily_rate": 5.30
}
Exemplo de saída:

json
Copy
{
  "id": 1,
  "date": "2025-02-01",
  "daily_variation": 0.8,
  "daily_rate": 5.30
}
4. Remoção de Registros
DELETE /exchange-rates/old: Remove taxas de câmbio com mais de 1 ano.

Exemplo de saída:

json
Copy
{
  "mensagem": "Taxas de câmbio antigas excluídas"
}
DELETE /investor/{id}: Remove um investidor e seus investimentos associados.

Exemplo de saída:

json
Copy
{
  "mensagem": "Investidor e investimentos associados excluídos"
}
Como Utilizar o Sistema
Aqui estão os passos para utilizar o sistema e incluir informações:

1. Cadastrar uma Moeda
Faça uma requisição POST para /currencies com os dados da moeda:

bash
Copy
curl -X POST http://localhost:5000/currencies -H "Content-Type: application/json" -d '{"name": "Dólar Americano", "type": "USD"}'
2. Cadastrar uma Taxa de Câmbio
Faça uma requisição POST para /exchange-rates com os dados da taxa de câmbio:

bash
Copy
curl -X POST http://localhost:5000/exchange-rates -H "Content-Type: application/json" -d '{"date": "2025-02-01", "daily_variation": 0.5, "daily_rate": 5.25, "currency_id": 1}'
3. Cadastrar um Investidor
Faça uma requisição POST para /investors com os dados do investidor:

bash
Copy
curl -X POST http://localhost:5000/investors -H "Content-Type: application/json" -d '{"name": "João Silva", "email": "joao@email.com"}'
4. Cadastrar um Investimento
Faça uma requisição POST para /investments com os dados do investimento:

bash
Copy
curl -X POST http://localhost:5000/investments -H "Content-Type: application/json" -d '{"initial_amount": 10000, "months": 12, "interest_rate": 5.5, "currency_id": 1, "investor_id": 1}'
5. Listar Moedas
Faça uma requisição GET para /currencies:

bash
Copy
curl http://localhost:5000/currencies
6. Listar Taxas de Câmbio Recentes
Faça uma requisição GET para /exchange-rates/recent:

bash
Copy
curl http://localhost:5000/exchange-rates/recent
7. Atualizar uma Taxa de Câmbio
Faça uma requisição PUT para /exchange-rates/{id} com os novos dados:

bash
Copy
curl -X PUT http://localhost:5000/exchange-rates/1 -H "Content-Type: application/json" -d '{"daily_variation": 0.8, "daily_rate": 5.30}'
8. Excluir Taxas de Câmbio Antigas
Faça uma requisição DELETE para /exchange-rates/old:

bash
Copy
curl -X DELETE http://localhost:5000/exchange-rates/old
9. Excluir um Investidor
Faça uma requisição DELETE para /investor/{id}:

bash
Copy
curl -X DELETE http://localhost:5000/investor/1
Tecnologias Utilizadas
Flask: Framework web para Python.

SQLAlchemy: ORM para interagir com o banco de dados.

SQLite: Banco de dados leve e embutido.

unittest: Framework para testes automatizados.

Como Executar o Projeto
Pré-requisitos
Python 3.8 ou superior.

Pip (gerenciador de pacotes do Python).

Passos para Configuração
Clone o repositório:

bash
Copy
git clone https://github.com/seu-usuario/giro-tech.git
cd giro-tech
Crie um ambiente virtual:

bash
Copy
python -m venv .venv
Ative o ambiente virtual:

No Windows:

bash
Copy
.venv\Scripts\activate
No macOS/Linux:

bash
Copy
source .venv/bin/activate
Instale as dependências:

bash
Copy
pip install flask flask-sqlalchemy
Execute a aplicação:

bash
Copy
python run.py
A API estará disponível em http://127.0.0.1:5000/.

Testes Automatizados
O projeto inclui testes unitários para garantir o funcionamento correto das rotas da API. Para executar os testes:

Navegue até o diretório do projeto:

bash
Copy
cd giro-tech
Execute os testes:

bash
Copy
python -m unittest test_app.py
Saída esperada:

Copy
.......
----------------------------------------------------------------------
Ran 7 tests in 0.456s

OK
Estrutura do Projeto
Copy
giro-tech/
│
├── app/
│   ├── __init__.py         # Inicialização da aplicação Flask
│   ├── config.py           # Configurações da aplicação
│   ├── models.py           # Modelos de dados (Currency, ExchangeRate, Investor, InvestmentHistory)
│   └── routes.py           # Rotas da API
├── run.py                  # Script para rodar a aplicação
├── test_app.py             # Testes automatizados
├── finance.db              # Banco de dados SQLite (criado automaticamente)
├── README.md               # Documentação do projeto
└── .venv/                  # Ambiente virtual (opcional)
Contribuição
Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork do repositório.

Crie uma branch para sua feature (git checkout -b feature/nova-feature).

Commit suas alterações (git commit -m 'Adiciona nova feature').

Push para a branch (git push origin feature/nova-feature).

Abra um Pull Request.

Contato
Se tiver dúvidas ou sugestões, entre em contato:

Nome: Kevin

E-mail: kevin@email.com

GitHub: seu-usuario
