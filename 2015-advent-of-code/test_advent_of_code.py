"""
Tests for Advent of Code
"""

import day1, day2, day3, day4


def test_day_1():
    version = day1.find_santas_floor_v3
    assert day1.find_santas_floor('(())', version=version) == 0
    assert day1.find_santas_floor('()()', version=version) == 0
    assert day1.find_santas_floor('(((', version=version) == 3
    assert day1.find_santas_floor('(()(()(', version=version) == 3
    assert day1.find_santas_floor('))(((((', version=version) == 3
    assert day1.find_santas_floor('())', version=version) == -1
    assert day1.find_santas_floor('))(', version=version) == -1
    assert day1.find_santas_floor(')))', version=version) == -3
    assert day1.find_santas_floor(')())())', version=version) == -3

    assert day1.basement_entrance(')') == 1
    assert day1.basement_entrance('()())') == 5

def test_day_2():
    assert day2.order_paper(['2x3x4']) == 58
    assert day2.order_paper(['1x1x10']) == 43
    assert day2.order_paper(['2x3x4', '1x1x10']) == 58 + 43

    assert day2.order_ribbons(['2x3x4']) == 34
    assert day2.order_ribbons(['1x1x10']) == 14
    assert day2.order_ribbons(['2x3x4', '1x1x10']) == 34 + 14

def test_day_3():
    assert day3.delivered_houses('>') == 2
    assert day3.delivered_houses('^>v<') == 4
    assert day3.delivered_houses('^v^v^v^v^v') == 2

    assert day3.delivered_houses_with_robot('^v') == 3
    assert day3.delivered_houses_with_robot('^>v<') == 3
    assert day3.delivered_houses_with_robot('^v^v^v^v^v') == 11

def test_day_4():
    assert day4.generate_advent_coins('abcdef') == 609043
    assert day4.generate_advent_coins('pqrstuv') == 1048970