class Mision:
    def __init__(self, nombre, rango, recompensa, es_grupal, min_miembros=1):
        """Inicializa los atributos de una Misión"""
        self.nombre = nombre
        self.rango = rango
        self.recompensa = recompensa
        self.es_grupal = es_grupal
        self.min_miembros = min_miembros
        self.completada = False

    def completar_mision(self):
        """Marca la misión como completada"""
        self.completada = True

gremio = []  # Lista para almacenar los aventureros
misiones = []  # Lista para almacenar las misiones

def registrar_aventurero():
    """Función para registrar un aventurero"""
    try:
        nombre = input("Ingrese el nombre del aventurero: ")
        id_unico = int(input("Ingrese el ID del aventurero: "))
        puntos_habilidad = int(input("Ingrese los puntos de habilidad (1-100): "))
        experiencia = int(input("Ingrese la experiencia del aventurero: "))
        dinero = float(input("Ingrese la cantidad de dinero: "))

        if not (1 <= puntos_habilidad <= 100):
            raise ValueError("Los puntos de habilidad deben estar entre 1 y 100.")
        
        clase = int(input("Elija la clase del aventurero: 1-Guerrero, 2-Mago, 3-Ranger: "))
        
        match clase:
            case 1:
                fuerza = int(input("Ingrese la fuerza del guerrero (1-100): "))
                if not (1 <= fuerza <= 100):
                    raise ValueError("La fuerza debe estar entre 1 y 100.")
                aventurero = Guerrero(nombre, id_unico, puntos_habilidad, experiencia, dinero, fuerza)
            case 2:
                mana = int(input("Ingrese el mana del mago (1-1000): "))
                if not (1 <= mana <= 1000):
                    raise ValueError("El mana debe estar entre 1 y 1000.")
                aventurero = Mago(nombre, id_unico, puntos_habilidad, experiencia, dinero, mana)
            case 3:
                tiene_mascota = input("¿Tiene mascota? (S/N): ").upper()
                mascota = None
                if tiene_mascota == "S":
                    nombre_mascota = input("Ingrese el nombre de la mascota: ")
                    puntos_habilidad_mascota = int(input("Ingrese los puntos de habilidad de la mascota (1-50): "))
                    if not (1 <= puntos_habilidad_mascota <= 50):
                        raise ValueError("Los puntos de habilidad de la mascota deben estar entre 1 y 50.")
                    mascota = Mascota(nombre_mascota, puntos_habilidad_mascota)
                aventurero = Ranger(nombre, id_unico, puntos_habilidad, experiencia, dinero, mascota)
            case _:
                raise ValueError("Clase no válida.")
        
        gremio.append(aventurero)
        print(f"Aventurero {nombre} registrado.")
    
    except ValueError as e:
        print(f"Error: {e}")

def registrar_mision():
    """Función para registrar una misión"""
    try:
        nombre = input("Ingrese el nombre de la misión: ")
        rango = int(input("Ingrese el rango de la misión (1-5): "))
        recompensa = float(input("Ingrese la recompensa: "))
        es_grupal = input("¿Es misión grupal? (S/N): ").upper()
        
        if es_grupal == "S":
            min_miembros = int(input("Ingrese el mínimo de miembros para la misión: "))
            mision = Mision(nombre, rango, recompensa, True, min_miembros)
        else:
            mision = Mision(nombre, rango, recompensa, False)

        if not (1 <= rango <= 5):
            raise ValueError("El rango debe estar entre 1 y 5.")
        
        misiones.append(mision)
        print(f"Misión {nombre} registrada")
    
    except ValueError as e:
        print(f"Error: {e}")

def realizar_mision():
    """Función para realizar una misión"""
    try:
        nombre_mision = input("Ingrese el nombre de la misión a realizar: ")
        mision = next((m for m in misiones if m.nombre == nombre_mision), None)
        
        if not mision:
            raise ValueError("Misión no encontrada.")
        
        aventureros_participantes = []
        while True:
            id_aventurero = int(input("Ingrese el ID del aventurero: "))
            aventurero = next((a for a in gremio if a.id_unico == id_aventurero), None)
            if aventurero:
                aventureros_participantes.append(aventurero)
            else:
                print("Aventurero no encontrado.")
            
            continuar = input("¿Registrar otro aventurero? (S/N): ").upper()
            if continuar == "N":
                break

        if mision.es_grupal and len(aventureros_participantes) < mision.min_miembros:
            raise ValueError("No hay suficientes aventureros para la misión grupal.")

        for aventurero in aventureros_participantes:
            if aventurero.calcular_habilidad_total() < mision.rango * 20:
                raise ValueError(f"El aventurero {aventurero.nombre} no cumple con el rango de la misión.")
        
        mision.completar_mision()
        recompensa_por_aventurero = mision.recompensa / len(aventureros_participantes)
        
        for aventurero in aventureros_participantes:
            aventurero.incrementar_dinero(recompensa_por_aventurero)
            aventurero.incrementar_experiencia(mision.rango * 10)
            aventurero.incrementar_misiones_completadas()

        print(f"Misión {nombre_mision} completada.")
    
    except ValueError as e:
        print(f"Error: {e}")

def consultar_aventureros_misiones():
    """Función que muestra el Top 10 aventureros con más misiones completadas"""
    top_aventureros = sorted(gremio, key=lambda a: (-a.misiones_completadas, a.nombre))[:10]
    for aventurero in top_aventureros:
        print(f"{aventurero.nombre}: {aventurero.misiones_completadas} misiones completadas")

def consultar_aventureros_habilidad():
    """Función que muestra el Top 10 aventureros con mayor habilidad"""
    top_aventureros = sorted(gremio, key=lambda a: (-a.calcular_habilidad_total(), a.nombre))[:10]
    for aventurero in top_aventureros:
        print(f"{aventurero.nombre}: Habilidad total {aventurero.calcular_habilidad_total()}")

def consultar_misiones_recompensa():
    """Función que muestra el Top 5 misiones con mayor recompensa"""
    top_misiones = sorted(misiones, key=lambda m: -m.recompensa)[:5]
    for mision in top_misiones:
        print(f"{mision.nombre}: Recompensa {mision.recompensa}")

def menu_principal():
    """Menú principal del simulador de gremio de aventureros"""
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar aventurero")
        print("2. Registrar misión")
        print("3. Realizar misión")
        print("4. Otras consultas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                registrar_aventurero()
            case "2":
                registrar_mision()
            case "3":
                realizar_mision()
            case "4":
                menu_consultas()
            case "5":
                print("Saliendo... Muchas Gracias por Jugar")
                break
            case _:
                print("Opción no válida, por favor seleccione otra.")
