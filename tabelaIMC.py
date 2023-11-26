x = input("Digite seu nome: ")


print("Olá,"  + x + "!!!")
pes = float(input("Digite seu peso:  "))
    
print("Agora digite sua altura")
alt= float(input("digite sua altura é: "))
    
imc = (pes)/alt**2
#com {0:.2F}%'.format(imc) coloquei em formato de porcentagem e limitei o nº de casas decimais
print("seu imc é :",'{0:.2F}%'.format(imc))

#Usando as condicionais para cumprir a tabela do IMC e envia uma mensagem ao usuário          
if imc == 18.6 < 25:
    print("Parabéns, você chegou ao seu peso ideal!!!")
    
elif imc <= 29.9:
    print("Levemente acima do peso,atenção!!!")
        
elif imc <= 34.9:
    print("Cuidado você está com obesidade grau 1!!!")

elif imc <= 39.9:
    print("Precisa procurar ajuda profissional, obesidade grau 2!!!")
                               
elif imc >= 40:
     print("OBESIDADE MORBIDA!!!")
        
