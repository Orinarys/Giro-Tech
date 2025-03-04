# Giro.Tech - Desafio Técnico Backend

Este repositório contém a solução para o desafio técnico proposto pela **Giro.Tech**, que consiste no desenvolvimento de uma **API RESTful** para gerenciar moedas, taxas de câmbio, investidores e investimentos. A aplicação foi desenvolvida utilizando **Flask** e **SQLAlchemy**, com um banco de dados **SQLite** para armazenamento dos dados.

## 🌐 Introdução
O objetivo deste desafio é demonstrar habilidades no desenvolvimento de **APIs RESTful**, com foco na manipulação eficiente e estruturada de dados. A aplicação implementa operações **CRUD (Create, Read, Update, Delete)** para as entidades descritas no modelo de banco de dados, incluindo regras de negócio específicas e testes automatizados.

---

## 🛠️ Tecnologias Utilizadas
- **Flask**: Framework web para Python
- **SQLAlchemy**: ORM para interação com banco de dados
- **SQLite**: Banco de dados leve e embutido
- **unittest**: Framework para testes automatizados

---

## 📂 Modelo de Banco de Dados
A aplicação utiliza um banco de dados relacional composto pelas seguintes tabelas:

### **Currency (Moeda)**
- `id`: Identificador único
- `name`: Nome da moeda
- `type`: Tipo da moeda (ex: USD, EUR)

### **ExchangeRate (Taxa de Câmbio)**
- `id`: Identificador único
- `date`: Data da taxa
- `daily_variation`: Variação diária
- `daily_rate`: Taxa diária
- `currency_id`: Chave estrangeira para **Currency**

### **Investor (Investidor)**
- `id`: Identificador único
- `name`: Nome do investidor
- `email`: E-mail do investidor (**único**)

### **InvestmentHistory (Histórico de Investimento)**
- `id`: Identificador único
- `initial_amount`: Valor inicial
- `months`: Período do investimento (meses)
- `interest_rate`: Taxa de juros
- `final_amount`: Valor final
- `currency_id`: Chave estrangeira para **Currency**
- `investor_id`: Chave estrangeira para **Investor**

---

## 🔄 Funcionalidades Implementadas

### 👉 **1. Inserção de Dados**
- **POST /currencies**: Cadastra uma nova moeda
- **POST /exchange-rates**: Cadastra uma nova taxa de câmbio
- **POST /investors**: Cadastra um novo investidor (**e-mail único**)
- **POST /investments**: Cadastra um novo investimento

### 👈 **2. Consulta de Dados**
- **GET /currencies**: Lista todas as moedas cadastradas
- **GET /exchange-rates/recent**: Retorna taxas de câmbio dos últimos 7 dias

### ✏️ **3. Atualização de Dados**
- **PUT /exchange-rates/{id}**: Atualiza uma taxa de câmbio

### ❌ **4. Remoção de Registros**
- **DELETE /exchange-rates/old**: Remove taxas de câmbio com mais de 1 ano
- **DELETE /investors/{id}**: Remove um investidor e seus investimentos associados

---

## 🚀 Como Executar o Projeto

### 🛠️ **Pré-requisitos**
- **Python 3.8 ou superior**
- **Pip** (gerenciador de pacotes do Python)

### 📖 **Passos para Configuração**
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/giro-tech.git
cd giro-tech

# Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Para macOS/Linux
.venv\Scripts\activate    # Para Windows

# Instale as dependências
pip install flask flask-sqlalchemy

# Execute a aplicação
python run.py
```
A API estará disponível em **http://127.0.0.1:5000/**.

---

## 🎯 Testes Automatizados

A API conta com testes unitários para verificar o funcionamento correto das rotas. Para executar os testes:
```bash
python -m unittest test_app.py
```
**Saída esperada:**
```bash
.......
----------------------------------------------------------------------
Ran 7 tests in 0.456s

OK
```

---

## 📚 Estrutura do Projeto
```
giro-tech/
│
├── app/
│   ├── __init__.py         # Inicialização da aplicação Flask
│   ├── config.py           # Configurações da aplicação
│   ├── models.py           # Modelos de dados
│   └── routes.py           # Rotas da API
├── run.py                  # Script para rodar a aplicação
├── test_app.py             # Testes automatizados
├── finance.db              # Banco de dados SQLite (gerado automaticamente)
├── README.md               # Documentação do projeto
└── .venv/                  # Ambiente virtual (opcional)
```

---

## 🤝 Contribuição
Contribuições são bem-vindas! Para sugerir melhorias:
1. **Fork** o repositório
2. Crie uma **branch** para sua funcionalidade: `git checkout -b minha-melhoria`
3. **Commit** suas alterações: `git commit -m "Adiciona nova funcionalidade"`
4. **Push** para o repositório remoto: `git push origin minha-melhoria`
5. Abra um **Pull Request**

---

## 📢 Contato
- **Nome:** Kevin Andrew
- **E-mail:** kevin.andrew08rs@gmail.com
- **GitHub:** [Orinarys](https://github.com/Orinarys)

👉 **Feito com ❤️ por Kevin Andrew**

