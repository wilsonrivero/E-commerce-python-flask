from flask import Flask

app = Flask(__name__)
PORT = 3000


if __name__ == "__main__":
   app.run(True, PORT)