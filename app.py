#!/usr/bin/env python
# coding: utf-8

import os

from flask import Flask, render_template, flash, request, jsonify

from lib import calculate_data

app = Flask(__name__)


@app.route('/_points_six')
def points_six_recomm():
    p_max = request.args.get('points_max', 0, type=int)
    if p_max in range(0, 13):
        res = 0
    elif p_max in range(13, 25):
        res = 1
    elif p_max in range(25, 37):
        res = 2
    elif p_max in range(37, 49):
        res = 3
    else:
        res = 4

    return jsonify(result=res)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    try:
        points_max = int(request.form['points_max'])
        points_six = int(request.form['points_six'])
    except ValueError:
        flash(u'Keine gültigen Zahlen angeben.')
        data = list()
    else:
        data = calculate_data(points_max, points_six)
    return render_template('result.html', data=data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
