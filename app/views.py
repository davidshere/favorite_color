from datetime import datetime

from flask import render_template, flash, redirect, url_for
from sqlalchemy import func

from .forms import GetFavoriteColor, RetrieveFavoriteColor
from app import app, db
from models import User


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
  form = GetFavoriteColor()
  if form.validate_on_submit():
    flash("Thanks %s!" % form.name.data)
    user_name = form.name.data.lower()
    user_fav = form.favorite.data.lower()
    ''' Check if the value is already in the db 
    if user_name in "select user_name from user_table:
      flash("I'm sorry, I've already got a favorite color for %s) % user_name
    '''
    created = datetime.utcnow()
    user = User(name=user_name, favorite=user_fav, created=created)
    db.session.add(user)
    db.session.commit()
    return redirect('/index')
  return render_template('index.html', form=form)

@app.route('/find', methods=['GET', 'POST'])
def find():
  form = RetrieveFavoriteColor()
  if form.validate_on_submit():
    name = form.name.data.lower()
    user = User.query.get(name)
    if user:
      flash("%s, your favorite color is %s" % (user.name.title(), user.favorite))
    else:
      flash("Sorry, %s, I don't know your favorite color" % name.title())
    return redirect(url_for('find'))
  return render_template('find.html', form=form)

@app.route('/facts')
def facts():
  query = db.session.query(User.favorite, db.func.count(User.name)).group_by(User.favorite)
  fact_table = query.all()
  print fact_table

  #User.query.get((User.favorite, func.count(User.name))).group_by(User.favorite).all()
  #flash(fact_table)
  return render_template('facts.html')