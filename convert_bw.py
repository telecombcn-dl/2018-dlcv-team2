import cv2
import os
from os import listdir,makedirs
from os.path import isfile,join


#path = 'dataset/facades/test/b' # Source Folder
#dstpath = 'dataset/facades/test/bw' # Destination Folder

path = 'dataset/cat_dataset/test/b' # Source Folder
dstpath = 'dataset/cat_dataset/test/bw' # Destination Folder
print(dstpath)

try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")

# Folder won't used
files = [f for f in listdir(path) if isfile(join(path,f))]
print('converting')
for image in files:
    img = cv2.imread(os.path.join(path,image))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    dstPath = join(dstpath,image)
    cv2.imwrite(dstPath,gray)
