from dataset_preparation.diffusion import img2img
import cv2

def test_canny_img2img():
    img = cv2.imread('data/downloaded_images/spilled_coffee_on_the_tableimage_1.jpg')
    # defining threshold1 and dy

    canny = img2img.canny_img2img(img)
    assert canny.shape == img.shape[:2]
    # visualizing the canny image
    cv2.imshow('canny', canny)
    cv2.waitKey(0)



def test_LineArt():
        img = cv2.imread('data/downloaded_images/spilled_coffee_on_the_tableimage_1.jpg')
        line_art = img2img.LineArt(img)
        assert line_art.shape == img.shape[:2]
        # visualizing the line art
        cv2.imshow('line_art', line_art)
        cv2.waitKey(0)



if __name__ == "__main__":
    # test_canny_img2img()
    test_LineArt()
    print("Everything passed")