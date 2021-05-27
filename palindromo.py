
import re

def esPalindroma(texto):
	texto = re.sub(r'[^\w\s]','',texto)
	texto2 = texto.lower()
	texto3 =  texto2.replace(" ","")
	return texto3== texto3[::-1]


print(esPalindroma(input('Escriba la palabra: ')))
