################
# Sofía Silva - @sofiaslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
4. Suma lenta
Escribir una función que haga la suma entre
dos números enteros sin hacer la operación de manera directa. Esto quiere decir que
para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.
"""
def suma_lenta(numero, otro_numero):
    descomp=0
    while descomp < otro_numero:
        descomp+=1
        suma= numero + descomp
    return suma

def suma_lenta_impresa(numero, otro_numero):
    descomp=0
    print (numero)
    while descomp < otro_numero:
        descomp+=1
        print ('+1')
        suma= numero + descomp
    return suma
        
def principal():
    """ 
    Precondiciones: dos números enteros
    Postcondicion: suma de los números
    """
    numero= int(input('Ingresar número'))
    numero2= int(input('Ingresar otro número'))
    suma= suma_lenta_impresa(numero, numero2)
    print (suma)
    
if __name__ == "__main__":
    principal()