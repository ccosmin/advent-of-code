import sys

fn = sys.argv[1]
with open(fn) as f:
    content = f.readlines()
    counter = 0
    for line in content:
        words = line.split()
        ints = [int(w) for w in words]
        maX = max(ints)
        miN = min(ints)
        counter = counter + (maX - miN)
    print(counter)

