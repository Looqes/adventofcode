input = [line for line in open('input5').read().split("\n\n") if line]


# Challenge1

stacks = [list(reversed([row[i] for row in input[0].split("\n")[0:-1] if row[i] != " "])) 
          for i in range(1, len(input[0].split("\n")[0]), 4)]

moves = [(int(amount), int(orig) - 1, int(dest) - 1) for _, amount, _, orig, _, dest 
          in [(move.split(" ")) 
          for move in 
          [line for line in input[1].split("\n") if line]]]

for move in moves:
    for i in range(move[0]):
        stacks[move[2]].append(stacks[move[1]].pop())

result = [stack[-1] for stack in stacks]

for letter in result:
    print(letter, end = '')
print()


# Challenge2

stacks = [list(reversed([row[i] for row in input[0].split("\n")[0:-1] if row[i] != " "])) 
          for i in range(1, len(input[0].split("\n")[0]), 4)]

for move in moves:
    group = []

    for i in range(move[0]):
        group.append(stacks[move[1]].pop())
    
    group.reverse()

    for box in group:
        stacks[move[2]].append(box)

result = [stack[-1] for stack in stacks]

for i in range(len(result)):
    print(result[i], end = '')
print()