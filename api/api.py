import flask
from flask import request, jsonify
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>New Testament Helper API</h1>
<p>A prototype API for New Testament Studies.</p>'''

# Route to return all available texts that can be compared
@app.route('/texts', methods=['GET'])
def texts():
    # TODO Rather than using local files use a database
    return jsonify(os.listdir('./resources'))

@app.route('/levenshtein', methods=['GET'])
def levenshtein():
    document1 = request.args.get('document1')
    document2 = request.args.get('document2')
    print('Query')
    print(document1)
    print(document2)
    # TODO Calculate leventshtein distance and return in json response
    arr = os.listdir('./resources')
    response = {
        'levenshtein': {
            'mss': arr,
            'values': {
                'x': { 
                    'label': arr[0],
                    'values': [1,2,3]
                },
                'y': {
                    'label': arr[1],
                    'values': [1,2,3]
                }
            }
        }
    }
    return jsonify(response)

app.run()