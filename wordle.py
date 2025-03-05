import random
ListaPalabras=["nariz","casco","mango"]
intentos=5
class Colors:
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
ENDC = '\033[0m'
def verde (pos):
return Colors.OKGREEN+pos+Colors.ENDC
def azul (pos):
return Colors.OKBLUE+pos+Colors.ENDC
resp="S"
while resp.upper()=="S":
num =random.randint(0,(len(ListaPalabras)-1))
sol=(ListaPalabras[num])
print("REGLAS:")
print("1- Si la letra se muestra de color verde es correcta")
print("2- Si la letra se muestra en color azul, la letra está dentro de la palabra pero en la posición incorrecta")
print("3- Si la letra no está coloreada significa que la letra no se encuentra en la palabra")
print("4- Tienes 5 intentos")
print("")
for i in range (intentos):
ListaPalabra=[]
ListaSol=[]
print("")
palabra=input("Dame una palabra de 5 letras: ")
print("")
whilenot (len(palabra)==5):
palabra=input("La palabra debe contener 5 letras: ")
if sol==palabra:
break
else:
for i in palabra:
ListaPalabra.append(i)
for i in sol:
ListaSol.append(i)
for i in range (len(ListaPalabra)):
if ListaPalabra[i] in ListaSol[i]:
print(verde(ListaPalabra[i]), end="")
ifnot ListaPalabra[i] in ListaSol:
print(ListaPalabra[i], end="")
elif ListaPalabra[i] in sol andnot (ListaPalabra[i] in ListaSol[i]):
print(azul(ListaPalabra[i]), end= "")
print("")
if palabra==sol:
print(verde(palabra))
print("La palabra es correcta")
else:
print("Se han acabado los intentos")
print("No has acertado")
resp=input("¿Quieres volver a jugar?(S/N)")
whilenot resp.upper() in ["S", "N"]:
resp=input("Introduce S o N: ")
print("Adiós")