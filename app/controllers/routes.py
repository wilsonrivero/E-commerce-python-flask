from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.models.tables import Products


@app.route('/')
def home():
   try:
      product = Products.query.all()
      total = 0
      for p in product:
         total += p.price
      
      total = f'{total:.2f}'

      return render_template('index.html', products=product, total_of_money=total)
   except:
      flash("houver um erro!")
      return redirect(url_for('home'))


#UPDATE
@app.route('/edit/<int:_id>', methods=["POST", "GET"])
def edit(_id):
   try:
      product = Products.query.get(_id)

      if request.method == "POST":
         name = request.form['name']
         price = request.form['price']

         

         if name == '' or name == None:
            flash('Por favor preencha o campo nome !')
         elif price == '' or price == None:
            flash('Erro por favor verifique o campo de preço')
         else:
            varejo = request.form.get('retail')
            if varejo == 'ok':
               varejo = True
            else:
               varejo = False
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


#ADD
@app.route('/register', methods=['POST', 'GET'])
def register():
   if request.method == "POST":
      name = request.form['name']
      price = request.form['price']
      varejo = request.form.get('retail')

      if name == '' or name == None:
         flash('Por favor preencha o campo nome !')
      elif price == '' or price == None:
         flash('Erro por favor verifique o campo de preço')
      else:
         
         if varejo == 'ok':
            varejo = True
         else:
            varejo = False
         
         flash('Cadastrado com sucesso')
         price = float(price)
         product = Products(name, price , varejo)
         db.session.add(product)
         db.session.commit()
         return redirect(url_for('home'))


   return render_template('register.html')


#DELETE
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



@app.route('/search', methods=["GET", "POST"])
def search():

   if request.method == "POST":
      name = request.form['name']
      product = Products.query.filter_by(name=name).all()
      
      print(len(product))

      list_of_products_search = []

      for x in range(len(product)):
         list_of_products_search.append(product[x].name, product[x].price)

      return render_template('search.html', products=list_of_products_search)



   return render_template('search.html')