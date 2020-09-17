myString = "Hello world"

print("Hey, " + myString)
print(f"Hey, {myString}")
print("Hey, {0}".format(myString))

# Nos muestra que podemos hacer con el tipo de dato que se le pase

print(dir(myString))

print(myString.upper())
print(myString.lower())
print(myString.swapcase())
print(myString.capitalize())

# Si no se encuentra el string a buscar entonces no lo cambia, cuentan las mayusculas y las minusculas
print(myString.replace('Hello', 'bye'))

print(myString.count('l'))

print(myString.startswith('he'))
print(myString.endswith('world'))

# Separa la cadena de caracter en funcion de los caracteres en blanco que existan, 
# se le puede indicar apartir de que se quiere separar la cadena
print(myString.split())

# Indica la posicion en la que se encuentra el caracter colocado
print(myString.find('o'))

print(len(myString))

print(myString.index('e'))

print(myString.isnumeric())
print(myString.isalpha())