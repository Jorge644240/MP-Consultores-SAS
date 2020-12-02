from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def mp():
    return render_template("mp.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/productos")
def productos():
    return render_template("productos.html")

@app.route("/servicios")
def services():
    return render_template("servicios.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

@app.route("/software")
def software():
    return render_template("altova.html")