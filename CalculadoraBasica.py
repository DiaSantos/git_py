
def calc():
    op =  input('Por favor selecione a operação dejejada: \n + para soma;\n - para subtração;\n * para multipicação; \n /para divisão;\n R:  ')

    numb1 = float(input("Insisira um numero: "))
    numb2 = float(input("Insisira um numero: "))

    if op ==  '+':
        print("{} + {}".format(numb1,numb2))
        print(numb1 + numb2)
    elif op ==  '-':
        print("{} - {}".format(numb1,numb2))
        print(numb1 - numb2)
    elif op ==  '*':
        print("{} * {}".format(numb1,numb2))
        print(numb1 * numb2)
    elif op ==  '/':
        print("{} / {}".format(numb1,numb2))
        print(numb1 / numb2)
    else:
        print("Operação inválida...")
calc()
def resp():
    calc_novamente = input("Deseja calcular novamente:\n Utilize 's' para sim e 'n' para não: ")
    if calc_novamente == 's':
        calc()
    elif calc_novamente == 'n':
        print("Volte sempre!!")
resp()

#     if calc_novamente == 'y':
#         calc()
#     elif calc_novamente == 'n':
#         print("Até a próxima!!!")
# resp()
