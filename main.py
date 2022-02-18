import sys

inp = sys.stdin.readlines()

for x in range(0, len(inp)):
    if x == 0:
        t = inp[0]
        continue

    if x % 2 != 0: n = inp[x][0], k = inp[x][2]
    else: s = inp[x]

    def isNotEqual(s, new_s):
        if new_s != s: return True
        else: return False

    count = 0

    for i in k:
        rev_s = reversed(s).__new__(str)
        if i % 2 != 0:
            new_s = s + rev_s
            if isNotEqual(s, new_s):
                count = + 1
        else:
            new_s = rev_s + s
            if isNotEqual(s, new_s):
                count = + 1

    print(count)
