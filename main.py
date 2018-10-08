from PIL import Image

fitxer='C:\Users\Pc\Pictures\rubber-duck.jpg'
img = Image.open(fitxer)

newidth = 400
width, height = img.size
ratio = floor(height / width)
newheight = ratio * newidth
img = img.resize((newidth, newheight), Image.NEAREST)

img.show()