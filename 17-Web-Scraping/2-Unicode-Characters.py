# ASCII VS UNICODE
# ASCII supports 128 characters (now 256), Unicode supports wide range of characters.
# ASCII uses 8 bits to represent character, Unicode Uses 8-bit, 16 bit or 32 bit.
# ASCII uses less space, UNICODE recieves more space.
# American Standard Code For Information Interchange, Universal Character Set.

# ASCII
# A-Z - 65-90
# a-z - 97-122
# 0-9 - 48-57
# Special - 0-47, 58-64, 91-96, 123-127
# \t - 9
# \n - 10
# ord() gives ASCII character.
print(ord('e')) # 101
print(ord('A')) # 65

# UTL-16 - 2 bytes (fixed size)
# UTF-32 - 4 bytes (fixed size)
# UTF-8 - 1-4 bytes, more language support
