def bubblesort(arr, randomized_image):
    """
    Performs bubblesort on a given list of randomized one-pixel wide
    columns of an image in order to remake said image.

    Parameters
    ----------
    arr: list
        A list of randomized one-pixel wide columns of an image
        to perform bubblesort on.

    randomized_image : PIL Image File
        The original image after it was randomized.

    Return
    ------
    list
        A list containing all instances of the image that is being sorted
        during the operation of bubblesort. That is, a list of instances of the
        image after every swap during bubblesort. This is what is used
        to make the video.

    """
    frames = [randomized_image]   # The first frame is the random image
    size = randomized_image.size  # Size of the image

    n = len(arr)
    swap_ctr = 0  # Counts how many swaps occur
    comp_ctr = 0  # Counts how many comparisons occur

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place,
        # so traverse the array from 0 to n-i-1
        for j in range(0, n - i - 1):

            # Swap if the element found is greater than the next element
            if arr[j][0] > arr[j + 1][0]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap array elements

                # Swap image elements too
                remaking_image = frames[-1].copy()
                remaking_image.paste(arr[j][1], (j, 0, j + 1, size[1]))
                remaking_image.paste(arr[j + 1][1], (j + 1, 0, j + 2, size[1]))

                frames.append(remaking_image)  # Append to list of frames

                swap_ctr += 1

            comp_ctr += 1

    # Print statistics
    print("Number of Image Columns: ", n)
    print("Number of Comparisons: ", comp_ctr)
    print("Number of Swaps: ", swap_ctr)

    return frames
