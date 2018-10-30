# Kalman filter example demo in Python

# A Python implementation of the example given in pages 11-15 of "An
# Introduction to the Kalman Filter" by Greg Welch and Gary Bishop,
# University of North Carolina at Chapel Hill, Department of Computer
# Science, TR 95-041,
# http://www.cs.unc.edu/~welch/kalman/kalmanIntro.html

# by Andrew D. Straw
import matplotlib.pyplot as plt

mu, sigma = 0, 500

x = np.arange(1, 100, 0.1) # x axis
z = np.random.normal(mu, sigma, len(x)) # noise
y = x ** 2 + z # data
plt.plot(x, y, linewidth=2, linestyle="-", c="b") # it include some noise
plt.show()