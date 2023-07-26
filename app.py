from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
metrics = PrometheusMetrics(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'
    

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    active_page = "home"
    return render_template('home.html')

@app.route('/sayhello', methods=['GET', 'POST'])
def greet():
    active_page = "greet"
    if request.method == 'POST':
        username = request.form['username']
        if username:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
        return render_template('greet.html', username=username)
    else:
        return redirect(url_for('home'))

@app.route('/db')
def view_db():
    active_page = "db"
    users = db.session.query(User).all()
    return render_template('db.html', users=users)




if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
 