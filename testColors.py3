# Importem les llibreries
from PIL import Image
from os import path, listdir, mkdir as newdir

# Creem fitxer de sortida, amb el nom introduit per a l'usuari, i hi posem les comandes basiques
name = input("Si et plau, introduiex el nom del fitxer de sortida (Es desar"+chr(133)+" a la carpeta de \"Codes\"): ")
if not path.isdir('Codes'):
	newdir("Codes")
while len(name) < 1 or "/" in name or "\\" in name or "|" in name or "*" in name or ":" in name or "<" in name or ">" in name or "\"" in name or "?" in name:
	name = input("El nom intrudu"+chr(139)+"t no "+chr(130)+"s v"+chr(133)+"lid. Torna-ho a intentar: ")
out = open(path.join("Codes",name+("" if name[-4:-1]+name[-1] == ".lgo" else ".lgo")),"w" if path.exists(name+".lgo") else "a")
out.write("rt 180 setpensize 10")

# Importem la imatge, si no n'hi ha, reportem el problema
if not path.isdir('Images'):
	newdir("Images")
print("Seleccioni una imatge (Les imatges han de ser png i est ubicades a la carpeta de \"Images\"): \n")
files = listdir("Images")
restador = 0
for f in range(len(files)):
	f -= restador
	if files[f].split(".")[-1].lower() in ["png", "jpg", "jpeg"]:
		print("\t" + chr(175) + " " + str(f) + " -> " + files[f])
	else:
		files.remove(files[f])
		restador += 1
if len(files)==0:
	print("\t" + chr(175) + "No hi ha imatges disponibles" + chr(174))
	exit()
source = input("\nIntrodueix el nom, amb o sense extensi"+chr(162)+", de la imatge o el seu n"+chr(163)+"mero: ")
try:
	source = int(source)
	try:
		source = files[source]
	except:
		print("El fitxer no existeix")
		exit()
except:
	if ".png" not in source:
		source += ".png"
if source not in files:
	print("El fitxer no existeix")
	exit()
fitxer = path.join('Images',source)
img = Image.open(fitxer)

# Canviem la mida de la imatge a 400px
newidth = 50
width, height = img.size
newheight = height - (width - newidth)
img = img.resize((newidth, newheight), Image.NEAREST)

# Canviem la imatge a RGB
img = img.convert('P', palette=Image.ADAPTIVE, colors=50)
img = img.convert('RGB')

# Recorrem cada pixel de la imatge
pixel = img.load()
for j in range(newidth):
	# Inicialitzem variable per al color
	actualcolor = None
	# Movem la tortuga al lloc desitjat
	out.write(" setxy " + str(j*10) + " 0")
	for i in range(newheight):
		#print(pixel[j,i]);
		if actualcolor != pixel[j,i]:
			if actualcolor is not None:
				out.write(" color " + str(list(actualcolor)).replace(",", "") + " fd " + str(length*10)) # The list format is the one that Logo requires (With [] instead of ()). The program also romves commas (Logo does not want them)
			actualcolor = pixel[j,i]
			length = 1
		else:
			length += 1
	out.write(" color " + str(list(actualcolor)).replace(",", "") + " fd " + str(length*10)) # The same as the before print - See comment