# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}") # converts all chars to their lowercase form
print(f"Modified String 2: {user_string.upper()}") # ditto for uppercase
print(f"Modified String 3: {user_string.strip()}") # removes leading and trailing whitespace
print(f"Modified String 4: {user_string.replace('a', '@')}") # replaces all 'a' characters with '@'
print(f"Modified String 5: {user_string.capitalize()}") # make first char uppercase and the rest lowercase
print(f"Modified String 6: {user_string[::-1]}") # reverses the string
print(f"Modified String 7: {user_string.title()}") # make every first char of each word uppercase and the rest lowercase
print(f"Modified String 8: {len(user_string)}") # returns the length of the string (how many characters)
print(f"Modified String 9: {user_string.find('a')}") # returns the index of the first occurance of the character 'a' in the string
print(f"Modified String 10: {user_string.count('a')}") # returns the amount of occurances of 'a' in the string
print(f"Modified String 11: {user_string.startswith('Hello')}") # returns a Boolean that denotes whether the string begins with the substring 'Hello'
print(f"Modified String 12: {user_string.endswith('!')}") # returns a Boolean that denotes whether the string ends with the character '!'
print(f"Modified String 13: {user_string.isalnum()}") # returns a Boolean that denotes whether the string is made up completely of alphanumeric characters
print(f"Modified String 14: {user_string.isalpha()}") # returns a Boolean that denotes whether the string is made up completely of alphabetic characters
print(f"Modified String 15: {user_string.isdigit()}") # returns a Boolean that denotes whether the string is made up of only digits



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!