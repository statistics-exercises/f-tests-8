# Taking multiple samples

You now know how to use the f-distribution to test whether the variances for two sampled distributions are the same or different.  In the remainder of this exercise, we are going to consider one further kind of test we can perform using the f-distribution.  Before we get on to doing these tests, however, we are going to complete a few tasks in order to understand this new test a bit better.

Let's start with an example of what we are trying to find out.  Consider the data in the table below:

![](mytable.png)

To generate the data in this table a farmer sewed 16 fields with cabbage plants.  Each of the numbers in the tables is thus the tonnage of cabbage that was harvested from a particular field.  The farmer fertilised the 16 fields in four different ways.  4 of the fields were fertilised with straw only.   4 fields were fertilized with a combination of straw and nitrate.   4 of the fields were fertilized with a combination of straw and phosphate.  The remaining fields were then fertilised with straw, nitrate and phosphate.  The farmer would like to determine if one of these fertiliser treatments was more effective than the others.  The farmer's hope is to determine how he should fertilise his fields next year in order to get the largest possible cabbage crop. 

The numbers in each row of the table are yields from fields that were fertilised in the same way.  You can see that a particular method of fertilisation does not generate consistent yields.  There is instead some variation in the yields even when they are fertilised in the same way.  The yield for a field that was fertilised with only straw is thus a sample from a distribution.  The yield for a field that was fertilized using straw and nitrate, by contrast, is a sample from a second distribution.  The question the farmer is asking is, therefore, are the parameters of the four distributions that have been sampled to generate the data in the table above the same or different?  In other words, we are testing:

![](https://render.githubusercontent.com/render/math?math=H_0:\mu_1=\mu_2=\mu_3=\mu_4\qquad\textrm{against}\qquad\H_1: \textrm{these four expectations are not all equal})

where ![](https://render.githubusercontent.com/render/math?math=\mu_1), ![](https://render.githubusercontent.com/render/math?math=\mu_2), ![](https://render.githubusercontent.com/render/math?math=\mu_3) and ![](https://render.githubusercontent.com/render/math?math=\mu_4) are the expectations of the four distributions that have been sampled to generate the data.  

As discussed above, we will come back to how precisely this sort of test is performed.  Over the next few tasks, we are instead going to introduce the statistic that we will use to perform this hypothesis test and we are going to consider how it is distributed under the assumption of the null hypothesis.  __The goal in this particular task is to create a data set that is similar to that in the table above.__    To do this you will need to complete the function called `sample`.  This function takes a single integer `N` in input.  It should return a NumPy array with `N` elements that are all `samples` from a standard normal random variable.  We will thus be able to use this function to generate as many samples as we need.

In addition to writing the function called sample you will also need to complete the function called `sample_mean`.  This function takes a NumPy array in input called `data`.  It should return the sample mean that is calculated using the data in `data`.

Once you have completed the `sample` and `sample_mean` functions you can generate the graph that is the ultimate goal in this exercise.  __To pass the test you will need to set the variables called `fmean` and `yvals` that are plotted in the graph.__ 

1. `yvals` - is a NumPy array with 10 elements.  Each of these 10 elements should be set equal to __a sample mean that is calculated from 20 standard normal random variables__.  You can obviously use the function called `sample` to generate each set of 20 random variables.
2. `fval` - is a scalar.  The value of this quantity should be calculated by computing a sample mean using __all__ the data that was used to calculate the 10 sample means in `yvals`. 

Once you complete the code a graph is generated in which the 10 sample means in yvals are plotted as black points.  A red horizontal line is then drawn to indicate the value of `fval`.  Think about what you have learned in this module when you look at the graph.  All the numbers in `yvals` are random variables.  `fval` is also a random variable.  Are the expectations and variances of these distributions are sampled from the same or different? 
