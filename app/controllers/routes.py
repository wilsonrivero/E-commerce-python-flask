from flask import render_template, request
from app import app


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
   try:
      if request.method == "POST":
         name = request.form['name']
         price = request.form['price']
         retail = False

         if request.form['retail'] == 'on':
            retail = True
         else:
            retail = False

         print(f'\033[1;32m retail: {retail} \033[1;32m')
   except:
      return render_template('register.html')


   return render_template('register.html')