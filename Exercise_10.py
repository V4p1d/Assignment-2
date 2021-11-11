# Write a function that reiceves a string and an integer between 0 and 26. The functions returns
# the string, encrypted with the Caesar encryption. 

# In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar 
# shift, is one of the simplest and most widely known encryption techniques. It is a type of 
# substitution cipher in which each letter in the plaintext is replaced by a letter some fixed 
# number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, 
# E would become B, and so on. The method is named after Julius Caesar, who used it in his 
# private correspondence.
# Write this function in a way that by default it will shift words to the right.


def caesarEncr():

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    return 

'''
IMPORTANT
You can access the individual elements of a string as if the string was a tuple (strings are also immutable).
For example:

    myString = "hello"

myString[0] would be equal to h, myString[1] would be equal to e and so on. 

This means that you can also use a string in a for loop as if it was a list:

for letter in myString:
    print(letter)

This code would output every letter in the string individually.

'''