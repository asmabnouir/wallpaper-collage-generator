import os
import ctypes
from PIL import Image

# --------------------------------------
# Estimate how many images are needed
# --------------------------------------
def estimate_needed_images(screen_width, screen_height, columns, margin):
 
    """
     Estimate the number of images needed to fill the screen
    based on screen size, number of columns, and margin spacing.

    Parameters:
        screen_width (int): Width of the screen in pixels
        screen_height (int): Height of the screen in pixels
        columns (int): Number of image columns
        margin (int): Space between images in pixels

    Returns:
        int: Total number of images estimated
    """
    column_width = (screen_width - (columns + 1) * margin) // columns
    estimated_image_height = int(column_width * 1.3)
    per_column = (screen_height + margin) // (estimated_image_height + margin)
    return columns * per_column + 7


# --------------------------------------
# Correct image orientation based on EXIF
# --------------------------------------
def correct_image_orientation(img):
    try:
        exif = img._getexif()
        if exif and 274 in exif:
            orientation = exif[274]  # "274" is the standard identifier of the Orientation tag in EXIF metadata.
            if orientation == 3:
                img = img.rotate(180, expand=True)
            elif orientation == 6:
                img = img.rotate(270, expand=True)
            elif orientation == 8:
                img = img.rotate(90, expand=True)
    except:
        pass
    return img

# --------------------------------------
# Set image as Windows wallpaper
# --------------------------------------
def set_wallpaper(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(path), 3)