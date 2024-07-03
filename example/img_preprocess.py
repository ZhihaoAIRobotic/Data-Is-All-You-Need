from preparation.diffusion.img2img import canny_img2img, LineArt
import cv2
import os
import json
from preparation.utils import resize_square_image

def resize_imgs(read_path, write_path):
    if read_path[-1] != "/":
        read_path += "/"
    if write_path[-1] != "/":
        write_path += "/"
    if not os.path.exists(write_path):
        os.makedirs(write_path)
    img_list = os.listdir(read_path)

    for i, img_name in enumerate(img_list):
        print(read_path + img_name)
        
        img = resize_square_image(read_path + img_name, size=512, mode = 'center_crop')
        cv2.imwrite(write_path + img_name, img)



if __name__ == "__main__":
    read_path = "data/downloaded_images/"
    write_path = "data/resize_downloaded_images"
    resize_imgs(read_path, write_path)
    