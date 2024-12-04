from flask import render_template, request
from src import create_app
import requests

app = create_app()

@app.route('/')
def get_home():
    return render_template("base.html")

@app.route('/about')
def get_about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)