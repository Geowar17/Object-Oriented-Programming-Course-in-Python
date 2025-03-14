
class Celular():
    
    def __init__(self, marca, modelo, camara):
      
      self.marca= marca
      self.modelo= modelo
      self.camara= camara
      
    def llamar(self):
    
        print(f'estas haciendo un llamado desde un : {self.modelo}')
         
    def cortar(self):
        
        print(f'cortaste la llamada desde tu: {self.modelo}')

celular1 = Celular( "samsung" , "s23", "48MP")
celular2 = Celular ("Apple", "Iphone 15 Pro", "96MP")

celular1.llamar()