scores = [2,45,102,4,9,12,45,90,1,0,1]
print(len(scores)) # 11

sum = 0
for score in scores:
    sum = sum + score
print(f"Total runs scored: {sum}") # Total runs scored: 311

# Highest Score
highest = scores[0] # Assumes that first value is highest
for score in scores:
    if highest < score:
        highest = score
print(f"Highest score is {highest}") # 102

# Lowest Score
lowest = scores[0]
for score in scores:
    if score < lowest:
        lowest = score
print(f"Lowest score is {lowest}") # 0

lowest = min(scores)
print(lowest) # 0
highest = max(scores)
print(highest) # 102





