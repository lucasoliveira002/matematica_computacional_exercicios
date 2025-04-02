conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

interseccao = set()  

for elemento in conjunto_a:
    if elemento in conjunto_b:
        interseccao.add(elemento)
print("Interseção:", interseccao)