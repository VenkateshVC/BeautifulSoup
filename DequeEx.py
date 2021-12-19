#Collections -- Deque

from collections import deque

#Deque is a Double Ended Queue and it can be used to remove or add elements from both ends of the Queue

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.extend([4,5,6]) #Extend to the Right
print(d)
d.extendleft([15,14,13]) #Extend with a List of 3 elements to the LEFT
print(d)
d.rotate(2) #Will rotate n place to the right. -n will rotate to the left
print(d)
d.rotate(-1) #Rotate -N will rotate to the left
print(d)