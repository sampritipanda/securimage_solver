import os
import numpy as np
from PIL import Image

images = []
for i, file_name in enumerate(os.listdir('./images')):
    if i % 10 == 0:
        print(i)
    path = './images/' + file_name
    image = Image.open(path)
    image_gray = image.convert('L')
    image_resize = image_gray.resize(size=(215,80))
    input_img = np.array(image_resize, dtype='int16')
    image.close()
    images.append(input_img)

images = np.array(images)
avg = np.mean(images, axis=0)
img = Image.fromarray(avg.astype(np.uint8)).resize((215,80))
img.save('mean.png')

