from flask import Flask
from config import Config
from grocerapp.dbhelper import DB

app = Flask(__name__)
app.config.from_object(Config)

#Initialize the database
db = DB()

from grocerapp import routes

