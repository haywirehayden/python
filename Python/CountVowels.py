
vowelcount = input("Enter a word: ")

count = 0

i = 0

for i in range(len(vowelcount)):
    if (
        (vowelcount[i] == "a")
        or (vowelcount[i] == "e")
        or (vowelcount[i] == "i")
        or (vowelcount[i] == "o")
        or (vowelcount[i] == "u")
    ):
        count += 1

print("Number of vowels is: ", count)
