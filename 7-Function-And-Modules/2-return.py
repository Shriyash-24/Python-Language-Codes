def even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd(10) # Even

# Is upper function returning anything? - Are we getting any value from this function.
# How to check if function returns something or not.
result = even_or_odd(10) # Even
print(result) # None

# If function doesn't return anything, it returns None and that gets stored in result.

# Instead of printing even or odd... if we want value even or odd outside the function.

def odd_or_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = odd_or_even(77)
print(result) # Odd

def add(num1,num2):
    result = num1 + num2
    return result

val_1 = int(input("Please enter a number: "))
val_2 = int(input("Please enter a number: "))
result = add(val_1,val_2)
print(result) # 11 ( val_1 = 5, val_2 = 6 )

def arithmetic(num1,num2):
    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    return add, sub, mult

res1, res2, res3 = arithmetic(10,20)
print(res1) # 30
print(res2) # -10
print(res3) # 200




