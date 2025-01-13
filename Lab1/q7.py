text = "Hello, welcome to the world of python programming!"
length_of_string = len(text)
print(f"Length of the string: {length_of_string}")


uppercase_string = text.upper()
print(f"Uppercase updated string is: {uppercase_string}")


lowercase_string = text.lower()
print(f"Lowercase updated string is: {lowercase_string}")


substring = "Python"
is_substring_present = substring in text
print(f"Is'{substring}'present in the string?{is_substring_present} ")


words_list = text.split()
print(f"List of Words: {words_list}")
