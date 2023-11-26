
valor_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcular o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Calcular os descontos
imposto_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto

sindicato = 0.05 * salario_bruto

# Calcular o salário líquido
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

# Exibir os resultados
print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto Imposto de Renda (11%): R$ {imposto_renda:.2f}")
print(f"Desconto INSS (8%): R$ {inss:.2f}")
print(f"Desconto Sindicato (5%): R$ {sindicato:.2f}")
print(f"\nSalário Líquido: R$ {salario_liquido:.2f}")