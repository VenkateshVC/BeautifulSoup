#formating using F-Strings
def square(x):
    return x*x

string_list = [1,2,3,4,5]
result = map(square,string_list)
print(list(result))