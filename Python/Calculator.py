def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num1, num2):
    return num1 / num2


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square")

select = input("Enter choice(1/2/3/4/5): ")

if select in ('1', '2', '3', '4', '5'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

if select == '1':
            print(num1, "+", num2, "=", add(num1, num2))

elif select == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

elif select == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

elif select == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

elif select == '5':
            print(num1, "**", num2, "=", square(num1, num2))
