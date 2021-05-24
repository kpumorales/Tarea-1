
def esPalindroma(texto):
	texto =  texto.replace(" ","")
	return texto== texto[::-1]


print(esPalindroma(input('Escriba la palabra: ')))