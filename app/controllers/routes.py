from flask import render_template, request
from app import app, db
from app.models.tables import Products


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
   if request.method == "POST":
      name = request.form['name']
      price = request.form['price']
      price = float(price)
      varejo = request.form.get('ok')

      if varejo == 'ok':
         varejo = True
      else:
         varejo = False

      product = Products(name, price , varejo)
      db.session.add(product)
      db.session.commit()
      return render_template('index.html')
   return render_template('register.html')