# coding: utf-8

import math


STEP_FACTORS = {'quarter': 4, 'tenth': 10}
STEP_INCREMENT = {'quarter': 0.25, 'tenth': 0.1}


def frange(limit1, limit2, increment):
    count = int(math.ceil((limit2 - limit1) / increment))
    return (limit1 + n * increment for n in xrange(count))


def calc_points(points_max, points_six, grade_step, sum_steps):
    dist_points = points_max - points_six
    diff = (dist_points / float(sum_steps)) * grade_step
    diff = math.ceil(diff * 2) / 2  # round to 0.5
    return points_max - diff


def calc_row(points_max, points_six, steps):
    step_factor = STEP_FACTORS[steps]
    sum_steps = 5 * step_factor
    for grade_step in xrange(sum_steps + 1):
        yield calc_points(points_max, points_six, grade_step, sum_steps)


def get_grades_row(steps):
    inc = STEP_INCREMENT[steps]
    return frange(1.0, 6.0 + inc, inc)


def get_table(points_start, points_end, factor_six=0.082, steps='quarter'):
    print points_start, points_end, factor_six, steps
    yield get_grades_row(steps)
    for points in xrange(points_start, points_end + 1):
        points_six = int(points * factor_six)
        yield calc_row(points, points_six, steps)
