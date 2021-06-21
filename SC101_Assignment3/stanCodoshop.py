"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

FILE: stanCodoshop.py
Name: 黃元品
"""
import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    dist = math.sqrt((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)
    return dist

def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red_pixel = 0
    green_pixel = 0
    blue_pixel = 0
    rgb = []
    for pixel in pixels:
        red_pixel += pixel.red
        green_pixel += pixel.green
        blue_pixel += pixel.blue

    rgb.append(int(red_pixel / len(pixels)))
    rgb.append(int(green_pixel / len(pixels)))
    rgb.append(int(blue_pixel / len(pixels)))

    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg = get_average(pixels)
    best = None
    for pixel in pixels:
        if best is None:
            best = pixel
            best_dict = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
        else:
            temp_dist = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
            if temp_dist < best_dict:
                best = pixel
    return best



def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    temp_dict = {}
    count = 0
    for image in images:  # store all of the pixel in different image
        count += 1
        for i in range(width):
            for j in range(height):  # store the pixel of each position
                if f'{i},{j}' in temp_dict:  # check if the key already exist
                    temp_dict[f'{i},{j}'].append(image.get_pixel(i, j))
                else:
                    temp_dict[f'{i},{j}'] = [image.get_pixel(i, j)]

                if count == len(images):  # check if it is the last image
                    result.set_pixel(i, j, get_best_pixel(temp_dict[f'{i},{j}']))
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
