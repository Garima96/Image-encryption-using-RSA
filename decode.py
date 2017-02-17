import os,sys
import numpy
import math
from PIL import Image
#import _imaging
jpgfile = Image.open("a.jpg")
#jpgfile.show()
print jpgfile.bits, jpgfile.size, jpgfile.format
row,col =  jpgfile.size
pixels = jpgfile.load()

p = 7
q = 37
n = p*q
t = (p-1)*(q-1)
mod = 259
e = 17
def power(x,y,m):
	if(y==0):
		return 1
	elif(y%2==0):
		return (power(x,y/2,m) * power(x,y/2,m))%m
	else:
		return (x*power(x,y/2,m)*power(x,y/2,m))%m
	
d = power(17,71,t)
#print (e*m)%t

Matrix = [[0 for x in range(row)] for y in range(col)]
Decrypt = [[0 for x in range(row)] for y in range(col)]
for i in range(col):
	for j in range(row):
		r,g,b =  pixels[j,i]
		r1 = power(r,e,mod)
		g1 = power(g,e,mod)
		b1 = power(b,e,mod)
		#if(r1>255 or g1>255 or b1>255):
		#	print r1,g1,b1
		Matrix[i][j] = r1,b1,g1
data = numpy.array(Matrix,dtype = numpy.uint8)
img = Image.fromarray(data,'RGB')
img.show()	
for i in range(col):
	for j in range(row):
		r1,g1,b1 =  Matrix[i][j]
		r1 = power(r1,d,mod)
		g1 = power(g1,d,mod)
		b1 = power(b1,d,mod)
		Decrypt[i][j] = r1,b1,g1
data1 = numpy.array(Decrypt,dtype = numpy.uint8)
img1 = Image.fromarray(data1,'RGB')
#image_transp = numpy.transpose(img, (1, 0, 2))
#out = img.transpose(Image.ROTATE_270)
img1.show()
img1.save('out.jpg')


