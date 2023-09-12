num = int(input("Enter an integer: ")) 

factor = 1

while num > 0:
    factor = num * factor
    num = num - 1
    print("factorial of ", num, " is ", factor)
 

