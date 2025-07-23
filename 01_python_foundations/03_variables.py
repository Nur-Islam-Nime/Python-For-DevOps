
# **********************************
# Python Variables - DevOps preparation Notes
# **********************************

    # Rule 1: Use snake_case for variable names
first_name = "Nur Islam"
last_name = "Nime"

    # CamelCase is not preferred in python

    #userName = "Nime"   


    # Rule 2: Must start with Letter or underscore
name = "Ansible"    # Good practice 
_language = "Bash"  # Good practice

    #   1name = "Wrong"     # Wrong Coz start with number

    # Rule 3: No spaces or special characters

    # &data = 100   # Wrong Coz start with special characters

    # Rule 4: Avoid reserved keywords
    # class = 'abc'     # Wrong Coz Class keyword reserved in python

    #f-string (modern and recommended)
print(f'My name is {last_name}')

print("Hello", first_name )


    # Casting : Specify the data type of a variable, this can be done with casting.

x = str(5)    # x will be '5'
y = int(6)    # y will be 6
z = float(8.5)  # z will be 8.5

    # Get the Type : Data type of a variable with the type() function.

x = 10
y = "Nime"
print(type(x))
print(type(y))


    # Many Values to Multiple Variables : Python allows assign values to multiple variables in one line:
    # Number of variables matches the number of values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

    # One Value to Multiple Variables 
    # The same value to multiple variables in one line:

""" 
x = y = z = "Orange"
print(x)
print(y)
print(z)

"""

