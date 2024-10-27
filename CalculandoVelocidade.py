'''
Nome: Clarissa
Data: 27/10/2024
'''

# Calcular-Velocidade-em-Python

velocidade = float(input ('Digite a Velocidade que o carro está: '))

if velocidade < 80:
    print ('velocidade abaixo da via')
    print ('aumente para 80km/h')
elif  80 <= velocidade <= 100:
    print ('velocidade permitida')
else:
    print ('velocidade está acima da Velocidade permitida')