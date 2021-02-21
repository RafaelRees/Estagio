elemento = int(input('Digite a quantidade de elementos da lista: '))
k = int(input('Digite o valor que deseja utilizar para dividir a soma dos pares: '))
contador=0

lista=[]

for x in range(elemento):
    n = int(input('Digite os numeros desejados: '))
    lista.append(n)
for i in range(elemento):
    for j in range(elemento):
        if lista[i] < lista[j] and (lista[i] + lista[j])%k == 0:
            contador += 1

print ('Saída: ', contador)