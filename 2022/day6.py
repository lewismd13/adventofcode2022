input = open("2022\day6input.txt", "r")

input = input.read()

print(input)

totalchars = len(input)

i=0
stop = False
while i < (totalchars - 3) and stop == False:
    sample = input[i:i+14]
    print(sample)
    stop = True
    for character in sample:
        if sample.count(character) > 1:
            print("Duplicate character found: ", character)
            answer = i + 15
            print("%s characters processed" % answer)
            stop = False
            break

    i+=1
    
