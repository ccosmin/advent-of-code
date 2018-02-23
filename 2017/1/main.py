import sys

fn = sys.argv[1]
with open(fn) as f:
    line = f.readline()
    digits = [int(d) for d in line]
    count = 0
    for i in range(0, len(digits)):
        n = digits[i + 1] if i < len(digits) - 1 else digits[0]
        if digits[i] == n:
            count = count + n
    print(count)

