from flask import Flask

PORT = 3000

app = Flask(__name__)


if __name__ == "__main__":
   app.run(debug=False, port=PORT)