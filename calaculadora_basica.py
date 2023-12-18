import os

cls = lambda : os.system('cls')

def calc():
    while True:
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
            continue
        novamente = input("Deseja realizar outro cálculo? (s/n): ")
        if novamente.lower() != 's':
            break
if __name__ =="__main__":
    calc()
cls()
