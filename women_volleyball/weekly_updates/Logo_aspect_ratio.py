#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image
# This runs on Python 3.6

# os.chdir("C:\\Users\\cesargb\\Documents\\Boricuas_NCAA\\Season_Summary_2019_2020\\Women\\School_Logos")

def write_image_sizes(image_dir, image_type = ".gif"):
  os.chdir(image_dir)
  img_sizes_filename = 'filesizes_' + image_type[1:] + '.csv'
  with open(img_sizes_filename, "w", encoding='utf8') as f:
    with os.scandir(image_dir) as dir:
      for file in dir:
        filename_w_ext = os.path.basename(file)
        filename, file_extension = os.path.splitext(filename_w_ext)
        if file_extension != image_type: continue
        im = Image.open(filename_w_ext)
        width, height = im.size
        f.write(filename + "," + str(width) + "," + str(height) + "\n")

# with open('filesizes.csv', "w") as f:
  # with os.scandir("C:\\Users\\cesargb\\Documents\\Boricuas_NCAA\\Season_Summary_2019_2020\\Women\\School_Logos") as dir:
    # for file in dir:
      # filename_w_ext = os.path.basename(file)
      # filename, file_extension = os.path.splitext(filename_w_ext)
      # try:
        # im = Image.open(filename_w_ext)
      # except OSError: # Thumbs.db or some other non-image
        # continue
      # width, height = im.size
      # f.write(filename + "," + str(width) + "," + str(height) + "\n")

# os.chdir("C:\\Users\\cesargb\\Documents\\Boricuas_NCAA\\Season_Summary_2019_2020\\Women\\Conference_Logos")
      
# with open('filesizes.csv', "w") as f:
  # with os.scandir("C:\\Users\\cesargb\\Documents\\Boricuas_NCAA\\Season_Summary_2019_2020\\Women\\Conference_Logos") as dir:
    # for file in dir:
      # filename_w_ext = os.path.basename(file)
      # filename, file_extension = os.path.splitext(filename_w_ext)
      # try:
        # im = Image.open(filename_w_ext)
      # except OSError: # Thumbs.db or some other non-image
        # continue
      # width, height = im.size
      # f.write(filename + "," + str(width) + "," + str(height) + "\n")
      
image_dir = "C:\\Users\\cesargb\\Documents\\Boricuas_NCAA_2021_2022\\women_volleyball\\weekly_updates\\School_Logos"
write_image_sizes(image_dir)

image_dir = "C:\\Users\\cesargb\\Documents\\Boricuas_NCAA_2021_2022\\women_volleyball\\weekly_updates\\Conference_logos"
write_image_sizes(image_dir, ".png")

# image_dir = "C:\\Users\\cesargb\\Documents\\Boricuas_NCAA\\Season_Summary_2019_2020\\Women\\Escudos"
# write_image_sizes(image_dir, ".jpg")

# image_dir = "C:\\Users\\cesargb\\Documents\\Boricuas_NCAA\\Season_Summary_2019_2020\\Women\\Escuelas"
# write_image_sizes(image_dir, ".png")

# image_dir = "C:\\Users\\cesargb\\Documents\\Boricuas_NCAA\\Season_Summary_2019_2020\\Women\\Tournament_Logos"
# write_image_sizes(image_dir, ".png")