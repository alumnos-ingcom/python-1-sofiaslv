################
# Sofía Silva - @sofiaslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
3. Comparación de números
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""
def compara(numero, otro_numero):
    primero= numero - otro_numero
    if primero <= 0:
        primero= primero + primero
        if primero==0:
            iguales= 0
            return iguales
        else:
            menor= -1
            return menor
    else:
        mayor= 1
        return mayor

def principal():
    """ 
    Precondiciones: dos números enteros
    Postcondicion: 
    """
    numero= int(input('Ingresar número'))
    otro_numero= int(input('Ingresar otro número'))
    comparacion= compara(numero, otro_numero)
    
    if comparacion == -1:
        print (f'{numero} es menor que {otro_numero}')
    elif comparacion == 0:
        print (f'{numero} es igual que {otro_numero}')
    elif comparacion == 1:
        print (f'{numero} es mayor que {otro_numero}')
    
if __name__ == "__main__":
    principal()