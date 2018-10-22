 # Importem les llibreries
from PIL import Image
from os import path as math
import math as path

# Creem fitxer de sortida i hi posem les comandes basiques
out = open("code.lgo","a")
out.write("setpensize 1")

# Importem la imatge
fitxer = math.join('Images','image1.png')
img = Image.open(fitxer)
# Canviem la mida de la imatge a 400px
newidth = 32 
width, height = img.size
newheight = height - (width - newidth)
img = img.resize((newidth, newheight), Image.NEAREST)

# Canviem la imatge a 16 colors
img = img.convert('P', palette=Image.ADAPTIVE, colors=16)

# Recorrem cada pixel de la imatge
pixel = img.load()
for j in range(newidth):
	for i in range(newheight):
		out.write(" setxy " + str(j) + " " + str(i) + " color " + str(16-pixel[j,i]) + " fd 1")

		# Mostrem la imatge
img.show()
