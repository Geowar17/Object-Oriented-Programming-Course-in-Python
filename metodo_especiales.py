class Persona:
    def __init__(self,nombre,edad):
        self.nombre= nombre
        self.edad= edad
    
    def __str__(self):
        return f'Persona nombre: {self.nombre}, edad= {self.edad})'
    
    def __repr__(self):
        
        return f'Persona ("{self.nombre}",{self.edad})'
    
    def __add__(self,otro):
        
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)

dalto = Persona("lucas",21)
pedro= Persona("pedro",30)

resultado= dalto + pedro

print(resultado.nombre)
