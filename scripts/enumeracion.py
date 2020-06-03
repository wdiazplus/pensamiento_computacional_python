# importamos el paquete para medir tiempos
import time

objetivo = int(input('Escoge un entero: '))
respuesta = 0
tinicial=time.time()
while respuesta**2 < objetivo:
    respuesta +=1
    print(respuesta)  #Me permite observar que ejecuta el algoritmo
if respuesta**2 == objetivo:
    print(f'El número {objetivo} posee una raíz cuadrada exacta y es {respuesta}')
else:
    print(f'El número {objetivo} no posee una raíz cuadrada exacta')

print(f'El tiempo que tardó en responder fue {time.time()-tinicial} segundos')



# 6510.631077624