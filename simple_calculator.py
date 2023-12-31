def addition(num1,num2):
    return num1 + num2;

def subtraction(num1,num2):
    return num1 - num2;

def multiplication(num1,num2):
    return num1 * num2;

def division(num1,num2):
    if (num2 == 0):
        print("Error! Division by zero is not allowed.");
    else:
        return num1 / num2;

def modulo(num1,num2):
    if (num2 == 0):
        print("Error! Cannot find the remainder of a number divided by zero.")
    else:
        return num1 % num2;
print("Please! Enter any Two numbers:")    
print("Enter first No.:")
num1 = int(input())
print("Enter second No.:")
num2 = int(input())
print("->For Addition Operation enter:'+'\n->For Subtraction Operation enter:'-'\n->For Multiplication Operation enter:'*'\n->For Division Operation enter:'/'\n->For Modulo Operation enter:'%'")
oper = input()
if oper=='+':
    print("Result :",addition(num1,num2))
elif oper=='-':
    print("Result :",subtraction(num1,num2))
elif oper=='*':
    print("Result :",multiplication(num1,num2))
elif oper=='/':
    print("Result :",division(num1,num2))
elif oper=='%':
    print("Result :",modulo(num1,num2))
