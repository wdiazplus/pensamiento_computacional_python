
def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        return ('No se puede divir la lista por cero')

lista = list(range(10))
# Generamos un error
divisor = 0

print(divide_elementos_de_lista(lista,divisor))
