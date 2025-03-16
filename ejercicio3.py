
class Animal():
   def comer(self):
       
       print("puedo comer")
       
class Mamifero(Animal):
    
    def amamantar(self):
       print("puedo amamantar")
    
class  Ave(Animal):
    
    def volar(self):
        
        print("puedo volar")
        
class Murcialago(Mamifero,Ave):
    
    pass

murcielago= Murcialago()
murcielago.comer()
murcielago.amamantar()
murcielago.volar()
    
    

       