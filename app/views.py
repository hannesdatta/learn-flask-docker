from app import app
import os

@app.route('/')
def home():

   return "Hello world! I can also display (non-secret) environment variables: " + os.getenv('FLASK_APP') + ' and secret credentials: '
