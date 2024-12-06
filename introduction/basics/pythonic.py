# Pythonic example #1

# A tuple is similar to a list except that it’s immutable, meaning that you cannot modify it. 
my_tuple = ("I", "am", "learning", "Python")

# Not Pythonic
# This solution certainly works, and it would be correct in a language like C.
word1 = my_tuple[0]
word2 = my_tuple[1]
word3 = my_tuple[2]
word4 = my_tuple[3]


# Pythonic
# This solution is more Pythonic because it uses tuple unpacking, which is a more Pythonic way to assign multiple variables at once.
word1, word2, word3, word4 = my_tuple

print(word1, word2, word3, word4)

# Pythonic example #2
names_non_pythonic =["jOan", "AliCE", "ChaRLY", "bob"]

# Not Pythonic
# This solution is not Pythonic because it uses a for loop to iterate over the list and title each name.
for i in range(len(names_non_pythonic)):
    # Title is a built-in function that returns a string with the first letter of each word capitalized and the rest of the letters in lowercase.
    names_non_pythonic[i] = names_non_pythonic[i].title()

# F before quotes is used to concatenate the string with the variable.
print(f"names_non_pythonic: {names_non_pythonic}")

# Pythonic
names_pythonic = ["jOan", "AliCE", "ChaRLY", "bob"]
# List comprehension is a more Pythonic way to title each name in the list.
names_pythonic = [name.title() for name in names_pythonic]
print(f"names_pythonic: {names_pythonic}")
