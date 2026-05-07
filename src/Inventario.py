# inventario
inventario = ["Espada de hierro",
              "Pocion de vida",
              "Escudo de madera",
              "Llave dorada"
              ]
print (" INVENTARIO ")

# Indice

for i, item in enumerate (inventario, 1):
    print (f'{i}. {item}')
    
# Buscar item
buscar = "Pocion de vida"

if buscar in inventario:
    print (f'[OK] {buscar} encontrada')
else:
    print (f'[X] {buscar} no disponible')

# Simulacion combate RPG

vida_heroe = 80
vida_enemigo = 60
ronda = 1
while vida_heroe > 0 and vida_enemigo > 0:
    #Heroe ataca
    dano_heroe = 15
    vida_enemigo -= dano_heroe
    
    # Enemigo contraataca
    if vida_enemigo > 0:
        dano_enemigo = 10
        vida_heroe -= dano_enemigo
        
        print (f'Ronda {ronda} :')
        print (f' Heroe: {vida_heroe} | Enemigo: {vida_enemigo}')
        
        ronda += 1
        
# Resultado final

resultado = 'VICTORIA' if vida_heroe > 0 else 'DERROTA'
print (resultado)

# Ejercicio 3A
xp = 0
nivel = 1
xp_necesario = 100
batallas = [20, 15, 40, 30]
for xp_ganado in batallas:
    xp += xp_ganado
    if xp >= xp_necesario:
        xp -= xp_necesario
        print (f' Subiste de nivel, Nivel actual: {nivel}' )   
        
