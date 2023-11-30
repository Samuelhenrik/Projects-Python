import random
import string
letras = string.ascii_letters
numeros = string.digits
caracteres_especiais = string.punctuation
caracteres = letras + numeros
tamanho = 20
senha = ''.join(random.choice(caracteres) for i in range(tamanho))
print(f"senha:{senha}")