from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definição dos modelos
class Moeda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(3), nullable=False)

class TaxaCambio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    variacao_diaria = db.Column(db.Float, nullable=False)
    taxa_diaria = db.Column(db.Float, nullable=False)
    moeda_id = db.Column(db.Integer, db.ForeignKey('moeda.id'), nullable=False)
    moeda = db.relationship('Moeda', backref='taxas_cambio')

class Investidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class HistoricoInvestimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor_inicial = db.Column(db.Float, nullable=False)
    meses = db.Column(db.Integer, nullable=False)
    taxa_juros = db.Column(db.Float, nullable=False)
    valor_final = db.Column(db.Float, nullable=False)
    moeda_id = db.Column(db.Integer, db.ForeignKey('moeda.id'), nullable=False)
    investidor_id = db.Column(db.Integer, db.ForeignKey('investidor.id'), nullable=False)

# Rotas
@app.route('/moedas', methods=['POST'])
def criar_moeda():
    dados = request.get_json()
    if not dados or not 'nome' in dados or not 'tipo' in dados:
        return jsonify({"erro": "Dados incompletos"}), 400
    nova_moeda = Moeda(nome=dados['nome'], tipo=dados['tipo'])
    db.session.add(nova_moeda)
    db.session.commit()
    return jsonify({"id": nova_moeda.id, "nome": nova_moeda.nome, "tipo": nova_moeda.tipo}), 201

@app.route('/taxas-cambio', methods=['POST'])
def criar_taxa_cambio():
    dados = request.get_json()
    if not dados or not 'moeda_id' in dados or not 'data' in dados or not 'variacao_diaria' in dados or not 'taxa_diaria' in dados:
        return jsonify({"erro": "Dados incompletos"}), 400
    moeda = db.session.get(Moeda, dados['moeda_id'])
    if not moeda:
        return jsonify({"erro": "Moeda não encontrada"}), 404
    try:
        data_obj = datetime.strptime(dados['data'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"erro": "Formato de data inválido"}), 400
    nova_taxa = TaxaCambio(
        data=data_obj,
        variacao_diaria=dados['variacao_diaria'],
        taxa_diaria=dados['taxa_diaria'],
        moeda_id=dados['moeda_id']
    )
    db.session.add(nova_taxa)
    db.session.commit()
    return jsonify({
        "id": nova_taxa.id,
        "data": nova_taxa.data.isoformat(),
        "variacao_diaria": nova_taxa.variacao_diaria,
        "taxa_diaria": nova_taxa.taxa_diaria,
        "moeda_id": nova_taxa.moeda_id
    }), 201

@app.route('/investidores', methods=['POST'])
def criar_investidor():
    dados = request.get_json()
    if not dados or not 'nome' in dados or not 'email' in dados:
        return jsonify({"erro": "Dados incompletos"}), 400
    if Investidor.query.filter_by(email=dados['email']).first():
        return jsonify({"erro": "E-mail já cadastrado"}), 400
    novo_investidor = Investidor(nome=dados['nome'], email=dados['email'])
    db.session.add(novo_investidor)
    db.session.commit()
    return jsonify({"id": novo_investidor.id, "nome": novo_investidor.nome, "email": novo_investidor.email}), 201

@app.route('/investimentos', methods=['POST'])
def criar_investimento():
    dados = request.get_json()
    if not dados or not 'valor_inicial' in dados or not 'meses' in dados or not 'taxa_juros' in dados or not 'moeda_id' in dados or not 'investidor_id' in dados:
        return jsonify({"erro": "Dados incompletos"}), 400
    moeda = db.session.get(Moeda, dados['moeda_id'])
    if not moeda:
        return jsonify({"erro": "Moeda não encontrada"}), 404
    investidor = db.session.get(Investidor, dados['investidor_id'])
    if not investidor:
        return jsonify({"erro": "Investidor não encontrado"}), 404
    valor_final = dados['valor_inicial'] * (1 + dados['taxa_juros'] / 100) ** dados['meses']
    novo_investimento = HistoricoInvestimento(
        valor_inicial=dados['valor_inicial'],
        meses=dados['meses'],
        taxa_juros=dados['taxa_juros'],
        valor_final=valor_final,
        moeda_id=dados['moeda_id'],
        investidor_id=dados['investidor_id']
    )
    db.session.add(novo_investimento)
    db.session.commit()
    return jsonify({
        "id": novo_investimento.id,
        "valor_inicial": novo_investimento.valor_inicial,
        "meses": novo_investimento.meses,
        "taxa_juros": novo_investimento.taxa_juros,
        "valor_final": novo_investimento.valor_final,
        "moeda_id": novo_investimento.moeda_id,
        "investidor_id": novo_investimento.investidor_id
    }), 201

@app.route('/moedas', methods=['GET'])
def listar_moedas():
    moedas = Moeda.query.all()
    data = [{"id": moeda.id, "nome": moeda.nome, "tipo": moeda.tipo} for moeda in moedas]
    return jsonify(data)

@app.route('/taxas-cambio/recentes', methods=['GET'])
def listar_taxas_cambio_recentes():
    sete_dias_atras = datetime.now() - timedelta(days=7)
    taxas_recentes = TaxaCambio.query.filter(TaxaCambio.data >= sete_dias_atras).all()
    resposta = [
        {
            "id": taxa.id,
            "data": taxa.data.isoformat(),
            "variacao_diaria": taxa.variacao_diaria,
            "taxa_diaria": taxa.taxa_diaria,
            "nome_moeda": taxa.moeda.nome,
            "tipo_moeda": taxa.moeda.tipo
        }
        for taxa in taxas_recentes
    ]
    return jsonify(resposta)

@app.route('/taxas-cambio/<int:id>', methods=['PUT'])
def atualizar_taxa_cambio(id):
    dados = request.get_json()
    if not dados or not 'variacao_diaria' in dados or not 'taxa_diaria' in dados:
        return jsonify({"erro": "Dados incompletos"}), 400
    taxa = db.session.get(TaxaCambio, id)
    if not taxa:
        return jsonify({"erro": "Taxa de câmbio não encontrada"}), 404
    taxa.variacao_diaria = dados['variacao_diaria']
    taxa.taxa_diaria = dados['taxa_diaria']
    db.session.commit()
    return jsonify({"id": taxa.id, "data": taxa.data.isoformat(), "variacao_diaria": taxa.variacao_diaria, "taxa_diaria": taxa.taxa_diaria})

@app.route('/taxas-cambio/antigas', methods=['DELETE'])
def excluir_taxas_cambio_antigas():
    data_limite = datetime.now() - timedelta(days=365)  # Excluir taxas com mais de 1 ano
    TaxaCambio.query.filter(TaxaCambio.data <= data_limite).delete()
    db.session.commit()
    return jsonify({"mensagem": "Taxas de câmbio antigas excluídas"})

@app.route('/investidor/<int:id>', methods=['DELETE'])
def excluir_investidor(id):
    investidor = db.session.get(Investidor, id)
    if not investidor:
        return jsonify({"erro": "Investidor não encontrado"}), 404
    HistoricoInvestimento.query.filter_by(investidor_id=id).delete()
    db.session.delete(investidor)
    db.session.commit()
    return jsonify({"mensagem": "Investidor e investimentos associados excluídos"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)