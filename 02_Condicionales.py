'''1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos'''
#1
x=33
if x >0 :
  print ("X es positivo")
else:
  print ("X es negativo")
#2
x=33
if x % 2 == 0:
  print("X es par")
else:
  print("X es impar")
#3
mi_lista = [14,33,35]
def mayor(mi_lista):
  max = mi_lista[0];
  for x in mi_lista:
    if x > max:
      max = x
  return max

print(mayor(mi_lista))

