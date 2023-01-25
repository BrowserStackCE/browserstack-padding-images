import os
from PIL import Image
  

directory = '/Input/Image/Directory/Path/'
store_pad_dir='/Output/Image/Directory/Path/'
rot_pad_dir='/Rotated/Image/Directory/Path/'



# Normal image padding value (no rotation)
right = 200
left = 200
top = 100
bottom = 100

# Rotated image padding value
rot_right=150
rot_left=150
rot_top=50
rot_bottom=50

# Deg to be rotated (multiples of 90 only)
deg_to_rotate=270


for filename in os.listdir(directory):
    # Open the image
    im = Image.open(directory + filename)
    width, height = im.size
    new_width = width + right + left
    new_height = height + top + bottom
    

    
    # Add the padding
    result = Image.new(im.mode, (new_width, new_height), (255, 255, 255))
    result.paste(im, (left,top))
    
    # Save the padded image as JPG
    result.save(store_pad_dir + filename.split(".")[0] + "_padded.png", "PNG")

    # Rotate Image
    rot_vals = {0: None, 90: Image.ROTATE_90, 180: Image.ROTATE_180,
                    270: Image.ROTATE_270, 360:None}

    rotated_image = im.transpose(rot_vals[deg_to_rotate])

    # Add Padding to rotated image
    rot_width, rot_height = rotated_image.size
    rot_new_width = rot_width + rot_right + rot_left
    rot_new_height = rot_height + rot_top + rot_bottom
    rot_result = Image.new(rotated_image.mode, (rot_new_width, rot_new_height), (255, 255, 255))
    rot_result.paste(rotated_image, (rot_left,rot_top))

    #Save rotated and padded image
    rot_result.save(rot_pad_dir + filename.split(".")[0] + "_rot_padded.png", "PNG")

    
