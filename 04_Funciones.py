'''
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.
'''
#1
def suma (a, b):
  return a + b
print (suma (15, 18))
#2
def factorial (n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)
print (factorial(33))
print (factorial(4))
#3
def primo(num):
  if num < 2:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True
print(primo(33))
print(primo(11))
#4 
def sumado_lista(list):
  return sum(list)
print(sumado_lista([1, 2, 3, 4, 5]))

#5 
def reversa(cadena):
  return cadena[::-1]
print(reversa("Fernando Alonso"))

  
