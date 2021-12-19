#reverse a string in 1 line code

StringX = "My Name is Venkatesh"
ReverseString = StringX[::-1]
print(ReverseString)

def reverse(text):

    lst = []
    count = 1

    for i in range(0,len(text)):

        lst.append(text[len(text)-count])
        count += 1

    lst = ''.join(lst)
    return lst

print(reverse("HELLO WORLD VENKATESH"))