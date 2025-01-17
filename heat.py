A = int(input())
x1, x2, x3 = map(int, input().split())
sus = ""
# YOUR CODE HERE

if ((A-x1) > 10) or ((A-x2) > 10) or ((A-x3) > 10):
    sus = 'Low'
else:
    sus = 'Ok'

print(sus)
