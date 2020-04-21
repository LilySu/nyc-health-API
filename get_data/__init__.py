from flask import Flask
import markdown
import os

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("data.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/README.md','r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)

# Class for each endpoint 
# Function for each method we accept
class CoronavirusData(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        datalist = []
        for key in keys:
            datalist.append(shelf[key])
        return {'message':'Success', 'data':datalist}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required= True)
        parser.add_argument('header_name', required= True)

        args = parser.parse_args()
        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'identifier understood','data':args}, 201

class Data(Resource):
    def get(self, identifier):
        shelf = get_db()

        if not (identifier in shelf):
            return {'message': 'data not found','data':{}}, 404
        return {'message': 'data found','data':shelf[identifier], 200

api.add_resource(CoronavirusData, '/datalist')
api.add_resource(Data, '/data/<string:identifier>')

