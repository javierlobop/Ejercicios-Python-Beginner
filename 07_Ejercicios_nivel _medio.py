#1Define una función que utilice un bucle para imprimir los primeros números de la serie de Fibonacci.
def fibonacci (n):
  a,b=0,1
  contador=0
  while contador < n:
    print(a,end="")
    a,b=b,a+b
    contador+=1
n = int(input("Ingrese la cantidad de números de Fibonacci que desea imprimir: "))
if n <= 0:
    print("Por favor, ingrese un número válido.")
else:
    fibonacci(n)
#2 Define una función que tome un número y retorne una lista de sus divisores.
def divisores (n):
  div=[]
  for i in range (1, n+1):
    if n % i==0:
      div.append(i)
  return div
num = int(input("Ingrese un número: "))
print(f"Los divisores de {num} son: {divisores(num)}")

#3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
def nueva_listaunicos(lista):
  lista_unica=[]
  for n in lista:
    if n not in lista_unica:
      lista_unica.append(n)
  return lista_unica

lista_original= [1,2,2,3,3,4,4,5,6,6,6]
print(nueva_listaunicos(lista_original))

#4 Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
def suma_digitos(n):
  suma=0
  while n>0:
    digito=n%10
    suma += digito
    n //=10
  return suma
num = int(input("Ingrese un número: "))
resultado = suma_digitos(num)
print(f"La suma de los dígitos de {num} es {resultado}")

#5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.
def contar_vocales(palabra):
  vocales ="aeiu"
  contador= 0
  for letra in palabra:
    if letra in vocales:
      contador +=1
  return contador
texto = input("Ingrese una cadena de texto: ")
resultado = contar_vocales(texto)
print(f"La cadena '{texto}' contiene {resultado} vocales.")

#6 Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
def n_elementos_lista(lista,n):
  if n<0:
    return []
  else:
    return lista[:n]
mi_lista = [2,8,5,4,3,5,6,4,2]
n = 4
resultado = n_elementos_lista(mi_lista, n)
print(f"Los primeros {n} elementos de la lista son: {resultado}")

#7 Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
def upper_lower(palabra):
  mayusculas=0
  minusculas=0
  for letra in palabra:
    if letra.isupper():
      mayusculas+=1
    else:
      minusculas +=1
  return mayusculas,minusculas

texto = input("Ingrese una cadena de texto: ")
mayusculas, minusculas = upper_lower(texto)
print(f"Mayúsculas: {mayusculas}")
print(f"Minúsculas: {minusculas}")


    
    

    



