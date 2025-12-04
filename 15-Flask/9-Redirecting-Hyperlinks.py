# IMPORTING
from flask import Flask, render_template
# INTERACTION
app = Flask(__name__)

# MAPPING
@app.route("/")

# INPUTS
def first():
    return render_template("home.html")

@app.route("/second")
def second():
    return "Welcome to second page."

# MAIN
if __name__ == "__main__":
    app.run(debug = True)
