import os
import sys
from PIL import Image, ImageEnhance, ImageFilter


def flip(img) -> Image:
    """
    flip image
    """
    img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
    return img_flip


def rotate(img) -> Image:
    """
    rotate image
    """
    img_rotate = img.rotate(90)
    return img_rotate


def zoom(img) -> Image:
    """
    zoom image
    """
    img_crop = img.crop((0, 0, img.width // 2, img.height // 2))
    img_zoom = img_crop.resize(img.size)
    return img_zoom


def contrast(img) -> Image:
    """
    contrast image
    """
    enhancer = ImageEnhance.Contrast(img)
    img_contrast = enhancer.enhance(2)
    return img_contrast


def bright(img) -> Image:
    """
    bright image
    """
    enhancer = ImageEnhance.Brightness(img)
    img_brightened = enhancer.enhance(2)
    return img_brightened


def blur(img) -> Image:
    """
    blur image
    """
    img_blurred = img.filter(ImageFilter.BLUR)
    return img_blurred


def save(img, path, type):
    """
    save image
    """
    name, ext = os.path.splitext(path)
    img.save(f"{name}_{type}{ext}")


def augment(img, path):
    """
    augment image
    """
    save(flip(img), path, "flip")
    save(rotate(img), path, "rotate")
    save(zoom(img), path, "zoom")
    save(contrast(img), path, "contrast")
    save(bright(img), path, "bright")
    save(blur(img), path, "blur")


def main():
    if len(sys.argv) != 2:
        print("./Augmentation.py './Apple/apple_healthy/image (1).JPG'")
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
