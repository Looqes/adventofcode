input = [line for line in open('input4').read().split("\n") if line]


# Challenge1

# Convert input into lists of two 2-tuples, where each tuple is an assignment
# range.
res = sum([
    # Count amount of occurences where either assignment range is a subset of
    # the other
    1 if
    (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1])
    or
    (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) 
    else 0
    for pair in
    # Convert to integers
   [[(int(first[0]), int(first[1])), (int(second[0]), int(second[1]))] for first, second in
    # Split input
   [[tuple(assignments.split("-")) for assignments in line.split(",")] for line in input]]
])

print(res)


# Challenge2

res2 = sum([
    # Count amount of occurences where either assignment range has some overlap
    # with the other
    1 if
    (pair[0][1] >= pair[1][0] and pair[0][0] <= pair[1][1])
    or
    (pair[1][1] >= pair[0][0] and pair[1][0] <= pair[0][1]) 
    else 0
    for pair in
    # Convert to integers
   [[(int(first[0]), int(first[1])), (int(second[0]), int(second[1]))] for first, second in
    # Split input
   [[tuple(assignments.split("-")) for assignments in line.split(",")] for line in input]]
])

print(res2)