# coding: utf-8

import math


def frange(limit1, limit2, increment):
    count = int(math.ceil(limit2 - limit1)/increment)
    return (limit1 + n*increment for n in xrange(count))


def calc_grade(points_max, points_six, points):
    grade = 6 - (points - points_six) * (5.0 / (points_max - points_six))
    grade = math.floor(grade * 4) / 4
    if grade > 6:
        return 6.
    return grade


def calculate_data(points_max, points_six):
    data = list()
    grade = 6.
    points_end = 0.
    points_start = 0.

    for points in frange(0, points_max + 1, 0.5):
        new_grade = calc_grade(points_max, points_six, points)
        if new_grade != grade:
            data.append((points_end, points_start, grade))
            points_start = points
            grade = new_grade
        points_end = points

    return reversed(data)