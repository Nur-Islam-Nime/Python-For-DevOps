# *******************************************
    # Python Strings
# *******************************************

    # quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello World"
print(a[2])
print(a[-1])
 # The len() function returns the length of a string:
print(len(a))  

    # Check String : If a certain phrase or character is present in a string, we can use the keyword in.

msz = "I am learning python for DevOps"
print("am" in msz)      # It just return true or false

    # Check if NOT : If a certain phrase or character is NOT present in a string, we can use the keyword not in.

print("love" not in msz)


# *******************************************
    # Python Slicing Strings
# *******************************************

# Slicing : Specify the start index and the end index, separated by a colon, to return a part of the string.

b = " Hello World "
print(b[2:5])
print(b[:5])    # Slice From the Start : The range will start at the first character.
print(b[2:])    # Slice To the End : Start from position 2 and the range will go to the end.
print(b[-5:-2]) # string[start:stop] Wor 


# *******************************************
    # Python Modify Strings
# *******************************************

# Upper Case : The upper() method returns the string in upper case.

print(b.upper()) 
print(b.lower())
print(b.split())    # The strip() method removes any whitespace from the beginning or the end.
print(b.replace("H", "J"))  # The replace() method replaces a string with another string.


# *******************************************
    # Python Strings Concatenation
# *******************************************

f_name = "Nur Islam"
l_name = "Nime"
full_name = f_name + " " + l_name
print(full_name)

# *******************************************
    # Python Format Strings 
# *******************************************

age = 27 
# f-strings or the format() method!
txt = f"My name is {l_name}, I am {age}"
print(txt)


# *******************************************
    # Python Escape Characters
# *******************************************

test = "I love to \"learn\" tech thing."    # \" \" use to Escape

print(test)