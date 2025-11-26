# LAMBDA

def add(a):
    return a + 1
res = add(1)
print(res) # 2

# Syntax - lambda argument : expression
fun = lambda a : a+1
res = fun(2)
print(res) # 3

## Passing 2 arguments
fu = lambda a,b : a + b
res = fu(2,3)
print(res) # 5