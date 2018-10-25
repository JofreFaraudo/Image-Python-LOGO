 # Importem les llibreries
from PIL import Image
from os import path as math
import math as path

# Creem fitxer de sortida i hi posem les comandes basiques
out = open("jaloiun.lgo","a")
out.write("rt 90 setpensize 1")

# Importem la imatge
fitxer = math.join('Images','jalouin.png')
img = Image.open(fitxer)

# Canviem la mida de la imatge a 400px
newidth = 200 
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
	out.write("\nsetxy 0 " + str(j))
	for i in range(newheight):
		if actualcolor != pixel[j,i]:
			if actualcolor != 0:
				out.write("\ncolor " + str(actualcolor) + "\nfd " + str(length*2))
			actualcolor = pixel[j,i]
			length = 1
		else:
			length += 1
		#out.write(" setxy " + str(j) + " " + str(i) + " color " + str(16-pixel[j,i]) + " fd 1")