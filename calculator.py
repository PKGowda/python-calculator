choice=int(input('Enter your Choice (1-Addition,2-Subtraction,3-Multiplication,4-Division)'))
a=int(input('Enter your first number'))
b=int(input('Enter your second number'))
if choice==1:
    print('Addition=',a+b)
elif choice==2:
    print('Subtraction=',a-b)
elif choice==3:
    print('Multiplication=',a*b)
elif choice==4:
    print('Division=',a/b)
else:
    print('Invalid Choice')
