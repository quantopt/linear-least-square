#!/usr/bin/python
import csv
import sys
from math import sqrt, pi
from operator import itemgetter
from optparse import OptionParser



def fit(x, t):
    n = len(x)
    mx = sum(x)/n
    my = sum(y)/n
    b = sum([yi*(xi-mx) for xi, yi in zip(x,y)])/sum([xi*(xi-mx) for xi in x])
    a = my - mx*b
    f = [a+b*xi for xi in x]
    r = [yi-fi for fi,yi in zip(f,y)]
    s = sum([ri**2 for ri in r])
    std_dev = sqrt(s/(n-2))
    
    ss_reg = sum([(fi-my)**2 for fi in f])
    ss_tot = sum([(yi-my)**2 for yi in y])
    rp = [sqrt((yi-fi)**2) for fi,yi in zip(f,y)]
    print sum(rp)/n

    r_squared = 100*ss_reg/ss_tot
    return (a, b, std_dev, r_squared)


def main():
    usage = "usage: %prog [options] input_file"
    description = "Least squares fit"
    parser = OptionParser(usage=usage, description=description)
    parser.set_defaults(freq=852.09, solver="0")
    parser.add_option("-f", "--freq", help="set frequency of laser in nm", type="float")
    parser.add_option("-p", "--printall", help="print intermediate calculations", action="store_true", default=False)
    (options, args) = parser.parse_args()
    return (options, args)
    

if __name__ == "__main__":
    options, args = main()
    filename = args[0]
    x = []
    y = []

    for line in open(filename):
        xi, yi = line.strip().split(" ")
        x.append(float(xi))
        y.append(float(yi))

    a, b, std_dev, r_squared = fit(x, y)
    print "a: %8.6s  b: %8.6s  stddev: %8.6s   r^2: %8.6s" % (round(a,4), round(b,4), round(std_dev,4), round(r_squared,4))

