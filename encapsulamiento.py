class Persona:
    def __init__(self, nombre,edad):
        self._nombre= nombre
        self._edad= edad
        
    def get_nombre(self):
        return self._nombre
                                   #realizando operaciones con getters

    def set_nombre(self, new_nombre):
        
        self._nombre = new_nombre
                                    #realizando operaciones con setters
dalto= Persona("lucas",21)

nombre= dalto.get_nombre()
print(nombre)

dalto.set_nombre("pepito")
nombre = dalto.get_nombre()
print(nombre)

