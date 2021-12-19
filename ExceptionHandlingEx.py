a = 5
try:
    b = a/0
    c = a + 10
    print(b)
except Exception as e:
    print(e)
else:
    print("alls well")
finally:
    print("Cleaning Up")
