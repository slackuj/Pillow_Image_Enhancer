from PIL import Image

def neighbor(img, width, height):
    return img.resize((width, height), resample = Image.NEAREST)
def bilinear(img, width, height):
    return img.resize((width, height), resample = Image.BILINEAR)
def bicubic(img, width, height):
    return img.resize((width, height), resample = Image.BICUBIC)
