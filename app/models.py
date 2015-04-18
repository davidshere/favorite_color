from app import db

class User(db.Model):
  id = db.Column(db.Integer)
  name = db.Column(db.String(25), index=True, unique=True, primary_key=True)
  favorite = db.Column(db.String(20), index=True, unique=True)
  created = db.Column(db.DateTime)
  
  def __repr__(self):
    return '<User %r>' % self.name
