name = input('Cuál es tu nombre ')

def saludo(name):
    ''' Nuestra función saluda a los nuevos usuarios
        name es un valor de tipo string que brinda el usuario
        la función retorna un saludo amigable '''
    print(f'Hola {name}, bienvenido a este nuevo mundo tech')

saludo(name)

help(saludo)