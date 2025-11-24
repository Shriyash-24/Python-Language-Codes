# Frozen sets are immutable sets

fs1 = frozenset({10,20,30})
print(fs1, type(fs1)) # frozenset({10, 20, 30}) <class 'frozenset'>

# fs1.add(40) # ERROR
# remove(), discard() also not allowed.

fs2 = frozenset({10,50,100,200})
print(fs1 | fs2) # frozenset({50, 20, 100, 200, 10, 30})
print(fs1 & fs2) # frozenset({10})
print(fs1 - fs2) # frozenset({20, 30})
print(fs2 - fs1) # frozenset({200, 50, 100})