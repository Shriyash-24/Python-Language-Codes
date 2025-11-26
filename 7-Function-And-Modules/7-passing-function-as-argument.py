def add_1(number):
    return number + 1

print(add_1(10)) # 11

def square(number):
    return number ** 2

print(square(4)) # 16

# Now, we take a input.. add 1 to it and then square it.

num = int(input('Enter a number: ')) # 6
res_1 = add_1(num)
res_2 = square(res_1)
print(f"Output is: {res_2}") # 49

res = square(add_1(num)) # Passing add function as a argument
print(f"Output is: {res}") # 36