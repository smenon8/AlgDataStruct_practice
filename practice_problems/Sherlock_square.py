import math
t = int(input())

for i in range(t):
    low,high = input().split()
    high = float(high)
    low = float(low)
    sqrt_high = math.sqrt(high)
    sqrt_low = math.sqrt(low)
    count = math.floor(sqrt_high) - math.ceil(sqrt_low) + 1           
    print(count)