#Ejercicio 1
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#Ejercicio 2
Lista_elementos = ["futbol", "pelota", 21, 77, "Agus"]
penultimo_elemento = Lista_elementos[3]
print("el penultimo elemento de la lista es =",penultimo_elemento)
#Ejercicio 3

lista_vacia = []
lista_vacia.append("futbol")
lista_vacia.append("tenis")
lista_vacia.append("basquet")
print("la nueva lista es =",lista_vacia)

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)

#Ejercicio 5
#en el ejercicio 5 se muestra una lista con numeros y debajo una funcion que elimina todos esos numeros de la lista.

#Ejercicio 6
numeros = list(range(10, 31, 5))  
print("Lista completa:", numeros)
print("Los dos primeros números son:", numeros[0], "y", numeros[1])

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "mustang"
autos[2] = "camaro"
print("autos")

#Ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][compras[1].index("fideos")] = "tallarines"
compras[0].remove("pan")
print(compras)

#Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
