# Writing your own functions


def cunctionName():
    #code bit goes here
    pass # This 'pass' keyword lets you define a function with no actual code

def showTwo(): # defines the function
    print(2)


showTwo() # This calls the function, to run it



def addTwo(inputvar):
    if inputvar.isnumber():
        print(int(inputvar) + 2)
    else:
        print("You didn't give me a number!") # Prnting in functions isnt ideal, should be kept outside of function

mynumber = input("Give me a number!: ")

addTwo(mynumber)

# Function with a return

def doubler(inputvar):
    return [inputvar, inputvar]

doubleme = input("What shall i double?!")
listofdoubledthings = doubler(doubleme)
print(listofdoubledthings)


# Importing your own functions