"""
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
"""

def multiply_values(number1, number2):
    product = number1 * number2
    if product <= 1000:
        return product
    else:
        return number1 * number2

result = multiply_values(20,30)
print("The result is: ", result)

def multiply_values(number1, number2):
    product = number1 * number2
    if product <= 1000:
        return product
    else:
        return number1 + number2

result = multiply_values(40,30)
print("The result is: ", result)


"""
Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
"""

print("Printing current and previous number and the sum in a range(10)")
previous_number = 0

for num in range(0,11):
    sum = previous_number + num
    print("Current number", num, "Previous number ", previous_number, "Sum: ", previous_number + num)
    previous_number = num

"""
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.
"""

#incomplete
randomword = input("Type any word")
print("Word entered is: ",randomword)

wordsize = len(randomword)
print("Printing only the even index values")



