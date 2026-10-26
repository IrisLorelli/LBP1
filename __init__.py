import os
from flask import Flask
from app.model.personagem_model import Personagem

def create_app():
    # Caminho correto para a pasta 'view'
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'view')
    
    app = Flask(__name__, template_folder=template_dir)

    # Garante a criação da tabela nativa no SQLite
    Personagem.criar_tabela()

    # Registro das rotas através do Controller
    from app.controller.personagem_controller import main_bp
    app.register_blueprint(main_bp)

    return app