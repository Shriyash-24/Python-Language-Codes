# Modules - Contains definitions and statements
# .py file is a module, module can also contain .exe code.

# Built-in modules - Available to use but needs to be imported.
# math, random, datetime...

# Importing a module ~ Syntax - import module_name

# Importing a certain function from a module ~ Syntax - from module_name import f1, f2, f3......

import math
# Calculate square root of a number.
print(math.sqrt(25)) # 5.0 ( module.function_name(arg1, arg2..)
# Calculate area of circle ==> pi r^2
radius = 5
area = math.pi * (radius ** 2)
print(area) # 78.539816..

from random import randint
# Throw a die
value = randint(1,6) # When you import full module, you have to use module_name, but if you use upper syntax.. no need to use module_name.
print(value) # random value

# Import a module and provide alias for the module that is imported: import module_name as alias_name
import datetime as dt
t = dt.time(8,43,45)
print(t) # 08:43:45


