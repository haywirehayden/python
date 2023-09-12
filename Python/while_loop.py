# while loop
# Basic form
 
# var1 = 1 # Variable to test
# while <test on preset var>:
    # loop code goes here
    # change the variable

x = 1
while x < 5:
    print(x,"Hello World")
    x = x + 1   # x += 1 short form of x = x + 1 but not recommended

n = 1
while n <= 5:
    print('*' * n)
    n = n + 1
print ('*' * n)
while n > 0:
        n = n - 1
        print('*' * n)



# stopping loops on conditions

inputvar1 = int(input("Type in a number: "))
while inputvar1 > 0:
    if inputvar1 == 13:
        break   # Emergency stop the loop
    print(inputvar1)
    inputvar1 = inputvar1 - 1


# Skipping iterations on conditons

print("continue example")
inputvar1 = int(input("Type nin a number: "))
while inputvar1 > 0:
    inputvar1 = inputvar1 - 1   # this need to happen for the skip
    if inputvar1 == 13:
        continue    # Skipping a step in the loop
    print(inputvar1)
    

# While loops are useful if you dont know how many
# iterations something will take