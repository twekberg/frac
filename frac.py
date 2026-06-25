#!/usr/bin/env python
"""
Handles integers with fractions.
"""


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
                        help='The integer portion of thee number. ')
    parser.add_argument('numerator', type=int,
                        help='The numerator of the fractional part of thee number. ')
    parser.add_argument('denominator', type=int,
                        help='The denominator of the fractional part of thee number. ')
    return parser

class Frac():
    def __init__(self, integer, numerator, denominator):
        self.integer = integer
        self.fraction = Fraction(numerator, denominator)


    def normalize(self):
        """
        Move integer parts of fraction to self.integer.
        Only works on positive numbers.
        """
        if self.fraction > 1:
            numerator = self.fraction.numerator % self.fraction.denominator
            self.integer += int(self.fraction.numerator / self.fraction.denominator)
            self.fraction = Fraction(numerator, self.fraction.denominator)


    def __str__(self):
        self.normalize()
        return f"{self.integer}, {self.fraction}"


def main(args):
    """
    Starting point.
    """
    print(Frac(args.integer, args.numerator, args.denominator))


if __name__ == '__main__':
    sys.exit(main(build_parser().parse_args()))
