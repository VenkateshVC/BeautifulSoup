def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed
  # only once, and the value from guests1 taking precedence
  combined_guests = {}
  for key1, val1 in guests1.items():
    combined_guests[key1] = val1

  for key2, val2 in guests2.items():
    if key2 not in combined_guests:
      combined_guests[key2] = val2

  return combined_guests

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))