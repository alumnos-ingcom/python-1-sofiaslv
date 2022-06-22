################
# Sofía Silva - @sofiaslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
8. Números primos
Escribir una función que indique con True si un numero indicado es Primo.
"""

def es_primo(numero):
    divisor=1
    divisiblespor=0
    while divisor<=numero:
        if numero%divisor == 0:
            divisiblespor+=1
        divisor+=1
    if divisiblespor <= 2:
        return True
    
def principal():
    numero= int(input('Ingresar número'))
    primoono= es_primo(numero)
    if primoono == True:
        print (f' {numero} es primo')
    else:
        print (f'{numero} es compuesto')

if __name__ == "__main__":
    principal()
        