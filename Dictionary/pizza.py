pizza = {
    'crust': 'thick',  # Corrected to a colon (:)
    'toppings': ['mushrooms', 'extra cheese'],
}

print("you ordered a " + pizza['crust'] +
      " -crust pizza " + " WITH the following toppings:")

for topping in pizza['toppings']:
    print('\t ' + topping)
