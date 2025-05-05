# Ejercicio 1 
# Imprimir números del 0 al 100, uno por línea
for i in range(0, 101):
    print(i)

#Ejercicio 2
numero = (input("Ingrese un numero entero: "))
cantidad_digitos = len(numero)
print("El número tiene", cantidad_digitos, "dígito(s).")

#Ejercicio 3
contador = 0
valor_1 = int(input("ingrese el primer valor: "))
valor_2 = int(input("ingrese el segundo valor: "))

for i in range(min(valor_1,valor_2)+ 1, max(valor_1, valor_2)):
    contador= contador + 1
    
print("Cantidad de números entre los valores:", contador)

#Ejercicio 4

contador = 0
while True:
    num =int(input("ingrese un numero: "))
    if num == 0:
        break 
    contador += num
print("La suma total es:", contador)

#Ejercicio 5

import random
num_secreto = random.randint(0,9)
contador= 0
while True:
  intento= int(input("Ingrese un numero aleatorio entre 0 y 9: "))
  contador += 1
   
  if intento == num_secreto:
       break 
print("¡Adivinaste el número en", contador, "intento(s)!")

#Ejercicio 6 
for i in range(100, -1, -2):
    print(i)
    
 #Ejercicio 7
numero= int(input("ingrese un numero positivo: "))
suma = 0

for i in range(0, numero + 1):
    suma +=1
print("La suma de los números entre 0 y", numero, "es:", suma)

#Ejercicio 8

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(4):
    num = int(input("Ingresá un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
     positivos += 1
    elif num < 0:
     negativos += 1
     
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)
    
#Ejercicio 9
cantidad = 10
suma = 0
for i in range(cantidad):
    num = int(input("Ingresá un número: "))
    suma += num
media = suma / cantidad
print("La media de los", cantidad, "números ingresados es:", media)

#Ejercicio 10

numero = input("Ingresá un número: ")
# Invertir los dígitos usando slicing
numero_invertido = numero[::-1]
print("Número invertido:", numero_invertido)