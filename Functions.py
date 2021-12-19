def PowerFunction(Base,Power):
    Result = 1
    for x in range(1, Power+1):
        Result *= Base
    return Result

print(PowerFunction(7,4))