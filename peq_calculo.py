npintura =float(input("por favor, informe qual a metragem a ser pintada?"))

total_latas = npintura // 54
valor_total = total_latas * 80
 
if npintura == 1 <= 54:
    
    print("O total de latas são : ",'{:.0f}'.format(total_latas),"latas de tintas")
    print("E o valor a ser pago é: R$ ",'{:.2f}'.format(valor_total))

else :
    total_latas = (npintura //54 )+1
    valor_total = total_latas * 80
       
    print("O total de latas são : ",'{:.0f}'.format(total_latas),"latas de tintas")
    print("E o valor a ser pago é: R$ ",'{:.2f}'.format(valor_total))