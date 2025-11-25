countries = ["India","United Kingdom","United States", "Ireland", "Iran", "Poland"]

# Count all the countries which are starting with 'I'

count = 0
for country in countries:
    if country[0] == 'I':
        count = count + 1
print(count) # 3

# Another way.
count = 0
for country in countries:
    if country.startswith('I'):
        count = count + 1
print(count) # 3

# List all these countries as a list that start with 'I'
output = []
for country in countries:
    if country.startswith('I'):
        output.append(country)
print(output) # ['India', 'Ireland', 'Iran']



