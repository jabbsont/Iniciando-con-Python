# Los tipos de modulos que exiten

# Modulos de python preconstruidos

import datetime
# from datetime import timedelta, date

print(datetime.date.today())

print(datetime.timedelta(minutes=70))


# Modulos ue podemos crear nosotros mismos

from fmath import add, substract

add(1, 5)

substract(4, 8)

# Modulos de terceros atraves de import

from colorama import Fore, Style, init

init(convert = True)

print(Fore.RED + "Hello World")