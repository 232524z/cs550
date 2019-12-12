from PIL import Image
import random

dimx = 800
dimy = 800
pos = [[random.randint(0,800), 0, random.randint(0,255), random.randint(0,255),random.randint(0,255)] for i in range(100)]
file = Image.new("RGB", (dimx,dimy))

def next(position):
	global pos
	return [(position[0]+random.randint(-2,2)), (position[1]+1), position[2], position[3], position[4]]


for y in range(800):
	for x in range(len(pos)-1):

		if pos[x][0]< 0 or pos[x][0]>800:
			pos.pop(x)
		else:
			pos[x]=next(pos[x])
		try:
			file.putpixel(pos[x][0:2],(pos[x][2],pos[x][3],pos[x][4]))
		except:
			pass


file.save("lightning.png","PNG")