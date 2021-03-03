import os

from pprint import pprint as pp
from flask import Flask, render_template, request
from app.weather import query_api

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('weather.html', data=
    [
        {'name': 'Toronto'},
        {'name': 'Montreal'},
        {'name': 'Calgary'},
        {'name': 'Ottawa'},
        {'name': 'Edmonton'},
        {'name': 'Mississauga'},
        {'name': 'Winnipeg'},
        {'name': 'Vancouver'},
        {'name': 'Brampton'},
        {'name': 'Quebec'}
    ])


@app.route("/result", methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
        data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template('result.html', data=data, error=error)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=int(os.environ.get("PORT", 8080)))
