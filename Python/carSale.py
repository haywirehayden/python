import csv

companies = []
sales = [] 
#        print(row)
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = []

for inner_list in lists:

    for item in inner_list:

        flat_list.append(item)

print(flat_list)


companies = open("carSale.csv")