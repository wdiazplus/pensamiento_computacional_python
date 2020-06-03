number = int(input('Ingresa un número '))

def factorial(number):
    if number < 0:
      print('Ingresa un valor no negativo')
      exit()
    elif number == 0 or number==1:
        return 1
    return factorial(number-1)*number
        
print(f'El factorial de {number} es igual a {factorial(number)}')
