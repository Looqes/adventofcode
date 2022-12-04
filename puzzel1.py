
# Challenge 1
res = sum(sorted([sum([int(string) for string in x.split("\n")]) for x in open('input').read().split("\n\n") if x], reverse = True)[0:3])

print(res)




