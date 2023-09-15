import csv

companies = []
sales = [] fileObject = open("carSale.csv")#with open("carSale.csv") as fileObject: #   reader_obj = csv.reader(fileObject)#    for row in reader_obj:
#        print(row)#dataSplit = open("carSale.csv")with open("carSale.csv") as fileObject:    reader_obj = csv.reader(fileObject)sales = []for line in sales:    line = line.strip().split(',')    line[0] = int(line[0])    line[1] = line[1].split(',')    sales.append(list(map(int,line)))    print(line) 
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = []

for inner_list in lists:

    for item in inner_list:

        flat_list.append(item)

print(flat_list)


companies = open("carSale.csv")newCompanies = []for x in companies:    for item in x:    newCompanies.append(item)    print(newCompanies)