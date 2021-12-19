
def Hello(**params):
    listval = []
    for key,value in params.items():
        listval.append(value)
        print("{} = {}".format(key,value))
    return listval

Values = Hello(Ist = "Venkatesh",IInd = "Jyothi", IIIrd = "Aditya")
Venkat, Jyo, Adu = Values

print(f"The Family Members are {Venkat} , {Jyo} and {Adu}")

#Transpose a Matrix
matrix = [[1, 2, 3], [4, 5, 6]]
print(list(zip(*matrix)))

a = "Malayalam"
print("Reverse is", a[::-1])

