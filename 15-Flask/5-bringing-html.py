# IMPORTING
from flask import Flask, render_template

# INTERACTION
web = Flask(__name__)

# MAPPING
@web.route('/')
@web.route('/register')

# INPUTS
def homepage():
    return render_template('register.html')

# MAIN
if __name__ == "__main__":
    web.run(debug = True)
