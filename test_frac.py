#!/usr/bin/env python
"""
Test cases for frac.py

Unable to get pytest to work. This is almost as good for this file.
"""

import sys
import traceback

from frac import Frac

def test_abs():
    assert abs(Frac(-2, 1, 4)) == Frac(1, 3, 4)

def test_add():
    assert Frac(2, 1 ,4) + Frac(3, 2, 4) == Frac(5, 3, 4)

def test_eq():
    assert Frac(9, 2, 3) == Frac(8, 5, 3)

def test_gt():
    assert Frac(9, 2, 3) > Frac(8, 2, 3)
    assert Frac(9, 2, 3) > Frac(8, 1, 3)

def test_le():
    assert Frac(9, 2, 3) <= Frac(9, 2, 3)
    assert Frac(9, 2, 3) <= Frac(10, 2, 3)
    assert Frac(9, 2, 3) <= Frac(9, 5, 6)

def test_lt():
    assert Frac(9, 2, 3) < Frac(9, 5, 6)


def test_mul():
    assert Frac(9, 2, 3) * Frac(2, 5, 6) == Frac(27, 7, 18)

def test_ne():
    assert Frac(9, 2, 3) != Frac(2, 2, 3)
    assert Frac(9, 2, 3) != Frac(9, 1, 3)
    assert Frac(9, 2, 3) != Frac(9, 5, 6)

def test_neg():
    assert -Frac(9, 2, 3) == Frac(-9, -2, 3)
    assert -Frac(-9, -2, 3) == Frac(9, 2, 3)

def test_repr():
    assert repr(Frac(9,2,3)) == 'Frac(9, 2, 3)'

def test_sub():
    assert Frac(9,2,3) - Frac(9, 1, 3) == Frac(0, 1, 3)

def test_str():
    assert str(Frac(10,1,2)) == '10, 1/2'

def test_truediv():
    assert Frac(10, 2, 3) / Frac(2, 0, 1) == Frac(5, 1, 3)

TEST_CASES = [(test, func)
              for (test, func) in locals().items()
              if test.startswith('test_')]


def main():
    test_counter = 0
    error_counter = 0
    for (test, func) in TEST_CASES:
        test_counter += 1
        try:
            func()
        except AssertionError as e:
            error_counter += 1
            print(f'{test} got an error')
            # The -1 says to print the line that got the assert exception.
            print(traceback.format_exc(limit=-1))
            
    print(f'N Tests: {test_counter}, Errors: {error_counter}')

if __name__ == '__main__':
    sys.exit(main())
