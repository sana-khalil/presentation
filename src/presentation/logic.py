import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage, misc

def retrieveimage(image):
    i = cv2.imread(image, 0)
    return i

def show(input):
    plt.imshow(input, 'gray')
    plt.show()

def save(array):
    h = f'{array=}'
    print(h)
    plt.imsave('name.png', array)

def blur(imagedata, blur_amount):
    shift = np.fft.fftshift(np.fft.fft2(imagedata))
    ncols, nrows = imagedata.shape[0], imagedata.shape[1]

    # Build and apply a Gaussian filter.
    sigmax, sigmay = blur_amount, blur_amount
    cy, cx = nrows / 2, ncols / 2
    x = np.linspace(0, nrows, nrows)
    y = np.linspace(0, ncols, ncols)
    X, Y = np.meshgrid(x, y)
    gmask = np.exp(-(((X - cx) / sigmax) ** 2 + ((Y - cy) / sigmay) ** 2))

    ftimagep = shift * gmask
    return ftimagep

def blur2(imagedata):
    #built-in gaussian fourier filter which is multiplied
    input_ = np.fft.fft2(imagedata)
    result = ndimage.fourier_gaussian(input_, sigma=4)
    result = np.fft.ifft2(result)
    return result
