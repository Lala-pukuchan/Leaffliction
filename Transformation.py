import os
import sys
from PIL import Image, ImageEnhance, ImageFilter
from plantcv import plantcv as pcv
import numpy as np
import matplotlib.pyplot as plt


def gaussianBlur(img) -> Image:
    """
    gaussianBlur image
    """
    gray = pcv.rgb2gray(rgb_img=img)
    threshold_dark = pcv.threshold.binary(
        gray_img=gray, threshold=110, object_type="dark"
    )
    gaussian_img = pcv.gaussian_blur(
        img=threshold_dark, ksize=(5, 5), sigma_x=0, sigma_y=None
    )
    return gaussian_img


def mask(img, gaussian_img) -> Image:
    """
    mask image
    """
    masked_image = pcv.apply_mask(img=img, mask=gaussian_img, mask_color="white")
    return masked_image


def roi(img) -> Image:
    """
    roi image
    """
    roi, roi_hierarchy = pcv.roi.rectangle(img=img, x=100, y=100, h=200, w=200)

    return roi


def save(img_arr, path, type):
    """
    save image
    """
    if type == "GaussianBlur":
        plt.imshow(img_arr, cmap="gray")
    else:
        plt.imshow(img_arr)
    plt.title(type)
    plt.axis("on")
    name, ext = os.path.splitext(path)
    plt.savefig(f"{name}_{type}{ext}")


def augment(img, path):
    """
    augment image
    """
    img_arr = np.array(img)
    save(gaussianBlur(img_arr), path, "GaussianBlur")
    save(mask(img_arr, gaussianBlur(img_arr)), path, "mask")
    save(roi(img_arr), path, "roi")
    # save(contrast(img_arr), path, "contrast")
    # save(bright(img_arr), path, "bright")
    # save(blur(img_arr), path, "blur")


def main():
    if len(sys.argv) != 2:
        print("python Transformation.py './Apple/apple_healthy/image (1).JPG'")
        exit(1)
    path = sys.argv[1]
    try:
        with Image.open(path) as img:
            img.verify()
        with Image.open(path) as img:
            augment(img, path)
    except (IOError, SyntaxError) as e:
        print(f"Error loading image {path}: {e}")
        exit(1)


if __name__ == "__main__":
    main()
