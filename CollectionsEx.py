#Collections : Counter, namedtuple, orderDict, DefaultDict, DeQueues

from collections import Counter
Str = ["AaBbCc","Math is fun! 2+2=4","This is a sentence."]

for listItem in Str:
    my_counter = Counter(listItem.lower())
    print(listItem)
    for key, value in my_counter.items():
        print("{} : {} ".format(key, value))


