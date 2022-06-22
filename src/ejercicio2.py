################
# Sofía Silva - @sofiaslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos
Escribir una función que reciba un número e indique si el mismo es positivo,
negativo o cero utilizando sumas y restas.
"""

def signo(numero):
    suma= numero + numero
    resta= numero - numero
    if resta == numero:
        return 'cero'
    elif suma == 0:
        return 'negativo'
    else:
        return 'positivo'


def principal():
    """ 
    Precondiciones:número entero
    Postcondicion: valor del número
    """
    numero= int(input('Ingresar número'))
    sign= signo(numero)
    print (f'{numero} es {sign}')
    
if __name__ == "__main__":
    principal()