from ..Main import app
from flask import render_template


@app.route('index')
@app.route('/')  # define a rota para acessar a página
def index():
    return "Hello, world!"


# rotas com parâmetros
@app.route('pagina1/<id>')
def pag(id):
    return id


# deixando opcional a passagem de query na rota:
@app.route('/teste')
@app.route('/teste/<id>')
def testa(id=None):
    print("TESTE")


# deixando opcional a passagem de query na rota:
@app.route('/teste', defaults={"id": None})
@app.route('/teste/<id>')
def testa(id=None):
    print("TESTE")


# forçando o tipo de uma variavel:
#
@app.route('/teste')
@app.route('/teste/<int:id>')
def testa(id=None):
    print("TESTE")


## métodos:
#
@app.route('/teste', methods=['GET'])  # métodos http
@app.route('/teste/<id>')
def testa(id=None):
    print("TESTE")

## renderizar um template
@app.route('/pagina/<usuario>')
def render(usuario):
    return render_template('index.html', user=usuario)  # nome da variavel