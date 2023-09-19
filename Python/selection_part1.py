
age = int(input('Input a number:'))

#if age >= 18:
#    print("You are in category A")

#if age >= 16 or (age <=17):
#    print("You are in category B")

#if age < 16:
#    print("You are in category C")


if age >= 18:
    print("You are in category A")
elif age >= 16 or (age <=17):
    print("You are in category B")
else:
    print("You are in category C")