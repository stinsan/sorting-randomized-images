# Sorting Randomized Images and the Visualization of Sorting Algorithms
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)<br/>

## Getting Started :heavy_check_mark:
### Prerequisites
This program uses the following Python modules:

- Pillow
```
pip install Pillow
```

- NumPy
```
pip install numpy
```

- OpenCV
```
pip install opencv
```
### Installation
- First, clone this repository.
```
git clone https://github.com/stinsan/Sorting-Randomized-Images.git
```
- Then, the H264 video codec must also be installed becuase OpenCV does not include
it in the default installation. <br/>
After downloading, unzip the file, then place the .dll file in the same directory as main.py. <br/>
Download the latest release from here: https://github.com/cisco/openh264/releases

## Running the Program :runner:
The program is invoked by the following command:
```
python main.py <sorting_algorithm>
```

The <sorting_algorithm> parameter can be one of the following: 

| Parameter Name | Sorting Algorithm Used|
|----------------|-------------------|
|bubble|Bubblesort|
|insert|Insertion Sort|
|select|Selection Sort|
|dselect|Double Selection Sort
|merge|Merge Sort|
|quick|Quicksort|
|heap|Heapsort|
|count|Counting Sort|
|radix|Radix Sort|
|bucket|Bucket Sort|

If no parameter is set, the program defaults to using bubblesort.

Then, the user will be prompted to select an image that will be randomized and sorted.

After a few seconds, a video showing the sorting algorithm at work will open and begin playing.
This video will also be saved in the same directory as the program as "result.mp4".

The statistics of the sorting algorithm, such as the number of array comparisons and
swaps, will also be output to the terminal.

## Examples and Results :100:
Here is an example of how this program works and the results that come from it.

Take this cute picture of myself as the input image:

![](screenshots/input.png)

This is the image after randomization:

![](screenshots/random.png)

This is a snippet of the resulting video showing a visualization of how the 
sorting algorithm works  (bubblesort, in this case):

![](screenshots/result.gif)

These are the statistics that are printed to the terminal:

![](screenshots/terminal_output.png)

## TODO :scroll:

- ~Insertion sort~
- ~Selection sort~
- ~Double selection sort~
- Merge sort
- ~Quicksort~
- Heapsort
- Counting sort
- Radix sort
- Bucket sort
- GUI
- Optimizations

