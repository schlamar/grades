# coding: utf-8

import math


STEP_FACTORS = {'quarter': 4, 'tenth': 10}


def frange(limit1, limit2, increment):
    count = int(math.ceil(limit2 - limit1) / increment)
    return (limit1 + n * increment for n in xrange(count))


def calc_grade(points_max, points_six, points, steps):
    step_factor = STEP_FACTORS[steps]
    grade = 6 - (points - points_six) * (5.0 / (points_max - points_six))
    grade = math.floor(grade * step_factor) / step_factor
    if grade > 6:
        return 6.
    return grade


def calculate_data(points_max, points_six, steps):

    data = list()
    grade = 6.
    points_end = 0.
    points_start = 0.

    for points in frange(0, points_max + 1, 0.5):
        new_grade = calc_grade(points_max, points_six, points, steps)
        if new_grade != grade:
            data.append((points_end, points_start, grade))
            points_start = points
            grade = new_grade
        points_end = points

    return reversed(data)
