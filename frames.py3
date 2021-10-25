# Importem les llibreries
from PIL import Image
from os import path, listdir, mkdir as newdir
import copy

# Creem fitxer de sortida, amb el nom introduit per a l'usuari, i hi posem les comandes basiques
name = input("Si et plau, introduiex el nom del fitxer de sortida (Es desar"+chr(133)+" a la carpeta de \"Codes\"): ")
if not path.isdir('Codes'):
	newdir("Codes")
while len(name) < 1 or "/" in name or "\\" in name or "|" in name or "*" in name or ":" in name or "<" in name or ">" in name or "\"" in name or "?" in name:
	name = input("El nom intrudu"+chr(139)+"t no "+chr(130)+"s v"+chr(133)+"lid. Torna-ho a intentar: ")
out = open(path.join("Codes",name+("" if name[-4:-1]+name[-1] == ".lgo" else ".lgo")),"w" if path.exists(name+".lgo") else "a")
out.write("rt 180 setpensize 1")

# Importem la imatge, si no n'hi ha, reportem el problema
bg = Image.open(path.join('Images',"background.png"))
fg = Image.open(path.join('Images',"parenoel.png"))

numframes = 26
rate = 10
canvasize = 500

while numframes > 0:
	img = copy.deepcopy(bg)
	# Merging the two images
	img.paste(fg, (numframes*rate, 0), fg)
	# Recorrem cada pixel de la imatge
	pixel = img.load()
	print(numframes)
	for j in range(canvasize):
		# Inicialitzem variable per al color
		actualcolor = None
		# Movem la tortuga al lloc desitjat
		out.write(" setxy " + str(j) + " 0")
		for i in range(canvasize):
			if actualcolor != pixel[j,i]:
				if actualcolor is not None:
					out.write(" color " + str(list(actualcolor)).replace(",", "") + " fd " + str(length)) # The list format is the one that Logo requires (With [] instead of ()). The program also romves commas (Logo does not want them)
				actualcolor = pixel[j,i]
				length = 1
			else:
				length += 1
		out.write(" color " + str(list(actualcolor)).replace(",", "") + " fd " + str(length)) # The same as the before print - See comment
	if numframes > 1:
		out.write(" color 1 setpensize 500 setxy 250 0 fd 500\nsetpensize 1")
	numframes -= 1