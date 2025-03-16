class A:
    def hablar(self):
        print("Hola Desde A")
class F(A):
            
    def hablar(self):
        print("Hola Desde F")


class B(A):
            
    def hablar(self):
        print("Hola Desde B")
        
        
class C(F):
            
    def hablar(self):
        print("Hola Desde C")
class D(B,C):
            
    def hablar(self):
        print("Hola Desde D")
         

d = D()

C.hablar(d)
