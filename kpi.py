# Solicitar o nome do usuario
nome = input('Qual o se nome ? : ')

#Solicitar o valor do salario
salario = float(input('Qual o valor do salario? : '))

# Solicitar o valor percentual do bonus
bonus = float(input('Qual o valor do seu bonus (%)? : '))

#Calculo do KPI
kpi = 1000 + salario * bonus

print(f'Ola {nome} o seu valor bonus foi de {kpi}')