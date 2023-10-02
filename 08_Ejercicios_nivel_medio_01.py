'''8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.'''
def numero_perfecto(n):
  suma_divisores=0
  for i in range(1,n):
    if n % i ==0:
      suma_divisores+=i
  if suma_divisores==n:
    return True
  else:
    return False
numero=int(input("Ingrese numero"))
resultado= numero_perfecto(numero)
print(f"Este numero es perfecto? {resultado}")

#9. Ejercicio: Define una función que reciba un número y retorne su representación en binario.
def numero_binario(n):
  binario=bin(n)
  return binario
numero=int(input("Ingrese numero: "))
resultado= numero_binario(numero)
print(f"Este numero {numero} en binario es {resultado}")

#10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
def interseccion_listas (lista1,lista2):
  conjunto1=set(lista1)
  conjunto2=set(lista2)
  interserccion= conjunto1&conjunto2
  return list(interserccion)
listax=[1,2,3,4,5]
listay=[3,5,7]

print(interseccion_listas(listax,listay))
#11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
def palindromo(palabra):
  palabra=palabra.replace(" ", "")
  if palabra == palabra[::-1]:
    return "es un palindromo"
  else:
    return "no es un palindromo"
cadena=str(input("Inserta una cadena de texto: "))
resultado = palindromo(cadena)
print(f"Es{cadena} un palindromo? {cadena} {resultado}")

#12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”
for n in range(1,51):
    if n % 3 == 0:
      print ("Fizz")
    elif n % 5==0:
      print("Buzz")
    elif n % 3==0 and n % 5 ==0:
      print ("FizzBuzz")
    else:
      print (n)

#13 13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
def ordenar_lista(lista):
  lista.sort()
  return lista
lista1=[9,4,33,5,2,8]
lista_ordenada= ordenar_lista(lista1)
print (lista_ordenada)
#14 Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n
def palabras_mas_largas_que_n(lista_palabras, n):
    palabras_filtradas = [palabra for palabra in lista_palabras if len(palabra) > n]
    return palabras_filtradas
lista_de_palabras = ["Fernando", "Alonso", "Aston", "Martin","Max"]
n = 4
resultado = palabras_mas_largas_que_n(lista_de_palabras, n)
print(resultado)
#15  Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
def fibonacci (n):
  a,b=0,1
  contador=0
  while contador < n:
    print(a,end=" ")
    a,b=b,a+b
    contador+=1
n = int(input("Ingrese la cantidad de números de Fibonacci que desea imprimir: "))
if n <= 0:
    print("Por favor, ingrese un número válido.")
else:
    fibonacci(n)