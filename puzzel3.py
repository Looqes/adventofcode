input =  [line for line in open("input3").read().split("\n") if line]


# Challenge1

# Slice each line down the middle and perform the intersection of the set
# of each line. Count scores (priorities) for each character found, where 
# a .. z : 1 .. 26 & A .. Z : 27 .. 52.
sum_of_priorities = sum([ord(c) - 96 if ord(c) > 96 else ord(c) - 38 for c in 
   [character 
    for sack in input 
    for character in 
    list(set(sack[:int(len(sack) / 2)]) & set(sack[int(len(sack) / 2):]))]
])

print(sum_of_priorities)


# Challenge2

# Split input into sublists, where each sublists contains 3 lines of input
input = [input[i : i + 3] for i in range(0, len(input), 3)]

# Take intersection of each trio and determine priority of found characters
sum_of_priorities2 = sum([ord(c) - 96 if ord(c) > 96 else ord(c) - 38 for c in 
   [character 
    for trio in input 
    for character in 
    set(trio[0]) & set(trio[1]) & set(trio[2])]
])

print(sum_of_priorities2)