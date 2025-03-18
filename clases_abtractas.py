from abc import ABC, abstractmethod

class Persona(ABC):
    
    @abstractmethod
    def __init__(self, nombre, edad, sexo,actividad):
        
        self.nombre= nombre
        self.edad= edad
        self.sexo= sexo
        self.actividad= actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        
        print(f"Estoy estudiando: {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        
        print(f"actualmente estoy trabajando en el rubro de: {self.actividad}")
        
        
pedrito = Estudiante("pedrito",21,"masculino","programacion")
dalto = Trabajador("lucas",25,"masculino","programador")

dalto.presentarse()
dalto.hacer_actividad()
pedrito.presentarse()
pedrito.hacer_actividad()