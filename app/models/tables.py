from app import db


class Products(db.Model):
   __tablename__ = 'products'
   _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   name = db.Column(db.String)
   price = db.Column(db.Float)
   retail = db.Column(db.Boolean)


   def __init__(self, name, price, retail=False):
      self.name = name
      self.price = price
      self.retail = retail