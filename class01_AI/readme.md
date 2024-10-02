### Matematicas basicas para inteligencia artificial

### Vectores: 
Un vector es un arreglo uni-dimensional de numero.

### Ejemplo:
´´´
import numpy as np

# Crear un vector
v = np.array([1, 2, 3, 4, 5])

' ' ' python
x = 10 
learning_rate = 0.1

def f(x):
   return x**2
def df (x):
   return 2*x
# gradiente descendiente
for _ in range(20):
    x=x-learning_rate * df(x)
    print(f"x: {x}, f(x): {f(x)"})