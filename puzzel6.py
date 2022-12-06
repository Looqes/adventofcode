input = [line for line in open("input6").read() if line]



# Challenge1

res = next(i for i in range(len(input)) if i > 3 and len(set(input[i - 4: i])) > 3)

print(res)



# Challenge2

res = next(i for i in range(len(input)) if i > 13 and len(set(input[i - 14: i])) > 13)

print(res)