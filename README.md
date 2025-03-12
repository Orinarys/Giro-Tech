# 🚀 Meu Projeto de Backend

Este repositório contém a solução para um projeto pessoal de **Backend**.

## 🚀 Como Executar o Projeto

### Pré-requisitos
- **Python 3.x**
- **Pip** (gerenciador de pacotes do Python)

### Instalação

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/meu-projeto-backend.git
    cd meu-projeto-backend
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

#### **Recursos**

- **POST /recursos**: Cadastra um novo recurso.
    - **Exemplo de Entrada:**
        ```json
        {
          "nome": "Exemplo",
          "descricao": "Um recurso de exemplo"
        }
        ```
    - **Exemplo de Saída:**
        ```json
        {
          "id": 1,
          "nome": "Exemplo",
          "descricao": "Um recurso de exemplo"
        }
        ```

- **GET /recursos**: Lista todos os recursos cadastrados.
    - **Exemplo de Saída:**
        ```json
        [
          {
            "id": 1,
            "nome": "Exemplo",
            "descricao": "Um recurso de exemplo"
          }
        ]
        ```

## 🧪 Testes

O projeto inclui testes unitários e de integração para garantir o funcionamento correto dos endpoints e da lógica de negócios.

Para executar os testes, utilize o comando:
```bash
python -m unittest tests/test_app.py
```

## 📝 Considerações Finais

Este projeto foi desenvolvido como parte de um estudo pessoal, com o objetivo de demonstrar habilidades em desenvolvimento backend, manipulação de banco de dados e testes automatizados.

