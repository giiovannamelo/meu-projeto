import random

print("Bem vindo ao jogo de adivinhação!")
print("Estou pensando em um número de 1 a 100...")

numero_secreto = random.randint (1,100)
tentativas = 0

while true: 
try: 
palpite = int(input("digite seu palpite"))
tentativas += 1 

if palpite < 1 or palpite > 100:
  print ("o número precisa estar entre 1 e 100!!")
  continue

if palpite < numero_secreto: 
  print ("Tente um número maior")
if palpite > numero_secreto:
  print ("Tente um número maior")

else: 
  print(f"Parabéns, você acertou em {tentativas} tentativas")
  break

except ValueError:
print ("por favor, digite um número válido")
