import unittest
from flask import Flask
from app import app, db, Moeda, TaxaCambio, Investidor, HistoricoInvestimento
from datetime import datetime, timedelta

class TestApp(unittest.TestCase):

    def setUp(self):
        # Configuração do ambiente de teste
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Limpeza após cada teste
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Testes para Inserção de Dados
    def test_criar_moeda(self):
        # Teste para a rota POST /moedas
        response = self.app.post('/moedas', json={
            "nome": "Dólar Americano",
            "tipo": "USD"
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["nome"], "Dólar Americano")
        self.assertEqual(data["tipo"], "USD")

    def test_criar_taxa_cambio(self):
        # Cria uma moeda para associar à taxa de câmbio
        with app.app_context():
            moeda = Moeda(nome="Dólar Americano", tipo="USD")
            db.session.add(moeda)
            db.session.commit()

            # Teste para a rota POST /taxas-cambio
            response = self.app.post('/taxas-cambio', json={
                "moeda_id": moeda.id,
                "data": "2025-02-01",
                "variacao_diaria": 0.5,
                "taxa_diaria": 5.25
            })
            self.assertEqual(response.status_code, 201)
            data = response.get_json()
            self.assertEqual(data["data"], "2025-02-01")
            self.assertEqual(data["variacao_diaria"], 0.5)
            self.assertEqual(data["taxa_diaria"], 5.25)
            self.assertEqual(data["moeda_id"], moeda.id)

    def test_criar_investidor(self):
        # Teste para a rota POST /investidores
        response = self.app.post('/investidores', json={
            "nome": "João Silva",
            "email": "joao@email.com"
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["nome"], "João Silva")
        self.assertEqual(data["email"], "joao@email.com")

        # Teste para evitar duplicação de e-mail
        response = self.app.post('/investidores', json={
            "nome": "João Silva",
            "email": "joao@email.com"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("erro", response.get_json())

    def test_criar_investimento(self):
        # Cria uma moeda e um investidor para associar ao investimento
        with app.app_context():
            moeda = Moeda(nome="Dólar Americano", tipo="USD")
            investidor = Investidor(nome="João Silva", email="joao@email.com")
            db.session.add(moeda)
            db.session.add(investidor)
            db.session.commit()

            # Teste para a rota POST /investimentos
            response = self.app.post('/investimentos', json={
                "valor_inicial": 10000,
                "meses": 12,
                "taxa_juros": 5.5,
                "moeda_id": moeda.id,
                "investidor_id": investidor.id
            })
            self.assertEqual(response.status_code, 201)
            data = response.get_json()
            self.assertEqual(data["valor_inicial"], 10000)
            self.assertEqual(data["meses"], 12)
            self.assertEqual(data["taxa_juros"], 5.5)
            self.assertEqual(data["moeda_id"], moeda.id)
            self.assertEqual(data["investidor_id"], investidor.id)

    # Testes para Consultas
    def test_listar_moedas(self):
        # Cria duas moedas para testar a listagem
        with app.app_context():
            moeda1 = Moeda(nome="Dólar Americano", tipo="USD")
            moeda2 = Moeda(nome="Euro", tipo="EUR")
            db.session.add(moeda1)
            db.session.add(moeda2)
            db.session.commit()

            # Teste para a rota GET /moedas
            response = self.app.get('/moedas')
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]["nome"], "Dólar Americano")
            self.assertEqual(data[1]["nome"], "Euro")

    def test_listar_taxas_cambio_recentes(self):
        # Cria uma moeda e taxas de câmbio para testar a listagem
        with app.app_context():
            moeda = Moeda(nome="Dólar Americano", tipo="USD")
            db.session.add(moeda)
            db.session.commit()

            taxa1 = TaxaCambio(
                data=datetime.now().date(),
                variacao_diaria=0.5,
                taxa_diaria=5.25,
                moeda_id=moeda.id
            )
            taxa2 = TaxaCambio(
                data=(datetime.now() - timedelta(days=8)).date(),
                variacao_diaria=-0.3,
                taxa_diaria=5.22,
                moeda_id=moeda.id
            )
            db.session.add(taxa1)
            db.session.add(taxa2)
            db.session.commit()

            # Teste para a rota GET /taxas-cambio/recentes
            response = self.app.get('/taxas-cambio/recentes')
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(len(data), 1)  # Apenas a taxa dos últimos 7 dias deve ser retornada
            self.assertEqual(data[0]["variacao_diaria"], 0.5)
            self.assertEqual(data[0]["taxa_diaria"], 5.25)

    # Testes para Atualização de Dados
    def test_atualizar_taxa_cambio(self):
        # Cria uma moeda e uma taxa de câmbio para testar a atualização
        with app.app_context():
            moeda = Moeda(nome="Dólar Americano", tipo="USD")
            db.session.add(moeda)
            db.session.commit()

            taxa = TaxaCambio(
                data=datetime.now().date(),
                variacao_diaria=0.5,
                taxa_diaria=5.25,
                moeda_id=moeda.id
            )
            db.session.add(taxa)
            db.session.commit()

            # Teste para a rota PUT /taxas-cambio/{id}
            response = self.app.put(f'/taxas-cambio/{taxa.id}', json={
                "variacao_diaria": 0.8,
                "taxa_diaria": 5.30
            })
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(data["variacao_diaria"], 0.8)
            self.assertEqual(data["taxa_diaria"], 5.30)

if __name__ == '__main__':
    unittest.main()