from flask import render_template, request
from app import app


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
   if request.method == "POST":
      name = request.form['name']
      price = request.form['price']
      print(f'\033[1;32m name: {name} price: {price} \033[1;32m')

   return render_template('register.html')