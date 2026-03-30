import numpy as np
from PIL import Image
from CONFIG import *

#load image
pil_image = Image.open("img.png").convert('RGB')

#convertSize
original_size = (pil_image.width, pil_image.height)
resized_img = pil_image.resize(SIZEIMAGE, Image.Resampling.LANCZOS)

#numpy convert
image_np = np.asarray(resized_img)


#reshape to original data
pilImageRecreated = Image.fromarray(image_np, 'RGB')
pilImageRecreated = pilImageRecreated.resize(original_size, Image.Resampling.LANCZOS)

#save final result
pilImageRecreated.save("output.png")