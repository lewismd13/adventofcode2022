rawinput = open("2022\day3input.txt", "r")

priority = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0

input = list(rawinput)
i = 0
while (i<300):
    group = input[i:i+3]
    print(group)
    print(i/3)
    for item in group[0]:
        if item in group[1] and item in group[2]:
            print('Match!', item)
            print('Priority', priority.index(item))
            total+=priority.index(item)
            break
    i+=3
print('Total: ', total)