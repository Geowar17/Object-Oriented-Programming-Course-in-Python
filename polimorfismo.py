class Gato():
    def sonido (self):
        return "Miau"
    
class Perro():
    def sonido (self):
        return "Guau"
    
    
gato= Gato()
perro= Perro()

#print(perro.sonido())
def recorrer(elemento):
    for item in elemento:
        print(f"el elemento actual es: {item}")

lista1= [1,2,3,4]
lista2= ["uno","dos","tres","cuatro"]

recorrer(lista2)