import time

#1° Aqui o progama vai te perguntar quanto o funcionário recebe por mes
salariomensal = float(input("Qual o valor do salario recebido mensalmente pelo funcionário(a)? "))
#2° Aqui o progama vai perguntar quantas horas o funcionário trabalha por dia
horastrabalhadas = float(input("Quantas horas o(a) funcionário(a) trabalha mensalmente? "))
#3° Aqui o a variavel de soma do valor final, que é salario divido por horas trabalhadas mensalmente é definido
valorhora = salariomensal/horastrabalhadas
#4° Aqui você tera o seu resultado de quanto o funcionário recebe por hora
print(("O valor recebido por hora trabalhada é ", valorhora))
time.sleep (1000000)