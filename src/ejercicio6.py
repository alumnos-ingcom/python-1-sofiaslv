################
# Sofía Silva - @sofiaslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
6. Ordenar 3 valores
Escribir una función que a partir de tres variables de tipo
entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
"""

def ordenar_mayor_a_menor(uno, dos, tres):
    if uno > dos and dos > tres:
        return (uno, dos, tres)
    elif dos > tres and tres > uno:
        return (dos, tres, uno)
    else:
        return (tres, dos, uno)


def ordenar_menor_a_mayor(uno, dos, tres):
    if uno < dos and dos < tres:
        return (uno, dos, tres)
    elif dos < tres and tres < uno:
        return (dos, tres, uno)
    else:
        return (tres, dos, uno)


def principal():
    """ 
    Precondiciones: tres números enteros
    Postcondicion: números ordenados de mayor a menor y viceversa.
    """
    numero= int(input('Ingresar número'))
    numero2= int(input('Ingresar otro número'))
    numero3= int(input('Ingresar último número'))
    ordenmenosmas= ordenar_menor_a_mayor(numero, numero2, numero3)
    ordenmasmenos= ordenar_mayor_a_menor(numero, numero2, numero3)
    print (f'Orden de menor a mayor: {ordenmenosmas}')
    print (f'Orden de mayor a menor: {ordenmasmenos}')
    
if __name__ == "__main__":
    principal()