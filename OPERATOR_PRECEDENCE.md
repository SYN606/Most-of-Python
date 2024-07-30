# Python Operator Precedence

In Python, operator precedence determines the order in which operations are evaluated. Operators with higher precedence are evaluated before operators with lower precedence. When operators have the same precedence, they are typically evaluated from left to right (except for exponentiation, which is evaluated from right to left).

## Operator Precedence Table

The following table lists the operators in Python from highest to lowest precedence:

| Operator Type      | Operators                                             |
|--------------------|-------------------------------------------------------|
| Parentheses        | `()`                                                  |
| Exponentiation     | `**`                                                  |
| Unary operations   | `+`, `-`, `~`                                         |
| Multiplication, Division, Floor Division, Modulus | `*`, `/`, `//`, `%`    |
| Addition, Subtraction | `+`, `-`                                           |
| Bitwise Shift      | `<<`, `>>`                                            |
| Bitwise AND        | `&`                                                   |
| Bitwise XOR        | `^`                                                   |
| Bitwise OR         | `|`                                                   |
| Comparison         | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` |
| Logical NOT        | `not`                                                 |
| Logical AND        | `and`                                                 |
| Logical OR         | `or`                                                  |
| Conditional Expression | `if ... else`                                     |
| Lambda Expression  | `lambda`                                              |

## Examples

Here are some examples to illustrate how operator precedence works in Python:

### Example 1: Basic Arithmetic Operations

```python
result = 2 + 3 * 4
print(result)  # Output: 14
