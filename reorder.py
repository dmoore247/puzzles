
'''
Take input of negative and positive integers.
  Output numbers, negative numbers first, then positive integers, preserving order

  Why?
  How might this be used?
  What's the size of the input?
  Any other requirements?

  Solution brainstorm:
    Scan input twice, once for negative, once for positive values, output values in order
    Scan once, use two stacks, one for positive, one for negatives
    Scan once, use two output arrays
    Generator with a position marker?
'''

# Input
X = [4, -2, 5, -1, 6, -3 ]

# Sample output
Y = [-2, -1, -3, 4, 5, 6 ]

# Answer buffer
A = []

# scan twice
for x in X:
    if x < 0:
        A.append(x)
for x in X:
    if x >= 0:
        A.append(x)

print ('Input   ', X)
print ('Answer 1', A)
assert A == Y

negative=[]
positive=[]

for x in X:
    if x < 0:
        negative.append(x)
    else:
        positive.append(x)

import numpy as np

A2 = np.concatenate( [ negative, positive ] ).tolist()

print ('Answer 2', A2) 
