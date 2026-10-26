from flask import Blueprint, render_template, request, redirect, url_for
from app.model.personagem_model import Personagem

# Blueprint organizando as rotas da aplicação
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
#    """Busca os personagens no banco de dados e os envia para a página."""
    lista_personagens = Personagem.buscar_todos()
    return render_template('index.html', personagens=lista_personagens)

@main_bp.route('/cadastrar', methods=['POST'])
def cadastrar():
#    """Recebe dados via POST do formulário HTML, instancia e salva no SQLite."""
    nome = request.form.get('nome')
    elemento = request.form.get('elemento')
    arma = request.form.get('arma')
    raridade = request.form.get('raridade')

    if nome and elemento and arma and raridade:
        novo = Personagem(
            nome=nome,
            elemento=elemento,
            arma=arma,
            raridade=int(raridade)
        )
        novo.salvar()

    return redirect(url_for('main.index'))