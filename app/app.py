import os
from flask import Flask
from rest_api.app import urls_rest
from graph_api.app import urls_graph


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
    app.register_blueprint(urls_rest, url_prefix='/verify')
    app.register_blueprint(urls_graph, url_prefix='/graphql')
    return app

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
