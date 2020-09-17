# Nos permiten comparacion y tener un control de flujo 

# Operadores de condicion
# >   Mayor que
# <   Mneoy que
# >=  Mayor o igual que
# <=  Menor o igual que
# ==  Igual a

x = 20
y = 40

if x < 30: 
    print('x es menor que 30') # Se debe hacer la tabulacion para que pueda funcionar
elif x == 30:
    print('x es 30')
else:
    print('x es mayor que 30')

name = "Jefferson"
lastname = "Brioso"

# Condicionales anidadas, condicional dentro de otra condicion

if name == "Jefferson":
    if lastname == "Brioso":
        print("Tu eres Jefferson Brioso")
    else:
        print("Tu no eres Jefferson Brioso")
else:
    print("Tu no eres Jefferson")


# Operadores logicos
# and
# or 
# not

# Uso de operadores logicos

if x > 2 and x <= 10:
    print("x es mayor que dos y menor o igual que 10")

if x > 2 or x <= 20:
    print("x es mayor que dos o menor igual que 20")

if (not(x == y)):
    print("x no es igual a y")