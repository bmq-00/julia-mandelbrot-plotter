import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image
import numpy as np

s = input('julia or mandelbrot?')

c =  -0.835 - 0.2321j
MAX_ITER = 250
ZOOM = 15 
SIZE_w = 15360
SIZE_h = 8640
STEP = 0.004

def julia(c,z0):
	z = z0
	bound = max(2, abs(c))
	n = 0
	while(abs(z) <= bound and n < MAX_ITER):
		z = z*z + c
		n += 1
	return n

def mandelbrot(c):
	n = 0
	z = 0
	while abs(z) <= 2 and n < MAX_ITER:
		z = z**2 + c
		n += 1
	return n

def plane(x,y):
	return( ((1/ZOOM)*STEP*(x-SIZE_w/2)) + ((1/ZOOM)*STEP*(SIZE_h/2-y))*1j)

x = []
if s == 'julia':
	for i in range(SIZE_h):
		y = []
		for k in range(SIZE_w):
			y.append(julia(c, plane(k,i))/255)
		x.append(y)
elif s == 'mandelbrot':
	for i in range(SIZE_h):
		y = []
		for k in range(SIZE_w):
			y.append(mandelbrot(plane(k,i))/255)
		x.append(y)

data = np.asarray(x)
img = Image.fromarray(cm.turbo(data, bytes=True))
img.save('b.png')