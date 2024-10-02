import sympy as sp 

def main():
    x=10 # valor inicial de x
    learning_rate = 0.1 # tasa de aprendizaje == learning_rate controla el tamaño de pasos que tendriamos en cada iteracion
    
    #Definir la funcion f(x) = x^2 --> funcion de costos
    def f(x):
        return x**2
    
    # derivada de la funcion f'(x)= 2x--->derivada de funcion de costos
    def df(x):
        return 2*x
    
    for _ in range(20):
        x=x-learning_rate*df(x) #actualizar x en la direccion opuesta al gradiente negativo
        print(f"x: {x}, f(x): {f(x)}")
if __name__ == "__main__":
    main()