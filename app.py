"""HW2: Application that supports campus study spaces:
    1) Building name 2)Building code 3)Building Floor 4)Closeest room number
    5) Rating is stored
"""
import flask
from flask.views import MethodView
from index import Index
from sign import Sign
#from remove import Remove

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/sign',
                 view_func=Sign.as_view('sign'),
                 methods=['GET', 'POST'])
'''app.add_url_rule('/remove',
                 view_func=Remove.as_view('remove'),
                 methods=['POST'])'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
