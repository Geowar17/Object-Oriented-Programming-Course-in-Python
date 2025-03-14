class Persona: 
    
    def __init__(self, nombre, edad, nacionalidad):
        
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        
        print("hola, estoy hablando un poco")
        
class Artista:
    def __init__(self,habilidad):
        
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        
        return f"Mi habilidad es: {self.habilidad}"   
     
class EmpleadoArtista(Persona, Artista):
    
    def __init__(self,nombre,edad,nacionalidad,habilidad,empresa,salario):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario= salario
        self.empresa= empresa
      
    def presentarse(self):
        print( f'hola, soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo em {self.empresa}')    


roberto = EmpleadoArtista("Ronerto",49,"venezuela","cantar","google",1000000)


#print(roberto.edad)
#roberto.presentarse()

herencia = issubclass(EmpleadoArtista,Persona)
instancia = isinstance(roberto,Persona)

print(instancia)