from flask import Flask,jsonify
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/name')
def hello_name():
    return 'hello pratheek'

@app.route('/details')
def details_json():
    retJson={
    'name':'pratheek',
    'age':25,
    'contact':[
    {
    'email':'p@gmail.com',
    'phone':'9393939'
    },
    {
    'phone2':242353252
    }
    ]
    }

    return jsonify(retJson)


if __name__=="__main__":
    app.run()
