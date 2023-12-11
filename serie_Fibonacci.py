#Fn = Fn - 1 + Fn - 2
print("Sequência Fibonacci será iniciada.")

#é uma série onde um número será sempre somado ao seu anterior 
x = int(input("Por favor,insira total de sequências: "))
ant = 0
prox = 1
soma = 1
for n in range(0,x):
    soma = prox + ant
    ant = prox
    prox = soma
    print(ant)