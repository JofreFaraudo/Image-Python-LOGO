# Importem les llibreries
from PIL import Image
from os import path, listdir, mkdir as newdir

# Creem fitxer de sortida, amb el nom introduit per a l'usuari, i hi posem les comandes basiques
name = raw_input("Si et plau, introduiex el nom del fitxer de sortida (Es desar"+chr(133)+" a la carpeta de \"Codes\"): ").encode("cp1252")
if not path.isdir('Codes'):
	newdir("Codes")
while len(name) < 1 or "/" in name or "\\" in name or "|" in name or "*" in name or ":" in name or "<" in name or ">" in name or "\"" in name or "?" in name:
	name = raw_input("El nom intrudu"+chr(139)+"t no "+chr(130)+"s v"+chr(133)+"lid. Torna-ho a intentar: ").encode("cp1252")
out = open(name+".lgo","w" if path.exists(name+".lgo") else "a")
out.write("rt 180 setpensize 1")

# Importem la imatge
print "Seleccioni una imatge (Les imatges han de ser png i est ubicades a la carpeta de \"Images\"): \n"
files = listdir("Images")
restador = 0
for f in range(len(files)):
	f -= restador
	if files[f].split(".")[-1] == "png":
		print "\t" + chr(175) + " " + str(f) + " -> " + files[f]
	else:
		files.remove(files[f])
		restador += 1
if len(files)==0:
	print "\t" + chr(175) + "No hi ha imatges disponibles" + chr(174)
	exit()
source = raw_input("\nIntrodueix el nom, amb o sense extensi"+chr(162)+", de la imatge o el seu n"+chr(163)+"mero: ")
try:
	source = str(source)
except:
	print "w"
if ".png" not in source:
	source += ".png"
fitxer = path.join('Images',source)
img = Image.open(fitxer)

# Canviem la mida de la imatge a 400px
newidth = 500 
width, height = img.size
newheight = height - (width - newidth)
img = img.resize((newidth, newheight), Image.NEAREST)

# Canviem la imatge a 16 colors
img = img.convert('P', palette=Image.ADAPTIVE, colors=16)

# Recorrem cada pixel de la imatge
pixel = img.load()
for j in range(newidth):
	# Inicialitzem variable per al color, zero es cap
	actualcolor = 0
	# Movem la tortuga al lloc desitjat
	out.write("\nsetxy " + str(j) + " 0")
	for i in range(newheight):
		if actualcolor != pixel[j,i]+1:
			if actualcolor != 0:
				out.write("\ncolor " + str(actualcolor) + "\nfd " + str(length))
			actualcolor = pixel[j,i]+1
			length = 1
		else:
			length += 1
	out.write("\ncolor " + str(actualcolor) + "\nfd " + str(length))