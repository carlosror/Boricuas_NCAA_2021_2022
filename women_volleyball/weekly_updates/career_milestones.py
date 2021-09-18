#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scribus import *
margins = (0, 0, 0, 0)

doc_w = 1200
doc_h = 675

if newDocument((1200, 675), margins, PORTRAIT, 1,  UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):

  defineColor("NJCAA Blue", 217, 168, 55, 94)
  defineColor("NJCAA Gray", 0, 0, 0, 40)
  
  background_rect = createRect(0, 0, doc_w, doc_h)
  setFillColor("NJCAA Gray", background_rect); setLineColor("NJCAA Gray", background_rect)
  
  top_rect_height = doc_h / 30.0
  top_rect = createRect(0, 0, 1200, top_rect_height)
  setFillColor("NJCAA Blue", top_rect); setLineColor("NJCAA Blue", top_rect)
  
  player_img = createImage(doc_w * (5.0 / 12),  doc_h * (1.0 / 30), doc_w * (7.0 / 12), doc_h * (29.0 / 30))
  loadImage("./week_2/Dariana_Hollingsworth_Santana_2.jpg", player_img); setScaleImageToFrame(1, 1, player_img)