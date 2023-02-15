def sum(n1=0, n2=0):
	return n1 + n2

def sub(n1=0, n2=0):
	return n1 - n2

def div(n1, n2):
	return n1 // n2

def pow(n1, n2):
	return n1 * n2

fonction = str(input("entrez l'oppération que vous voulez effectuer : sum / sub / div / pow"))

nombre1 = int(input("1er nombre : "))
nombre2 = int(input("2nd nombre : "))

if fonction == sum:
	print(sum(nombre1, nombre2))
elif fonction == sub:
	print(sub(nombre1, nombre2))
elif fonction == div:
	print(div(nombre1, nombre2))
else fonction == pow:
	print(pow(nombre1, nombre2))

