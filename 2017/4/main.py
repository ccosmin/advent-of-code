import sys

fn = sys.argv[1]
with open(fn) as f:
    content = f.readlines()
    count = 0
    for line in content:
        words = line.split()
        s = set(words)
        if len(s) == len(words):
            count = count + 1
    print(count)
