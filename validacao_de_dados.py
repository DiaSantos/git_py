def valide_nome(nome):
    return len(nome) > 3

def valide_idade(idade):
    return 0 <= idade <= 150

def valide_salario(salario):
    return salario > 0

def valide_sexo(sexo):
    return sexo.upper() in ['F','M']

def valide_estado_civil(estado_civil):
    return estado_civil.upper() in ['S','C','V','D']

def main():
    nome = input("Digite seu nome: ")
    while not valide_nome(nome):
        print("Informação invávilda, a mesma deve conter mais que 3 caracteres.")
        nome = input("Digite seu nome novamente:")
        
    idade = int(input("Digite sua idade: "))
    while not valide_idade(idade):
        print("Informação invávilda, digite novamente sua idade: ")
        idade = int(input("Digite sua idade novamente: "))
                    
    salario = float(input("Digite se salário: "))
    while not valide_salario(salario):
        print("Informação invávilda, digite novamente eu salario; ")
        salario = float(("Digite novamente seu salário: "))
        
    sexo = input("Digite o sexo, no formato F/M:")
    while not valide_sexo(sexo):
        print("Informação invávilda, digite novamente o sexo, no formato F/M:")
        sexo = input("Digite o sexo, no formato F/M:")
        
        
    estado_civil = input("Digite seu estado civil, no formato S/C/V/D: ")
    while not valide_estado_civil(estado_civil):
        print("Informação invávilda digite novamente seu estado civil: ")
        estado_civil = input("Digite estado civil, no formato S/C/V/D/: ")
        
        
    print("\nAs informações do cliente cadastrado são:")
    print("Nome: ", nome)
    print("idade: ", idade)
    print("Salário: ",'{:.2f}'.format(salario))
    print("Sexo: ",sexo)
    print("Estado civil: ", estado_civil)

if __name__ == "__main__":
    main()