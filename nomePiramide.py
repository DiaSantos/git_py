def nome_piramide(nome):
    for i in range(1, len(nome) + 1):
        escada = nome[:i]
        print(escada)
nome = input("Digite um nome: ")
#chamando a função
nome_piramide(nome)

  