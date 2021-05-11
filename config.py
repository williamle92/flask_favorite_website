import os
#Creatre the configuration class in a separate Python module. Thye configuration settings are dfined as class variables inside the Config class. 
class Config():
    FLASK_APP=os.environ.get('FLASK_APP')
    FLASK_ENV=os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'