from flask import Flask

app = Flask(__name__)



# @ signifies a decorator - way to wrap a function an modifying its behavior

# ROTAS ===================================================================
@app.route('/')
def index():
    return 'Essa é a página Inicial.'



@app.route('/mateus')
def mateus():
    return "Esse é o caminho do Mateus"


@app.route('/profile/<username>')
def profile(username):
    return "Olá {}".format(username)


@app.route('/post/<int:post_id>')
def mostrar_post(post_id):
    return "Número {}".format(post_id)





if __name__ == "__main__":   # Não entendi bem
    app.run()