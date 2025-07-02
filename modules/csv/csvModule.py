import csv
with open("people.csv","w") as csvreader:
    csvwriter=csv.writer(csvreader)
    csvwriter.writerow(["name","age"])
    for _ in range(2):
        name = input("Enter name:")
        age = int(input("Enter age:"))
        csvwriter.writerow([name,age])
with open("people.csv","r") as csvreader:
    for i in csvreader:
        print(i)
print("Data written on csv file")    