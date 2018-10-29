# Importem les llibreries
from PIL import Image
from os import path

# Creem fitxer de sortida, amb el nom introduit per a l'usuari, i hi posem les comandes basiques
name = raw_input("Si et plau, introduiex el nom del fitxer de sortida (Es desar"+chr(133)+" a la carpeta de \"Codes\"): ").encode("cp1252")
while len(name) < 1 or "/" in name or "\\" in name or "|" in name or "*" in name or ":" in name or "<" in name or ">" in name or "\"" in name or "?" in name:
	name = raw_input("El nom intrudu"+chr(139)+"t no "+chr(130)+"s v"+chr(133)+"lid. Torna-ho a intentar: ").encode("cp1252")
if path.exists(name+".lgo"):
	out = open("jaloiun.lgo")
else:
	out = open("jaloiun.lgo","a")
out.write("rt 180 setpensize 1")

# Importem la imatge
print "Seleccioni una imatge: (Les imatges han de ser png i est ubicades a la carpeta de \"Images\"")os.listdir(".png")
fitxer = path.join('Images','jalouin.png')
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
