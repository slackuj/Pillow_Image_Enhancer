from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy
import technique 

def threshold(img):
    """Thresholding Function"""
    count = 0
    while True:
        try:
            T = int(input("Enter threshold [0-255] :"))
        except ValueError:
            count = count + 1
        else:
            if (0 <= T <= 255):
                img = img.point(lambda x: 255 if x > T else 0)
                return img
            if (count > 10):
                print("\nYou can enter 'quit' to exit\n")
            if (count > 15):
                threshold(img)


def negative(img):
    """negative of an image with intensity levels in the range [0,255]"""
    return ImageOps.invert(img)
def intensity_slicing(img):
    """ displays the interested range of intensities as white
    and all other as black """
    count = 0
    while True:
        try:
            a = int(input("Enter lower threshold [0-255] :"))
            b = int(input("Enter higher threshold [0-255] :"))
        except ValueError:
            count = count + 1
        else:
            if (0 <= a <= 255 and 0 <= b <= 255):
                img = img.point(lambda x: 255 if a < x < b else 0)
                return img
            if (count > 10):
                print("\nYou can enter 'quit' to exit\n")
            if (count > 15):
                intensity_slicing(img)


def bit_plane_slicing(img):
    """ Performs bit plane slicing on an image"""
    width , height = img.size
    bp_img = Image.new("L", (width, height))
    
    pixels = img.load()
    bp_pixels = bp_img.load()

    for k in range(0,8):
        for i in range(width):
            for j in range(height):
                pixel = pixels[i, j]
                bit_value = (pixel >> k) & 1
                bp_pixels[i, j] = bit_value * 255

        l = k + 1
        image_plane = str(l) + "bit plane"
        bp_img.show(title = image_plane)

def histogram_processing(img):
    print("\nHistogram Processing:")
    print("1.Display Histogram")
    print("2.Equalize the histogram")
    option = technique.options(2)
    match(option):
        case 1: display_hist(img)
        case 2: equalize_hist(img)

def display_hist(img):
    print("Dispaying the input image")
    img.show()
    print("Plotting the histogram...")
    hist = img.histogram()
    #plt.figure()
    plt.bar(range(256), hist, color = "gray")
    #plt.plot(hist)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.title("Histogram of the image")
    #plt.xlim([0, 255])
    plt.show(block = False)

def equalize_hist(img):
    img = ImageOps.equalize(img)
    return img
