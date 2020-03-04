from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SelectField, StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired

class PatchCordForm(FlaskForm):
    typePatchCord = SelectField('Type', validators=[DataRequired()], choices=[('SC-SC', 'sc-sc'),
                                 ('SC-LC', 'sc-lc'),
                                 ('LC-LC', 'lc-lc')], default='SC-SC')
    lengthPatchCord = StringField('Length', validators=[DataRequired()])
    notePatchCord = TextAreaField('Deskripsi/Status Produk', validators=[DataRequired()])
    recordOfTransferPatchCord = FileField('Berita Acara', validators=[FileRequired(), FileAllowed(['.jpg', '.pdf'])])
    submitPatchCord = SubmitField('Simpan')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')