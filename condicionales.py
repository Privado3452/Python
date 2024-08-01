"""temperature = 40

if temperature > 35:
    print('Aviso por alta temperatura')"""
    

#condicionales anidados
"""temperature = 28

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
else:
    if temperature < 30:
        print('Nivel naranja')
    else:
        print('Nivel rojo')"""
        

"""temperature = 28

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
elif temperature < 30:
    print('Nivel naranja')
else:
    print('Nivel rojo')"""
    
#Asignaciones condicionales

"""temperature = 35

fire_risk = 'LOW' if temperature < 30 else 'HIGH'



fire_risk"""

#Operadores logicos

"""value = 8

value == 8

value != 8

value < 12

value <= 7

value > 4

value >= 9

# Asignación de valor inicial
>>> x = 8

>>> x > 4 or x > 12  # True or False
True

>>> x < 4 or x > 12  # False or False
False

>>> x > 4 and x > 12  # True and False
False

>>> x > 4 and x < 12  # True and True
True

>>> not(x != 8)  # not False
True"""

#match-case

"""color = '#FF0000'

match color:
    case '#FF0000':
        print('🔴')
    case '#00FF00':
        print('🟢')
    case '#0000FF':
        print('🔵')"""
    
"""color = '#AF549B'

match color:
    case '#FF0000':
        print('🔴')
    case '#00FF00':
        print('🟢')
    case '#0000FF':
        print('🔵')
    case _:
        print('Unknown color!')"""
        
#Patrones avanzados

"""point = (2, 5)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')

point = (3, 1, 7)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')"""
        
#Operador morsa

"""radius = 4.25
perimeter = 2 * 3.14 * radius
if perimeter < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)
"""
radius = 4.25
if (perimeter := 2 * 3.14 * radius) < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)
