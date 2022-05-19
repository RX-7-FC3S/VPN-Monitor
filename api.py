# coding: utf-8

import os
import re
from flask import Flask
from flask import render_template, jsonify, send_from_directory


app = Flask(__name__, template_folder='templates', static_folder='statics')
methods = ['GET', 'POST']


@app.route('/', methods=methods)
def index():
    return render_template('index.html')


@app.route('/service_xl2tpd_status')
def service_xl2tpd_status():
    status = os.popen('sudo service xl2tpd status').readlines()
    res = []
    for line in status:
        res.append(line)
    res = {'res': res}
    return jsonify(res)


@app.route('/service_ipsec_status')
def service_ipsec_status():
    status = os.popen('sudo service ipsec status').readlines()
    res = []
    for line in status:
        res.append(line)
    res = {'res': res}
    return jsonify(res)


@app.route('/connecting_number')
def connecting_number():
    task_number = os.popen('sudo service xl2tpd status | grep Tasks').read()
    return task_number


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='1025', debug=True)
