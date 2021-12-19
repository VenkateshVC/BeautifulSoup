#Dictionary Comprehensions

City_Weather = {"New York" : "Snow", "Chicago":"Wind", "Florida": "Sun", "Texas":"Sun","Arizona":"Sun","Iowa":"Snow"}

Sunny_Cities = {key:value for (key,value) in City_Weather.items() if value=="Sun"}
Snow_Cities = {key:value for (key,value) in City_Weather.items() if value=="Snow"}
Wind_Cities = {key:value for (key,value) in City_Weather.items() if value=="Wind"}

print("--- Sunny Cities in USA ---")
for keys in Sunny_Cities.keys():
    print(keys,end= " ")
print("\n")

print("--- Snowy Cities in USA ---")
for keys in Snow_Cities.keys():
    print(keys,end= " ")
print("\n")

print("--- Windy Cities in USA ---")
for keys in Wind_Cities.keys():
    print(keys,end= " ")


