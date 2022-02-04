print("Enter five integers:")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

sum=a+b+c+d+e
avg=sum/5
#print("The average of",a,b,c,d,  "and" ,e,"is:",avg)
#print()
# print("The average of", a, "\b,", b, "\b,", c, "\b,", d, "and", e, "is:", avg)
# f-string
print(f"The average of {a}, {b}, {c}, {d} and {e} is: {avg}")
