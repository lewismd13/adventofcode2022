input = open("2021\day1input2021.txt", "r")

answer = 0

inputlist = []
for depth in input:
    inputlist.append(int(depth))
    # print(depth)

values = range(len(inputlist))

prior = 0
current = 0


for i in values:
    print(i)
    if i > 3 or i < len(inputlist) - 3:
        prior = inputlist[i-1] + inputlist[i-2] + inputlist[i-3]
        current = inputlist[i] + inputlist[i-1] + inputlist[i-2]
        print("Prior: %s" % prior)
        print("Current: %s" % current)
        if current > prior:
            answer += 1
            print('Bingo, that is %s increases so far' % answer)
        else:
            print('ope, that one went down')