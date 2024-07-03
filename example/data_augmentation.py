import os

import cv2

from augmentation.augmentation import random_crop, random_flip, random_rotate, random_crop_square

img_path = os.path.join(os.getcwd(), "data", "test_imgs","cat_2.jpg")
cropped = random_crop(img_path, 300, 400)
# save
cv2.imwrite("data/test_imgs/cropped.jpg", cropped)
flipped = random_flip(img_path, 1)
cv2.imwrite("data/test_imgs/flipped.jpg", flipped)
rotated = random_rotate(img_path, 45)
cv2.imwrite("data/test_imgs/rotated.jpg", rotated)
cropped = random_crop_square(img_path, 512)
cv2.imwrite("data/test_imgs/cropped_square.jpg", cropped)