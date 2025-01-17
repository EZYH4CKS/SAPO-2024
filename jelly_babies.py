N = int(input())
s = list(map(int, input().split()))
x = [list(map(int, input().split())) for _ in range(N)]
n_jelly_tots = 0
# YOUR CODE HERE

inf = False
sBefore = list()
while (max(s) != 0) and (inf == False):
    if (not sBefore.__contains__(s)):
        sBefore.append(s)
    for i in range(0, len(s)):
        result = []
        for j in range(0, len(x[i])):
            result.append(s[i]*x[i][j])
        n_jelly_tots = n_jelly_tots + result[len(result)-1]
        s[i] = 0
        for j in range(0, len(s)):
            s[j] = s[j] + result[j]
    if ((sBefore.__contains__(s)) and (max(s) != 0)):
        print(sBefore)
        print(s)
        inf = True
        n_jelly_tots = 0

print(n_jelly_tots)
