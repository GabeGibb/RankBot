import main
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bot is up and running'

# with app.app_context():
#     import main

# Thread(target=app.run, kwargs={'host': '0.0.0.0'}).start()
# app.run(host='0.0.0.0')

