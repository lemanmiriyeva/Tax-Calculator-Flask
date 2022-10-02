from logging import PlaceHolder
from re import U
from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class TaxForm(FlaskForm):
    gross_salary=IntegerField(validators=[DataRequired()],render_kw={"placeholder": "Aylıq əmək haqqı (AZN)"})
    options=SelectField(U"Qeyri-neft",choices=[("Qeyri-dövlət və qeyri-neft sektoru","Qeyri-dövlət və qeyri-neft sektoru"),("Dövlət və neft sektoru","Dövlət və neft sektoru")])
