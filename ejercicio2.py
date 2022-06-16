## Ejercicio 2
## Escribir una función ``es_vocal(caracter)`` que tome un carácter y 
## devuelva un valor logico(True si es una vocal, de lo contrario devuelve False)

opcion = (int(input("1_quiero ingresar una palabra\n2_quiero ingresar una letra\n")))


def es_vocal_string(string):
    vocales = "aeiou"
    hay = False
    for letra in range(len(string)):
        print(string[letra])
        if string[letra] in vocales:
            hay = True
    return hay


def es_vocal_letra(caracter):
    vocales = "aeiou"
    if caracter in vocales:
        return  True
    else:
        return False
 
 
if opcion == 1:
    palabra = input("ingrese una palabra\n")
    resultado = es_vocal_string(palabra)
    if resultado:
        print("Hay una vocal en la palabra ingresada\n")
    else:
        print("No hay ninguna vocal en la palabra ingresada\n")
    
elif opcion == 2:
    letra = input("ingrese una letra")
    resultado = es_vocal_letra(letra)
    if resultado:
     print("La letra es una vocal\n")
    else:
        print("La letra no es una vocal\n")

