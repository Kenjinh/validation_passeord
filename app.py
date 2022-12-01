from flask import Flask
from rest_api.app import urls_rest
from graph_api.app import urls_graph

app = Flask(__name__)
app.register_blueprint(urls_rest, url_prefix='/verify')
app.register_blueprint(urls_graph, url_prefix='/graphql')

@app.route('/')
def hello_world():  # put application's code here
    return ''


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
