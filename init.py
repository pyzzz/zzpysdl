#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import define
import share
from core import sdl
from core import core
from core import image
from core import label
from core import music

def initFont():
	share.font = sdl.TTF_OpenFont(define.fontPath, define.fontDefaultSize)
	if not share.font: core.raisesdlerr()
	
	share.font_outline = sdl.TTF_OpenFont(define.fontPath, define.fontDefaultSize)
	if not share.font_outline: core.raisesdlerr()
	sdl.TTF_SetFontOutline(share.font_outline, 1)

def update():
	pass

def initTest():
	img_deltest = image.Image("data/img.png", 0.5)
	share.img = image.Image("data/img.png", 1.0)
	share.img.setScreenRect(0, 0)
	#share.img.moveScreenRect(xdiff=-500, ydiff=-400)
	share.img.moveScreenRect(xdiff=-300, ydiff=-500)
	share.img.moveScreenRect(xdiff=-200, ydiff=100)
	share.label = label.Label("test", share.font)
	share.label.moveScreenRect(ydiff=100)
	noise = music.Music("data/noise.wav")
	noisec = music.Chunk("data/noise.wav")
	music.bgm.load(noise)
	#music.bgm.play(0)

def init():
	initFont()
	initTest()