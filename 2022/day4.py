rawinput = open("2022\day4input.txt", "r")

input = list(rawinput)

score1 = 0
score2 = 0

for pair in input:
    pair = pair.strip()
    pair = pair.split(",")
    print(pair)
    elf1 = pair[0].split('-')
    elf1 = list(map(int, elf1))
    print(elf1)
    elf2 = pair[1].split('-')
    elf2 = list(map(int, elf2))
    print(elf2)
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
        print("Ding!")
        score1+=1
    elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
        print("Ding!")
        score1+=1
    if elf1[0] >= elf2[0] and elf1[0] <= elf2[1]:
        print("Ding!")
        score2+=1
    elif elf2[0] >= elf1[0] and elf2[0] <= elf1[1]:
        print("Ding!")
        score2+=1
print("There were %s pairs that met part 1 criteria" % score1)
print("There were %s pairs that met part 2 criteria" % score2)