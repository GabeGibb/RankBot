import main

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bot is up and running'




# app.run(host='0.0.0.0')