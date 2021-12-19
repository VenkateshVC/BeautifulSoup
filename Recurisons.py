def is_palindrome(input_string):
  new_string = ""
  reverse_string = ""
  input_string = input_string.upper()
  for x in range(0,len(input_string)):
    ReadChar = input_string[x].strip()
    if ReadChar != "":
      new_string += ReadChar
      reverse_string += ReadChar

  print(new_string,reverse_string)
  if new_string == reverse_string:
    return True

  return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True