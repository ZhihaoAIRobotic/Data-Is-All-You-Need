import cv2
import os
import imutils
from typing import Union, List, Tuple
from numpy import ndarray


def change_name_batch(path, new_name):
    for count, filename in enumerate(os.listdir(path)):
        dst = new_name + str(count) + ".jpg"
        src = path + filename
        dst = path + dst

        os.rename(src, dst)
        print(f"Renamed {filename} to {dst}")


def resize_image(path: str, width: int = None, height: int = None) -> ndarray:
    '''
    Resize an image to a specific width or height. Keep the aspect ratio.
    '''
     # if both the width and the height are not None 
    if width is not None and height is not None:
        raise ValueError("Cannot set both width and height. Please set only one of them.")
    
    if width is None and height is None:
        raise ValueError("Please set either width or height.")
    
    img = cv2.imread(path)

    if width is not None:
        resized = imutils.resize(img, width=width)

    if height is not None:
        resized = imutils.resize(img, height=height)

    return resized

def resize_square_image(path: str, size: int, mode: str) -> ndarray:
    """Resize an image to a square shape.
    mode (str): 'center_crop' , 'random_crop' or 'padding'
    """
    try:
        img = cv2.imread(path)
        h, w = img.shape[:2]
    except AttributeError:
        raise FileNotFoundError(f"The file {path} does not exist. Please check the path.")
    img = cv2.imread(path)
    if mode not in ['center_crop', 'random_crop', 'padding']:
        raise ValueError("Invalid mode. Please choose one of the following: 'center_crop' , 'random_crop' or 'padding'")
    if mode == 'center_crop':
        # crop the image to the center
        h, w = img.shape[:2]
        if h > w:
            d_min = w
        else:
            d_min = h
        # center crop to the d_min
        center_h = h//2
        center_w = w//2
        half_d_min = d_min//2
        cropped = img[center_h-half_d_min:center_h+half_d_min, center_w-half_d_min:center_w+half_d_min]
        resized = cv2.resize(cropped, (size, size), interpolation=cv2.INTER_AREA)

    if mode == 'random_crop': #TODO: Add random crop
        # crop the image to the center
        h, w = img.shape[:2]
        if h > w:
            d_min = w
        else:
            d_min = h
        # center crop to the d_min
        center_h = h//2
        center_w = w//2
        half_d_min = d_min//2
        cropped = img[center_h-half_d_min:center_h+half_d_min, center_w-half_d_min:center_w+half_d_min]
        resized = imutils.resize(cropped, width=size)

    if mode == 'padding':
        # pad the image to the size
        h, w = img.shape[:2]
        if h > w:
            d_max = h
        else:
            d_max = w

        # pad the image to the d_max
        top = (d_max - h) // 2
        bottom = d_max - h - top
        left = (d_max - w) // 2
        right = d_max - w - left

        resized = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])
        h, w = resized.shape[:2]

        resized = cv2.resize(resized, (size, size), interpolation=cv2.INTER_AREA)
    # check if the resized image is square and has the correct size
    h, w = resized.shape[:2]
    if h != size or w != size:
        raise ValueError(f"Resized image is not square. Expected size: {size}x{size}. Got: {h}x{w}")
    return resized

