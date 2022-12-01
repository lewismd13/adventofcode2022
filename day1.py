
input = open("day1input.txt", "r")

calorie_totals = []

temp_cal = 0

i = 0

for line in input:
    print(line)
    if line != "\n":
        print(line)
        temp_cal += int(line)
        print(temp_cal)
    else:
        i+=1
        print("Elf number " + str(i) + " has " + str(temp_cal) + " calories.")
        calorie_totals.append(temp_cal)
        temp_cal = 0

i+=1
print("Elf number " + str(i) + " has " + str(temp_cal) + " calories.")
calorie_totals.append(temp_cal)
temp_cal = 0

calorie_totals.sort(reverse=True)

for elf in calorie_totals:
    print(elf)
    
top_three = calorie_totals[0] + calorie_totals[1] + calorie_totals[2]

print(top_three)



input.close()

