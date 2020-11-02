import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_sample(self) : 
        for n in range(1,10) : 
            d = sample(n) 
            self.assertTrue( len(d)==n, "Your code for generating the samples does not generate NumPy arrays with the correct number of elements" )
        data = sample(20)
        for d in data : 
            lll, uuu = scipy.stats.norm.ppf( 0.005 ), scipy.stats.norm.ppf( 0.995 )
            self.assertTrue( lll<d and d<uuu, "Your code for generating the samples does not generate normal random variables with expectation 0.  I test this by performing a hypothesis test with a confidence limit of 1%.  There is thus a small chance that this test will fail for a correct code." )
            
    def test_sample_mean(self) : 
        data = sample(20)
        mm = sum(data)/ len(data) 
        self.assertTrue( np.abs( mm - sample_mean(data))<1e-7, "Your code for calculating the sample mean is not correct" )
        
    def test_graph(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_y)==10, "The wrong number of y-coordinates have been plotted in the graph.  There should be 10 sample means." )
        for y in this_y :
            lll, uuu = scipy.stats.norm.ppf(0.005, loc=0, scale=1/np.sqrt(20)), scipy.stats.norm.ppf(0.995, loc=0, scale=1/np.sqrt(20))
            self.assertTrue( lll<y and y<uuu, "The points generated on the graphs do not appear to be samples from the correct distribution.  I test this by performing a hypothesis test with a confidence limit of 1%.  There is thus a small chance that this test will fail for a correct code." )
        figdat = fighand.get_lines()[1].get_xydata()
        this_x2, this_y2 = zip(*figdat)
        self.assertTrue( np.abs( sum(this_y)/len(this_y) - this_y2[0] )<1e-7, "The horizonal line you have drawn on the graph is not equal to the sample mean computed from the points on the graph as it should be" )
