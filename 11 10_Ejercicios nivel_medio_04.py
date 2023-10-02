#29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
def promedio_lista(lista):
  suma= sum (lista)
  promedio=suma/len(lista)
  return promedio
lista1= [2,4,6,33]
resultado =promedio_lista(lista1)
print ("El promedio de la lista es", resultado)

#30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
def cadena_mas_larga(lista):
  mas_larga=" "
  for cadena in lista:
    if len (cadena)> len(mas_larga):
      mas_larga=cadena
  return mas_larga
mi_lista = ["Fernando", "Alonso", "Aston", "Martin"]
resultado = cadena_mas_larga(mi_lista)
print("La cadena más larga de la lista es:", resultado)

#31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True
def n_primeros_primos(n):
    numeros_primos = []
    numero = 2
    while len(numeros_primos) < n:
        if es_primo(numero):
            numeros_primos.append(numero)
        numero += 1
    return numeros_primos
n = int(input("Ingrese un número entero positivo n: "))
if n <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    resultado = n_primeros_primos(n)
    print(f"Los {n} primeros números primos son:", resultado)
#32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
def cadena_inverso(cadena):
  cadena= cadena[::-1]
  return cadena
cadena1=str(input("Inserta una cadena de texto: "))
resultado= cadena_inverso(cadena1)
print (resultado)

#33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
def ordenar_por_ultimo_elemento(lista_de_tuplas):
    lista_ordenada = sorted(lista_de_tuplas, key=lambda x: x[-1])
    return lista_ordenada
tuplas = [(1, 5), (3, 2), (2, 8), (4, 1)]
resultado = ordenar_por_ultimo_elemento(tuplas)
print("Lista ordenada por el último elemento de cada tupla:", resultado)

#34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.

def contar_vocales(cadena):
    cadena = cadena.lower()
    contador = 0
    vocales = {'a', 'e', 'i', 'o', 'u'}
    for caracter in cadena:
        if caracter in vocales:
            contador += 1     
    return contador
mi_cadena = "Fernando ganara la 33"
resultado = contar_vocales(mi_cadena)
print("Cantidad de vocales en la cadena:", resultado)

#35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True
numero=int(input("Inserte un numero: "))
resultado = es_primo (numero)
print (resultado)
  