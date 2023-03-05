import numpy as np
import matplotlib.pyplot as plt

#loading image and converting to numpy array
img = plt.imread('cat.jpg')
np_img = np.array(img)

#splitting image first time
splitted_img1 = np.array_split(np_img, 41, axis=1)

#creating first image of splitted pieces
img1 = splitted_img1[0]
for i in range(1, len(splitted_img1), 2):
    img1 = np.concatenate((img1, splitted_img1[i]), axis=1)
# plt.imshow(img1)

#creating second image of splitted pieces
img2 = splitted_img1[0]
for i in range(0, len(splitted_img1), 2):
    img2 = np.concatenate((img2, splitted_img1[i]), axis=1)
# plt.imshow(img2)

#merging two images
two_img_merged = np.concatenate((img1, img2), axis=1)

#splitting merged image time
splitted_img2 = np.array_split(two_img_merged, 42, axis=0)

#creating third image of splitted pieces
img3 = splitted_img2[0]
for i in range(1, len(splitted_img2), 2):
    img3 = np.concatenate((img3, splitted_img2[i]), axis=0)
# plt.imshow(img3)

#creating fourth image of splitted pieces
img4 = splitted_img2[0]
for i in range(1, len(splitted_img2), 2):
    img4 = np.concatenate((img4, splitted_img2[i]), axis=0)
# plt.imshow(img4)

#merging images for final view
four_img_merged = np.concatenate((img3, img4), axis=1)

plt.imshow(four_img_merged)