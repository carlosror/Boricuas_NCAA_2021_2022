#!/usr/bin/env python
# -*- coding: utf-8 -*-

current_week = "1"
with open("./week_" + current_week + "/Facebook_text_week_" + current_week + ".txt", mode = 'w') as out:
  out.write("Jugadoras de la Semana\n\n")
  with open("./week_" + current_week + "/players_of_the_week_" + current_week + ".csv") as f:
    next(f) # skip headers row
    for line in f:
      current_line_list = line.split(",")
      full_name = current_line_list[0].split()
      player_name = " ".join(full_name)
      player_hometown = current_line_list[1]
      player_school = current_line_list[2]
      school_state = current_line_list[3]
      player_conf = current_line_list[4]
      school_division = current_line_list[5]
      player_award = current_line_list[7]
      notes = current_line_list[11].replace("\n", "").replace('"', '')
      out.write(player_name + " (" + player_hometown + ", " + player_school + " en " + school_state + ", " + school_division + ") ")
      out.write("es nombrada " + player_award + " en la " + player_conf + ". ")
      out.write(notes + "\n")
  out.write("\nPartidos Destacados\n\n")
  with open("./week_" + current_week + "/outstanding_matches_week_" + current_week + ".csv") as f:
    next(f) # skip headers row
    for line in f:
      current_line_list = line.split(",")
      full_name = current_line_list[0].split()
      player_name = " ".join(full_name)
      player_hometown = current_line_list[1]
      player_school = current_line_list[2]
      school_state = current_line_list[3]
      player_conf = current_line_list[4]
      school_division = current_line_list[5]
      player_performance = current_line_list[7]
      notes = current_line_list[10].replace("\n", "").replace('"', '')
      out.write(player_name + " (" + player_hometown + ", " + player_school + " en " + school_state + ", " + school_division + ") - ")
      out.write(player_performance + ". " + notes + "\n")