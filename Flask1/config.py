from flask_sqlalchemy import SQLAlchemy
from Main import app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'  # banco de dados sqlite
SQLAlCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
