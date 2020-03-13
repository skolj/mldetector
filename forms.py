from wtforms import Form, StringField, SubmitField, PasswordField, validators

class Input(Form):
    url = StringField('Username', [validators.URL()])
    submit = SubmitField('Test')