from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/name')
def hello_name():
    return 'hello pratheek'

<<<<<<< HEAD
if __name__=="__main__":
    app.run(debug=True)
    app.run(host='127.0.0.1',port=80)
=======

@app.route('/details')
def details_json():
    retJson = {
        'name': 'pratheek',
        'age': 25,
        'contact': [
            {
                'email': 'p@gmail.com',
                'phone': '9393939'
            },
            {
                'phone2': 242353252
            }
        ]
    }

    return jsonify(retJson)


if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> baaeaf7ca772751222099ef6f4756364400aab52
