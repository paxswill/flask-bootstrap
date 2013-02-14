#!/usr/bin/env python
# coding=utf8

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form, HiddenField, ValidationError,\
                          Required, RecaptchaField, PasswordField
from flask.ext.bootstrap.wtf import BooleanField, RadioField, ButtonField,\
                                    SubmitField, TextField, EmailField,\
                                    SubmitButtonField

app = Flask(__name__)
Bootstrap(app)

app.config['BOOTSTRAP_USE_MINIFIED'] = True
app.config['BOOTSTRAP_USE_CDN'] = True
app.config['BOOTSTRAP_FONTAWESOME'] = True
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'


class ExampleForm(Form):
    field1 = TextField('First Field', description='This is field one.',
                       placeholder='A placeholder value')
    field2 = TextField('Second Field', description='This is field two.',
                       validators=[Required()])
    field3 = BooleanField('Third Field', description='This is field three.')
    field4 = RadioField('Fourth Field', description='This is field four.',
                        choices=[('1', 'Option One'), ('2', 'Option Two'),
                                ('3', 'Option Three')])
    hidden_field = HiddenField('You cannot see this', description='Nope')
    recaptcha = RecaptchaField('A sample recaptcha field')
    button = ButtonField('Button')
    input_submit = SubmitField('Submit')

    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')


class LoginForm(Form):
    email = EmailField('Email')
    password = PasswordField('Password')
    remember = BooleanField('Remember Me')
    signin = SubmitButtonField('Sign in')


@app.route('/', methods=('GET', 'POST',))
def index():
    form = ExampleForm()
    login = LoginForm()
    if form.validate_on_submit():
        return "PASSED"
    return render_template('example.html', form=form, login=login)


if '__main__' == __name__:
    app.run(debug=True)
