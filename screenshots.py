import pyautogui
# Python program to read an write an image

import imageio as iio

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'c:\Users\shriy\OneDrive\Desktop\Projects\s1.png')

# read an image
img = iio.imread("s1.png")

# write it in a new format
iio.imwrite("new.txt", img)
