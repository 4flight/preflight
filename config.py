from wtforms import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('ICAO or IATA code ?', validators=[Required()])
    submit = SubmitField('Submit')

class Config:
    #session key code
    SECRET_KEY = 'B!1w98NAt10wkl#T^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flight_tracker'
    
config = {
    'development': DevelopmentConfig
}
