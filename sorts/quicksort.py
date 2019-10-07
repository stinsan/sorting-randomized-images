def partition(arr, left, right, frames, size, counters):
    """
    This is a modified version of the partition procedure to fit my needs when
    sorting a picture. This partitions the array with the pivot being the
    right-most array element. Partitioning works such that everything that is
    less than the pivot is on the left side, and everything greater than the
    pivot is on the right side.

    Parameters
    ----------
    arr : list
        A list of randomized one-pixel wide columns of an image
        to partition.

    left : int
        The low index value of the subarray to be partitioned.

    right : int
        The high index value of the subarray to be partitioned.

    frames : list
        One of the modifications I added.  A list containing all instances of the image
        that is being sorted during the operation of quicksort. That is,
        a list of instances of the image after every swap during the sort.
        This is what is used to make the video.

    size : tuple
        One of the modifications I added. This is the dimensions of the image.
        The first element is the width, the second element is the height.

    counters : tuple
        One of the modification I added. This are the counters that is printed
        at the end of the sort for statistical purposes. The first element
        is the number of comparisons, and the second element is the number of
        swaps.

    Return
    ------
    tuple
        The first element is the partition index.
        The second element is the frames. Refer to the parameters for more information on that.
        The third element is a tuple of counters. Refer to the parameters for more information.
    """
    i = left - 1
    pivot = arr[right][0]  # This partition has a high element pivot

    for j in range(left, right):

        counters[0] += 1  # Increment comparison counter

        if arr[j][0] < pivot:

            i += 1

            # Swap and increment swap counter
            arr[i], arr[j] = arr[j], arr[i]
            counters[1] += 1

            # Swap columns of the image too
            remaking_image = frames[-1].copy()
            remaking_image.paste(arr[i][1], (i, 0, i + 1, size[1]))
            remaking_image.paste(arr[j][1], (j, 0, j + 1, size[1]))
            frames.append(remaking_image)  # Append to list of frames

    # Swap with pivot and increment swap counter
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    counters[1] += 1

    # Swap columns oof the image too
    remaking_image = frames[-1].copy()
    remaking_image.paste(arr[i + 1][1], (i + 1, 0, i + 2, size[1]))
    remaking_image.paste(arr[right][1], (right, 0, right + 1, size[1]))
    frames.append(remaking_image)  # Append to list of frames

    return i + 1, frames, counters


def quicksort(arr, left, right, frames, randomized_image, counters):
    """
    This is a modified version of quicksort to fit my needs when sorting a picture.
    Note the immense amount of parameters involved; this is because quicksort is a
    recursive function and I could not think of a way to keep track of variables
    through recursive calls.

    Parameters
    ----------
    arr : list
        A list of randomized one-pixel wide columns of an image
        to perform quicksort on.

    left : int
        The low index value of the subarray to be sorted.

    right : int
        The high index value of the subarray to be sorted

    frames : list
        One of the modifications I added.  A list containing all instances of the image
        that is being sorted during the operation of quicksort. That is,
        a list of instances of the image after every swap during the sort.
        This is what is used to make the video.

    Return
    ------
    tuple
        The first element is the frames. Refer to the parameters for more information on that.
        The second element is a tuple of counters; counters[0] is the comparison counter, and
        counter[1] is the swap counter.
    """

    if left < right:
        partition_ret = partition(arr, left, right, frames, randomized_image.size, counters)

        quicksort(arr, left, partition_ret[0] - 1, partition_ret[1], randomized_image,
                  partition_ret[2])

        quicksort(arr, partition_ret[0] + 1, right, partition_ret[1], randomized_image,
                  partition_ret[2])

    return frames, counters
