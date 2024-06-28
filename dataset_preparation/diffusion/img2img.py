import json
import cv2
import os
def canny_img2img(img):
    """Converts an image to a Canny edge image.

    Args:
        img (np.ndarray): Image to convert.

    Returns:
        np.ndarray: Canny edge image.
    """
    return cv2.Canny(img, 100, 200)

def LineArt(img, **kwargs):
    """Converts an image to a line art image.

    Args:
        img (np.ndarray): Image to convert.

    Returns:
        np.ndarray: Line art image.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (21, 21), 0)
    return cv2.divide(gray, gray_blur, scale=256)


