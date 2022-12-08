#Función para indicar si el número introducido es binario o no
def esBinario(strbinario):
    for digitos in strbinario:
        if((digitos != "0") and (digitos != "1")):
            print("El número introducido no es binario")
            return False
    print ("El número introducido es binario")
    conversiondecimal(strbinario)
    return True

#Función para convertir el número binario en decimal
def conversiondecimal(strbinario):
    decimal = 0

    for posicion, digito in enumerate(strbinario[::-1]):
        decimal += int(digito) * 2 ** posicion
    print(f"Y su valor en decimal es: {decimal}")
    return decimal

binario = input("Introduce un número binario: ")
esBinario(binario)