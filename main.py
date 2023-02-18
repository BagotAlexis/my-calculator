def sum(n1=0, n2=0):
	return n1 + n2

def sub(n1=0, n2=0):
	return n1 - n2

def div(n1, n2):
	return n1 // n2

def pow(2, n2):
	return n1 * n2

fonction = str(input("entrez l'oppération que vous voulez effectuer : sum / sub / div / pow : "))

nombre1 = int(input("1er nombre : "))
nombre2 = int(input("2nd nombre : "))

if fonction == "sum":
	print(f"{nombre1} + {nombre2} =  {sum(nombre1, nombre2)}")
elif fonction == "sub":
	print(f"{nombre1} - {nombre2} = {sub(nombre1, nombre2)}")
elif fonction == "div":
	print(f"{nombre1} % {nombre2} = {div(nombre1, nombre2)}")
else:
	if  fonction == "pow":
		print(f"{nombre1} * {nombre2} = {pow(nombre1, nombre2)}")

