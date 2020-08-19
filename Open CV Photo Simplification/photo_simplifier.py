import os
import numpy as np
import cv2

IMAGE_PATH = ""


def get_image_path():
    global IMAGE_PATH
    DIR_PATH = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(DIR_PATH)
    IMAGE_PATH = os.path.join(BASE_DIR, "grackle.jpg")
    return IMAGE_PATH


def get_image(path):
    return cv2.imread(path)


def convert_bw(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def show_image(image):
    name = IMAGE_PATH.split("/")[-1]
    cv2.imshow(name, image)


def get_outlines(image):
    # the value of 15 is chosen by trial-and-error to produce the best outline
    # of the skull
    ret, thresh1 = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
    # square image kernel used for erosion
    kernel = np.ones((5, 5), np.uint8)
    # refines all edges in the binary image
    erosion = cv2.erode(thresh1, kernel, iterations=1)

    opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
    # this is for further removing small noises and holes in the image
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    # find contours with simple approximation
    contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow('cleaner', closing)
    cv2.drawContours(closing, contours, -1, (255, 255, 255), 4)
    cv2.waitKey(0)


def main():
    path = get_image_path()
    image = get_image(path)
    bw = convert_bw(image)
    outlines = get_outlines(bw)


if __name__ == '__main__':
    main()