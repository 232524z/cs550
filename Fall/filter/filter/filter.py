#Ian
#OMH
#Sources: Spencer, https://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html, https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
from PIL import Image, ImageFilter, ImageEnhance
from random import randint

picture = Image.open("boar.jpg")
emoji = Image.open("emoji.png")
for i in range(4):
	picture.paste(emoji, ((randint(0,picture.width-emoji.width),randint(0,picture.height-emoji.height))))

sharpen = ImageEnhance.Sharpness(picture)
factor = 15
picture = sharpen.enhance(factor)

cont = ImageEnhance.Contrast(picture)
factor = 2000
picture = cont.enhance(factor)


picture.save("im.png","PNG")