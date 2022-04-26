'''
Pregunta 2
Para obtener ciertas estadísticas de un recorrido, se pide realizar un programa que dada una distancia, 
entregue la velocidad en kilómetros por hora y en metros por segundo. 
Para esto, existen dos variables tiempo y distancia que vienen en segundos y kilómetros respectivamente. 
Tu programa debe guardar en la variable resultado un string
'''
def velocidad(distancia, tiempo):
    resultado = ""
    velocidad = distancia/tiempo

    vel_kmh = velocidad * 3600
    vel_ms = velocidad * 1000
    resultado = f'la velocidad es {vel_kmh} km/h o {vel_ms} m/s'
    print(f'La velocidad es {resultado}')
    return resultado
tiempo = 1
distancia = 0.01

velocidad(distancia, tiempo)