Python language is a dynamic typed language that uses indentation for block separation for example when we are defining if elif else statements, functions, classes for separation we use `:` (colon symbol) unlike other programming language, as in C language we use `{}` (curly braces)

## if statement syntax in C language
 ```
 if (condition) {
    statement
 }
```
## if statement syntax in Python 
```
if (condition):
    statement 1
    statement 2    
```
# What means the indentation in Python ?
**Python Indentation:**

In Python, indentation is a crucial aspect of the language's syntax and is used to define blocks of code. Unlike many programming languages that use braces `{}` or keywords to denote code blocks, Python relies on indentation to indicate the scope of code.

**Key points about Python indentation:**

1. **Whitespace Matters:**
   - Python uses spaces or tabs to define indentation levels.
   - Consistent indentation is essential for the interpreter to understand the structure of the code.

2. **Blocks of Code:**
   - Indentation is used to define blocks of code under control structures (if statements, loops, functions, etc.).
   - All statements within the same block must have the same level of indentation.

3. **No Curly Braces:**
   - Python does not use curly braces to delineate blocks of code.
   - The absence of braces emphasizes the importance of indentation.

4. **Readability:**
   - Code readability is enhanced by consistent and proper indentation.
   - It makes the code visually appealing and helps in quickly understanding the program's logic.

**Example:**

```python
if x > 0:
    print("x is positive")
    print("This statement is also in the 'if' block")

print("This statement is outside the 'if' block")
