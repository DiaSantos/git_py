#calculo de média , tbm pode  ser adicionado 3 ou quatro notas

print("Olá, por favor insira os dados solicitados...")

#Foi feito tipo float , para inserção de valor decimal 
nota_1 = float(input('Por favor insira a 1ª nota: '))
nota_2 = float(input('Por favor insira a 2ª nota: '))

media = (nota_1 + nota_2) / 2 


# usei 2 "IF" para mostra que é possivel, mas tbm pode ser com "ELIF"
if media == 10:
    print("A média calculada é:{}",'{:.2f}'.format(media))
    print("Aluno foi aprovado!!!")

if media >= 7:
    print("A média calculada é:{}",'{:.2f}'.format(media))
    print("Aluno foi aprovado!!!")

    
else:
    print("A média calculada é:{}",'{:.2f}'.format(media))
    print("Aluno reprovado!!!")