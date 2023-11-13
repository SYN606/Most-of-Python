# Addition
result_addition = 2 + 3
print(result_addition)  # Output: 5

# Subtraction
result_subtraction = 5 - 2
print(result_subtraction)  # Output: 3

# Multiplication
result_multiplication = 3 * 4
print(result_multiplication)  # Output: 12

# Division
result_division = 10 / 2
print(result_division)  # Output: 5.0

# Floor Division
result_floor_division = 10 // 3
print(result_floor_division)  # Output: 3

# Modulus
result_modulus = 11 % 2
print(result_modulus)  # Output: 1

# Exponent (Power)
result_exponent = 2 ** 3
print(result_exponent)  # Output: 8

# ------------------------------------------------------------

# assignment operators

# Assign
x = 5
print(x)  # Output: 5

# Add and Assign
x += 3
print(x)  # Output: 8

# Subtract and Assign
y = 7
y -= 2
print(y)  # Output: 5

# Multiply and Assign
z = 2
z *= 4
print(z)  # Output: 8

# Divide and Assign
w = 10
w /= 2
print(w)  # Output: 5.0

# Floor Divide and Assign
a = 9
a //= 3
print(a)  # Output: 3

# Modulus and Assign
b = 11
b %= 2
print(b)  # Output: 1

# Exponent and Assign
c = 2
c **= 3
print(c)  # Output: 8

# ------------------------------------------------------------

# Comparison operators 

# Equal
result_equal = 5 == 5
print(result_equal)  # Output: True

# Not Equal
result_not_equal = 5 != 3
print(result_not_equal)  # Output: True

# Less Than
result_less_than = 3 < 5
print(result_less_than)  # Output: True

# Greater Than
result_greater_than = 3 > 5
print(result_greater_than)  # Output: False

# Less Than or Equal To
result_less_than_equal = 3 <= 3
print(result_less_than_equal)  # Output: True

# Greater Than or Equal To
result_greater_than_equal = 5 >= 5
print(result_greater_than_equal)  # Output: True

# ------------------------------------------------------------

# Logical Operators

# Logical AND
x = True
y = False
result_and = x and y
print(result_and)  # Output: False

# Logical OR
result_or = x or y
print(result_or)   # Output: True

# Logical NOT
result_not = not x
print(result_not)  # Output: False

# ------------------------------------------------------------

# Membership Operators

# Membership - True example
fruits = ['apple', 'banana', 'orange']
result_in_true = 'banana' in fruits
print(result_in_true)  # Output: True

# Membership - False example
result_in_false = 'grape' in fruits
print(result_in_false)  # Output: False

# Not in - True example
result_not_in_true = 'grape' not in fruits
print(result_not_in_true)  # Output: True

# Not in - False example
result_not_in_false = 'banana' not in fruits
print(result_not_in_false)  # Output: False

# ------------------------------------------------------------

# Identity Operators

# is - True example
a = [1, 2, 3]
b = a
result_is_true = a is b
print(result_is_true)  # Output: True

# is - False example
c = [1, 2, 3]
result_is_false = a is c
print(result_is_false)  # Output: False

# is not - True example
result_is_not_true = a is not c
print(result_is_not_true)  # Output: True

# is not - False example
result_is_not_false = a is not b
print(result_is_not_false)  # Output: False
