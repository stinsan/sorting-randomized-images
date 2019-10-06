def selection_sort(arr, randomized_image):
    """
    Performs selection sort on a given list of randomized one-pixel wide
    columns of an image in order to remake said image.

    Parameters
    ----------
    arr: list
        A list of randomized one-pixel wide columns of an image
        to perform selection sort on.

    randomized_image : PIL Image File
        The original image after it was randomized.

    Return
    ------
    list
        A list containing all instances of the image that is being sorted
        during the operation of selection sort. That is, a list of instances of the
        image after every swap during selection. This is what is used
        to make the video.

    """
    frames = [randomized_image]   # The first frame is the random image
    size = randomized_image.size  # Size of the image

    n = len(arr)
    swap_ctr = 0  # Counter for swaps
    comp_ctr = 0  # Counter for comparisons

    for i in range(n - 1):
        # Find the minimum in the unsorted portion of the list
        min_index = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_index][0]:
                min_index = j

            comp_ctr += 1

        # Put the minimum where it needs to be
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Swap image elements too
        remaking_image = frames[-1].copy()
        remaking_image.paste(arr[i][1], (i, 0, i + 1, size[1]))
        remaking_image.paste(arr[min_index][1], (min_index, 0, min_index + 1, size[1]))

        frames.append(remaking_image)
        swap_ctr += 1

    # Print statistics
    print("Sorting Algorithm: Selection Sort")
    print("Number of Columns to be Sorted: ", n)
    print("Number of Array Comparisons: ", comp_ctr)
    print("Number of Array Swaps: ", swap_ctr)

    return frames
