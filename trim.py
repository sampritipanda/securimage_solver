import os
import sys
import numpy as np
from PIL import Image

height_trim = 16
width_trim = 20

def trim(image):
    arr = np.asarray(image).tolist()
    arr = arr[height_trim:-height_trim]
    if len(arr[0]) == 215:
        arr = [row[(width_trim-1):-width_trim] for row in arr]
    else:
        arr = [row[width_trim:-width_trim] for row in arr]
    arr = np.asarray(arr)
    image_new = Image.fromarray(arr.astype(np.uint8))
    return image_new


def main():
    dir_name = sys.argv[1]
    for i, file_name in enumerate(os.listdir('./' + dir_name)):
        path = './' + dir_name + '/' + file_name
        print(path)
        image = Image.open(path)
        image_new = trim(image)
        image.close()
        image_new.save(path)


if __name__ == '__main__':
    main()
