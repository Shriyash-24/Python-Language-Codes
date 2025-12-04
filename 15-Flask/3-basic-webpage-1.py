from flask import Flask

web = Flask(__name__)

@web.route('/')

def home():
    return "Welcome"

if __name__ == "__main__":
    web.run(debug = True)

# www.youtube.com --> / refers to this..