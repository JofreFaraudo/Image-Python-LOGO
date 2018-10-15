# Importem les llibreries
from PIL import Image
from os import path as math
import math as path

# Importem la imatge
fitxer = math.join('Images','image1.png')
img = Image.open(fitxer)

# Canviem la mida de la imatge a 400px de 
newidth = 400
width, height = img.size
newheight = height - (width - newidth)
img = img.resize((newidth, newheight), Image.NEAREST)

# Canviem la imatge a 16 colors
img = img.convert('P', palette=Image.ADAPTIVE, colors=16)

# Recorrem cada pixel de la imatge
pixel = img.load()
for j in range(newidth):
	for i in range(newheight):
		print "x: " + str(i) + " y: " + str(j) + " Val: " + str(pixel[j,i])

# Mostrem la imatge
img.show()