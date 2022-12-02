points = {"A": 1, "X": 1, "B": 2, "Y":2, "C": 3, "Z": 3}

res = sum([[3, 0, 6][points[match[0]] - points[match[1]]] + points[match[1]] 
          for match in 
          [line.split(" ") for line in open('input2').read().split("\n") if line]])

print(res)