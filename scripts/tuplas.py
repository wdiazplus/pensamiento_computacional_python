# Mostraremos algunos ejemplos de tuplas y operaciones sobre ellas

suma = lambda x,y: x+y

mix = (2,'text',False, suma(2,3) )

#A continuación verificamos que el tipo de mix sea 'tuple'
print(type(mix))

# Mostramos el valor de la suma de 2 y 3 a partir de la tupla mix
print(f'El valor de sumar 2 y 3 usando una función anónima dentro de la tupla mix es {mix[3]}')

# Cuando queremos iniciar una tupla con un solo valor debemos agregar coma al elemento así

tupla_unica = (1,)

#Lo anterior debido a que si no agregamos la coma, asumirá python que es tipo del elemento, es decir:

tupla_unica_int =(1)
tupla_unica_booleano =(True)
tupla_unica_float =(1.36)
tupla_unica_string =('Hola')

#Verifiquemos ello con type

print(type(tupla_unica_int))
print(type(tupla_unica_booleano))
print(type(tupla_unica_float))
print(type(tupla_unica_string))

# Para agregar una tupla con otra, podemos reasignar 
#la existente y sobreescibir los elementos

new_tupla = (1,True,suma(8,3))

new_tupla += mix
print(new_tupla)
print(type(new_tupla))



