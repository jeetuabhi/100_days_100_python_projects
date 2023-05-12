operation= input('''
PLease tell me which operation to perform:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
#asking from the user about the required operation

num_1 = int(input('Please enter the first number:')) 
#taking the first integer number input from the user , if floating numbers the write float in place of int

num_2 = int(input('Please enter the second number:')) 
#taking the second integer number input from the user,if floating numbers the write float in place of int

if operation == '+':
    print('{}+{} ='.format(num_1,num_2))
    print(num_1+num_2) #using if,else if,else conditional statements for various operations

elif operation == '-':
    print('{}-{} ='.format(num_1,num_2))
    print(num_1-num_2)

elif operation == '*':
    print('{}*{} ='.format(num_1,num_2))
    print(num_1*num_2)

elif operation == '/':
    print('{}/{} ='.format(num_1,num_2))
    print(num_1/num_2)

else:
    print('wrong operation selected')
