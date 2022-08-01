from flask import Flask
from flask_restful import Api
import logging
from flask_migrate import Migrate
from flask_login import LoginManager, login_required
from flask_sse import sse
from flask_security import Security, SQLAlchemySessionUserDatastore, SQLAlchemyUserDatastore
from flask_security import auth_required, login_required, roles_accepted, roles_required, auth_token_required
from flask import render_template
logging.basicConfig(filename='debug.log',level=logging.DEBUG,format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s %(message)s')
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
engine=None
Base=declarative_base()
db=SQLAlchemy()
app=Flask(__name__)
@app.route("/")
def index():
    return "HELLO TO LOGIN PAGE"


if __name__=="__main__":
    app.run(debug=True)