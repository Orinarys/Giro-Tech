# 🚀 GiroTech - Desafio Técnico

Este repositório contém a solução para o desafio de **Backend**.

## 🚀 Como Executar o Projeto

### Pré-requisitos
- **Python 3.x**
- **Pip** (gerenciador de pacotes do Python)

### Instalação

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/girotech-backend.git
    cd girotech-backend
    ```

2. **Crie um ambiente virtual e ative-o:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use venv\Scripts\activate
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Executando a Aplicação

1. **Inicie o servidor Flask:**
    ```bash
    python run.py
    ```

A API estará disponível em: `http://127.0.0.1:5000/`.

### Executando os Testes

Para rodar os testes unitários e de integração, execute:
```bash
python -m unittest tests/test_app.py
```

## 📚 Documentação da API

### Endpoints

#### **Moedas**

- **POST /moedas**: Cadastra uma nova moeda.
    - **Exemplo de Entrada:**
        ```json
        {
          "nome": "Dólar Americano",
          "tipo": "USD"
        }
        ```
    - **Exemplo de Saída:**
        ```json
        {
          "id": 1,
          "nome": "Dólar Americano",
          "tipo": "USD"
        }
        ```

- **GET /moedas**: Lista todas as moedas cadastradas.
    - **Exemplo de Saída:**
        ```json
        [
          {
            "id": 1,
            "nome": "Dólar Americano",
            "tipo": "USD"
          },
          {
            "id": 2,
            "nome": "Euro",
            "tipo": "EUR"
          }
        ]
        ```

#### **Taxas de Câmbio**

- **POST /taxas-cambio**: Cadastra uma nova taxa de câmbio.
    - **Exemplo de Entrada:**
        ```json
        {
          "moeda_id": 1,
          "data": "2025-02-01",
          "variacao_diaria": 0.5,
          "taxa_diaria": 5.25
        }
        ```
    - **Exemplo de Saída:**
        ```json
        {
          "id": 1,
          "data": "2025-02-01",
          "variacao_diaria": 0.5,
          "taxa_diaria": 5.25,
          "moeda_id": 1
        }
        ```

- **GET /taxas-cambio/recentes**: Retorna as taxas de câmbio dos últimos 7 dias.
    - **Exemplo de Saída:**
        ```json
        [
          {
            "id": 1,
            "data": "2025-02-01",
            "variacao_diaria": 0.5,
            "taxa_diaria": 5.25,
            "nome_moeda": "Dólar Americano",
            "tipo_moeda": "USD"
          }
        ]
        ```

- **PUT /taxas-cambio/{id}**: Atualiza uma taxa de câmbio específica.
    - **Exemplo de Entrada:**
        ```json
        {
          "variacao_diaria": 0.8,
          "taxa_diaria": 5.30
        }
        ```
    - **Exemplo de Saída:**
        ```json
        {
          "id": 1,
          "data": "2025-02-01",
          "variacao_diaria": 0.8,
          "taxa_diaria": 5.30
        }
        ```

- **DELETE /taxas-cambio/antigas**: Remove taxas de câmbio com mais de 365 dias.
    - **Exemplo de Saída:**
        ```json
        {
          "mensagem": "Taxas de câmbio antigas excluídas"
        }
        ```

#### **Investidores**

- **POST /investidores**: Cadastra um novo investidor.
    - **Exemplo de Entrada:**
        ```json
        {
          "nome": "João Silva",
          "email": "joao@email.com"
        }
        ```
    - **Exemplo de Saída:**
        ```json
        {
          "id": 1,
          "nome": "João Silva",
          "email": "joao@email.com"
        }
        ```

- **DELETE /investidor/{id}**: Deleta um investidor e seus investimentos associados.
    - **Exemplo de Saída:**
        ```json
        {
          "mensagem": "Investidor e investimentos associados excluídos"
        }
        ```

#### **Investimentos**

- **POST /investimentos**: Cadastra um novo investimento.
    - **Exemplo de Entrada:**
        ```json
        {
          "valor_inicial": 10000,
          "meses": 12,
          "taxa_juros": 5.5,
          "moeda_id": 1,
          "investidor_id": 1
        }
        ```
    - **Exemplo de Saída:**
        ```json
        {
          "id": 1,
          "valor_inicial": 10000,
          "meses": 12,
          "taxa_juros": 5.5,
          "valor_final": 10550,
          "moeda_id": 1,
          "investidor_id": 1
        }
        ```

## 🧪 Testes

O projeto inclui testes unitários e de integração para garantir o funcionamento correto dos endpoints e da lógica de negócios. Os testes cobrem:

- Inserção de dados (moedas, taxas de câmbio, investidores, investimentos).
- Consultas (listagem de moedas, taxas de câmbio recentes).
- Atualização de dados (taxas de câmbio).
- Remoção de registros (taxas de câmbio antigas, investidores).

Para executar os testes, utilize o comando:
```bash
python -m unittest tests/test_app.py
```

## 📝 Considerações Finais

Este projeto foi desenvolvido como parte do desafio técnico da **Giro.Tech**, com o objetivo de demonstrar habilidades em desenvolvimento backend, manipulação de banco de dados e testes automatizados.
```
