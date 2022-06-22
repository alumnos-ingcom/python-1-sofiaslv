################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo.
"""
def es_palindromo(texto):
    texto= texto.replace(" ", "")
    if (texto) == (texto)[::-1]:
        return True
    else:
        return False


def principal(): 
    texto= str(input('Ingresar una frase'))
    palindromo= es_palindromo(texto)
    if palindromo == True:
        print (f'{texto} es palíndromo')
    else:
        print (f'{texto} no es palíndromo')


if __name__ == "__main__": 
    principal()