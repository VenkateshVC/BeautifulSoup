def pig_latin(text):
	say = ""
	# Separate the text into words
	words = text.split()
	piglatinList = []
	for index, word in enumerate(words):
		# Create the pig latin word and add it to the list
		pigword = word[1:len(word)]+word[0]+"ay"
		piglatinList.append(pigword)
	# Turn the list back into a phrase
	return piglatinList


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"



