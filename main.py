from flask import render_template, request
from src import create_app
from src.utils import connect_to_mysql, query_county
import requests

app = create_app()

@app.route('/')
def get_home():
    return render_template("base.html")

@app.route('/county', methods=['GET'])
def get_county_info():
    con = connect_to_mysql()
    county = request.args.get('county')
    result = query_county(con, county)
    return result, 200

if __name__ == '__main__':
    app.run(debug=True)