n1 = input('Digite o primeiro número')
n2 = input('Digite o segundo número')
n3 = input('Digite o terceiro número')

if n1 < n2 and n2 < n3 :
    print("O menor e o maior números são: {} e {}".format(n1,n3))

elif n2 > n3 and n3 > n1 :
    print("O menor e o maior números são: {} e {}".format(n1,n2))
    
elif n1 < n2 and n3 < n1 :
    print("O menor e o maior números são: {} e {}".format(n3,n2))




# tbm tem esta maneira de fazer que segue abaixo


# usado aqui um laço 'FOR' 
n = int(input("Digite N: "))
ma = 0
me = 0
for i in range(n):
   x = int(input("Digite um número: "))
   ma = ma if ma != 0 and ma >  x else x
   me = me if me != 0 and me < x else x

print ('O maior valor digitado foi {} e o menor foi {}'.format(ma,me))