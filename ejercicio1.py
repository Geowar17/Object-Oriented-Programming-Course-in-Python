class Estudiante:
    def __init__(self,nombre, edad,grado):
        
        self.nombre= nombre
        self.edad= edad
        self.grado= grado
    
    def estudiar (self):
        print("estudiando.......")
                
nombre = input("digame su nombre: ")
edad = input("ahora su edad: ")
grado = input("por ultimo, su grado: ")
    
estudiante = Estudiante(nombre, edad, grado)

print (f"""
       
       DATO DEL ESTUDIANTE: \n\n
       Nombre: {estudiante.nombre}\n
       Edad: {estudiante.edad}\n
       grado: {estudiante.grado}\n
    
       
       """)

while True:
   estudiar= input()

   if (estudiar.lower() =="estudiar" ):
    
    estudiante.estudiar()
    