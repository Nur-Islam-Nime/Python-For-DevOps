
# **********************************************
    # Python Lists
# **********************************************

# List items are ordered, changeable, and allow duplicate values.
# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets: []
# List items can be of any data type: String, int and boolean data types
fruits = ["apple","banana","mango","Banana", "orange" ]
print(fruits)
print(len(fruits))

# **********************************************
    # Python Access List Items
# **********************************************

print(fruits[1])
print(fruits[-1])   # Negative indexing means start from the end
print(fruits[1:4])  # Return the second, third, and fourth item
if "apple" in fruits:
    print("Yes,'Apple' is in the list")


# **********************************************
    # Python Change List Items
# **********************************************

fruits[2] = "blackcurrent"
print(fruits)
fruits[1:3] = ["cherry", "orange"]
print(fruits)
fruits.insert(2, "watermelon")  # The insert() method inserts an item at the specified index:without replacing any of the existing values
print(fruits)

# **********************************************
    # Python Add List Items
# **********************************************

fruits.append("lemon")  # Using the append() method to append an item: END
print(fruits)
    # Extend List: To append elements from another list to the current list, use the extend() method.
tropical = ["pineapple","papaya"]
fruits.extend(tropical)
print(fruits)

# **********************************************
    # Python Remove List Items
# **********************************************

    # Remove Specified Item : remove()
fruits.remove("Banana")     # case sensitive 
print(fruits)

    # Remove Specified Index : pop()
fruits.pop(1)   # Remove the second item: 
print(fruits)

    # Remove Specified Index : del
    # The del keyword can also delete the list completely.
    # The clear() method empties the list.
del fruits[0]
print(fruits)

# **********************************************
    # Python Sort Lists
# **********************************************

fruits.sort()   # Sort List Alphanumerically
print(fruits)

thislist = [100, 50, 65, 82, 23]
thislist.sort()     # Sort the list numerically
print(thislist)

fruits.sort(reverse=True)   # Sort Descending : the keyword argument reverse = True:
print(fruits)

thislist.reverse()
print(thislist)


# **********************************************
    # Python Copy Lists
# **********************************************

    # built-in List method copy() to copy a list.
newlist = thislist.copy
print(newlist)
    # copy is to use the built-in method list().
newlist = list(thislist)
print(newlist)


"""
List Methods
Python has a set of built-in methods that you can use on lists.

Method	        Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list

"""