cantidad = int(input('Cuantos personas vamos a utilizar?: '))
print('')

lista = []
for i in  range(cantidad):
	nombre = input("escriba el nombre: ")
	edad = int(input("escriba la edad: "))
	lista.append({'nombre':nombre,'edad':edad})

lista = sorted(lista, key = lambda i: i['edad'],reverse=True)
print('el mayor es: ',lista[0]['nombre'], ' y tiene: ',lista[0]['edad'],' años')