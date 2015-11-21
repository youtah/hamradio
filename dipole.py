#!/usr/bin/env python
import sys
import math
import argparse
from fractions import Fraction

def main():
    args = makeargs()
    print "Frequency: "+str(args.megahertz)
    print "Velocity: "+str(args.velocity)

    feet = (((300/args.megahertz)/4)*(args.velocity*0.01)*3.28084)
    inches = (feet-int(math.floor(feet)))*10
    fraction = Fraction(round(inches-math.floor(inches),2)).limit_denominator()
    if (fraction is not None) and (fraction != 0):
        frac_string = "and "+str(fraction)
    else:
        frac_string = ""
    feet = int(math.floor(feet))
    inches = int(math.floor(inches))
    if inches > 1:
        inches_string = "es"
    print str(feet)+" feet, "+str(inches)+" "+str(frac_string)+" inch"+str(inches_string)

def makeargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--megahertz', type=float, help='Interger or floating point in megahertz. Example: 14.225.')
    parser.add_argument('-v', '--velocity', type=int, default=95, help='Integer: This is the Velocity Factor, in a percentage. Example: 95 for 95 percent.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
