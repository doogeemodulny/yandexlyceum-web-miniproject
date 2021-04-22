from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddNoteForm(FlaskForm):
    text = TextAreaField('Напишите здесь что-нибудь', validators=[DataRequired()])
    submit = SubmitField('Ок')