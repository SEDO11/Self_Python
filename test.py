import sys

t = int(sys.stdin.readline().strip())
cnt = 0
for i in range(t):
    l = []
    n = sys.stdin.readline().strip()
    for j in range(len(n)):
        if (n[j] not in l) or n[j] == n[j-1]:
            l.append(n[j])
        else:
            break
    if len(n) == len(l):
        cnt += 1
print(cnt)