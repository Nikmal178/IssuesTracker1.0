from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

def index():
    return render_template("index.html")

@app.route('/issues/<name>')

def issues(name):
    return render_template("issues.html", username=name)


