#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuántos años tienes? ")
residencia = input("¿Dónde vives? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Ejercicio 4
import math
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área: {area}, Perímetro: {perimetro}")

#Ejercicio 5
segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos // 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

#Ejercicio 6
numero = int(input("Ingresa un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#Ejercicio 7
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
print(f"Suma: {numero1 + numero2}")
print(f"Resta: {numero1 - numero2}")
print(f"Multiplicación: {numero1 * numero2}")
print(f"División: {numero1 / numero2}")

#Ejercicio 8
altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kg: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc}")

#Ejercicio 9
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")

#Ejercicio 10
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los números es: {promedio}")















