
# Las funciones son porciones de codigo que se pueden reutilizar

# Declaracion de funciones

#Si no se le pasa un parametro se le puede colocar uno por defecto
# el cual tomara en el caso de que no se le pase alguno al llamar a la funcion

def hello(name = "person"):
    print("Hello", name)

# Llamado de la funcion
 
hello("Jefferson")


def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10, 20))


# Funciones lambda

add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(10, 30))