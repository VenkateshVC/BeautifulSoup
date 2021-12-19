#Test for List Comprehensions

StudentsMarks = [98, 80, 86, 90, 94,65, 72, 81, 87, 37, 58, 23, 10, 88, 95, 97,75,35,55,]

AGrade = list(filter(lambda y: y >=90, StudentsMarks))
BGrade = list(filter(lambda y: 89>=y >75, StudentsMarks))
CGrade = list(filter(lambda y: 75>=y >55, StudentsMarks))
DGrade = list(filter(lambda y: 55>=y >35, StudentsMarks))
FGrade = list(filter(lambda y: 35>=y, StudentsMarks))

print(AGrade)
print(BGrade)
print(CGrade)
print(DGrade)
print(FGrade)