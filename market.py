from flask import Flask, render_template
from dotenv import load_dotenv
import os


app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True, port=os.getenv("PORT"))
