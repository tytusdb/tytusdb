from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms import Form, IntegerField,SelectField,SubmitField
from wtforms.validators import Required	


class consola(FlaskForm):                      
	text = TextAreaField('Text', render_kw={"rows": 15})