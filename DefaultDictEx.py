#Collections -- DefaultDict

from collections import defaultdict

#Default Dict will use a default key value if the key has not been set
d = defaultdict(int) #Defined as an integer value. If the Key does not exist, instead of error, it will return 0
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['f'])

#NOTE: We can define the DEFAULT Value as a Float also.
