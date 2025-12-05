# 5.3

# alien_colour = "red"

# if alien_colour == "green":
#     print("you just earned 5 points for shooting the alien!")
# else:
#     print("you just earned 10 points")

# another example
# alien_color = 'red'  # Change to 'green', 'yellow', or 'red'

# if alien_color == 'blue':
#     print("You earned 5 points!")
# elif alien_color == 'yellow':
#     print("You earned 10 points!")
# else:
# #     print("You earned 15 points!")

# # another example
# age = 15

# if age < 2:
#     print("You're a baby!")
# elif age < 4:
#     print("You're a toddler!")
# elif age < 13:
#     print("You're a kid!")
# elif age < 20:
#     print("You're a teenager!")
# elif age < 65:
#     print("You're an adult!")
# else:
#     print("You're an elder!")

usernames = ['eric', 'willie', 'admin', 'erin', 'ever']

# 5-9: Check if the list is empty first
# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print("Hello admin, would you like to see a status report?")
#         else:
#             print(f"Hello {username.title()}, thank you for logging in again!")
# else:
#     print("We need to find some users!")

# To test the empty condition, remove items from the list: usernames = []

# current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
# new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

# # current_users এর সব নাম ছোট হাতের অক্ষরে কনভার্ট করে একটি কপি তৈরি করি
# # এটি করার কারণ হলো case-insensitive comparison করা
# current_users_lower = [user.lower() for user in current_users]

# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print(
#             f"Sorry, {new_user} is already taken. Please enter a new username.")
#     else:
#         print(f"Great, {new_user} is available!")

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
