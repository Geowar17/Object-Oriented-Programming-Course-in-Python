

class Persona():
    def __init__ (self, nombre,edad):
    
        self.nombre = nombre
        self.edad= edad
        
    
    def hablar(self):
        
        print(f"mi nombre es ,{self.nombre} y mi edad es : {self.edad}")
        

class Estudiante(Persona):
    
    def __init__ (self, nombre,edad, grado): 
        
        Persona.__init__(self,nombre,edad)
        self.grado= grado
        
    def presentarse(self):
        
        print (f"mi nombre es ,{self.nombre} y mi edad es : {self.edad} y mi grado es :{self.grado}")
    

estudiante= Estudiante("geo",40,5)

estudiante.presentarse()
        
        
 

