from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contatos.sqlite3'

db = SQLAlchemy(app)

class Contatos(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(100))
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


@app.route('/')
def index():
    contatos = Contatos.query.all()
    return render_template('index.html', contatos = contatos)

@app.route('/add', methods=['POST', 'GET'])
def add():

    if request.method == "POST":
        contato = Contatos(request.form['name'], request.form['phone'], request.form['email'])
        if contato.name == "":
            return render_template('add.html')
        db.session.add(contato)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    contato = Contatos.query.get(id)
    db.session.delete(contato)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    contato = Contatos.query.get(id)
    if request.method == 'POST':
        contato.name = request.form['name']
        contato.email = request.form['email']
        contato.phone = request.form['phone']
        db.session.commit()
        return redirect(url_for('index'))
    
        
    return render_template('edit.html', contato= contato)

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)