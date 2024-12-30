from PIL import Image, ImageOps, ImageFilter,ImageShow, UnidentifiedImageError
from bit_plane_slicing import bit_plane_slicing
import glevel_transforms, technique, spatial_filters, image_interpolations, interpolate 
import sys, os
from fortune import fortune

def main() :

    if (len(sys.argv) == 2) :
        try:
            img = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit(f"The file {sys.argv[1]}  does not exists.")
        except UnidentifiedImageError:
            sys.exit(f"The file {sys.argv[1]} cannot be identified as an image file.")

    elif (len(sys.argv) == 1):
        try:
            file = input("Enter the path to your image: ")
            img = Image.open(file)
        except FileNotFoundError:
            sys.exit(f"The file {sys.argv[1]}  does not exists.")
        except UnidentifiedImageError:
            sys.exit(f"The file {sys.argv[1]} cannot be identified as an image file.")
    else:
        sys.exit("Usage : python project.py <image>")


    img = img.convert("L")
    enhance(img)

    prompt = input("Do you want to continue? [Y/n] : ") 
    if (prompt.lower() == 'yes' or prompt.lower() == 'y'):
       enhance(img)
    
    print(fortune())

def enhance(img):
    print("PILLOW IMAGE ENHANCER : PIE")
    print("\n1.Some Basic Gray Level Transformations")
    print("2.Some Basic Spatial Filters")
    print("3.Some Basic Image Interpolation Techniques")
    print("\nEnter 'quit' to exit")

    option = technique.options(3)
    if (option == 1): result = glevel_transform(img)
    elif (option == 2): result = spatial_filter(img)
    else: result = image_interpolation(img)

    
    if (result != None):
        try:
            os.mkdir("output")
        except FileExistsError:
            pass

        count = 0
        while True:
            try:
                filename = input("Enter the name of filename to be saved : ")
                filename = "output/" + filename
                print("Saving the processed image...")
                result.save(filename)
            except OSError:
                print("The file could not be written. The file may have been created, and may contain partial data")
                count = count + 1
                if (count > 3):
                    sys.exit("Exiting with inappropriate filename...")
            except ValueError:
                print("The output format could not be determined from the file name")
                print("Please try again")
                count = count + 1
                if (count > 3):
                    sys.exit("Exiting with inappropriate filename...")
            else:
                return
   
def glevel_transform(img):
    """Some Gray Level Transformations"""
    print("1.Thresholding\n2.Digital Negative\n3.Intensity Level Slicig\n4.Bit Plane Slicing\5.Histogram Processing")
    print("\nEnter 'quit' to exit")
    option = technique.options(5)
    match(option):
        case 1: result = glevel_transforms.threshold(img)
        case 2: result = glevel_transforms.negative(img)
        case 3: result = glevel_transforms.intensity_slicing(img)
        case 4: result = glevel_transforms.bit_plane_slicing(img)
        case 5: result = glevel_transforms.histogram_processing(img)
    return result
def spatial_filter(img):
    """Some Basic Spatial Filters"""
    print("1.Box Filter\n2.Gaussian Filter\n3.Median Filter\n4.Unsharp Masking")
    print("\nEnter 'quit' to exit")
    option = technique.options(3)
    match(option):
        case 1: result = spatial_filters.box_filter(img)
        case 2: result = spatial_filters.gaussian_filter(img)
        case 3: result = spatial_filters.median_filter(img)
        case 4: result = spatial_filters.unsharp_masking(img)
    return result
def image_interpolation(img):
    """Some Basic Image Interpolation Techniques"""
    print("1.Nearest Neighborhood Interpolation\2.Bilinear Interpolation\3.Bicubic Interpolation")
    print("\nEnter 'quit' to exit")
    option = technique.options(3)
    width, height = interpolate.options()
    match(option):
        case 1: result = image_interpolations.neighbor(img, width, height)
        case 2: result = image_interpolations.bilinear(img, width, height)
        case 3: result = image_interpolations.bicubic(img, width, height)
    return result

if __name__ == "__main__" :
    main()
