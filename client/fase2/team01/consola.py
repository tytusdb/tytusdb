from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms import Form, IntegerField,SelectField,SubmitField
from wtforms.validators import Required	
from flask_codemirror.fields import CodeMirrorField


class consola(FlaskForm):       
#	entrada = CodeMirrorField(language='sql', config={'lineNumbers': 'true'})
	entrada2 = TextAreaField('Entrada')
	text = TextAreaField('Text', render_kw={"rows": 15})