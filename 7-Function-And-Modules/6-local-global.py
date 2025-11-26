n = 1 # Global variable ~ Acessing inside or outside the function
def fn():
    global n # Keyword to change the global variable inside the function
    n = 5 # Local variable
    print('IN', n)

fn()
print('OUT', n)
# Local variable is given more priority.