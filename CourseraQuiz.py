
def highlight_word(sentence, word):
    new_sentence = ""
    index = sentence.find(word)
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
    new_sentence = sentence[:index] + word.upper() + sentence[index+len(word):]
    return new_sentence


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "don't"))
print(highlight_word("Automating with Python is fun", "Python"))