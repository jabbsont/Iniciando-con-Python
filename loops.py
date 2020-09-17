foods = ['apples', 'bread', 'cheese', 'milk', 'graves', 'bananas']

for food in foods:
    if food == "cheese":
        print("Debes comprar esto")
        break  # rompe el ciclo y se detiene
    print(food)

for food in foods:
    if food == "cheese":
        print("Debes comprar esto")
        continue # continua a partir de donde se cumpla la condicion
    print(food)


for number in range(1, 8):
    print(number)

for letter in "Hello":
    print(letter)


count = 4

while count <= 10:
    print(count)
    count = count + 1