# **Projeto Giro-Tech**

Este projeto é uma API Flask para gerenciar moedas, taxas de câmbio, investidores e investimentos. Ele utiliza SQLAlchemy para interagir com um banco de dados SQLite.

---

## **Funcionalidades**

1. **Moedas**:
   - Cadastrar uma nova moeda.
   - Listar todas as moedas cadastradas.

2. **Taxas de Câmbio**:
   - Cadastrar uma nova taxa de câmbio.
   - Listar taxas de câmbio recentes (últimos 7 dias).
   - Atualizar uma taxa de câmbio existente.
   - Excluir taxas de câmbio antigas (mais de 1 ano).

3. **Investidores**:
   - Cadastrar um novo investidor.
   - Excluir um investidor e seus investimentos associados.

4. **Investimentos**:
   - Cadastrar um novo investimento.
   - Calcular o valor final do investimento com base na taxa de juros e no período.

---

## **Tecnologias Utilizadas**

- **Flask**: Framework web para Python.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **SQLite**: Banco de dados leve e embutido.

---

## **Como Executar o Projeto**

### **Pré-requisitos**

- Python 3.8 ou superior.
- Pip (gerenciador de pacotes do Python).

### **Passos para Configuração**

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/giro-tech.git
   cd giro-tech
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   ```

3. Ative o ambiente virtual:
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Instale as dependências:
   ```bash
   pip install flask flask-sqlalchemy
   ```

5. Execute a aplicação:
   ```bash
   python app.py
   ```

   O servidor Flask será iniciado em `http://127.0.0.1:5000/`.

---

## **Testando a API**

Você pode testar as rotas da API usando ferramentas como **Postman** ou **cURL**.

### **Exemplos de Requisições**

1. **Cadastrar uma nova moeda**:
   ```bash
   curl -X POST http://localhost:5000/moedas -H "Content-Type: application/json" -d '{"nome": "Dólar Americano", "tipo": "USD"}'
   ```

2. **Listar todas as moedas**:
   ```bash
   curl http://localhost:5000/moedas
   ```

3. **Cadastrar uma nova taxa de câmbio**:
   ```bash
   curl -X POST http://localhost:5000/taxas-cambio -H "Content-Type: application/json" -d '{"moeda_id": 1, "data": "2023-10-01", "variacao_diaria": 0.5, "taxa_diaria": 5.25}'
   ```

4. **Listar taxas de câmbio recentes**:
   ```bash
   curl http://localhost:5000/taxas-cambio/recentes
   ```

5. **Cadastrar um novo investidor**:
   ```bash
   curl -X POST http://localhost:5000/investidores -H "Content-Type: application/json" -d '{"nome": "João Silva", "email": "joao@email.com"}'
   ```

6. **Cadastrar um novo investimento**:
   ```bash
   curl -X POST http://localhost:5000/investimentos -H "Content-Type: application/json" -d '{"valor_inicial": 10000, "meses": 12, "taxa_juros": 5.5, "moeda_id": 1, "investidor_id": 1}'
   ```

---

## **Executando os Testes**

O projeto inclui testes automatizados para garantir o funcionamento correto das rotas da API. Para executar os testes:

1. Navegue até o diretório do projeto:
   ```bash
   cd giro-tech
   ```

2. Execute os testes:
   ```bash
   python -m unittest test_app.py
   ```

   Você verá uma saída como esta se todos os testes passarem:
   ```
   .......
   ----------------------------------------------------------------------
   Ran 7 tests in 0.456s

   OK
   ```

---

## **Estrutura do Projeto**

```
giro-tech/
│
├── app.py                  # Arquivo principal da aplicação
├── test_app.py             # Testes automatizados
├── finance.db              # Banco de dados SQLite (criado automaticamente)
├── README.md               # Documentação do projeto
└── .venv/                  # Ambiente virtual (opcional)
```

---

## **Contribuição**

Se você deseja contribuir para este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## **Licença**

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## **Contato**

Se tiver dúvidas ou sugestões, entre em contato:

- **Nome**: Kevin
- **E-mail**: kevin@email.com
- **GitHub**: [seu-usuario](https://github.com/seu-usuario)

---

**Divirta-se usando o Giro-Tech!** 🚀

---

### **Observações**

- Substitua `seu-usuario` pelo seu nome de usuário do GitHub.
- Adicione um arquivo `LICENSE` se desejar licenciar o projeto.
- Personalize as informações de contato conforme necessário.

Se precisar de mais ajustes ou tiver dúvidas, é só perguntar! 😊
