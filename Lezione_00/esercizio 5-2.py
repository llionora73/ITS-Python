# esercizio 5-2

# Equality test
print("apple" == "apple")  # True
print("apple" == "orange")  # False

# Inequality test
print("apple" != "banana")  # True
print("apple" != "apple")  # False

# Equality test (lowercase)
print("Hello".lower() == "hello".lower())  # True
print("Hello".lower() == "HELLO".lower())  # True

# Inequality test (lowercase)
print("Hello".lower() == "world".lower())  # False

x = 10
y = 5

# Equality
print(x == y) 

# Inequality
print(x != y) 

# Greater than
print(x > y) 

# Less than
print(x < y)   

# Greater than or equal to
print(x >= y)  

# Less than or equal to
print(x <= y)  


# Test with `and`
a = 10
b = 5
if a > 0 and b < 10:
    print("Both conditions are true.")  # This will be printed.

# Test with `or`
x = 20
y = 15
if x > 25 or y < 20:
    print("At least one condition is true.")  # This will be printed because y < 20.


my_list = [1, 2, 3, 4, 5]

# Test if item is in the list
if 3 in my_list:
    print("3 is in the list.")
else:
    print("3 is not in the list.")

# Test if item is not in the list
if 6 not in my_list:
    print("6 is not in the list.")
else:
    print("6 is in the list.")