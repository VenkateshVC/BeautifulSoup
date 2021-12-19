import re as regExp
#Import Regular Expressions Library

strX = "My Favorite Numbers Are 7, 11, 13, 19 And 23"

lstNum = regExp.findall('[0-9]+', strX)
lstChar = regExp.findall('[A-Z]+',strX)
outChar = regExp.search("ori",strX)
print(outChar)
print(lstNum)
print(lstChar)