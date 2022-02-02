# Single line comment
# print("Hello World!")   # inline comment
"""
This is
multiline 
comment
"""
'''
This is
also multiline
comment
'''
# print('Hello Python')
# print("Alakh Pandya","987654321")
# print("Alakh Pandya"            "987654321")
"""
Escape sequence characters in Python:
\   Basic Escape Sequence Character
\n  New line character
\t  Tab character
\b  Backspace
\r  Carriage Return
end statement

Write a Python code that prints the following msgs:
1. Dhruvish says "Jinil is teasing Rutvik"
2. Dhruvish says "Jinil is teasing Rutvik but Rutvik says that Jinil didn't tease me." Now what to do?
3. The location of Python interpreter is: "C:\new folder\temp\Python:"
4. "In Python, we use '\t' to give tab. But, if you want to print '\t' then you have to type '\\t'"
"""
"""
print('Dhruvish says "Jinil is teasing Rutvik"')
print('Dhruvish says "Jinil is teasing Rutvik but Rutvik says that Jinil', "didn't",'tease me." Now what to do?')
print('The location of Python interpreter is: "C:\\new folder\\temp\\Python\\"')
print("Python\b\b\bRoyal")
print("Python\rRoyal")
print("Alakh Pandya", end=" - ")
print("987654321")
print("Alakh Pandya", end="\b\b\b")
print("987654321")
print("Alakh Pandya", end="\r")
print("987654321")
"""
# Variables in Python
"""
a = 5
print("a")
print(a)
print(type(a))
b = 10.9
print("b =", b, ";\ttype of b is: ", type(b))
c = 98374698170328974198034572349578012349870198273404624357197275345103984109572347473198573149807893219408321340987029843
print("c =", c)
print("Type of c:", type(c))
d = 9018347928436018734098712098437059871324097120349851098374598723.108329740982374198273094871509832740918273409871230984
print("Type of d:", type(d))
print("d =", d)
e = 5 + 7j
print("e =", e, "type of e:", type(e))
"""
# Taking input from user:
# print("Enter a:")
# a = input()
# b = input("Enter b: ")
# c = int(a) + float(b)
# print("a + b =", c)
# print("a + b =", int(a) + float(b))
# print(type(a))
# print(type(b))

print("Enter two numbers:")
a = int(input())        # 7
b = float(input())      # 11
print(type(a))
print(type(b))
sum = a + b
print(a, "+", b, "=", sum)               # 7 + 11.0 = 18.0
"""
Write a Python program that takes 5 integers (a, b, c, d and e) from user, finds their average and print the final output exactly as below:
Sample Execution:
Enter five integers:
3
4
5
6
7
Output:
The average of 3, 4, 5, 6 and 7 is: 5.0

not allowed:
The average of a, b, c, d and d is: 5.0
5.0
The average of 3 , 4 , 5 , 6 and 7 is: 5.0
"""