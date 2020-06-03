#Este programa ayuda a conseguir una aproximación a la raíz cuadrada de un número.

import time

objetivo = float(input('Ingresa el número que deseas hallarle la raíz cuadrada: '))
epsilon= 0.01
paso = epsilon**2
respuesta = 0.0

tinicial=time.time()  #Permite conocer el tiempo al iniciar el código

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    # print(abs(respuesta**2-objetivo),respuesta)
    respuesta +=paso

if abs(respuesta**2 - objetivo) >=epsilon:
    print(f'No se encontró la raíz cuadrada de {objetivo}')
else: 
    print(f'la raíz cuadrada de {objetivo} es aproximadamente {respuesta}')

print(f'El tiempo que tardó en responder fue {time.time()-tinicial} segundos')
