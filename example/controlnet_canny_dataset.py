from preparation.diffusion.img2img import canny_img2img, LineArt
import cv2
import os
import json

def canny_imgs(read_path, write_path):
    if write_path[-1] != "/":
        write_path += "/"
    if not os.path.exists(write_path):
        os.makedirs(write_path)
    img_list = os.listdir(read_path)
    dataset_json_list = []
    
    for i, img_name in enumerate(img_list):
        print(f"Processing image {i}")
        try:
            img_name = read_path + img_name
            img = cv2.imread(img_name)
            canny = canny_img2img(img)
            print(canny)
            canny_img_name = write_path + f"canny_{i}.jpg"
            print(canny_img_name)
            cv2.imwrite(canny_img_name, canny)
            # add source image, target image, and prompt to the dataset json
            if 'coffee' in img_name:
                prompt = "spilled coffee on the table"
            elif 'milk' in img_name:
                prompt = "spilled milk on the table"
            elif 'juice' in img_name:
                prompt = "spilled juice on the table"
            elif 'water' in img_name:
                prompt = "spilled water on the table"
    
            dataset_json_dict = {
                "source": canny_img_name,
                "target": img_name,
                "prompt": prompt
            }
    
            dataset_json_list.append(dataset_json_dict)

        except Exception as e:
            print(f"Error processing image {i}: {e}")
            continue
    print(dataset_json_list)
    with open("data/imagination_dataset.json", "w") as f:
        json.dump(dataset_json_list, f, indent=4)

if __name__ == "__main__":
    read_path = "data/downloaded_images/"
    write_path = "data/canny_images/"
    canny_imgs(read_path, write_path)
    print("Canny images saved to data/processed_images/")
    