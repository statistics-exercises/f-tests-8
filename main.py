import matplotlib.pyplot as plt
import numpy as np

def sample(N) : 
  # Your code to generate and return a numpy array with 
  # N samples from a standard normal random variable goes
  # here.
  
  
def sample_mean( data ) : 
  # Your code to calcualte the sample mean from the input data 
  # goes here.
  
  
# You need to modify the code here to generate the data for your graph.
# To generate this data you need to use the function called sample to create 10 samples of size 20.
# A sample mean should be computed for each 20 element block of data generated using sample.
# the values of these sample means should be stored in the 10 elements of the NumPy array callled yvals.
# At the same time a sample mean should be computed from all the 10*20 data points in the 10 separate 
# samples you generate.  This variable fmean should be set equal to the mean that is computed in this way.
fmean, xvals, yvals = 0, np.zeros(10), np.zeros(10)
for i in range(10) :
  xvals[i] = i+1


# This will plot your graph once you have prepared the data using the instructions
# on the right
plt.plot( xvals, yvals, 'ko' )
plt.plot( [0,10], [fmean,fmean], 'r-' )
plt.savefig("means.png")
