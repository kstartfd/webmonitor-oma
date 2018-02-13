from wtforms import Form, validators, StringField, SelectMultipleField, widgets


class Login(Form):
    username = StringField(validators=[validators.required()])
    password = StringField(validators=[validators.required()])


class FormFromIndex(Form):
    search = StringField(validators=[validators.required()])
    # search = StringField(validators=[validators.Length(min=3, max=6)])
    # search = StringField(validators=[validators.Regexp(r'^[0-9]+$', 0, )])


