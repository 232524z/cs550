def HSL(h,s,l):
	import colorsys
	color = [h, s, l]
	color = colorsys.hls_to_rgb(color[0]/360, color[1]/100, color[2]/100)
	color = [int(color[i]*255) for i in range(3)]
	return tuple(color)