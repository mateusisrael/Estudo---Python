# METÓDOS HTTP
# Mateus, 10 de agosto de 2018


from flask import Flask, request

app = Flask(__name__)



@app.route("/")
def index():
    return "Metodo usado: {}".format(request.method)

@app.route("/bacon", methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "Você está usando POST"
    else:
        return "Provavelmente você está usando GET"


if __name__ == "__main__":
    app.run(debug=True)