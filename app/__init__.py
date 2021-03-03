import os

from pprint import pprint as pp
from flask import Flask, render_template, request
from app.weather import query_api

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('weather.html', data=[])


@app.route("/result", methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('search_country')
    resp = query_api(select)
    pp(resp)
    if resp:
        data.append(resp)
        pp(len(data))
    if "message" in data[0]:
        error = data[0]["message"]
        return render_template('error.html', data=data, context={"error":error})
    return render_template('result.html', data=data, error=error)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=int(os.environ.get("PORT", 8080)))
