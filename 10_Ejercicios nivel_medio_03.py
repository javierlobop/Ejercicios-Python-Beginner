#22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números
def suma_num_lista(lista):
  suma=0
  suma_acumulada=[]
  for num in lista:
    suma += num
    suma_acumulada.append(suma)
  return suma_acumulada
lista1=[12,33,46,2]
resultado= suma_num_lista(lista1)
print (resultado)
#23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
#24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
from collections import Counter
def contar_apariciones(cadena):
    apariciones = Counter(cadena)
    return apariciones
mi_cadena = "Fernando Alonso"
resultado = contar_apariciones(mi_cadena)
print("Apariciones de caracteres en la cadena:")
for caracter, cantidad in resultado.items():
    print(f"'{caracter}': {cantidad}")

#26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
def elementos_no_comunes(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    diferencia1 = conjunto1.difference(conjunto2)
    diferencia2 = conjunto2.difference(conjunto1)
    elementos_no_comunes = list(diferencia1.union(diferencia2))
    return elementos_no_comunes
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
resultado = elementos_no_comunes(lista1, lista2)
print("Elementos no comunes entre lista1 y lista2:", resultado)
#27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
def lista_sin_duplicados(lista):
    conjunto_sin_duplicados = set(lista)
    lista_sin_duplicados = list(conjunto_sin_duplicados)
    return lista_sin_duplicados

# Ejemplo de uso:
mi_lista = [1, 2, 2, 3, 4, 4, 5]
resultado = lista_sin_duplicados(mi_lista)
print("Lista sin duplicados:", resultado)
#28 Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número
def suma_cuadrados_pares(numero):
    suma = 0
    for i in range(2, numero + 1, 2):
        suma += i ** 2
    return suma
n = int(input("Ingrese un número entero positivo: "))
if n <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    resultado = suma_cuadrados_pares(n)
    print("La suma de los cuadrados de números pares hasta", n, "es:", resultado)