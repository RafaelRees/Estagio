def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)
diagonalEsquerda = 0
diagonalDireita = 0

L = int(input("Informe o número de linhas/colunas: "))

matriz = []
for i in range(L):
    linha = []
    for j in range(L):
        elemento = input("Elemento da linha {} e coluna {}: ".format(i,j))
        linha.append(int(elemento))
    matriz.append(linha)
for i in range(L):
    for j in range(L):
        if i == j:
            diagonalEsquerda += matriz[i][j]
for i in range(L):
    for j in range(L):
        if i+j == L-1:
            diagonalDireita += matriz[i][j]
          
exibir_matriz(matriz)

print('Diagonal Esquerda: ', diagonalEsquerda) 
print('Diagonal Direita: ',diagonalDireita)    
print('Saída: ', abs(diagonalEsquerda - diagonalDireita)) 