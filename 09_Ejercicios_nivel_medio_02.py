#16 16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
def maximo_lista(lista):
    return max(lista)
lista1=[1,2,3,4,55,6]
resultado= maximo_lista(lista1)
print (resultado)
#17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
def suma_cubo(n):
  numero_str=str(n)
  suma_cubos= 0
  for d in numero_str:
    d=int(d)
    suma_cubos += d ** 3
  return suma_cubos
num=int(input("Ingrese numero: "))
resultado=suma_cubo(num)
print (resultado)
#18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista   
def segundo_mayor(lista):
        lista_unicos = list(set(lista))
        lista_unicos.sort(reverse=True)
        return lista_unicos[1]
mi_lista = [12,33,2,43,16]
resultado = segundo_mayor(mi_lista)
print("El segundo número más grande es:",resultado)

#19 Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
def listas_comun(lista1,lista2):
   for elemento1 in lista1:
    for elemento2 in lista2:
     if elemento1 == elemento2:
      return True
lista_1=[1,2,4,7,9]
lista_2=[2,5,8]
resultado=listas_comun(lista_1,lista_2)
print(resultado)    

#20  Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
def orden_inverso(lista):
  lista_inversa= lista[::-1]
  return lista_inversa
lista1=[23,12,165,32]
resultado= orden_inverso(lista1) 
print (resultado)

#21 Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
def contar_letras_y_digitos(cadena):
 letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
 digitos = '0123456789'
 contador_letras = 0
 contador_digitos = 0
 for caracter in cadena:
  if caracter in letras:
   contador_letras += 1
  elif caracter in digitos:
   contador_digitos +=1 
 return contador_letras, contador_digitos
cadena = "Fernado Alonso tiene 32 victorias y 2 mundiales"
letras, digitos = contar_letras_y_digitos(cadena)
print("Número de letras:", letras)
print("Número de dígitos:", digitos) 

