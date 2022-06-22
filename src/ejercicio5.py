################
# Sofía Silva - @sofiaslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
5. Divisiones
Escribir una función que mediante
restas sucesivas, obtenga el valor del cociente
y resto de dos números enteros.
"""

def division_lenta(dividendo, divisor):
    cociente=0
    resto= dividendo
    while resto >= divisor:
        resto= resto - divisor
        cociente= cociente + 1
    return cociente
        
def principal():
    """ 
    Precondiciones: dos números enteros
    Postcondicion: cociente entero de la división entre esos números
    """
    dividendo= int(input('Ingresar dividendo'))
    divisor= int(input('Ingresar divisor'))
    cociente= division_lenta(dividendo, divisor)
    print (f'El resultado de dividir {dividendo} y {divisor} es {cociente}')
    
if __name__ == "__main__":
    principal()