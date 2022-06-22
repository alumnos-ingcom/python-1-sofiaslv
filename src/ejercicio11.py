################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de
Escribir una función que indique con True si un número entero es multiplo de otro, utilizando sumas y restas.
"""
def es_multiplo(numero, multiplo):
    suma=numero
    resta=multiplo
    while suma < multiplo:
        suma= suma + numero
    while resta > 0:
        resta= resta - numero
    if suma == multiplo and resta == 0:
        return True


def principal(): 
    numero= int(input('Ingresar número'))
    numero2=int(input('Ingresar otro número'))
    multiplo= es_multiplo(numero, numero2)
    if multiplo == True:
        print (f'{numero2} es multiplo de {numero}')
    else:
        print (f'{numero2} no es multiplo de {numero}')


if __name__ == "__main__": 
    principal()