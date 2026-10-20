# file = open("groceries.txt", "w")
with open("groceries.csv") as file:
    # file.write("Milk, 1ltr\nEggs, 4pc\nRice, 2kg")

    for line in file:
        item, qty = line.rstrip().split(",")
        print(f"Buy {item} of {qty}")