"""
Loops : Loop statements are used to iterate (repeat) until the condition isn't false. In python there are 2 types of loops :-
1. while loops
2. for loops

WHILE LOOPS :
            while loops are simple yet they are powerful. it can iterate primitive and sequential data types both but in most cases while loops are preferred to use with primitive data types.
FOR LOOPS :
            for loops are quite a bit tricky yet also they are powerful. A for loops is best for iteration of sequential datatypes, also we can use range() function to iterate the primitive data types.

|> Check out : DATATYPES.md
"""

num = 5

while num >= 0:
    print("hello i am while loop")
    num -= 1 # this is similar to num = num - 1. also if we dont increment or decrement as per need the loop will stuck in an infinite loop.

num = 5 # again assigning the value for for loop.

# for loops are quite tricky.

"""
Syntax of for loop :

for <temp_var> in <sequential_datatype>:
    statement


the range function is used is to enumerate the number in a sequence from 0 to n-1 where the n is given argument in the function.
Syntax of range() Function :

range(start_value,stop_value,step_value)
if we give only one argument to range it acts as stop value the default start value is 0.
if we give 2 arguments first one is start value and second one is stop value.

"""

number = 10

for i in range(number):
    print(i)