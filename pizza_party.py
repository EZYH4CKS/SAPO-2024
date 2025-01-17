N = int(input())
C = map(int, input().split())
pizza_price = 0
# YOUR CODE HERE

sortedList = list(C)
sortedList.sort(reverse=True)

i = 0
while (i < N):
    if (i % 2 == 0):
        pizza_price = pizza_price + sortedList[i]
    i = i + 1

print(pizza_price)