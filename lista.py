#Lista con los números que indica el ejercicio 3 del libro "Aprende python desde cero".
lista = [6, 14, 11, 3, 2, 1, 15, 19]

#Esta función indica si el valor está dentro del rango o si es mayor o menos
def estaEnRango(valor, minimo, maximo):
    if valor > maximo:
        print("El número introducido es mayor al rango indicado")
        return False
    elif valor < minimo:
        print("El número introducido es menor al rango indicado")
        return False
    else:
        print("El número introducido está en el rango indicado")
        estaEnLista(valor, lista)
        return True

#Esta función indica si el valor está dentro de la lista o no
def estaEnLista(valor, lista):

    numerolista = 0

    for numeros in lista:
        if valor == numeros:
            numerolista = 1
    if numerolista == 1:
        print("El número está en lista")
        return True
    else:
        print("El número no esta en lista")
        return False
    
valor = int(input("Escribe un número entre 1 y 20: "))
minimo = 1
maximo = 20

estaEnRango(valor, minimo, maximo)