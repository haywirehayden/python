# Maths operators

# stadard symbols

#=
#-
#/
#*

# other symbols

# ** - to the power of

# e.g

intvar1 = 5
intvar2 = 7

print(intvar1 ** intvar2)

# % - modulo

# divides one number by another
# returns only the remainder

# 10 / 5 = 2.0
# 10 / 3 = 3 1/3 - modulo returns after decimal point


print(10 % 5)
print(12 % 3)

# finding an even number

testnum = int(input("Type a number: "))
evenorodd = testnum % 2
print("evenorodd is:" , evenorodd)
if evenorodd == 0:
    print("This is an even number")
else:
    print("This is an even number")