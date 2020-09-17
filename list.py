# Se crean albergando elementos dentro de una llaves []

demo_list = [1, 'hello', 1.34, True, [1,2,3]]

colors = ['red', 'blue', 'black']

lista_numero = list((1,2,3,4))
print(type(lista_numero))

# Llena la lista con elementos en el rango que se le haya colocado
r = list(range(1, 10))
print(r)

print(dir(colors))

print(colors[2])

print('blue' in colors)

colors.append('violet')

# No se le puede pasan varios elementos por separado, debe hacerse uso de una tupla o una lista
colors.extend(('violet', 'green'))
colors.extend({'orange', 'white'})

# Inserta un elemento en la lista en la posicion que se le indique
colors.insert(len(colors), 'violet')

# Elimina el ultimo elemento de la lista y si se le pasa una posicion entonces se elimina ese indice
colors.pop()

# Remueve un elemento en especifico
colors.remove('green')

# Elimina todos los elementos de la lista
colors.clear()

# Ordena los elementos alfabeticamente
colors.sort()

# Indica el indice del elemento que se le pase
colors.index('blue')

# Indica la cantidad de veces que se repite un elemento en la lista
colors.count()