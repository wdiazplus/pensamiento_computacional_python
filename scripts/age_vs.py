#  En el presente código, se compara la edad de los usuarios y 
# se informa si uno es mayor, menor o tiene la misma edad del otro


user_name_1 = input('Ingresa tu nombre  ')
user_age_1 = int(input('Ingresa tu edad  '))
user_name_2 = input('Ingresa tu nombre  ')
user_age_2 = int(input('Ingresa tu edad  '))

if user_age_1 > user_age_2:
    print(f'{user_name_1} es mayor que {user_name_2}')
elif user_age_1 < user_age_2:
    print(f'{user_name_1} es menor que {user_name_2}')
else: 
    print('Hey !!! tienen la misma edad')
