# Lists

shoppinglist = [ "cake", "biscuits", "canned-fish", "sparling-water", "carrots", "potatoes" ]

# Python list of string objects

oddnumlist = [ 1, 5, 7, 9, 11 ] # list of integers

boolist = [True,False,False,True,True,False,True]

print(["list", "of", "things"])

print(shoppinglist)
print(oddnumlist)

for loopvar in shoppinglist: # list can be used as iterators
    print(loopvar)

print(shoppinglist[1]) # Biscuits
print(shoppinglist[-1]) # last item of the list
print(shoppinglist[2:4])


megalist = [shoppinglist, oddnumlist, boolist]

print(megalist)
print(megalist[1][2]) # return from list index 1, item index 2


#function for list length

print(len(boolist))

# strings as lists

stringvar = "Type Anything Here"

for letter in stringvar:
    print(letter)

print(len(stringvar))


print(stringvar[3])     # single letter from a string
print(stringvar[0:4])   # range of letter




#help(shoppinglist)

shoppinglist.append("plasters")
shoppinglist.append("batteries")
print(shoppinglist)

print(boolist.count(True)) # count how manu of a specific item is in the list

shoppinglist.remove("biscuits")
print(shoppinglist)

shoppinglist.insert("biscuits")
print(shoppinglist)

shoppinglist.sort()

# Converting lists to strings

joinchar = ","
shoppingliststr = joinchar.join(shoppinglist)
print(shoppingliststr)
print(type(shoppingliststr))

# Converting strings to lists

splitstr = "monitor,laptop,glass,ipad,mouse,webcam,"
newlist1 = splitstr.split(",") #split the string on the commas to a list

print(newlist1)
print(type(newlist1))