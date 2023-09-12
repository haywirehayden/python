# Selection Examples

# Basic Form

# if <test>:
    # perform an action # this will run if the test is true, and skip if false

inputvar = int(input('Input a number that is not 7:'))

if inputvar == 7:
    print("You typed a seven even though i told you not to")
    result = inputvar2
    print("if your number was a square, it would have the area:", result)

    # == is equal to

if inputvar > 7:
    print("you typed in a big number")


if inputvar != 7:
    print("You typed a number that isn't 7")


if inputvar <= 7:
   print("You typed a number that is 7 or less")

if inputvar > 7 and inputvar < 1000:
    print("Your number is between 8 and 999")

if inputvar == 7 or (inputvar > 12 and inputvar < 20):
    print("Either 7 or in the teens")

    # using else for returning information is the test is false

if inputvar > 10:
    print("You Passed!")
else:
    print("You Failed!")

# Using elif to perform multiple sequential tests

if inputvar < 10:
    print("You have a single digit number")
elif inputvar < 100:
     print("You have a double digit number")
elif inputvar < 1000:
    print ("You have a triple digit number")
else:
    print("Your number is huge")


# Nesting IF statement

if inputvar < 1000:
    if inputvar < 100:
        if inputvar < 10:
            print("You have a single digit number")
        else:
            print("You have a double digit number")
    else:
        print("You have a triple digit number")
else:
    print("Your number is huge")

print ("end program")