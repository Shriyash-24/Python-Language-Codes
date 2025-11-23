days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days_of_week) # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# reverse() - Reversing the elements of the list
days_of_week.reverse()
print(days_of_week) # ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']

nums  = [9,6,4,2,1,0]
nums.reverse()
print(nums) # [0, 1, 2, 4, 6, 9]

# sort()
nums  = [9,6,4,2,1,0]
nums.sort()
print("Sorted List:",nums) # Sorted List: [0, 1, 2, 4, 6, 9]
nums  = [9,6,4,2,1,0]
nums.sort(reverse=True)
print("Sorted List:",nums) # Sorted List: [9, 6, 4, 2, 1, 0]

# count()
numbers = [0,1,3,4,1,0,5,0,0,3,0]
print(f"The list is: {numbers}")
item_to_count = int(input("Enter item to count: ")) # 5
c = numbers.count(item_to_count)
print(f"Occurrence Of {item_to_count} is {c}") # Occurrence Of 5 is 1

# Membership operator
lang = ["Python", "Java", "C++", "Python"]
print("Python" in lang) # T
print("JavaScript" in lang) # F
print("Python" not in lang) # F
print("JavaScript" not in lang) # T



