import cv2
import math
import numpy as np
import random
import sys
import time
import tkinter as tk
from os import startfile
from PIL import Image
from sorts import bubblesort
from sorts import selection_sort
from tkinter import filedialog

MAX_IMAGE_WIDTH = {"bubble": 350,
                   "select": 1500}

FRAME_SKIP = {"bubble": 12,
              "select": 1}


def open_input_window():
    """
    Opens a window for the user to choose the image to be
    randomized then sorted.

    Returns
    -------
    string
        The name of the image file that is to be opened.

    """
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(title='Select Image')

    return filename


def resize_image(image, argv):
    """
    Resizes the image so that the program does not run out of memory
    when processing the sorting of the image.

    Parameters
    ----------
    image : PIL Image File
        The image to be resized.

    argv : list
        A list of commands used in the program invocation.
        The command at argv[1] designates what sorting algorithm
        will be used.

    Returns
    -------
    PIL Image File
        The resized image.

    """

    # Constant value that sets the width of the image, beware
    # when changing because higher resolutions may crash the program.
    required_image_width = MAX_IMAGE_WIDTH[argv[1]]

    # The amount to divide the size by to meet the required image width
    divisor = image.size[0] / required_image_width

    # No need to resize divisor is <1, meaning that image width is
    # already less than the required image width.
    if divisor > 1:
        image_dimensions = (math.floor(image.size[0] / divisor),
                            math.floor(image.size[1] / divisor))
        image = image.resize(image_dimensions)  # Resizing

    return image


def make_columns(image, size):
    """
    Processes an image and makes a list containing all one-pixel
    wide columns of the image.

    Parameters
    ----------
    image : PIL Image File
        The image to be processed.

    size : (int, int)
        The dimensions of the image.

    Returns
    -------
    list
        A list containing all one-pixel wide columns of the image.

    """
    columns = []

    # For every pixel-wide column in the image, crop it, then
    # append the PIL image reference to the list.
    for i in range(size[0] - 1):
        cropped_img = image.crop((i, 0, i + 1, size[1]))
        columns.append((i, cropped_img))

    return columns


def make_image(image_columns, size):
    """
    Creates an PIL image from a list of one-pixel wide columns of
    an image.

    Parameters
    ----------
    image_columns : list
        A list of one-pixel wide columns of an image.

    size : (int, int)
        The dimensions of the image.

    Returns
    -------
    PIL Image File
        The image formed from the list.

    """

    image = Image.new("RGB", size)

    # "Stitch" together the picture from the elements in the list
    for i in range(size[0] - 1):
        image.paste(image_columns[i][1], (i, 0, i + 1, size[1]))

    return image


def sort(image_columns, randomized_image, argv):
    """
    Chooses which sorting algorithm to use based on the parameters in argv.

    Parameters
    ----------
    image_columns : list
        A list of one-pixel wide columns of an image.

    randomized_image : PIL Image File
        The user's original image after it was randomized.

    argv : list
        A list of commands used in the program invocation.
        The command at argv[1] designates what sorting algorithm
        will be used.

    Returns
    -------
    list
        A list of images that are, essentially, the frames of the video.

    """
    video_frames = []

    if len(argv) == 1 or argv[1] == "bubble":
        video_frames = bubblesort.bubblesort(image_columns, randomized_image)

    elif argv[1] == "select":
        video_frames = selection_sort.selection_sort(image_columns, randomized_image)

    elif argv[1] == "insert":
        print("Insertion Sort")
        exit(0)

    elif argv[1] == "merge":
        print("Merge Sort")
        exit(0)

    elif argv[1] == "quick":
        print("Quicksort")
        exit(0)

    elif argv[1] == "heap":
        print("Heap Sort")
        exit(0)

    elif argv[1] == "count":
        print("Counting Sort")
        exit(0)

    elif argv[1] == "radix":
        print("Radix Sort")
        exit(0)

    elif argv[1] == "bucket":
        print("Bucket Sort")
        exit(0)

    else:
        print("Not a valid sort, try again.")
        exit(0)

    return video_frames


def make_video(frames, original_image, randomized_image, size, filename, argv):
    """
    Creates a video showing a given sorting algorithm on a given input image.

    Parameters
    ----------
    frames : list
        A list of images that are, essentially, the frames of the video.

    original_image : PIL Image File
        The original, resized image that was chosen by the user.

    randomized_image : PIL Image File
        The user's original image after it was randomized.

    size : (int, int)
        The size of the resized image.

    filename : string
        The file name of the video to be output.

    argv : list
        A list of commands used in the program invocation.
        The command at argv[1] designates what sorting algorithm
        will be used.

    """
    # These are constants that affect the formation of the video.
    #
    # fps is the frame-rate of the resulting video.
    # frame_skip = n means that the video will only insert every nth frame in
    #              the frames list.
    #
    # Higher values of both fps and frame_skip will lead to shorter video times.
    # A higher frame_skip value will lead to a choppier video, but shorter
    # video processing time.
    fps = 60
    frame_skip = FRAME_SKIP[argv[1]]

    fourcc = cv2.VideoWriter_fourcc(*'avc1')  # Identifies the video codec (H264)
    video = cv2.VideoWriter(filename, fourcc, fps, size)

    # Show the original, un-randomized image for two seconds.
    for i in range(fps * 2):
        video.write(cv2.cvtColor(np.array(original_image), cv2.COLOR_RGB2BGR))

    # Show a blending of the un-randomized and randomized image for two seconds.
    for i in range(fps * 2):
        blended_image = Image.blend(original_image, randomized_image, i / (fps * 2))
        video.write(cv2.cvtColor(np.array(blended_image), cv2.COLOR_RGB2BGR))

    # Show the randomized image for two seconds.
    for i in range(fps * 2):
        video.write(cv2.cvtColor(np.array(randomized_image), cv2.COLOR_RGB2BGR))

    # Inserts every nth frame as defined by the frame_skip constant.
    frame_ctr = 0
    for f in frames:
        if frame_ctr % frame_skip == 0:
            frame_copy = f.copy()
            video.write(cv2.cvtColor(np.array(frame_copy), cv2.COLOR_RGB2BGR))
        frame_ctr += 1

    # Show the sorted image (the final frame) for two seconds.
    for i in range(fps * 2):
        video.write(cv2.cvtColor(np.array(frames[-1]), cv2.COLOR_RGB2BGR))

    video.release()  # Release the kraken


if __name__ == "__main__":

    if len(sys.argv) == 1:
        sys.argv.append("bubble")

    filename = open_input_window()

    img = Image.open(filename)
    img = resize_image(img, sys.argv)

    columns = make_columns(img, img.size)

    random.shuffle(columns)
    random_img = make_image(columns, img.size)

    frames = sort(columns, random_img, sys.argv)

    make_video(frames, img, random_img, img.size, "result.mp4", sys.argv)

    # Automatically open the video after 3 seconds
    time.sleep(3)
    startfile("result.mp4")

    '''
    TODO:
    insertion sort
    selection sort
    merge sort
    quick sort
    heap sort
    counting sort
    radix sort
    bucket sort
    '''