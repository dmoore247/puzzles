'''
    Cartesian product of a vector of vectors
    
    The coding challenge was print all combinations you can create  from a vector of a vector of strings, find all valid strings you can create from a list of letters you have.

    Input: [ [ a, b ], [ c, d, e ], [ f, g ] ]
    
  Questions
    ? Max scale of Input
    ? Domain - single ascii/utf-8 characters
    ? Strict Cartesian or all combinations, e.g. are single character strings included?
    ? Vector of a Vector of Strings, yet example shows single characters
    ? What would you like returned in case of invalid input
    ? Invalid:
        Empty set
        numbers
        non-alphanumeric
        non-printable
        multi-byte
  
  Solution Approaches
    a. Decompose problem to cartesian product of two vectors, then appy to all vectors within the vector.
    b. Some kind of looping, array of loops...
    c. Faster python: Numpy
    d. Large Scale: Create large scale data tables for each vector, use iterative Spark cartesian join
    e. Tensorflow + GPU matrix calculation
    Issues: A x B x C x D is not commuttative, but does ( A x B ) x ( C x D ) == A x B x C x D? If so, computation can be parallelized

  Acceptance
    Solution length = the product of all of the individual vector lengths
    Length of each string = length of the outside vector
    Solution contains first character of each inside vector, concatenated
    Solution contains the set of last characters of each inside vector, concatenated
'''
from functools import reduce
import operator

def cart2 (a, b):
    out=[]
    for x1 in a:
        #print ('x1 ',x1)
        for x2 in b:
            out.append(reduce(operator.concat,[x1,x2]))
    return out

def cartesian( input ):
    # check input
    return  reduce ( lambda x, y : cart2(x,y), INPUT )

'''
    Run tests on cart2 and cartesian
'''
if __name__ == "__main__":
    INPUT = [ [ 'a', 'b' ], [ '1', '2', '3' ], [ 'f', 'g' ], ['h','i','j','k'] ]
    r1 = cart2( INPUT[0], INPUT[1] )
    print ('r1 =', r1)

    r2 = cart2(r1, INPUT[2])
    print ('r2 = ', r2)

    r3 = cartesian( INPUT )
    print ('r3 = ', r3)

    # Verification
    assert 48 == len(r3)
    assert 4 == len(INPUT)
    assert 'a1fh' == r3[0]
    assert 'b2gi' in r3
    assert 'b3gk' in r3
