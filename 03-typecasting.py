# +----------------------+-------------------------------------------+---------------------------------------------------+
# | **Function**         | **Description**                           | **Example**                                       |
# +----------------------+-------------------------------------------+---------------------------------------------------+
# | `int(x)`             | Converts `x` to an integer.               | `int(3.14)` → `3`                                 |
# | `float(x)`           | Converts `x` to a floating-point number.  | `float(5)` → `5.0`                                |
# | `str(x)`             | Converts `x` to a string.                 | `str(42)` → `'42'`                                |
# | `list(x)`            | Converts `x` to a list.                   | `list("hello")` → `['h', 'e', 'l', 'l', 'o']`     |
# | `tuple(x)`           | Converts `x` to a tuple.                  | `tuple([1, 2, 3])` → `(1, 2, 3)`                  |
# | `set(x)`             | Converts `x` to a set.                    | `set([1, 2, 2, 3])` → `{1, 2, 3}`                 |
# | `dict(x)`            | Converts `x` to a dictionary.             | `dict([('a', 1), ('b', 2)])` → `{'a': 1, 'b': 2}` |
# | `bool(x)`            | Converts `x` to a Boolean value.          | `bool(42)` → `True`                               |
# | `chr(x)`             | Converts an integer to a character.       | `chr(65)` → `'A'`                                 |
# | `ord(x)`             | Converts a character to its Unicode code. | `ord('A')` → `65`                                 |
# +----------------------+------------------------------------------+----------------------------------------------------+


""" explicit type-casting & implicit type-casting 

When a user does typecasting in a program it is known as explicit typecasting.On the other hand when python typecasts a variable value from one data type to another to prevent data lose it is known as implicit typecasting.

"""
# Ex :-
# num = input("Enter a num : ")
# print(type(num))
# num = int(num)
# print(type(num))

num_1 = 40
num_2 = input("Enter a number : ")
# By default whenever python takes input by a user its default data type is string, we can use type() function for checking the data type of a variabel.
print(type(num_2))
num_3 = 2

div_1 = num_1 / num_3
print(type(div_1)) # Implicit Typecasting
print(div_1)

num_2 = int(num_2) # Explicit Typecasting
div_2 = num_1 / num_2
print(type(div_2), div_2) # Implicit Typecasting
