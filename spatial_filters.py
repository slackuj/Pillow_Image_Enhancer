from PIL import Image, ImageFilter

def box_filter(img):
    return img.filter(ImageFilter.BoxBlur(21))
def gaussian_filter(img):
    return img.filter(ImageFilter.GaussianBlur(21))
def median_filter(img):
    return img.filter(ImageFilter.MedianFilter(21))
def unsharp_masking(img):
    return img.filter(ImageFilter.UnsharpMask(percent = 1000))
