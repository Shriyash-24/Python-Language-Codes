# While is always True, while condition never becomes false.
#while True:
    #print("Hello") # Infinite times' hello.

correct_password = "Python"
while True:
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("Correct!")
        break
    else:
        print("Incorrect, Try Again!")
print("Successful Login!")

num = 10
while num <= 20:
    print(num) # 10,12,14,16,18,20
    num = num + 2

num = 20
while num >= 10:
    print(num) @ 20,18,16,14,12,10
    num = num - 2




