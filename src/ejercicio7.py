################
# Sofía Silva - @sofiaslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
7. Transformación de un número
Escribir un programa que permita transformar un número solicitado expresado en grados,
minutos y segundos a segundos a segundos.
Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.
"""

def sexadecimal_a_decimal(horas, minutos, segundos):
    horassegundos= horas * 3600
    minutossegundos= minutos*60
    return segundos + minutossegundos + horassegundos
    
def decimal_a_sexadecimal(segundos):
    minutos= int(segundos/60)
    horas= int(minutos/60)
    segundos= segundos%60
    minutos= minutos%60
    tuple_tiempo= (horas, minutos, segundos)
    return tuple_tiempo

def principal():
    """ 
    Precondiciones: tres números enteros
    Postcondicion: números ordenados de mayor a menor y viceversa.
    """
    horas= int(input('Ingresar hora/s'))
    minutos= int(input('Ingresar minuto/s'))
    segundos= int(input('Ingresar segundo/s'))
    tiempoen_segundos= sexadecimal_a_decimal(horas, minutos, segundos)
    segundosen_tiempo= decimal_a_sexadecimal(segundos)
    print (f'{horas} hora/s {minutos} minuto/s {segundos} segundo/s son {tiempoen_segundos} segundos')
    print (f'{segundos} segundos son {segundosen_tiempo} en horas, minutos y segundos')
    
if __name__ == "__main__":
    principal()