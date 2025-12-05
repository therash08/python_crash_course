# age = (int(input("enter a number:  ")))

# if age < 4:
#     print("your admission cost is free")
# elif 4 <= age <= 18:
#     print("your admission cost is 5$")
# else:
#     print("your cost is 10$")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10


print("your admission cost is $" + str(price) + ".")
