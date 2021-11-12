from flask import Flask, jsonify,request
from flask_restful import Api, Resource

app = Flask(__name__)
api=Api(app)

class Add(Resource):
    def post(self):
        req_data=request.get_json()
        x=int(req_data['x'])
        y=int(req_data['y'])
        sum=x+y
        ret={
        'Message':sum,
        'Status Code':200
        }
        return jsonify(ret)





api.add_resource(Add,'/add')



@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/name')
def hello_name():
    return 'hello pratheek'


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

@app.route('/addition',methods=["POST"])
def addition():
    d_dict=request.get_json()
    num1=d_dict["x"]
    num2=d_dict["y"]
    sum=num1+num2
    retjson={
        'Sum':sum
    }
    return jsonify(retjson),200


if __name__ == "__main__":
    app.run(debug=True,port=5000)
