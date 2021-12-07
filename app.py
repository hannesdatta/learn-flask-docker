from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    #f = open('/run/secrets/db_password', 'r')
    f = open('myapp/test.txt', 'r')
    con = f.read()
    return "Hello, Worlnd!" + con + os.getenv('FLASK_APP') + os.getenv('SECRETPWD')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)
