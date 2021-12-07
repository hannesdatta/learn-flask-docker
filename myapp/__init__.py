from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    #f = open('/run/secrets/db_password', 'r')
    f = open('test.txt', 'r')
    con = f.read()
    return "Hello, my amazing World!" + con + os.getenv('FLASK_APP') + os.getenv('SECRETPWD')
