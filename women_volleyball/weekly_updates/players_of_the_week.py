#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (36, 36, 0, 0)

# Dictionary of logos' height/width aspect ratios. It is used to position the school logo
# There's no way to programatically adjust frame to image.
# The Python Scribus uses doesn't have any image utilities like PIL so I could not
# figure out a way to determine the image's aspect ratio programatically. :|
# There is a program I wrote called Logo_aspect_ratio.py that takes all the images files
# in a directory and generates a CSV file of their width and height. The program is located in 
# the Women directory. After you run that program, you can run this one.

school_logos_dict = {}
with open("./School_Logos/filesizes_gif.csv") as f:
  for line in f:
    current_line_list = line.split(",")
    school_logos_dict[current_line_list[0]] = float(current_line_list[2]) / float (current_line_list[1])

conf_logos_dict = {}
with open("./Conference_Logos/filesizes_png.csv") as f:
  for line in f:
    current_line_list = line.split(",")
    conf_logos_dict[current_line_list[0]] = float(current_line_list[2]) / float (current_line_list[1])
    
players_list = []
current_week = "2"
with open("./week_" + current_week + "/players_of_the_week_" + current_week + ".csv") as f:
  next(f) # skip headers row
  for line in f:
    current_line_list = line.split(",")
    full_name = current_line_list[0].split()
    player_name = " ".join(full_name)
    # first_name = full_name[0]
    # first_last_name = full_name[1]
    # if (full_name[1] == "de" or full_name[1] == "La"):
      # player_name = full_name[0] + " " + full_name[1] + " " + full_name[2]
    # else:
      # player_name = first_name + " " + first_last_name
      
    # image_filename = first_name + "_" + first_last_name + ".jpg"
    image_filename = "_".join(full_name) + ".jpg"
    player_school = current_line_list[2]
    school_state = current_line_list[3]
    if current_line_list[3] == "Washington D.C.": school_state = "Washington, D.C."
    player_conf = current_line_list[4]
    school_division = current_line_list[5]
    player_award = current_line_list[6]
    award_date = current_line_list[8]
    photo_credit = current_line_list[10]
    
    single_player_list = [player_name, image_filename, player_school, school_state, player_conf, school_division, player_award, award_date, photo_credit]
    players_list.append(single_player_list)


if newDocument(PAPER_LETTER, margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  defineColor("NJCAA Gray 2", 0, 0, 0, 153)
  defineColor("NJCAA Blue 2", 221, 168, 15, 30)
  defineColor("Darker Gray", 0, 0, 0, 64)
  
  player_count = 0
  for current_player in players_list:
  
    award_rect_height = 60
    award_rect = createRect(0, 0, 612, award_rect_height)
    setFillColor("NJCAA Blue", award_rect); setLineColor("NJCAA Blue", award_rect)
  
    conf_rect_height = 37
    conf_rect = createRect(0, award_rect_height, 612, conf_rect_height)
    setFillColor("White", conf_rect); setLineColor("White", conf_rect)
  
    star_1 = createImage(6,  5, 50, 50)
    loadImage("Star.png", star_1); setScaleImageToFrame(1, 1, star_1)
    star_2 = createImage(554, 5, 50, 50)
    loadImage("Star.png", star_2); setScaleImageToFrame(1, 1, star_2)
  
    award_text = createText(0, 20, 612, award_rect_height)
    award_name = current_player[6]
    insertText(award_name, -1, award_text)
    if "National" in award_name: award_text_size = 22 
    else: award_text_size = 26
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", award_text); setFontSize(award_text_size, award_text)
    setTextColor("White", award_text); setTextAlignment(ALIGN_CENTERED, award_text)
  
    conf_text = createText(0, 70, 612, conf_rect_height)
    if "National" in award_name: conf_name = current_player[5].replace("D", "Division ")
    else: conf_name = current_player[4]
    insertText(conf_name, -1, conf_text)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", conf_text); setFontSize(20, conf_text)
    setTextColor("NJCAA Blue", conf_text); setTextAlignment(ALIGN_CENTERED, conf_text)
  
    player_height = 612
    player_image = current_player[1]
    player = createImage(0, (award_rect_height + conf_rect_height), 612, player_height)
    loadImage("./week_" + current_week + "/" + player_image, player); setScaleImageToFrame(1, 1, player)
    
    date_rect = createRect(612 - 75, award_rect_height + conf_rect_height + 1, 75, 30)
    setFillColor("NJCAA Blue", date_rect); setLineColor("NJCAA Blue", date_rect)
    date_text = createText(612 - 75, award_rect_height + conf_rect_height + 10, 75, 30)
    award_date = current_player[7]
    insertText(award_date, -1, date_text)
    setFont("Asimov Print C", date_text); setFontSize(15, date_text)
    setTextColor("White", date_text); setTextAlignment(ALIGN_CENTERED, date_text)
    
    if (current_player[5].replace("\n","") in ["NCAA DI", "NCAA DII", "NCAA DIII", "NJCAA DI", "NJCAA DII"]):
      division_y = (award_rect_height + conf_rect_height) + 15
      division_height = 65
      player_division = createImage(15, division_y, 65, division_height)
    else:
      division_y = (award_rect_height + conf_rect_height) + 20
      division_height = 32
      player_division = createImage(15, division_y, 65, division_height)
    loadImage("./Division_logos/" + current_player[5].replace(" ", "_").replace("\n","") + "_logo.png", player_division); setScaleImageToFrame(1, 1, player_division)
    
    player_conf_img = current_player[4].replace(" ", "_")
    if (conf_logos_dict[player_conf_img] < 0.7): # C-USA and ASUN are very wide
      player_conf_logo_w = 65.0
      player_conf_logo_h = min(player_conf_logo_w * conf_logos_dict[player_conf_img], 44.0)
    else:
      player_conf_logo_h = 44.0
      player_conf_logo_w = min(player_conf_logo_h / conf_logos_dict[player_conf_img], 65.0)
    conf_logo = createImage(15 + 65/2 - player_conf_logo_w/2, (award_rect_height + conf_rect_height + division_height + 30), player_conf_logo_w, player_conf_logo_h)
    loadImage("./Conference_Logos/" + player_conf_img + ".png", conf_logo); setScaleImageToFrame(1, 1, conf_logo)
    
    credit_rect = createRect(612 - 275, award_rect_height + conf_rect_height + player_height - 20, 275, 20)
    setFillColor("NJCAA Blue", credit_rect); setLineColor("NJCAA Blue", credit_rect)
    credit_text = createText(612 - 275, award_rect_height + conf_rect_height + player_height - 20 + 4, 275, 20)
    credit = "Photo: " + current_player[8]
    insertText(credit, -1, credit_text)
    setFont("Asimov Print C", credit_text); setFontSize(13, credit_text)
    setTextColor("White", credit_text); setTextAlignment(ALIGN_CENTERED, credit_text)
        
    player_banner_y = player_height + conf_rect_height + award_rect_height
    player_banner_height = 792 - player_banner_y
    player_rect = createRect(0, player_height + conf_rect_height + award_rect_height, 612, player_banner_height)
    setFillColor("White", player_rect); setLineColor("None", player_rect)
    
    logo_name = current_player[2].replace(" ", "_")
    if (school_logos_dict[logo_name] < 0.7):
      logo_width = 80.0
      logo_height = min(logo_width * school_logos_dict[logo_name], 68)
    else:
      logo_height = 68.0
      logo_width = min(logo_height / school_logos_dict[logo_name], 80)
    logo_ypos = (player_banner_y + (player_banner_height - logo_height) / 2.0)
    school_logo = createImage(15, logo_ypos, logo_width, logo_height)
    loadImage("./School_Logos/" + logo_name + ".gif", school_logo); setScaleImageToFrame(1, 1, school_logo)
    
    vocales_acentos = ["Á", "É", "Í", "Ó", "Ú", "Ñ"]
    if any(x in unicode(current_player[0]).upper() for x in vocales_acentos): player_name_ypos = player_banner_y + 2
    else: player_name_ypos = player_banner_y + 4
    player_name = createText(100, player_name_ypos - 1, 514, 85)
    insertText(unicode(current_player[0]).upper() + "\n", -1, player_name)
    setFont("Asimov Print C", player_name)
    if "Dariana" in current_player[0]: setFontSize(26, player_name)
    else: setFontSize(30, player_name)
    name_length = getTextLength(player_name)
    player_school = current_player[2]
    school_length = len(player_school) + 1
    insertText(unicode(player_school).upper() + "\n", -1, player_name)
    selectText(name_length, school_length, player_name)
    setFont("OLD SPORT 02 ATHLETIC NCV Regular", player_name)
    selectText(name_length, len(player_school), player_name); setFontSize(15.2, player_name)
    school_state = current_player[3]
    insertText(school_state, -1, player_name)
    selectText(name_length + school_length, len(school_state), player_name)
    setFont("Playball Regular", player_name)
    selectText(name_length + school_length, len(school_state), player_name); setFontSize(21, player_name)
    setTextColor("NJCAA Blue", player_name)
    setLineSpacing(24, player_name)
    setTextAlignment(ALIGN_CENTERED, player_name)
  
    player_count += 1
    if player_count < len(players_list): newPage(-1)
    
  import os
  cwd = os.path.abspath(os.getcwd())
  saveDocAs(cwd + "\week_" + current_week + "\\" + "Players_of_the_Week_week_" + current_week + ".sla")