# alien_1 = {'colour': 'green', 'points': 7}
# alien_2 = {'colour': 'blue', 'points': 17}
# alien_3 = {'colour': 'red', 'points': 10}

# aliens = [alien_1, alien_2, alien_3]
# for alien in aliens:
#     print(alien)


# from Dictionary import alien
# aliens = []

# for alien_number in range(30):
#     new_alien = {'colour': 'blue', 'points': 9, 'speed': 'fast'}
#     aliens.append(new_alien)

#     for alien in aliens:
#         print(alien)
#     print(" ")

# print("total number of aliens: " + str(len(aliens)))


aliens = []

for alien_number in range(0, 30):
    new_alien = {'colour': 'blue', 'points': 9, 'speed': 'fast'}
    aliens.append(new_alien)

for alien in aliens:
    if alien['colour'] == 'green':
        alien['colour'] = 'blue'
        alien['colour'] = 'red'
        alien['points'] = 10

for alien in aliens:
    print(alien)
print(" ")
