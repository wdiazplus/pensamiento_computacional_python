items=[0,'namestring']

print(f'items inicial {items}')
more_items=[1,2,3,True,False]


def agree():
    for i in range(0,len(more_items)):
     return more_items[i]  #Almacenar valores pero no como lista

print(agree()) #Verifico que sean los valores deseados
# items.insert(len(items), agree())
# print(f'items final {items}')

# Profe, que pena escribir a estar horas, pero estuve mucho tiempo tratando de hacer algo para agregar varios elementos a una lista ya creada con el método insert. Después de horas encontré que con extend se pueden juntar dos listas. Pero quisiera revisará el pequeño script que tengo y el porqué no me da un resultado similar y solo me agrega el último valor.   Gracias, mi código es: 