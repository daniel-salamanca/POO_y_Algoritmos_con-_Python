
def morral (tamaño_morral, peso, valores, cantidad_de_objetos):
    
    if cantidad_de_objetos == 0 or tamaño_morral == 0:
        return 0

    if peso[cantidad_de_objetos - 1] > tamaño_morral:
        return morral(tamaño_morral, peso, valores, cantidad_de_objetos -1)
    
    return max(valores[cantidad_de_objetos - 1] + morral(tamaño_morral - peso[cantidad_de_objetos - 1], peso, valores, cantidad_de_objetos -1),
             morral(tamaño_morral, peso, valores, cantidad_de_objetos-1))


if __name__ == "__main__":

    cantidad_de_objetos = int(input("cuantos objetos hay ")) 
    valores = []
    peso = []
    i = 0
    tamaño_morral = 50
    
  
    while i <= cantidad_de_objetos - 1:
        valor_es=int(input(f'introdusca el valor del objeto {i+1} '))
        valores.append(valor_es)
        peso_es=int(input(f'introdusca el peso del objeto {i+1} '))
        peso.append(peso_es)
        i +=1

 
    resultado = morral(tamaño_morral, peso, valores, cantidad_de_objetos)
    print(resultado)

def multiply(a, b):
    
  a * b



