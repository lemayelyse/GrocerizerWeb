from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddToListForm(FlaskForm):
    item = StringField('Type Item...', validators=[DataRequired()])
    submit = SubmitField('Add')