import math

angulo = float(input('Digite o ângulo que você deseja: '))
angulo_em_radianos = math.radians(angulo)

seno = math.sin(angulo_em_radianos)
cosseno = math.cos(angulo_em_radianos)
tangente = math.tan(angulo_em_radianos)

print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'COSSENO de {cosseno:.2f}')
print(f'TANGENTE {tangente:.2f}')
