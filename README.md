# Introduction

As the field of Transformers and Diffusions advances, the significance of data has become increasingly apparent. Many studies show that having a high-quality dataset is often more crucial than the algorithm you use. The objective of this repository is to offer a suite of tools designed to assist the community in acquiring high-quality data efficiently and with ease.

## Features
- **:card_file_box: Data Collection**
    :fire: Tools for downloading specific images from google.
- **:art: Data Preparation**
    :fire: Tools for preparing images for img2img conditional diffusion model, such as canny image generation, LineArt generation.

    :fire: Tools for preprocessing images.
- **:sparkles:Data Augumentation**
    :fire: Tools for getting more data through image manipulation techniques such as rotation, random cropping, and flipping.
    
    :fire: Tools for getting more data through generative models, such as change lighting, change background, change specific object or zone. (Coming soon)

# Examples
Original image:

![alt text](data/test_imgs/cat_2.jpg)

Cropped image 300*400:

![alt text](data/test_imgs/cropped.jpg)

Cropped square image 512*512:

![alt text](data/test_imgs/cropped_square.jpg)

Flipped image:

![alt text](data/test_imgs/flipped.jpg)

Rotated image:

![alt text](data/test_imgs/rotated.jpg)

# Usage
1. Download the repo.
```
git clone https://github.com/ZhihaoAIRobotic/Data-Is-All-You-Need.git
```

2. Read examples for using.