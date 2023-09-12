# For loop

# Basic form

# for variable in <list_of_items>:
#   code to run


for loopvar1 in range(4): # list of numbers, 0, 1, 2, 3
    print(loopvar1)
    print("----")

for loopvar1 in range(2,7): # list of numbers, 2, 3, 4, 5, 6
    print(loopvar1)
    print("----")

for loopvar1 in range(10,0,-1): # list of numbers, 10, 9, 8, 7, 6, 5, 4, 3, 2, 
    print(loopvar1)
    print("----")

for loopvar1 in range(0,100,5): # list of numbers, 0, 5, 10...95
    print(loopvar1)
    print("----")


 # If you know how many iterations your going to do
 # you probably want a for loop.

# Break 
for loopvar1 in range(0,100,5): # list of numbers, 0, 5, 10...95
    if loopval1 = 50:
        break
    print(loopvar1)
    print("----")