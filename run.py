# run.py
from app import create_app, db  # Aqui, estamos importando 'create_app' de 'app', não de 'run'

app = create_app()

with app.app_context():
    db.create_all() 

if __name__ == "__main__":
    app.run(debug=True)
