from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class GetFavoriteColor(Form):
  name = StringField('name', validators=[DataRequired()])
  favorite = StringField('fav', validators=[DataRequired()])

class RetrieveFavoriteColor(Form):
  name = StringField('name', validators=[DataRequired()])
