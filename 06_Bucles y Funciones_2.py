#1 Dados dos números, crea una función para encontrar el mínimo común múltiplo(MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.
def calcular_mcm(num1, num2):
    def calcular_mcd(a, b):
        while b:
            a, b = b, a % b
        return a
    mcd = calcular_mcd(num1, num2)
    mcm = (num1 * num2) // mcd
    return mcm
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print("El MCM es:", calcular_mcm(num1, num2))


#2  Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.
def calcular_area_triangulo(base, altura):
  return (base * altura) / 2 
base = float(input("Ingrese la base del triángulo: ")) 
altura = float(input("Ingrese la altura del triángulo: ")) 
print("El área del triángulo es:", calcular_area_triangulo(base, altura))
# 1. Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.
def verificar_signo(num): 
  if num > 0:
    return "positivo" 
  elif num < 0: 
    return "negativo"
  else:
    return "cero"
num = float(input("Ingresa un número: "))
print("El número es:",verificar_signo(num))


#4 Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.
def contar_letras (palabra):
  numero_letras= len(palabra)
  return numero_letras
palabra = input("Ingresa una palabra: ")
print("La cantidad de letras es:", contar_letras(palabra))

#5  Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.
def valor_absoluto_lista(lista):
    valor_absoluto = [abs(numero) for numero in lista]
    return valor_absoluto
lista_1 = [-5, 10, -15, 20, -25]
resultado = valor_absoluto_lista(lista_1)
print(f"Lista original: {lista_1}")
print(f"Lista de valor absoluto: {resultado}")

#6 Crea una función que, dado un número, verifique si un número es primo.
def numero_primo(n):
  if n<=1:
    return False
  for i in range (2,n):
    if n % i == 0:
      return False
  return True
num=int(input("Ingresa_numero: "))
if numero_primo(num): 
  print("Es un numero primo")
else:
  print ("No es un numero primo")

#7  Dados dos números, crea una función para encontrar el máximo común divisor(MCD) de esos dos números.
