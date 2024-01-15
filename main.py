import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    some = os.environ.get('someVar')
    return 'This is output: {}!\n second line'.format(some)


if __name__ == "__main__":
    app.debug = True
    app.host = '0.0.0.0'
    app.port = int(os.environ.get('PORT', 8080))
    app.run()
