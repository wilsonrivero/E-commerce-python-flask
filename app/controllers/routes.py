from flask import render_template, request
from app import app, db
from app.models.tables import Products


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
   if request.method == "POST":
      product = Products(request.form['name'], request.form['price'], retail=True)
      db.session.add(product)
      db.session.commit()
      return render_template('index.html')
   return render_template('register.html')