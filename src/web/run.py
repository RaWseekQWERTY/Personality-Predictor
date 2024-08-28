from flask import Flask
from src.web import pages

app = Flask(__name__)
app.register_blueprint(pages.bp)

if "__main__" == __name__:
    app.run(host='0.0.0.0', port=5000)