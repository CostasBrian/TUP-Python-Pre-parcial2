#Ejercicio 1
def max_de_tres (n1, n2, n3):
    return max(n1, n2, n3)

#Ejercicio 2
def es_vocal (x):
    x.lower()
    if x in "aeiou":
        return True
    else:
        return False
        
print(max_de_tres(1,2,3))
print(max_de_tres(1,1,1))
print(es_vocal('c'))
print(es_vocal('o'))