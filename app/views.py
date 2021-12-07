from app import app
import os

@app.route('/')
def home():
    f=open('secrets.txt').readlines()
    secr=f[0]
    return("Hello world! I can also display (non-secret) environment variables: " + os.getenv('FLASK_APP') + ' and secret credentials: '+ secr)
