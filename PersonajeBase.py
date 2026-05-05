# Variables del personaje RPG
nombre = 'Aragorn'
nivel = 7
vida = 100.0
vida_maxima = 100.0
esta_vivo = True
clase = 'Guerrero'
puntos_ataque = 15
puntos_defensa = 10

# Ejercicio 1A: El Mago Gandalf [cite: 18]
nombre_mago = 'Gandalf'
clase_mago = 'Mago'
nivel_mago = 5
vida_mago = 80.0
mana_mago = 120

# Ejercicio 2A

vida_enemigo = 40
ataque_jugador = 35
nivel_jugador = 6
bonificacion = 10 if nivel_jugador >= 5 else 0 #

dano_total = ataque_jugador + bonificacion
vida_restante = vida_enemigo - dano_total

if vida_restante <= 0:
    print('Enemigo derrotado! +50 XP')
elif vida_restante <= 20:
    print('Enemigo en estado critico')
else:
    print(f'Enemigo resiste. Vida restante: {vida_restante}')

print(f'{nombre_mago} [{clase_mago}] Nv.{nivel_mago} | Vida: {vida_mago} | Mana: {mana_mago}')

# Verificar tipos
print(type(nombre))      # <class 'str'>
print(type(nivel))       # <class 'int'>
print(type(vida))        # <class 'float'>
print(type(esta_vivo))   # <class 'bool'>

# Mostrar información del personaje
print(f'{nombre} (Nv.{nivel}) - Vida: {vida}')


# Conversiones de tipo
ataque = 15
dano = float(ataque) * 1.5   # cast
msg = 'Daño: ' + str(dano)   # explícito

# Leer del usuario (input)
nom = input('Nombre: ')
niv = int(input('Nivel: '))
print(f'{nom} Nv.{niv}')

# f-strings (muy útiles)
vida = 87.5
print(f'Vida: {vida:.1f}%')