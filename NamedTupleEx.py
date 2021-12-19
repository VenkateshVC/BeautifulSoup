#Collections : Counter, namedtuple, orderDict, DefaultDict, DeQueues
#namedtuple is similar to a Struct

from collections import namedtuple
Point = namedtuple('Point','x,y') #x, y are the variables of object Point
pt = Point(1,-4)
print(pt)
print(pt.x,pt.y)


