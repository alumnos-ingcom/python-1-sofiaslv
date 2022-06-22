################
# Sofía Silva - @sofiaslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.
"""

def convertir_a_fahrrenheit(centigrados): 
    fahrrenheit = (centigrados * (9/5)) + 32 
    return fahrrenheit

def convertir_a_centigrados(fahrenheit):
    centigrados= ((fahrenheit - 32)*(5/9))
    return centigrados

def principal():
    """
    El ejercicio consiste en realizar el calculo de conversion de grado a fahrrenheit
    y viceversa mediante sus formulas.
    
    Precondiciones: número flotante
    Postcondicion: número convertido en su respectiva escala de temperatura.
    
    """
    pass

if __name__ == "__main__":
    principal()