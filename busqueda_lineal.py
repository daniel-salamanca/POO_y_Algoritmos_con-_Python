import random, time

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: #O(n)
        if elemento == objetivo:
            match =True
            break
    
    return match


if __name__ == "__main__":
    tamano_de_lista = int(input('de que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista) ]

    comienzo = time.time()
    encontrado =busqueda_lineal(lista, objetivo)
    final = time.time()
    print(final - comienzo) 
    
    print(lista)
    print(f'elemento {objetivo} { "esta"if encontrado else "no esta"} enla lista')