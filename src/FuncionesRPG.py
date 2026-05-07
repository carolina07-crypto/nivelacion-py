class FuncionesRPG:

    # Retorna el daño real (mínimo 1)
    @staticmethod
    def calcular_dano(ataque, defensa):
        dano = ataque - defensa
        return dano if dano > 0 else 1

    # Cura sin pasar del máximo
    @staticmethod
    def aplicar_curacion(vida, cur, maximo):
        nueva = vida + cur
        return maximo if nueva > maximo else nueva

    # Sin retorno: solo imprime
    @staticmethod
    def mostrar_estado(nombre, vida, nivel):
        print(f"{nombre} [Nv{nivel}] HP: {vida:.0f}")

    @staticmethod
    def subir_nivel(xp_actual, xp_necesario, nivel_actual):
        if xp_actual >= xp_necesario:
            nivel_actual += 1
            print("Subiste de nivel", nivel_actual)
        return nivel_actual


# Programa principal
d = FuncionesRPG.calcular_dano(20, 0)
print("Daño", d)

v = FuncionesRPG.aplicar_curacion(40, 80, 100)
FuncionesRPG.mostrar_estado("Frodo", v, 3)

# Ejercicio 4A
e = FuncionesRPG.subir_nivel(110, 100, 3)