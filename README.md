# Pillow Image Enhancer
Pillow Image Enhancer(PIE) is a simple image enhancement tool that allows <br>
to carry out some basic intensity transformations and spatial filtering.<br>
PIE only deals with Gray Level Images.Therefore any image other than a gray-level<br>
image shall be first transformed into the gray-level image prior to any processsing<br>
begins.


# Features
Pillow Image Enhancer(PIE) provides three basic image enhancement techniques:<br>
<br>**1.Some Basic Gray Level Transformations**<br>
    i.  Thresholding<br>
   ii.  Digital Negative<br>
  iii.  Intensity Level Slicing<br>
   iv.  Bit Plane Slicing<br>
    v.  Histogram Processing<br>
<br>**2.Some Basic Spatial Filters**<br>
    i.  Box Filter <br>
   ii.  Gaussian Filter<br> 
  iii.  Median Filter<br>
   iv.  Unsharp Masking<br>
<br>**3.Some Basic Image Interpolation techniques**<br>
    i.  Nearest Neighborhood Interpolation<br>
   ii.  Bilinear Interpolation<br>
  iii.  Bicubic Interpolation<br>

  # REQUIREMENTS
  i. Python 3.12+<br>
 ii. PIL 11.0.0 (Python Imaging Library)<br>
iii. fortune-python 1.1.1 <br>
> ( Only if you want to have some good message at the end of your tasks !)<br>

iv.Terminal or IDE of your choice<br>

  # INSTALLATION
  The installation steps aside from step 1 and step 2 should be same in all environments.The following<br>
  lines of codes are for Ubuntu 24.04<br>
  1.Install Python 3.12+ on your machine.<br>
  
    sudo apt update
    sudo apt install python3
    
  2.Install pip <br>

    sudo apt install python3-pip
  3.Create a virtual environment using python3 -m venv path/to/venv.<br>

    python3 -m venv MyVirtualEnv
    cd MyVirtualEnv
 
  4.Clone this repository<br>

    git clone https://github.com/slackuj/Pillow_Image_Enhancer.git
    cd Pillow_Image_Enhancer
  5.Activate the virtual environment (this will be handy !!!)<br>

    source ../bin/activate 
> assuming you are inside **Pillow_Image_Enhancer** directory that was cloned at step 4.<br>
  6.Install the required modules<br>

    pip install pillow
    pip install matplotlib
    pip install fortune-python

# START GUIDE
You can now use Pillow Image Enhancer(PIE) to enhance your images.The output of the images shall be <br>
stored in the same project directory inside a new sub-directory 'output'.

    python project.py shlokpal.jpg
> Provide the prompt as you want to carryout the processing.<br>
> You can quit the program by simply typing 'quit' at any input prompt.

# BUGS 
Please report any bugs and issues here in this repository or to slackuj@gmail.com.
