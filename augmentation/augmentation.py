from typing import Union
import os

import cv2
import numpy as np

from preparation.utils import resize_square_image
from preparation.utils import resize_image


def random_crop(img_path: str, width: int, height: int, crop_ratio: float=0.8) -> np.ndarray:
    '''
    params:
    img_path: the path to the image
    width: the width of the cropped image
    height: the height of the cropped image
    crop_ratio: the crop ratio.
    '''
    aspect_ratio = width / height
    img = cv2.imread(img_path)
    h, w = img.shape[:2]
    # crop the image and keep the aspect ratio
    assum_width = h*aspect_ratio
    if (assum_width < w) or (assum_width == w):  # the image is in the range of the width, crop according to the height
        # crop the width
        crop_height = int(crop_ratio*h)
        crop_width = int(crop_height*aspect_ratio)
        crop_x = np.random.randint(0, w-crop_width)
        crop_y = np.random.randint(0, h-crop_height)
        cropped = img[crop_y:crop_y+crop_height, crop_x:crop_x+crop_width]
    else:  # crop according to the width
        crop_width = int(crop_ratio*w)
        crop_height = int(crop_width/aspect_ratio)
        crop_x = np.random.randint(0, w-crop_width)
        crop_y = np.random.randint(0, h-crop_height)
        cropped = img[crop_y:crop_y+crop_height, crop_x:crop_x+crop_width]

    cropped = cv2.resize(cropped, (width, height), interpolation=cv2.INTER_AREA)
    return cropped 

def random_crop_square(img_path: str, size: int, crop_ratio: float=0.8) -> np.ndarray:
    '''
    params:
    img_path: the path to the image
    size: the size of the cropped image
    crop_ratio: the crop ratio.
    '''
    img = cv2.imread(img_path)
    h, w = img.shape[:2]
    if h > w:
        d_min = w
    else:
        d_min = h
    # center crop to the d_min
    crop_size = int(d_min*crop_ratio)
    crop_x = np.random.randint(0, w-crop_size)
    crop_y = np.random.randint(0, h-crop_size)
    cropped = img[crop_y:crop_y+crop_size, crop_x:crop_x+crop_size]
    resized = cv2.resize(cropped, (size, size), interpolation=cv2.INTER_AREA)
    return resized

def random_flip(img_path: str, flip_code: int) -> np.ndarray:
    '''
    params:
    img_path: the path to the image
    flip_code: 0 for vertical flip, 1 for horizontal flip, -1 for both
    '''
    img = cv2.imread(img_path)
    return cv2.flip(img, flip_code)

def random_rotate(img_path: str, angle: int) -> np.ndarray:
    '''
    params:
    img_path: the path to the image
    angle: the angle of the rotation
    '''
    img = cv2.imread(img_path)
    h, w = img.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    rotated = cv2.warpAffine(img, M, (w, h))
    return rotated


if __name__ == "__main__":
    img_path = os.path.join(os.getcwd(), "data", "test_imgs", "cat_2.jpg")
    cropped = random_crop(img_path, 300, 400)
    cv2.imshow("cropped", cropped)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    flipped = random_flip(img_path, 1)
    cv2.imshow("flipped", flipped)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    rotated = random_rotate(img_path, 45)
    cv2.imshow("rotated", rotated)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cropped = random_crop_square(img_path, 512)
    cv2.imshow("cropped", cropped)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    