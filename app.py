from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Servidor Trabalhando !'


@app.route('/login', methods=['GET','POST'])
def login():
    user = request.form.get("user")
    password = request.form.get("password")
    print(user, password)
    return render_template('login.html')

if __name__ == "__main__":
    app.run()