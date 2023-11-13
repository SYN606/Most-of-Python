# Operators in Python

An operator is an instruction for a program that guides how to execute code sequentially and generate the desired logic.

Python has the following operators:

## 1. Arithmetic Operators

These operators are used for mathematical calculations.

# Arithmetic Operators in Python

Arithmetic operators are used for mathematical calculations.

| Operator | Description                | Example                   |
| -------- | -------------------------- | ------------------------- |
| `+`      | Used in addition           | `2 + 3` → `5`             |
| `-`      | Used in subtraction        | `5 - 2` → `3`             |
| `*`      | Used to multiply           | `3 * 4` → `12`            |
| `/`      | Used to divide             | `10 / 2` → `5.0`          |
| `//`     | Used for floor division    | `10 // 3` → `3`           |
| `%`      | Used for modulus           | `11 % 2` → `1`            |
| `**`     | Used for exponent (power)  | `2 ** 3` → `8`            |

### Difference between `/` and `//`

- `/` (single forward slash) is used for normal division, returning values as floats.
  
  Example: `print(10/2)` returns `5.0` (float).

- `//` (double forward slash) is used for floor division, returning values as integers.
  
  Example: `print(10//3)` returns `3` (integer).

#### Modulus (`%`)

The modulus operator is used to calculate the remainder of a division.

Example: `print(11 % 2)` returns `1` (remainder of 11 / 2).

#### Exponent (`**`)

The exponent operator is used to calculate power.

Example: `print(3 ** 2)` returns `9` (square of 3).



## 2. Comparison Operators

Comparison operators are used for comparing two variable values (Relational operators).It is used to compare values and return Boolean results.

| Operator | Description             | Example         |
| -------- | ----------------------- | --------------- |
| `==`     | Equal                   | `5 == 5` → `True`|
| `!=`     | Not equal               | `5 != 3` → `True`|
| `<`      | Less than               | `3 < 5` → `True` |
| `>`      | Greater than            | `3 > 5` → `False`|
| `<=`     | Less than or equal to   | `3 <= 3` → `True`|
| `>=`     | Greater than or equal to| `5 >= 5` → `True`|



## 3. Assignment Operators
These operators are used to assign values to the variables. An assignment operator goes from right to left.
| Operator | Description           | Example           |
| -------- | --------------------- | ----------------- |
| `=`      | Assign                | `x = 5`           |
| `+=`     | Add and Assign        | `x += 3`          |
| `-=`     | Subtract and Assign   | `y -= 2`          |
| `*=`     | Multiply and Assign   | `z *= 4`          |
| `/=`     | Divide and Assign     | `w /= 2`          |
| `//=`    | Floor Divide and Assign| `a //= 3`        |
| `%=`     | Modulus and Assign    | `b %= 2`          |
| `**=`    | Exponent and Assign   | `c **= 3`         |


## 4. Logical Operators
Logical operators are used to combine and manipulate Boolean values.

| Operator | Description       | Example             |
| -------- | ----------------- | ------------------- |
| `and`    | Logical AND       | `x and y`           |
| `or`     | Logical OR        | `x or y`            |
| `not`    | Logical NOT       | `not x`             |


## 5. Bitwise Operators
Bitwise operators in Python are used to perform operations on individual bits of binary numbers. Bitwise operators are often used in low-level programming and can be useful in scenarios involving bit manipulation.

## 6. Membership Operators
Membership operators are used to test whether a value or variable is found in a sequence (like strings, lists, or tuples).

| Operator | Description            | Example                |
| -------- | ---------------------- | ---------------------- |
| `in`     | Returns `True` if a value is found in the sequence | `x in sequence` |
| `not in` | Returns `True` if a value is not found in the sequence | `x not in sequence` |


## 7. Identity Operators
Identity operators are used to compare the memory locations of two objects.

| Operator | Description               | Example                |
| -------- | ------------------------- | ---------------------- |
| `is`     | Returns `True` if both variables point to the same object | `x is y` |
| `is not` | Returns `True` if both variables do not point to the same object | `x is not y` |


