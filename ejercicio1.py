
## Ejercicio 1
## Definir una función ``max_de_tres(nr1, nr2, nr3)``, que tome tres números como argumentos y devuelva el mayor de ellos.

num1 = int(input("ingrese un numero\n"))
num2 = int(input("ingrese otro numero\n"))
num3 = int(input("ingrese otro numero\n"))

def max_de_tres(a, b, c):
    if b < a > c:
        return a
    if a < b > c:
        return b
    return c

resultado = max_de_tres(num1, num2, num3)
print("El numero mayor es: ", resultado)

