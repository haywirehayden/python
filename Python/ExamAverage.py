mathresult = int(input(" Please enter the math exam mark: ")) 
englishresult = int(input(" Please enter the english exam mark: "))
ictresult = int(input(" Please enter the ICT exam mark: "))

averagemark =(mathresult+englishresult+ictresult)/3

if averagemark >= 65:
    print("Pass")
else:
    print("Fail")

print("The average of three numbers is ", averagemark)



# Do step 4?