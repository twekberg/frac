#!/usr/bin/env python
"""
Handles integers with fractions.
"""

# TODO:
# Do methods for these:
# neg, 
# do this to find more: dir(int)

import argparse
from fractions import Fraction
import sys


def build_parser():
    """
    Collect command line arguments.
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('integer', type=int,
                        help='The integer portion of the number.')
    parser.add_argument('numerator', type=int,
                        help='The numerator of the fractional part of the number.')
    parser.add_argument('denominator', type=int,
                        help='The denominator of the fractional part of the number.')
    return parser


class Frac():
    def __init__(self, integer, numerator, denominator):
        self.integer = integer
        self.fraction = Fraction(numerator, denominator)
        self.normalize()


    def normalize(self):
        """
        Move integer parts of fraction to self.integer.
        """
        if abs(self.fraction.numerator) >= abs(self.fraction.denominator):
            new_numerator = self.fraction.numerator % self.fraction.denominator
            self.integer += int(self.fraction.numerator / self.fraction.denominator)
            self.fraction = Fraction(new_numerator, self.fraction.denominator)
        return self


    def __repr__(self):
        return f"Frac({self.integer}, {self.fraction.numerator}, {self.fraction.denominator})"


    def __str__(self):
        return f"{self.integer}, {self.fraction}"


    def unary(self, operator_func):
        # Convert self to fraction.
        self_temp = Fraction(
            self.integer * self.fraction.denominator + self.fraction.numerator,
            self.fraction.denominator)
        ans = operator_func(self_temp)
        temp = Frac(0, ans.numerator, ans.denominator)
        temp.normalize()
        return temp


    def binary(self, other, operator_func):
        # Convert self and other to fractions.
        self_temp = Fraction(
            self.integer * self.fraction.denominator + self.fraction.numerator,
            self.fraction.denominator)
        other_temp = other.integer + \
                     Fraction(other.fraction.numerator, other.fraction.denominator)
        ans = operator_func(self_temp, other_temp)
        temp = Frac(0, ans.numerator, ans.denominator)
        temp.normalize()
        return temp


    def __abs__(self):
        return self.unary(lambda a: abs(a))
        

    def __add__(self, other):
        return self.binary(other, lambda a, b: a + b)


    def __eq__(self, other):
        return (self.integer == other.integer) and \
            (self.fraction == other.fraction)


    def __ge__(self, other):
        if self.integer == other.integer:
            return self.fraction >= other.fraction
        return self.integer >= other.integer


    def __gt__(self, other):
        if self.integer == other.integer:
            return self.fraction > other.fraction
        return self.integer > other.integer


    def __le__(self, other):
        if self.integer == other.integer:
            return self.fraction <= other.fraction
        return self.integer <= other.integer


    def __lt__(self, other):
        if self.integer == other.integer:
            return self.fraction < other.fraction
        return self.integer < other.integer


    def __mul__(self, other):
        return self.binary(other, lambda a, b: a * b)


    def __ne__(self, other):
        if self.integer == other.integer:
            return self.fraction != other.fraction
        return True



    def __neg__(self):
        return Frac(-self.integer, -self.fraction.numerator, self.fraction.denominator,)
      

    def __sub__(self, other):
        return self.binary(other, lambda a, b: a - b)


    def __truediv__(self, other):
        return self.binary(other, lambda a, b: a / b)


def main(args):
    """
    Starting point.
    """
    print(Frac(args.integer, args.numerator, args.denominator))


if __name__ == '__main__':
    sys.exit(main(build_parser().parse_args()))

"""
from frac import Frac

w2x4=Frac(3, 9, 16)
two = Frac(2,0,1)
half = w2x4 / two

down = Frac(18,0,1)
down + half - Frac(0,1,2)
Frac(19, 9, 32)
down - half + Frac(0,1,2)
Frac(16, 23, 32)


# 2x4
over = Frac(19,1,2)
length = Frac(10,7,8)
(over - length) / two + Frac(0,1,2)
Frac(4, 13, 16)
(over - length) / two + length - Frac(0,1,2)
Frac(14, 11, 16)

# (x,y) coordinates
# for screw holes
(4 13/16", 16 23/32")
(4 13/16",  19 9/32")
(14 11/16", 16 23/32")
(14 11/16", 19 9/32")
"""
