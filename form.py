from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from models import *
from wtforms import Form,PasswordField,SubmitField,StringField,BooleanField,RadioField
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from wtforms import validators

class RegistrationForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()])
    username = StringField('Username',validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
'Usernames must have only letters, '
'numbers, dots or underscores')])
    password = PasswordField('请输入密码',validators=[Required(),EqualTo('password2',message='password must match')])
    password2 = PasswordField('确认你的密码',validators= [Required()])
    submit = SubmitField('Retister')
    sex = RadioField('性别',choices=[('value','description'),('value_two','whatever')])
