
import random

number = random.randint(1, 100)  # O computador escolhe um número
tentativa = 0

while True:
    guess = input("Adivinhe um número entre 1 e 100: ")
    if not guess.isdigit(): 
        print("Por favor, insira um número válido.")
        continue

    guess = int(guess)
    tentativa += 1  

    if guess < number:
        print("Muito baixo! Tente novamente.")
    elif guess > number:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou em {tentativa} tentativas.")
        break