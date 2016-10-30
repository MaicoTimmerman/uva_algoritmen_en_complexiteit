# Algorithms and Complexity
# 02-10-2014
# Series 4 - Exercise 3c, 3d

# Boudewijn Braams  10401040
# Govert Verkes     10211748
# Maico Timmerman   10542590
# Robin Klusman     10675671

from math import *
import numpy as np

# All 8th roots of unity
roots_8th = [1,
             0.5*sqrt(2) - 0.5*sqrt(2)*1j,
             -1j,
             -0.5*sqrt(2) - 0.5*sqrt(2)*1j,
             -1,
             -0.5*sqrt(2) + 0.5*sqrt(2)*1j,
             1j,
             0.5*sqrt(2) + 0.5*sqrt(2)*1j]

# DFT of p(x), results from hand calculations (3b)
dft_px = [15,
          -4+3-1j*(2-3)+(0.5*sqrt(2)-0.5*sqrt(2)*1j)*(2+1j),
          2-1j,
          -4+3+1j*(2-3)+(-0.5*sqrt(2)-0.5*sqrt(2)*1j)*(2-1j),
          9,
          -4+3-1j*(2-3)+(-0.5*sqrt(2)+0.5*sqrt(2)*1j)*(2+1j),
          2+1j,
          -4+3+1j*(2-3)+(0.5*sqrt(2)+0.5*sqrt(2)*1j)*(2-1j)]

################################################################################

# 3c, solve p(x) for all 8th roots of unity
def solve(x):
    return x**7 + 3*x**6 + 4*x**4 + 2*x**2 + 2*x + 3

print "3c:"

# Prints out every element of the DFT vector, also prints the value calculated
# by hand, for verification purposes
for i, root in enumerate(roots_8th):
    entry = solve(root)
    print "\t{}:\t{}\n\t\t{} (from 3b)".format(i, entry, dft_px[i])

################################################################################

# 3d, apply inverse fourier transformation to vector

print "\n3d:"

# Apply inverse fourier transformation
for power, coefficient in enumerate(np.fft.ifft(dft_px)):
    print "\t{} x^{}".format(coefficient.real, power) # Ignore imaginary part