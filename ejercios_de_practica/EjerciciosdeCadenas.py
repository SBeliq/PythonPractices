# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

name = input('nombre de usuario: ')
num = int(input('un numero: '))
print((name + '\n') * num)


# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

usuario = input('nombre completo:')
print(f'{usuario.lower()} \n{usuario.upper()} \n{usuario.capitalize()}')


# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

name = input('Introduce your name: ')
print(f'{name.upper()} tiene {len(name.strip())} letras')


# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

user = input('introduce a number of telephone with code of country: ')
print(user[2:-2])


# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

user = input('introduce a letter: ')
print(user[::-1])


# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

user = input('Introduce una frase: ')
vocal = input('Intoduce una vocal: ')
print(user.replace(vocal, vocal.upper()))


# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

user = input('Introduce your email:')
print(user[:user.find('@')] + '@ceu.es')


# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

user = input('Introduce the price an object: ')
print('El producto vale $', user[:user.find('.')], 'con', user[user.find('.')+1:], 'centimos')


# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

date = input('Introduce el dia de nacimiento en este formato \ndd/mm/aaaa: ')
print('Nacimiento el dia', date[:date.find('/')], 'mes', date[date.find('/')+1:date.rfind('/')], 'año', date[date.rfind('/')+1:])


# Ejercicio 10
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

product = input('Introduce los productos a comprar, separalos con coma: ')
print(product.replace(' ', '').replace(',', '\n'))