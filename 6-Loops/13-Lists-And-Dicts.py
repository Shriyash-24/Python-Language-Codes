"""
We have the following dictionary:
user = {
    "user_name": "my_user",
    "password": "test@123",
    "email": "my_user@example.com",
    "address": "ABC road, 111111",
    "country": "Australia"
}
Delete the sensitive information from the dictionary present in a list
sensitive_info = ["password", "address"]
"""

user = {
    "user_name": "my_user",
    "password": "test@123",
    "email": "my_user@example.com",
    "address": "ABC road, 111111",
    "country": "Australia"
}
sensitive_info = ["password", "address", "phone"]

# for key in user:
#     if key in sensitive_info:
#         user.pop(key)
# print(user)
# Not possible to change the dictionary's length ~ Gives runtime error.

for i in sensitive_info:
    # print(f"Key: {i}, Value: {user[i]}")
    if i in user:
        user.pop(i) # {'user_name': 'my_user', 'email': 'my_user@example.com', 'country': 'Australia'}
    else:
        print(f"{i} is not present.") # phone is not present.
print(user) # {'user_name': 'my_user', 'email': 'my_user@example.com', 'country': 'Australia'}

