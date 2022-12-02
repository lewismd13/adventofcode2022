input = open("day2input.txt", "r")

score = 0

# A - X = Rock
# B - Y = Paper
# C - Z = Scissors
i = 0
for round in input:
    i +=1
    print('Round %s' % i)
    round_score = 0
    # 1 point for choosing rock
    if 'X' in round:
        round_score += 1
        # opponent also chose rock, 3 points for a draw
        if 'A' in round:
            print("Rock ties rock, 3 points")
            round_score += 3
        elif 'B' in round:
            print('Rock loses to paper, 0 points')
        # opponent chose scissors, 6 points for a win
        elif 'C' in round:
            print("Rock beats scissors, 6 points")
            round_score += 6
    # 2 points for choosing paper
    elif 'Y' in round:
        round_score += 2
        # opponent chose rock, 6 points for a win
        if 'A' in round:
            print("Paper beats rock, 6 points")
            round_score += 6
        # opponent chose paper, 3 points for a draw
        elif 'B' in round:
            print("Paper ties paper, 3 points")
            round_score += 3
        # opponent chose scissors, 0 points for a loss
        elif 'C' in round:
            print('Paper loses to scissors, 0 points')
    # 3 points for choosing scissors
    elif 'Z' in round:
        round_score += 3
        # opponent chose rock, 0 points for a loss
        if 'A' in round:
            print("Scissors loses to rock, 0 points")
        # opponent chose paper, 6 points for a win
        elif 'B' in round:
            print("Scissors beats paper, 6 points")
            round_score += 6
        # opponent chose scissors, 3 points for a draw
        elif 'C' in round:
            print('Scissors ties scissors, 3 points')
            round_score += 3
    print('Round Score: %s' % round_score)
    score += round_score
    print('Cumulative Score: %s' % score)
print('Final Score: %s' % score)
input.close()