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
    diagonalEsquerda += matriz[i][i]

for i in range(L):
    diagonalDireita += matriz[i][L-1 - i]

exibir_matriz(matriz)

print('Diagonal Esquerda: ', diagonalEsquerda) 
print('Diagonal Direita: ',diagonalDireita)
print('Saída: ', abs(diagonalEsquerda - diagonalDireita))
