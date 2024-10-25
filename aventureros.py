#Clase abstracta aventurero
from abc import ABC, abstractmethod
class Aventurero(ABC):
    def __init__(self, nombre: str, id: int, puntos_de_habilidad: int, experiencia: int, dinero: float): #Tipos de variables esperadas
        self.nombre=nombre
        self.id=id
        self.puntos_de_habilidad=puntos_de_habilidad
        self.experiencia=experiencia
        self.dinero=dinero

    def __str__(self):
        return (f"{self.__class__.__name__}({self.nombre}, ID: {self.id}, "
                f"Habilidad: {self.puntos_de_habilidad}, Experiencia: {self.experiencia}, "
                f"Dinero: {self.dinero:.2f})")
    
    @abstractmethod
    def calcular_habilidad_total(self):
        pass

class Guerrero(Aventurero): #La clase guerrero hereda el nombre, id, puntos de habilidad, experiencia y dinero de la clase Aventurero
    def __init__(self, nombre: str, id: int, puntos_de_habilidad: int, experiencia: int, dinero: float, fuerza:int ): #Agrego el atributo fuerza
        super().__init__(nombre, id, puntos_de_habilidad, experiencia, dinero)  # Llamo al constructor de la clase base, Aventurero
        if not (1 <= fuerza <= 100): #Me aseguro que la fuerza sea un valor entre 1 y 100, lanzo un error si no lo es
            raise ValueError("La fuerza debe estar entre 1 y 100.")
        self.fuerza = fuerza

    def __str__(self):
        return super().__str__() + f", Fuerza: {self.fuerza}"

  
    def calcular_habilidad_total(self): #Calculo de puntos de habilidad para hacer el top 10 aventureros con mayor habilidad
        return self.puntos_de_habilidad + self.fuerza / 2
    


class Mago(Aventurero): #La clase mago hereda el nombre, id, puntos de habilidad, experiencia y dinero de la clase Aventurero
    def __init__(self, nombre: str, id: int, puntos_de_habilidad: int, experiencia: int, dinero: float, mana:int ): #Agrego el atributo mana
        super().__init__(nombre, id, puntos_de_habilidad, experiencia, dinero)  # Llamo al constructor de la clase base, Aventurero
        if not (1 <= mana <= 1000): #Me aseguro que el mana sea un valor entre 1 y 1000, lanzo un error si no lo es
            raise ValueError("El mana debe estar entre 1 y 1000.")
        self.mana=mana
    
    def __str__(self):
        return super().__str__() + f", Mana: {self.mana}"
    

    def calcular_habilidad_total(self): #Calculo de puntos de habilidad para hacer el top 10 aventureros con mayor habilidad
        return self.puntos_de_habilidad + self.mana/100


class Mascota:
    def __init__(self, nombre: str, puntos_de_habilidad: int):
        self.nombre = nombre
        # Validar el valor de puntos de habilidad
        if not (1 <= puntos_de_habilidad <= 50):
            raise ValueError("Los puntos de habilidad de la mascota deben estar entre 1 y 50.")
        self.puntos_de_habilidad = puntos_de_habilidad

class Ranger(Aventurero):
    def __init__(self, nombre: str, id: int, puntos_de_habilidad: int, experiencia: int, dinero: float,  mascota: Mascota = None): #La clase Ranger has-a clase mascota
        super().__init__(nombre, id, puntos_de_habilidad, experiencia, dinero)
        self.mascota = mascota
    
    def __str__(self):
        mascota_info = f", Mascota: {self.mascota.nombre}, Habilidad: {self.mascota.puntos_de_habilidad}" if self.mascota else ""
        return super().__str__() + mascota_info
    
   
    def calcular_habilidad_total(self): #Calculo de puntos de habilidad para hacer el top 10 aventureros con mayor habilidad
        if self.mascota:
            return self.puntos_de_habilidad + self.mascota.puntos_de_habilidad
        else:
            return self.puntos_de_habilidad
        
        


    