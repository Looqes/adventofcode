input = [[int(digit) for digit in line] for line in open("input8").read().split("\n") if line]
# input = [[int(digit) for digit in line] for line in open("test8").read().split("\n") if line]


# Challenge1

res = 0

for y in range(1, len(input[1]) - 1):
    for x in range(1, len(input) - 1):
        if (
            input[y][x] > max([row[x] for row in input[:y]]) or
            input[y][x] > max([tree for tree in input[y][x + 1:]]) or
            input[y][x] > max([row[x] for row in input[y + 1:]]) or
            input[y][x] > max([tree for tree in input[y][:x]])
        ):
            res += 1

print(res + (2 * len(input) + 2 * len(input[0]) - 4))

        
# Challenge2

def get_score(trees, spot):
    score = 0

    for tree in trees:
        score += 1

        if tree >= spot:
            return score
    
    return score


result = max([(
    get_score(list(reversed([row[x] for row in input[:y]])), input[y][x]) *
    get_score([tree for tree in input[y][x + 1:]], input[y][x]) *
    get_score([row[x] for row in input[y + 1:]], input[y][x]) * 
    get_score(list(reversed([tree for tree in input[y][:x]])), input[y][x])
    )
    for y in range(1, len(input[1]) - 1)
    for x in range(1, len(input) - 1)
])

print(result)


