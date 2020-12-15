print('basic +/- "calculator" ')

while True:
    num1 = input('number 1 ')
    num2 = input('number 2 ')
 
    operation = input("+/-")
    if operation == "+":
       sum = float(num1) + float(num2)
       print(sum)
    else:
        sum = float(num1) - float(num2)
        print(sum)
    
