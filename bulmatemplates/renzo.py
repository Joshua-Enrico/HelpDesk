from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/registra_usuario")
def user_registre():
    return render_template('registra_usuario.html')


@app.route("/administracion_usuario")
def user_administration():
    return render_template('administracion_usuario.html')


@app.route("/registra_ticket")
def ticket_registre():
    return render_template('registra_ticket.html')


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/user_dashboard")
def user_dashboard():
    return render_template('user_dashboard.html')


if __name__ == "__main__":
    app.run(debug = True)