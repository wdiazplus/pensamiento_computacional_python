# Obteniendo los menores a 5

# number=0

# while number < 5:
#     print(f'El número {number} es menor que 5')
#     number+=1

# Ejemplo 2

contador_externo = 0
contador_interno = 0

while contador_externo <5:
    while contador_interno <6:
        print(contador_externo,contador_interno)
        contador_interno +=1

        if contador_interno>=3:
            break
    contador_externo+=1
    contador_interno=0        
    