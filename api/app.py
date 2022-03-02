import os
from flask import Flask
from flasgger import Swagger
from waitress import serve

from api.db import db
from api.elastic import elastic
from api.prints import base, search, uuid

def run():
    application = Flask(__name__)
    application.register_blueprint(base.bp)
    application.register_blueprint(search.search)
    application.register_blueprint(uuid.uuid)
    application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.environ['DB_USER'],
        os.environ['DB_PSWD'],
        os.environ['DB_HOST'],
        os.environ['DB_PORT'],
        os.environ['DB_NAME']
    )
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    application.config['ELASTICSEARCH_INDEX_URI'] = '{}:{}'.format(
        os.environ['ES_HOST'],
        os.environ['ES_PORT']
    )
    application.config['SWAGGER'] = {'title': 'CCE Search'}

    db.init_app(application)
    elastic.init_app(application)
    swagger = Swagger(application)

    if 'local' in os.environ['ENVIRONMENT']:
        application.config['ENV'] = 'development'
        application.config['DEBUG'] = True
        application.run()
    else:
        serve(self.app, host='0.0.0.0', port=80)
