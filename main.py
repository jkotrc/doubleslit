from scipy.integrate import *;
import numpy as np;
from numpy import exp;
from numpy import pi
from PIL import ImageTk, Image
from findiff import FinDiff
import cv2;


width = 600
height = 600
decim=6



spaceY = np.linspace(-2.5,7.5,600)
spaceX = np.linspace(-5,5,600)

#numerical step between two pixels on the numberline. Used for the laplacian
dx = 10/600;

gridX,gridY = np.meshgrid(spaceX, spaceY, indexing='ij')

laplacian = FinDiff(0,dx,2) + FinDiff(1,dx,2)


#array with a 0 where there is a slit and a 1 where there is no slit
slits = np.ones([600,600], dtype=np.uint8)
for i in range(250,255):
    for j in (list(range(0,280))    +   list(range(295,305))    +   list(range(320,600))):
        slits[j][i]=0




#initial wave function
k=100
def initialwf(X, Y):
    ret = exp(-0.5*(X**2+Y**2)+k*1j*Y)/(2*pi)
    return np.around(ret,decim) #round off tiny error


#potential (big at the slits, 0 elsewhere)
def V(X,Y):
    return -1000*(slits-1)


data = initialwf(gridX,gridY)


t=0
dt=0.0001	#step size
n=0
N=500		#500 iterations 
frames=[]
while (n<N):

    re=np.double(data.real)
    im=np.double(data.imag)
	
	#Runge-Kutta coefficients
    k1 = (1/1j) * (-0.5*laplacian(data)+V(gridX,gridY)*data)
    k2 = (1/1j) * (-0.5*laplacian(data+0.5*dt*k1)+V(gridX,gridY)*(data+0.5*dt*k1))
    k3 = (1/1j) * (-0.5*laplacian(data+0.5*dt*k2)+V(gridX,gridY)*(data+0.5*dt*k2))
    k4 = (1/1j) * (-0.5*laplacian(data+dt*k3)+V(gridX,gridY)*(data+dt*k3))


    data = data + (dt/6)*(k1+2*k2+2*k3+k4)
    t+=dt
    n+=1
	
	#Capture frame every 10 iterations to make the video faster
    if(n%10 == 0):
        imagedata = np.uint8(np.around((data.conjugate()*data).real*255*2*pi))
        image = Image.fromarray(np.uint8(imagedata), mode='L')
        image = image.convert('RGB')
        im=np.array(image)
        im[:,:,0] = -255*(slits-1)	#make the slits blue
        frames.append(im)


    print("{}% Complete\r".format(100*n/N))



size=(600,600)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4",fourcc, 10, size)

for i in range(len(frames)):
    out.write(frames[i])
out.release()