for num in range(10):
    print(num) # 0,1,2..9

# If divisible by 3 & remainder is 0 ~ skip that.

for num in range(10):
    if num % 3 == 0:
        continue
    print(num) # 1,2,4,5,7,8

# continue ~ Skips everything below it, hands control to the start of the loop.

for num in range(1,10):
    if num % 3 == 0:
        break
    print(num) # 1,2

# break - Terminates the loop. 