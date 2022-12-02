input = [line.split(" ") for line in open('input2').read().split("\n") if line]


# 1st part of challenge

# Dict for mapping moves to points
points = {"A": 1, "X": 1, "B": 2, "Y":2, "C": 3, "Z": 3}

# Play out the matches and determine points
res = sum([[3, 0, 6][points[match[0]] - points[match[1]]] + points[match[1]] 
          for match in input])

print(res)



# 2nd part of challenge

# Transform input to [move1, move2] for each line, instead of [move1, lose/draw/win]
# Take index of move1 and determine index of move2 in ["A", "B", "C"] according
# to required move2 (lose/draw/win)
data = [
    [match[0], ["A", "B", "C"][["A", "B", "C"].index(match[0]) + {"X": -1, "Y": 0, "Z": -2}[match[1]]]] 
    for match in input]

# Repeat calculation of first question by playing out the matches
res2 = sum([[3, 0, 6][points[match[0]] - points[match[1]]] + points[match[1]] 
          for match in data])

print(res2)