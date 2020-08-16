
class Operaciones:

    def __init__(self, var_1, var_2):
        self.var_1 = var_1
        self.var_2 = var_2

    def suma(self,var_1,var_2,):
        
        print(f'la suma de {var_1} + {var_2} es igual a {var_1 + var_2}')


    def resta(self,var_1,var_2):
 
        print(f'la resta de {var_1} - {var_2} es igual a {var_1 - var_2}')


if __name__ == "__main__":
    
    var_1=int(input("escribe un numero: "))
    var_2=int(input("escribe un numero: "))
    operaciones = input(""" que oprecion vas a ralizar:
    1 suma 
    2 resta
    """)
    if operaciones == "1":
        operaciones = Operaciones(var_1,var_2)
        operaciones.suma(var_1,var_2)
    elif operaciones == "2":
        operaciones = Operaciones(var_1,var_2)
        operaciones.resta(var_1,var_2)
    else:
        print('opción incorrecta ')


