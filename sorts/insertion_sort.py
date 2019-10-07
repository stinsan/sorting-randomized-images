def insertion_sort(arr, randomized_image):
    """
    Performs insertion sort on a given list of randomized one-pixel wide
    columns of an image in order to remake said image.

    Parameters
    ----------
    arr: list
        A list of randomized one-pixel wide columns of an image
        to perform insertion sort on.

    randomized_image : PIL Image File
        The original image after it was randomized.

    Return
    ------
    list
        A list containing all instances of the image that is being sorted
        during the operation of insertion sort. That is, a list of instances of the
        image after every swap during the sort. This is what is used
        to make the video.
    """
    frames = [randomized_image]   # The first frame is the random image
    size = randomized_image.size  # Size of the image

    n = len(arr)
    swap_ctr = 0  # Counts how many swaps occur
    comp_ctr = 0  # Counts how many comparisons occur

    for i in range(1, n - 1):
        j = i

        # Find the correct location to insert in sorted portion of array
        while j > 0 and arr[j][0] < arr[j - 1][0]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]

            remaking_image = frames[-1].copy()
            remaking_image.paste(arr[j][1], (j, 0, j + 1, size[1]))
            remaking_image.paste(arr[j - 1][1], (j - 1, 0, j, size[1]))
            frames.append(remaking_image)  # Append to list of frames

            j -= 1

            swap_ctr += 1
            comp_ctr += 1

    # Print statistics
    print("Sorting Algorithm: Insertion Sort")
    print("Number of Columns to be Sorted: ", n)
    print("Number of Array Comparisons: ", comp_ctr)
    print("Number of Array Swaps: ", swap_ctr)

    return frames
