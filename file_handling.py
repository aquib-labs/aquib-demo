import csv
with open("groceries.csv") as file:
    reader = csv.reader(file)

    for item, qty in reader:
        print(f"Buy {item} of {qty}")