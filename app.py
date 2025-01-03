import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world, welcome to Railway!'
# if __name__ == '__main__':
#     app.run(debug=True)