# Determinante por Laplace (n >= 4)
# Prompts + leitura/validação. COMPLETE o bloco # TODO com a lógica do determinante.
# NÃO ALTEREM O BLOCO DE CÓDIGO EXISTENTE!!! Ele já é a base de entrada das matrizes
print("Digite a ordem n da matriz:")
n = int(input())

if n < 4:
    print("Ordem inválida. A matriz deve ser de ordem >= 4.")
else:
    matriz = []
    i = 0
    while i < n:
        print(f"Digite os n valores da linha {i+1}, separados por espaço:")
        partes = input().split()
        if len(partes) != n:
            print(f"Erro: você digitou {len(partes)} valores. A linha deve conter exatamente n valores.")
            continue
        linha = []
        ok = True
        for p in partes:
            try:
                linha.append(int(p))
            except ValueError:
                print("Erro: digite apenas números inteiros.")
                ok = False
                break
        if not ok:
            continue
        matriz.append(linha)
        i += 1

    # =========================
    # TODO: implementar o cálculo do determinante por Laplace (primeira linha)
    # - Para 2x2: ad - bc
    # - Para 3x3: Sarrus
    # - Para n>=4: expandir na primeira linha recursivamente
    #
    # Ao final, imprimir exatamente:
    # print(f"ordem={n}")
    # print(f"det={DET}")
    # =========================
    
    
    #Para ajudar estou dando um código base
    def det2(m2):
       a = matriz[0][0]
       b = matriz[0][1]
       c = matriz[1][0]
       d = matriz[1][1]
       
       det = (a*d)-(b*c)
        
    def det3(m3):
        # Calcula o determinante de uma matriz 3x3 usando loops
        det = 0
        # Sarrus: soma dos produtos das diagonais principais
        for i in range(3):
            prod = 1
            for j in range(3):
                prod *= m3[j][(i + j) % 3]
            det += prod
        # Sarrus: subtrai os produtos das diagonais secundárias
        for i in range(3):
            prod = 1
            for j in range(3):
                prod *= m3[j][(i - j) % 3]
            det -= prod
        return det
        # Faz o cálculo de 3x3 (Sarrus)

        #a=matriz[0][0]
        #b=matriz[0][1]
        #c=matriz[0][2]
        #d=matriz[1][0]
        #e=matriz[1][1]
        #f=matriz[1][2]
        #g=matriz[2][0]
        #h=matriz[2][1]
        #i=matriz[2][2]
        
        #det = -((g*e*c) + (h*f*a) + (i*d*b)) + ((a*e*i) + (b*f*g) + (c*d*h))
        
    def submatriz(matriz, linha_remover, coluna_remover):
        while n in linha and matriz != 3:
            for linha in matriz:
                del linha[0]
            del matriz[0]
        return matriz
    
    def laplace(matriz):
        # Determinante por Laplace sempre na 1ª linha.
        #Determinante por Laplace sempre na 1ª linha.
        #Casos base: 2x2 e 3x3.
        #Caso geral (n>=4): soma de cofatores da linha 0.

        #Primeiro faz o teste se a matriz é:
        # 2x2
        # det2(matriz2x2)
        # 3x3
        # det3(matriz3x3)
        
        # Faz o cálculo recursivo
        # LEMBREM-SE QUE SEMPRE USA A PRIMEIRA LINHA ENTÃO OS ELEMENTOS SÃO SEMPRE [0][Y]
        # "Reduzir" a matriz pela lógica do COFATOR retornando a nova matriz e assim ir passando a nova matriz recursivamente. 
        # O Loop chama sempre a própria função "laplace(SUB)"
        for n in matriz[0]:
            for linha in range(n):
                for coluna in range(n):
                    sub = submatriz(matriz, linha, coluna)
                    det += ((-1)**(0+coluna)) * n * laplace(sub)


        
        
            


    #base
    print(submatriz)
    #det = laplace(matriz)
    #print(f"ordem={n}")
    #print(f"det={det}")
