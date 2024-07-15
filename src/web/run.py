from flask import Flask

app = Flask(__name__)

if "__main__" == __name__:
    app.run(host='0.0.0.0', prort='5000')