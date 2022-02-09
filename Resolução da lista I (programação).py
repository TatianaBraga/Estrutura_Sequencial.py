                                                                         #Exercício Lista 1

'''

#1) Faça um programa que receba, via teclado, a base e a altura de um triângulo e calcule sua área. Imprima o resultado na tela com 2 casas decimais.

b = float(input('Valor o comprimento da base do triângulo:'))
h = float(input('Valor da altura do triângulo:'))
área = b*h/2
print(f'A área de um triângulo de base {b} cm e altura {h} cm é igual a {área:.2f} cm^2 ')
'''


'''
# 2) Faça um programa que receba, via teclado, o raio de um círculo e calcule sua área e circunferência.
# Imprima os resultados na tela com 3 casas decimais. Considere π = 3.141592.

r = float(input('Valor do raio de um círculo é: '))   
π = 3.141592                       
a = π*((r))**2
c = 2*π*(r)
print(f' a área é: {a:.3f} cm**2 e circunferência é: {c:.3f} cm.')
'''


# 3)Faça um programa que receba, via teclado, o raio  de uma esfera e calcule seu volume e sua área superficial.
# Imprima os resultados na tela com 4 casas decimais. Considere π = 3.141592.
'''
r = float(input('Digite o valor do raio: ')) 
pi = 3.141592
v = 4/3*pi*(r**3)
a = 4*pi*(r**2)
print(f'volume é {v:.4f} cm^3; área surperficial é {a:.4f} cm^2.')
'''

# 4) Faça um programa que receba, via teclado, a altura e o raio da base de um cone e calcule seu volume.
# Imprima o resultado na tela com 4 casas decimais. Considere π = 3.141592.
'''
h = float(input('valor da altura do cone em cm:'))  #8 cm
r = float(input('raio do cone em cm:'))             #2.5 cm
pi = 3.141592
v = (pi*(r**2)*h)/3
print(f'volume do cone é igual a {v:.4f} cm^3.')    #52.3599
'''


# 5) Faça um programa que receba, via teclado, uma temperatura em graus Farenheit e a converta em graus Kelvin.
# Imprima o resultado na tela com 2 casas decimais, como mostrado no exemplo abaixo. 45.00 Fahrenheit = 280.37 Kelvin .
'''
F = float(input('temperatura em graus farenheit:')) # 37.00 graus
K = (F+459.67)/1.8                                     # 275,93
print(f'{F:.2f} Farenheit = {K:.2f} Kelvin.')
'''

#6) Faça um programa que receba, via teclado, uma temperatura em graus Rankine e a converta em graus Celsius.
# Imprima o resultado na tela com 1 casa decimal, como mostrado no exemplo abaixo. 645.2 Rankine = 85.3 Celsius.
'''
r = float(input('temeperatura em Rankine:')) #35
c = (r-491.67)/1.8                           #-253,706
pn1 = float(input('nota da prova 1:')) #7
n2 = float(input('nota da prova 2:')) #6
n3 = float(input('nota da prova 3:')) #8
n4 = float(input('nota da prova 4:')) #5
m = (n1 + n2 + n3 + n4)/4
print(f'média do aluno durante o bimestre foi de {m:.1f}')
'''

# 8) Faça um programa que receba, via teclado, um tempo em segundos (s) e uma distância em metros (m) e calcule a velocidade em quilômetros por hora (km/h).
# Imprima o resultado na tela com 1 casa decimal, como mostrado no exemplo abaixo. Velocidade = 30.5 km/h .
'''
t = float(input('Tempo (s):'))      # 3600 segundos
d = float(input('distância (m):'))  # 100 metros
D = d*0.001                          # 0.001 km
T= t/3600                           # 1 horas
Vm = (D/T)
print(f'velocidade = {Vm:.1f} km/h')
'''

# 9) Faça um programa que receba, via teclado, os catetos de um triângulo retângulo e calcule sua hipotenusa.
# Imprima o resultado na tela com 3 casas decimais, como mostrado no exemplo abaixo. Hipotenusa = 12.207.
'''
co = float(input('cateto oposto é igual:'))    # 4
ca = float(input('cateto adjacente é igual:')) # 6
h = (co**2 + ca**2)**0.5                       # 7.211
print(f'Hipotenusa = {h:.3f}. ')
'''

# 10) Faça um programa que receba, via teclado, 2 valores e calcule suas médias aritmética, aritmética ponderada, com pesos 7 e 3 para o primeiro
# e segundo valores respectivamente, geométrica e harmônica.Imprima os resultados na tela com 2 casas decimais, como mostrado no exemplo abaixo.
# Media aritmetica = 12.50 Media podenrada = 11.50 Media geometrica = 12.25 Media harmonica = 12.00
'''
n1 = float(input('Digite a nota 1:')) # 7
n2 = float(input('Digite a nota 2:')) # 6
mA = (n1 + n2)/ 2                     # 6.50
Ap = (7*n1 + 3*n2)/10                 # 6.70
mG = (n1*n2)**0.5                     # 6.48
mH = 2/(1/n1 + 1/n2)                  # 6.46
print(f'Média Aritimética = {mA:.2f}')
print(f'Média Ponderada = {Ap:.2f}')
print(f'Média Geométrica = {mG:.2f}')
print(f'Média Harmônica = {mH:.2f}')
'''

# 11) Faça um programa que receba, via teclado, o peso (em kg) e a altura (em cm) de uma pessoa, calcule e imprima na tela seu IMC (índice de massa corporal).
'''
p = float(input('Digite seu peso (em kg):'))  # 57
a= float(input('Digite sua altura (em cm):')) #172
IMC = p/(a**2)                                # 0.0019267171444023797
print(f'Seu índice de massa corporal é: {IMC}')
'''

# 12) Faça um programa que calcule e imprima na tela a distância entre dois pontos em coordenadas cartesianas tridimensionais.
# Cada ponto é um par ordenado (x, y, z).
'''
A = 2, 1, 3
B = 3, 5,2
Dab = ((3-2)**2 + (5-1)**2 + (2-3)**2)**0.5   # 4.2426
print(f'A distãncia entre os pontos A e B é: {Dab:.4f}.')
'''


# 13) Faça um programa que receba, via teclado, o valor de x e dos coeficientes a, b, c e d do polinômio cúbico P(x) = ax3 + bx2 + cx + d e calcule P(x).
# Imprima os resultados na tela com 4 casas decimais, como mostrado no exemplo abaixo. P(1.75) = −5.6406.
'''
a = float(input('Digite 0 valor do coeficiente a:')) # 1
b = float(input('Digiteo valor do coeficiente b:'))  # 2
c = float(input('Digiteo valor do coeficiente c:'))  # 3
d = float(input('Digiteo valor do coeficiente d:'))  # 1
x = float(input('Digite o valor de x:'))             # 2
P = a*x**3 + b*x**2 + c*x + d
print(f'P({x}) = {P:.4f}')
'''

# 14) Faça um programa que receba, via teclado, a quantidade de quilômetros percorridos por um carro alugado e o número de dias em que ele foi alugado.
# Calcule o preço a ser pago sabendo que o carro custa R$ 120, 00 por dia de aluguel mais R$ 0, 25 por km rodado. Imprima o resultado na tela.
'''
q = float(input('Digite os quilometros percorridos:')) # 13000
d = float(input('Digite a quantidade de dias:'))       # 5
p = 120*d + 0.25*q                                     # 3850 reais
print(f'O aluguel do carro custará {p:.2f} reais')
'''

# 15) Uma fábrica de camisetas produz três modelos: sport, polo e social; cada uma sendo vendido respectivamente por R$ 18,25, R$ 25,70 e R$ 33,85.
# Faça um programa em que o usuário forneça a quantidade de camisetas de cada modelo pedidas e este informe o valor arrecadado na venda.
'''
sp = float(input('Digite a quantidade de pedidos para a camisas modelo sport:')) # 23
p = float(input('Digite a quantidade de pedidos para a camisas modelo polo:'))   # 20
s = float(input('Digite a quantidade de pedidos para a camisas modelo social:')) # 34
T = 18.25*sp + 25.70*p +33.85*s                                                  # 2084.65
print(f'Valor arrecadado na venda das camisas foi de {T:.2f} reais')
'''

# 16) Seja v o valor arrecadado por uma loteria em um concurso, esta divide para seus ganhadores 70% desse valor.
# A importancia será dividida entre os três ganhadores da seguinte forma: o primeiro ganhador receberá 46%, o segundo receberá 32% e o terceiro receberá o restante.
# Faça um programa que receba, via teclado, o valor v arrecadado, calcule e imprima na tela quanto receberá cada um dos ganhadores e o lucro da loteria.
'''
v = float(input('Digite o valor arrecadado no concurso:')) # 500000
v1 = v*(70/100)                                            # 350000.0
g1 = v1*(46/100)                                           # 161000.00
g2 = v1*(32/100)                                           # 112000.00
g3 = v1*(22/100)                                           # 77000.00
g = v - v1                                                 # 150000.00
print(f'O valor a ser dividido entre os ganhadores será de:{v1:.2f}')
print(f'O primeiro ganhador levará:{g1:.2f}')
print(f'O segundo ganhador levará:{g2:.2f}')
print(f'O terceiro ganhador levará:{g3:.2f}')
print(f'Restará {g:.2f} reais de lucro para a loteria')
'''


# 17) Faça um programa para calcular os juros de uma aplicação bancária. O usuário deve informar o capital investido, C, a taxa de juros (ao mês), i, e o tempo de aplicação (em meses), t.
# Calcule o montante, M, ao final do investimento e juros acumulados no período, J.
# Utilize juros compostos nos cálculos. Imprima os resultados na tela, como mostrado no exemplo abaixo. Montante = 5634.13 R$ . Juros = 634.13 R$.

c = float(input('Digite o capital investido:'))  # 2000
i = float(input('Digite a taxa de juros:'))      # 0.5
t = float(input('Digite o tempo de aplicação:')) # 3
M = c*((1+i)**t)                                   # 6750.00
j = M-c                                          # 4750.00
print(f'Montante = {M:.2f} R$ ')
print(f'Juros = {j:.2f} R$ ')

