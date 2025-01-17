E, M, F, R = map(int, input().split())
e, m, f = map(int, input().split())
n_cakes_baked = 0
# YOUR CODE HERE
import math

nums = []
diff = []

nums.append(math.floor(E/e))
nums.append(math.floor(M/m))
nums.append(math.floor(F/f))

n_cakes_baked = min(nums)

diff.append(E-(e*n_cakes_baked))
diff.append(M-(m*n_cakes_baked))
diff.append(F-(f*n_cakes_baked))

min_buy = (3*(e-diff[0])) + (20*(m-diff[1])) + (15*(f-diff[2]))
n_cakes_baked += math.floor(R/min_buy)

print(n_cakes_baked)