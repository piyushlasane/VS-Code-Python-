o=input("Choose the operation(+ - * /): ")
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
if o=='+':
    print(a, '+', b, '=', a+b)
elif o=='-':
    print(a, '-', b, '=', a-b)
elif o=='*':
    print(a, 'x', b, '=', a*b)
elif o=='/':
    print(a, '/', b, '=', a/b)
else:
    print("invalid input")