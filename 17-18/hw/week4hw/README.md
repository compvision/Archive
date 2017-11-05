# Week 4 HW

### The Assignment

1.) Download image of Japanese flag from http://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/320px-Flag_of_Japan.svg.png

Remember: ```wget <url>```

2.) Write a program to do the following:

- Load image.
- Convert image to HSV color space.
- Threshold the hue to isolate the sun in the flag. Do this by trying several sets of values for Hue, Saturation, and Value, between 0 and 255 to find the values.
- Run the contour detector.
- Draw contours onto original image.
- Show the original image.

This should have drawn a circle around the sun in the flag

### Turning it in

As usual, fork [this repo](https://github.com/compvision/week4hw), and put your code, and submit a pull request.
