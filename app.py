#!/usr/bin/env python
# coding: utf-8

import itertools
import logging
import os

from flask import Flask, render_template, flash, request

import lib

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler())
app.secret_key = os.environ['SECRET_KEY']


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    try:
        points_start = int(request.form['points_start'])
        points_end = int(request.form['points_end'])
        if points_end < 0 or points_start < 0:
            raise ValueError
        if points_end < points_start:
            raise ValueError
        if points_end - points_start > 200:
            raise ValueError
        factor_six = float(request.form['factor_six'])
        if not 0 < factor_six < 1:
            raise ValueError
        steps = request.form['steps']
    except ValueError:
        flash(u'Keine gültigen Zahlen angeben.')
        table = list()
    else:
        table = lib.get_table(points_start, points_end, factor_six, steps)
        table = itertools.izip(*table)
    return render_template('result.html', table=table)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
