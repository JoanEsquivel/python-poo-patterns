# Pythonic example #1

# A tuple is similar to a list except that it’s immutable, meaning that you cannot modify it. 
my_tuple = ('I', 'am', 'learning', 'Python')

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
