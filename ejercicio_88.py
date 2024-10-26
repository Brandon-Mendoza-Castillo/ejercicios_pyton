
from num2words import num2words

def numero_a_texto(numero):
    return num2words(numero, lang='es')

print(numero_a_texto(1234))
