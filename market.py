from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello world but bigger</h1>"

@app.route('/about')
def about():
    return "about"


if __name__ == "__main__":
    app.run(debug=True)
