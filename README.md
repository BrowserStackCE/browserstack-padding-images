# browserstack-padding-images
This repo contains code which adds customised padding to images and also rotates images based on the angle specified.

## Pre requisites

1. Make sure to have python istalled in your local system. If not please follow [this](https://www.tutorialsteacher.com/python/install-python#:~:text=Visit%20https%3A%2F%2Fwww.python,download%20the%20standalone%20executable%20installer.) documentation.

2. pip should also be available in local system. If not please follow [this](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/) documentation.


## Install the Dependencies

1. Install PIL package.
```
pip install Pillow

or

pip3 install Pillow
```

## Required changes to the code

1. Add the directory path for input images, output images (with no padding) and rotated images (with rotation and padding).

2. Provide padding values.

3. Add deg of rotation (multiples of 90 only - 0, 90, 180, 270, 360)

## Execute the code

1. Execute the code with the following command.

```
python padding_images.py

or

python3 padding_images.py
```