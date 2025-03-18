def decorador(funcion):
    
    def funcion_modificada():
        print("antes de llamar a la funcion")
        funcion()
        
    return funcion_modificada

# def saludo():
#     print("hola dalto como andas")
    
# saludo_modificado= decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("hola dalto como estas")
    

saludo()