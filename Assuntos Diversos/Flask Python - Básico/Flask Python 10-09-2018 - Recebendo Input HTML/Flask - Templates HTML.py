# Templates HTML
# Mateus, 10 de agosto de 2018

from flask import Flask, render_template

app = Flask(__name__)

# Rotas
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/<name>")
def usuario(name):
    return render_template("profile.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)
