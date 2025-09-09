Determinantes - Laplace ( n ≥ 4 )

Escreva um programa em Python que leia uma matriz quadrada de ordem n ≥ 4 e calcule automaticamente o seu determinante pelo método de Laplace (expansão por cofatores), expandindo sempre pela primeira linha. Não use bibliotecas externas (NumPy).

    Apenas números inteiros.
    O cálculo deve ser feito recursivamente:
        2×2: caso básico → ad - bc;
        3×3: Regra de Sarrus;
        n≥4: expansão por cofatores na primeira linha, chamando recursivamente.

Regras

    Se n < 4, imprima exatamente:
    Ordem inválida. A matriz deve ser de ordem >= 4.
    Para cada linha i, se a quantidade de valores for diferente de n, imprima:
    Erro: você digitou K valores. A linha deve conter exatamente n valores.
    e repita a leitura dessa linha.
    Se algum valor não for inteiro:
    Erro: digite apenas números inteiros.
    e repita a leitura dessa linha.

Prompts obrigatórios

    Digite a ordem n da matriz:
    Para cada linha i (começando em 1):
    Digite os n valores da linha i, separados por espaço:

Saída

ordem=n
det=VALOR

Para ordem inválida, apenas a mensagem indicada.