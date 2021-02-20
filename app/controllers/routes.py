from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.models.tables import Products


@app.route('/')
def home():
   try:
      product = Products.query.all()
      return render_template('index.html', products=product)
   except:
      flash("houver um erro!")
      return redirect(url_for('home'))



@app.route('/edit/<int:_id>', methods=["POST", "GET"])
def edit(_id):
   try:
      product = Products.query.get(_id)

      if request.method == "POST":
         name = request.form['name']
         price = request.form['price']

         varejo = request.form.get('ok')
         if varejo == 'ok':
            varejo = True
         else:
            varejo = False

         if name == '' or name == None:
            flash('Por favor preencha o campo nome !')
         elif price == '' or price == None:
            flash('Erro por favor verifique o campo de preço')
         else:
            price = float(price)
            product.name = name 
            product.price = price
            product.retail = varejo

            flash('Editado com sucesso')
            db.session.commit()
            return redirect(url_for('home'))


      return render_template('update.html', p=product)

   except:
      print('erro')



@app.route('/register', methods=['POST', 'GET'])
def register():
   if request.method == "POST":
      name = request.form['name']
      price = request.form['price']
     
      varejo = request.form.get('ok')

      if varejo == 'ok':
         varejo = True
      else:
         varejo = False

      if name == '' or name == None:
         flash('Por favor preencha o campo nome !')
      elif price == '' or price == None:
         flash('Erro por favor verifique o campo de preço')
      else:
         
         flash('Cadastrado com sucesso')
         price = float(price)
         product = Products(name, price , varejo)
         db.session.add(product)
         db.session.commit()
         return redirect(url_for('home'))


   return render_template('register.html')



@app.route('/delete/<int:_id>')
def delete(_id):
   try:
      product = Products.query.get(_id)
      db.session.delete(product)
      db.session.commit()
      flash('Deletado com successo')
      return redirect(url_for('home'))
   except:
      flash('Houde um erro em deletar, tente novamente')
      return redirect(url_for('home'))