import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
mockData = {
    'levenshtein': {
        'mss': ['001', '002', '003'],
        'values': {
            'x': { 
                'label': 'x_values',
                'values': [1, 2, 3, 4, 5]
            },
            'y': {
                'label': 'y_values',
                'values': [2, 4, 5, 6, 8]
            }
        }
    }
}


@app.route('/', methods=['GET'])
def home():
    return '''<h1>New Testament Helper API</h1>
<p>A prototype API for New Testament Studies.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/all', methods=['GET'])
def api_all():
    return jsonify(mockData)

app.run()