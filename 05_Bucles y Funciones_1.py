#1 Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.
def par_impar (x):
  if x % 2 ==0:
    return "El numero es par"
  else:
    return "El numero es impar"
  
print (par_impar(33))
print (par_impar(12))
#2  Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.
def factorial( n ):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)
print (factorial(33))
print (factorial(4))
#3  Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.
def contar_digitos (x):
  return len(str(x))
print (contar_digitos(345))

#4  Dada una lista de números, crea una función que devuelva el número máximo de la lista.

def maximo_lista (lista):
  maximo=lista [0]
  for x in lista:
    if x > maximo:
      maximo =x
  return maximo
lista_1=[33,14,21,10]
lista_2=[23,14,21,10]
print(maximo_lista (lista_1))
print(maximo_lista (lista_2))

#05 Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.
def suma_digitos(x):
  suma = 0
  while x > 0:
    suma = suma + x % 10 
    x =x // 10
  return suma
print (suma_digitos(31))