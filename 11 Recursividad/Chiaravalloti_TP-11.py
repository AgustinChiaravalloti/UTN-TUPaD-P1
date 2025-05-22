#Ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

limite = int(input("Ingresá un número entero mayor que 0: "))

print(f"\nFactoriales del 1 al {limite}:\n")
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

#Ejercicio 2
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

limite = int(input("Ingresá una posición para la serie de Fibonacci: "))

print(f"\nSerie de Fibonacci hasta la posición {limite}:\n")
for i in range(limite + 1):
    print(f"F({i}) = {fibonacci(i)}")

#Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1  
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))

resultado = potencia(base, exponente)
print(f"\n{base} elevado a la {exponente} es: {resultado}")

#Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingresá un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"\nEl número {numero} en binario es: {binario}")

#Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input("Ingresá una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(texto):
    print(f"\n'{texto}' es un palíndromo.")
else:
    print(f"\n'{texto}' no es un palíndromo.")
    
#Ejercicio 6 
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingresá un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"\nLa suma de los dígitos de {numero} es: {resultado}")

#Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel_base = int(input("Ingresá la cantidad de bloques en el nivel más bajo: "))

if nivel_base < 1:
    print("El número debe ser mayor o igual a 1.")
else:
    total = contar_bloques(nivel_base)
    print(f"\nSe necesitan {total} bloques para construir la pirámide.")

#Ejercicio 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingresá un número entero positivo: "))
digito = int(input("Ingresá el dígito que querés contar (0 a 9): "))

if numero < 0 or digito < 0 or digito > 9:
    print("Entrada inválida.")
else:
    resultado = contar_digito(numero, digito)
    print(f"\nEl dígito {digito} aparece {resultado} veces en {numero}.")
