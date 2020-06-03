new_list = list(range(100))

# print(new_list)
#Vamos a duplicar new_list haciendo:
double_list = [ i * 2 for i in new_list]

# print(double_list)
# Mostrar solo los valores pares de new_list

even = [i for i in new_list if i % 2 ==0]

# print(even)

# Mostrar solo los valores impares de new_list

odd = [i for i in new_list if i % 2 !=0]

# print(odd)
