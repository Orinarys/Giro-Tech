from app import db

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

    def __str__(self):
        return f'ID: {self.id}, Valor: {self.variacao_diaria}, Data: {self.data}'

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
