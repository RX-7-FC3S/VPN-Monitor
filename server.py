# coding: utf-8

import xl2tpd
from flask import Flask
from flask import render_template, jsonify


app = Flask(__name__, template_folder='templates', static_folder='statics')
methods = ['GET', 'POST']


@app.route('/', methods=methods)
def index():
    return render_template('index.html')


@app.route('/service_xl2tpd_log')
def service_xl2tpd_status():
    xl2tpd_status = xl2tpd.status()
    return jsonify(xl2tpd_status)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='1025', debug=True)
