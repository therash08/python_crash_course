# Exercise 3-4
# guests = ['Albert Einstein', 'Isaac Newton', 'Nikola Tesla']

# print(f"Dear {guests[0]}, I would like to invite you to dinner.")
# print(f"Dear {guests[1]}, I would like to invite you to dinner.")
# print(f"Dear {guests[2]}, I would like to invite you to dinner.")

# Exercise 3-5 (3-4 এর কন্টিনিউয়েশন)


# print(f"\nUnfortunately, {guests[2]} can't make it to dinner.")

# # নতুন অতিথি অ্যাড করা (পুরানো জনকে রিপ্লেস করা)
# guests[2] = 'Marie Curie'

# # নতুন ইনভাইটেশন পাঠানো
# print(f"Dear {guests[0]}, please come to dinner.")
# print(f"Dear {guests[1]}, please come to dinner.")
# print(f"Dear {guests[2]}, please come to dinner.")


# Exercise 3-6 (3-5 এর কন্টিনিউয়েশন)

# print("\nGreat news! I found a bigger dinner table!")

# guests.insert(0, 'Stephen Hawking')


# guests.insert(2, 'Galileo Galilei')

# 3. শেষে যোগ করা
# guests.append('Charles Darwin')

# সবাইকে আবার ইনভাইট করা (লুপ ছাড়া ম্যানুয়ালি প্রিন্ট করছি যেহেতু বইয়ে লুপ পরে শেখানো হয়েছে)
# print(f"Invite sent to {guests[0]}")
# print(f"Invite sent to {guests[1]}")
# print(f"Invite sent to {guests[2]}")
# print(f"Invite sent to {guests[3]}")
# print(f"Invite sent to {guests[4]}")
# print(f"Invite sent to {guests[5]}")


# Exercise 3-8 Solution

# places = ['japan', 'iceland', 'new zealand', 'switzerland', 'brazil']

# # 1. Original order:
# print("Original list:", places)

# # 2. Alphabetical (temporary) - sorted()
# print("Alphabetical (temp):", sorted(places))

# # 3. Show list is still original
# print("Original list confirmed:", places)

# # 4. Reverse alphabetical (temporary) - sorted(reverse=True)
# print("Reverse alphabetical (temp):", sorted(places, reverse=True))

# # 5. Show list is still original
# print("Original list confirmed:", places)

# # 6. Reverse order (permanent) - reverse()
# places.reverse()
# print("Reversed order (permanent):", places)

# # 7. Reverse again (back to original) - reverse()
# places.reverse()
# print("Back to original order:", places)

# # 8. Sort (permanent) - sort()
# places.sort()
# print("Permanently sorted:", places)

# # 9. Reverse sort (permanent) - sort(reverse=True)
# places.sort(reverse=True)
# print("Permanently reverse sorted:", places)

# Exercise 3-10 Solution - Using Every List Function/Method

games = ['chess', 'ludo', 'football', 'cricket', 'carrom']
print("Initial list:", games)

# 1. append() - শেষে যোগ
games.append('badminton')
print("After append():", games)

# 2. insert() - নির্দিষ্ট স্থানে যোগ
games.insert(0, 'poker')
print("After insert():", games)

# 3. sorted() - সাময়িক সর্টিং (Temporary Sort)
print("Sorted (temp):", sorted(games))

# 4. remove() - মান দিয়ে অপসারণ
games.remove('ludo')
print("After remove('ludo'):", games)

# 5. pop() - শেষে থেকে অপসারণ এবং মান ব্যবহার
popped_game = games.pop()
print(f"Popped game was: {popped_game}")

# 6. del - ইনডেক্স দিয়ে অপসারণ
del games[1]  # এখানে 'chess' মুছে যাবে
print("After del games[1]:", games)

# 7. len()
print("List length (len()):", len(games))

# 8. sort() - স্থায়ী সর্টিং (Permanent Sort)
games.sort()
print("After sort():", games)

# 9. reverse() - ক্রম উল্টে দেওয়া
games.reverse()
print("After reverse():", games)

# Final list
print("Final list after all operations:", games)
