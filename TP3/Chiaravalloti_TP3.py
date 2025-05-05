#Ejercicio 1
edad = int(input("Por favor, ingrese su edad en años: "))
if edad > 18:
  print("Es mayor de edad")
else:
 print ("es menor de edad")

#Ejercicio 2
nota = int(input("inserte su nota: "))
if nota >= 6:
    print("Aprobado")
else: print ("Desaprobado") 

#Ejercicio 3
numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else: 
     print("Por favor, ingrese un número par")
     
#Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad< 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")     
    
    
#Ejercicio 5
contraseña = input("Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
from statistics import mode, median, mean
numeros_aleatorios = [1, 2, 5, 5, 3]

la_moda = mode(numeros_aleatorios)
la_mediana = median(numeros_aleatorios)
la_media = mean(numeros_aleatorios)

print("Moda:", la_moda)
print("Mediana:", la_mediana)
print("Media:", la_media)

if la_media > la_mediana > la_moda:
    print("Sesgo positivo o a la derecha")
elif la_media < la_mediana < la_moda:
    print("Sesgo negativo o a la izquierda")
elif la_media == la_mediana == la_moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro con estos datos")
    
#Ejercicio 7
texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in 'aeiou':
    texto += "!"
    
print(texto)
    
#Ejercicio 8
nombre = input("Por favor, ingrese su nombre: ")

print("""
En este programa puede realizar cualquiera de las siguientes operaciones:
1. Si quiere su nombre en mayúsculas.
2. Si quiere su nombre en minúsculas.
3. Si quiere su nombre con la primera letra mayúscula.
""")
opcion = int(input("Ingrese el número de operación que desea realizar: "))

if opcion == 1:
  nombre_mayuscula = nombre.upper()
  print(nombre_mayuscula)
elif opcion == 2:
  nombre_minuscula = nombre.lower()
  print(nombre_minuscula)

elif opcion == 3:
  nombre_title = nombre.title()
  print(nombre_title)

else:
  print("Por favor, ingrese únicamente 1, 2 o 3")

#Ejercicio 9
magnitud_terremoto = float(input("Por favor, ingrese la magnitud del terremoto según la escala de Ritcher: "))

if magnitud_terremoto < 3:
  print("Muy leve")

elif 3 <= magnitud_terremoto < 4:
  print("Leve")

elif 4 <= magnitud_terremoto < 5:
  print("Moderado")

elif 5 <= magnitud_terremoto < 6:
  print("Fuerte")

elif 6 <= magnitud_terremoto < 7:
  print("Muy fuerte")

  print("Extremo")
  
 #Ejercicio 10
  hemisferio = input("Por favor, ingrese el hemisferio (N/S): ")
hemisferio = hemisferio.lower()


mes = int(input("Por favor, ingrese el mes del año en números: "))


dia = int(input("Por favor, ingrese el día del mes en números: "))



if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
  
  if hemisferio == "s":
    print("Verano")
  
  elif hemisferio == "n":
    print("Verano")
elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
  if hemisferio == "s":
    print("Otoño")
  elif hemisferio == "n":
    print("Primavera")
elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
  if hemisferio == "s":
    print("Invierno")
  elif hemisferio == "n":
    print("Verano")
else:
  if hemisferio == "s":
    print("Primavera")
  elif hemisferio == "n":
    print("Otoño")