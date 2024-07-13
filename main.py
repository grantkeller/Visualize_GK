from flask import render_template
from website import create_app
from website.views import home, greet

app = create_app()

@app.route('/')
def get_home():
    return render_template("base.html")

@app.route('/greet')
def get_greet():
    response = greet('Grant')
    return response

if __name__ == '__main__':
    app.run(debug=True)