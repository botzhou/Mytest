from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from models import *
from wtforms import Form,PasswordField,SubmitField,StringField,BooleanField
from wtforms.validators import required,Length,Email,Regexp,EqualTo
from wtforms import validators


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        myusername = request.form['username']
        mypassword = request.form['userpassword']
        addTestUserTest(myusername,mypassword)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
