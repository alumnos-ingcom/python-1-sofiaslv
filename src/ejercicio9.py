################
# Sofía Silva - @sofiaslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
9. Factores Primos
Escribir una función
que retorne una tuple con factores primos de un numero entero positivo.
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

def lista_primos(num):
    listaprimos= []
    if es_primo(num)==True:
        listaprimos.append(num)
    return listaprimos

def factores_primos(numero):
    primo=1
    while primo<=numero:
        primo=primo + 1
        listaprimos=lista_primos(primo)
    factores=()
    for i in listaprimos:
        while numero%i == 0:
            numero= numero//i
            factores= factores + i
    return factores
         
def principal():
    """
    Precondiciones: número flotante
    Postcondicion: número convertido en su respectiva escala de temperatura.
    """
    numero= int(input('Ingresar número'))
    factoresprimos= factores_primos(numero)
    print (factoresprimos)
    
if __name__ == "__main__":
    principal()         

    