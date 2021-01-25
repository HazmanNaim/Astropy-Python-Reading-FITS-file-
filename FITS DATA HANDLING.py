import numpy as np
import matplotlib.pyplot as mpl
from matplotlib.colors import LogNorm 
from astropy.io import fits
from astropy.visualization import make_lupton_rgb


#Read FITS file
M42z = fits.open('z.fits') 
M42u = fits.open('u.fits') 
M42r = fits.open('r.fits') 
M42i = fits.open('i.fits') 
M42g = fits.open('g.fits') 

print("-------------------------------")
#All FITS information for z band
M42z.info()
print("-------------------------------")
#All FITS information for u band
M42u.info()
print("-------------------------------")
#All FITS information for r band
M42r.info()
print("-------------------------------")
#All FITS information for i band
M42i.info()
print("-------------------------------")
#All FITS information for g band
M42g.info()

#Basic Information
# print(M42[0].header)

#Storing the z band data as 2D numpy array
image_dataz= M42z[0].data
#Storing the u band data as 2D numpy array
image_datau= M42u[0].data
#Storing the r band data as 2D numpy array
image_datar= M42r[0].data
#Storing the i band data as 2D numpy array
image_datai= M42i[0].data
#Storing the g band data as 2D numpy array
image_datag= M42g[0].data

#This is to know the shape of the array (image is the array itself)
#For Z band data
print("-------------------------------")
print("z band data")
print(type(image_dataz))
print(image_dataz.shape)
print(image_dataz.dtype.name)
print("-------------------------------")
#For U band data
print("-------------------------------")
print("u band data")
print(type(image_datau))
print(image_datau.shape)
print(image_datau.dtype.name)
print("-------------------------------")
#For R band data
print("-------------------------------")
print("r band data")
print(type(image_datar))
print(image_datar.shape)
print(image_datar.dtype.name)
print("-------------------------------")
#For I band data
print("-------------------------------")
print("i band data")
print(type(image_datai))
print(image_datai.shape)
print(image_datai.dtype.name)
print("-------------------------------")
#For G band data
print("-------------------------------")
print("g band data")
print(type(image_datag))
print(image_datag.shape)
print(image_datag.dtype.name)
print("-------------------------------")

#Showing Image
#z data
mpl.imshow(image_dataz, cmap='gray')
mpl.title('RAW z band image M42', fontsize=10)
mpl.colorbar()
mpl.show()
#u data
mpl.imshow(image_datau, cmap='gray')
mpl.title('RAW u band image M42', fontsize=10)
mpl.colorbar()
mpl.show()
#r data
mpl.imshow(image_datar, cmap='gray')
mpl.title('RAW r band image M42', fontsize=10)
mpl.colorbar()
mpl.show()
#i data
mpl.imshow(image_datai, cmap='gray')
mpl.title('RAW i band image M42', fontsize=10)
mpl.colorbar()
mpl.show()
#g data
mpl.imshow(image_datag, cmap='gray')
mpl.title('RAW g band image M42', fontsize=10)
mpl.colorbar()
mpl.show()

#Histogram
#z data
histogram = mpl.hist(image_dataz.flat, bins=500)
mpl.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False) #Turn off Scientific Notation
mpl.xlim(0,100) #Set Range
mpl.ylim(0,5000000)
mpl.title('Intensity of each pixel (z band)')
mpl.show()
#u data
histogram = mpl.hist(image_datau.flat, bins=500)
mpl.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False) #Turn off Scientific Notation
mpl.xlim(0,100) #Set Range
mpl.ylim(0,5000000)
mpl.title('Intensity of each pixel (u band)')
mpl.show()
#r data
histogram = mpl.hist(image_datar.flat, bins=500)
mpl.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False) #Turn off Scientific Notation
mpl.xlim(0,40) #Set Range
mpl.ylim(0,1000000)
mpl.title('Intensity of each pixel (r band)')
mpl.show()
#i data
histogram = mpl.hist(image_datai.flat, bins=500)
mpl.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False) #Turn off Scientific Notation
mpl.xlim(0,100) #Set Range
mpl.ylim(0,1000000)
mpl.title('Intensity of each pixel (i band)')
mpl.show()
#g data
histogram = mpl.hist(image_datag.flat, bins=500)
mpl.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False) #Turn off Scientific Notation
mpl.xlim(0,100) #Set Range
mpl.ylim(0,1000000)
mpl.title('Intensity of each pixel (g band)')
mpl.show()

#Scaling in Logarithm
#z data
mpl.imshow(image_dataz, cmap='gray', norm=LogNorm())
mpl.colorbar()
mpl.title('RAW z band image M42 (Logarithmic Stretch)', fontsize=10)
mpl.show()
#u data
mpl.imshow(image_datau, cmap='gray', norm=LogNorm())
mpl.colorbar()
mpl.title('RAW u band image M42 (Logarithmic Stretch)', fontsize=10)
mpl.show()
#r data
mpl.imshow(image_datar, cmap='gray', norm=LogNorm())
mpl.colorbar()
mpl.title('RAW r band image M42 (Logarithmic Stretch)', fontsize=10)
mpl.show()
#i data
mpl.imshow(image_datai, cmap='gray', norm=LogNorm())
mpl.colorbar()
mpl.title('RAW i band image M42 (Logarithmic Stretch)', fontsize=10)
mpl.show()
#g data
mpl.imshow(image_datag, cmap='gray', norm=LogNorm())
mpl.colorbar()
mpl.title('RAW g band image M42 (Logarithmic Stretch)', fontsize=10)
mpl.show()

#Setting RGB
g = image_datag
i = image_datai
u = image_datau

#RGB Processing
rgb_default = make_lupton_rgb(u, i, g, stretch=4.0, Q = 11)
mpl.imshow(rgb_default, origin='Lower')
mpl.title('M42 RGB Channel Processed Data (Stretch = 4, Q = 11)', fontsize=10)
mpl.show()

