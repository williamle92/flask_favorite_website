#This is what the app package inherits 
from flask import Flask
from config import Config
#The name variable is passed to the Flask class
app = Flask(__name__)
app.config.from_object(Config)


from app import routes