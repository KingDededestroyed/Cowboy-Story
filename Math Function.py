def math_fun(x,y):
    if x.isdigit() and y.isdigit():
        num1 = int(x)
        num2 = int(y)
        numSum = num1 * num2
    else:
        return "Please enter valid digits."
    return numSum,num1,num2

x = input("Enter a number: ")
y = input("Enter a number: ")
answer,num1,num2 = math_fun(x,y)
print(num1)
print(num2)
print(answer)
