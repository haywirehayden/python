# An intorductions into Python

print("Hello World")

# 0101110111
# Binary representation of 4312858897
# Could be a telephone number
# Could be a decimal value of money
# Could be an ip address

# Data typing
# - Integer , any whole number e.g 1, -15 or 101,110,111
# - Floating, any fractional number e.g 1.0, -15.5, 101.110111
# - string, alphanumeric text e.g.'cat' 'Dinosaur2055', '01 110 1111'
# - Boolean, true ot fale value e.g 'True', 'False'

varname = 'value'

integervar = 123        # Integer
floatvar = 123.456      # Float
stringvar = "text here" # String
boolvar = True          # Boolean, no quotes, capitalized words

print (integervar)
print (floatvar)
print (stringvar)
print (boolvar)

myVar1 = "Intro to Python" # start vars with a lower case letter

print(myVar1)

# Input

input() # This will pause the program so you can type in text

inputString = input ("Please Type in a word: ")

print(inputString) # print the contents of the var

# Variable Manipulation

textVar1 = input('Type in your name')
textVar2 = input ('Type in an animal')

print (textVar1 + textVar2)

print (textVar1 + " typed in the animal" + textVar2)

# Numbers

numVar1 = 15
numVar2 = 12
print(numVar1 + numVar2)

# Example 2


#awesomenessVar1 = input('Type your awesomeness level: ')
#print(30 + awesomenessVar1) # unable to add sting and integer
#print(30 + int(awesomenessVar1) # correct process


# Casting

integervar = 123        
floatvar = 123.456      
stringvar = "20" 
boolvar = True 

stringVar = "20"
print (10 + int(stringVar))


# Commas in the print statement

print("string", 30, "another string") # comma convert everything
print("string" + str(30 + "another string")) # but also add spaces


# Casting to float

 floatvar2 = 1.23
 floatvar3 = 1.99 # this does not round up

 print(int(floatvar2))
 print(int(floatvar3))


 # casting to boolean

 integervar1 = 123
 integervar2 = 0
 floatvar1 = 123.45
 floatvar2 = 0
 stringvar1 = "20"
 stringvar2 = ""
 print(bool (integervar1)) #True
 print(bool (integervar2)) #False
 print(bool (floatvar1))   #True
 print(bool (floatvar2))   #False
 print(bool (stringvar1))  #True
 print(bool (stringvar2))  #False