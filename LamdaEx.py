#lamda Functions are Precise Functions that take values and return results
#It is used only in instances where it is used once
from functools import reduce

a = [1,2,3,4,5,6,7,8,9,10]
print(a)
reduce_A = reduce(lambda x,y: x+y, a)
print(reduce_A)