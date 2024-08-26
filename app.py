import webview
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import threading

# Configuração do Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Modelo de Usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('usuario')
        password = request.form.get('senha')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        return "Credenciais inválidas, tente novamente."
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# Função para rodar o Flask
def run_flask():
    app.run(port=5000, debug=False)

# Função para abrir o PyWebview
def open_browser():
    webview.create_window('Meu Flask App', 'http://127.0.0.1:5000')
    webview.start()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    open_browser()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)