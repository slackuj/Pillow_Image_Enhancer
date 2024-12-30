from PIL import Image
#import tkinter

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

        #root = tkinter.Tk() #create a tkinter root window
        l = k + 1
        title = str(l) + "bit plane"
        #root.title(title) #set the window title
        bp_img.show(title)
        #root.mainloop() #runt the tkinter loop

