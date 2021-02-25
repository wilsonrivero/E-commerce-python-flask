from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.models.tables import Products
import matplotlib.pyplot as plt 
import os



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
      
      list_of_products = [product]
      print(len(list_of_products))


      for  value in list_of_products:
         length = len(value)
         for x in range(length):
            pass

      return render_template('search.html', products=list_of_products, size=length)


   return render_template('search.html')



@app.route('/graphic' ,methods=['GET'])
def graphic():
   
   products = Products.query.all()
   list_of_names_sorted = []
   list_of_names = []
   for value in products:

      list_of_names_sorted.append(value.name)
      list_of_names_sorted.sort()
      list_of_names_sorted = list(dict.fromkeys(list_of_names_sorted))

      list_of_names.append(value.name)
      list_of_names.sort()

   list_of_how_many_times = []
   count_m = 0
   count_cha = 0
   count_cre = 0
   count_seb = 0
   count_pros = 0
   count_mil = 0
   for name in list_of_names:
      if name == 'Milagrosa':
         count_m += 1
      elif name == 'Chá':
         count_cha += 1
      elif name == 'Creme':
         count_cre += 1
      elif name == 'Sebo de Carneiro':
         count_seb += 1
      elif name == 'Prostata':
         count_pros += 1
   
      elif name == 'milagrosa mil ervas':
         count_mil += 1
   
   list_of_how_many_times.append(count_cha)
   list_of_how_many_times.append(count_cre)
   list_of_how_many_times.append(count_m)
   list_of_how_many_times.append(count_pros)
   list_of_how_many_times.append(count_seb)
   list_of_how_many_times.append(count_mil)

   return render_template('graphic.html', values=list_of_how_many_times, labels=list_of_names_sorted)




   


