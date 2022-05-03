#!/usr/bin/env python3

# I created this script to find images with a specific 
# width and height for carplay screenshots so they could
# be moved into a folder where I can easily review
# and delete them

import os
import shutil
from PIL import Image

path = "D:\Dropbox\Camera Uploads\\"
looking_width = 800
looking_height = 480
found_files = False

if __name__ == "__main__":
    print("starting cleanup-carplay")
    
    # for all files in the given directory
    for filename in os.listdir(path):
        file = os.path.join(path, filename)

        # checking if it is a file
        if os.path.isfile(file):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                # try reading file with image attributes
                try:
                    img = Image.open(file)

                    # check width and height for carplay dimensions
                    if img.width == looking_width and img.height == looking_height:
                        # tickler for found hits
                        if found_files == False:
                            found_files = True
                            print("Files are found, running script")
                        
                        # close the read from library so we can move the file
                        img.close()

                        # try moving files to carplay directory
                        try:
                            print("Trying to move", filename)
                            shutil.move(file, path + "\carplay\\" + filename)
                        except IOError as e:
                            print("Error trying to move", filename)
                            print(e)
                except IOError as e:
                    print("Error trying to read", filename)
                    print(e)