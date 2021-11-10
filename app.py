from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/name')
def hello_name():
    return 'hello pratheek'

if __name__=="__main__":
    app.run()
    app.run(debug=True,host='127.0.0.1',port='80')
