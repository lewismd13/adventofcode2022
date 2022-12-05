input = open("2022\day3input.txt", "r")

priority = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0
for elvenrucks in input:
    duplicates = ''
    elvenrucks = elvenrucks.strip()
    print(len(elvenrucks))
    middle = int(len(elvenrucks)/2)
    ruck1 = elvenrucks[0:middle]
    ruck2 = elvenrucks[middle:(len(elvenrucks))]
    print(ruck1)
    print(ruck2)
    for item in ruck1:
        if item in ruck2 and item not in duplicates:
            print(item)
            print(priority.index(item))
            duplicates += item
    for dupe in duplicates:
        total += priority.index(dupe)
    print("Total score of: ", total)