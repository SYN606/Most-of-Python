"""
if else statements : these statements are used to define the conditions and then been executed on specific time when the condition is true.

SYNTAX |> CHECKOUT THE IMPORTANT.md
if <condition>:
    <statement>

"""
num = 5

if num > 0:
    print("Number is greater than 5.")

# we can use any type of values such as bool, int anything in python if conditions.
    
if True:
    print("Hello world")

# ELIF statements

value = False # here is an easter egg | try to find out it.

if value:
    print("Hello python")
elif value:
    print("Hello user")
    # and after this, we can write the else statement.
else:
    print("Nothing happened")


# Something Extra :

x = 10
# by using this type of syntax we can directly check condition in one line. This helps in code readability and in concise the expression.
result = "Even" if x % 2 == 0 else "Odd"
print(result) # output : even

# we can perform chaining comparisons :

is_valid = 10 <= x <= 20
print(is_valid) # output : True



# Use any() and all() functions for checking conditions in an iterable.
numbers = [1, 2, 3, 4, 5]
all_positive = all(x > 0 for x in numbers)

print(all_positive) # output : True