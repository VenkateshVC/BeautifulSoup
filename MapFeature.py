#Program to test the map feature of Python

#The map function is a powerful function that executes any function on an iterable.
#Syntax is map(function, iterable).

#This program prints a list of squares defined in an external function

def squares(x):
    return x*x
#1. Print the squares of an input list unsing Map Function
intList = [3,6,8,9,11]
SquareList = []
SquareList = list(map(squares, intList))
print(SquareList)

#2. Calculate the Power of 2 lists using the MAP Function and the predefined pow function
base = [2,3,5,7]
power = [2,2,3,4]
result = list(map(pow, base,power))
print(result)

#3. Use the Lambda function feature to calculate the resulting list and using the MAP Function
result_2 = list(map((lambda base,power: 2*(base*power)),base, power))
print(result_2)