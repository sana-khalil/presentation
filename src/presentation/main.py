from presentation.logic import retrieveimage, blur, blur2, show, save
import numpy as np

imagedata = retrieveimage('data/sunset.jpg')
show(imagedata)

ft = np.fft.fft2(imagedata)
shift = np.fft.fftshift(ft)

#apply filter here
ftimagep = blur(imagedata, 50)
#show(np.log(1+np.abs(ftimagep)))

# Finally, take the inverse transform and show the blurred image
imagep = np.fft.ifft2(ftimagep)
show(np.log(1+np.abs(imagep)))

#save(imagep)

g = blur2(imagedata)
show(g.real)
