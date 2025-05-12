#Ejercicio 1
def creando_hola_mundo():
    print("Hola Mundo!")
creando_hola_mundo()
#Ejercicio 2
def saludar_usuario(nombre):
    return "Hola " + nombre + "!"

nombre = input("Ingresá tu nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)
#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy " + nombre + " " + apellido + ", tengo " + edad + " años y vivo en " + residencia)

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")

informacion_personal(nombre, apellido, edad, residencia)
#Ejercicio 4
def calcular_area_circulo(radio):
    return 3.14 * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio = float(input("Ingresá el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print("Área del círculo:", area)
print("Perímetro del círculo:", perimetro)

#Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresá la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print("Equivale a", horas, "horas")

#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

numero = int(input("Ingresá un número: "))
tabla_multiplicar(numero)

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))

resultados = operaciones_basicas(a, b)

print("Suma:", resultados[0])
print("Resta:", resultados[1])
print("Multiplicación:", resultados[2])
print("División:", resultados[3])

#Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))

imc = calcular_imc(peso, altura)
print("Tu IMC es:", round(imc, 2))

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingresá la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print("La temperatura en Fahrenheit es:", round(fahrenheit, 2))

#Ejercicio 10
 
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
c = float(input("Ingresá el tercer número: "))

promedio = calcular_promedio(a, b, c)
print("El promedio es:", round(promedio, 2))
