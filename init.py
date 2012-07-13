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
from core import animation
from core import rw

def initFont():
	share.font = sdl.TTF_OpenFont(define.fontPath, define.fontDefaultSize)
	if not share.font: core.raisesdlerr()
	
	share.font_outline = sdl.TTF_OpenFont(define.fontPath, define.fontDefaultSize)
	if not share.font_outline: core.raisesdlerr()
	sdl.TTF_SetFontOutline(share.font_outline, 1)

def startDelTest():
	for i in xrange(1):
		img_deltest = image.Image("data/bin>img.png", 0.5)
		img_subdeltest = image.SubImage(img_deltest)
		label_deltest = label.Label("test", share.font)
		music_deltest = music.Music("data/bin>noise.wav")
		chunk_deltest = music.Chunk("data/bin>noise.wav")

def initTest():
	startDelTest()
	img_master = image.Image("data/bin>img.png", 1.0)
	img_sub = image.SubImage(img_master)
	
	share.img = img_sub
	#share.img.moveScreenRect(xdiff=-300, ydiff=-400)
	share.img.moveScreenRect(xdiff=-100, ydiff=-500)
	share.img.moveScreenRect(xdiff=-200, ydiff=100)
	
	share.label = label.Label("test", share.font)
	share.label.setLabel("test setLabel", share.font)
	share.label.setScreenRectCenter()
	share.label.moveScreenRect(ydiff=100)
	
	noise = music.Music("data/bin>noise.wav")
	noisec = music.Chunk("data/bin>noise.wav")
	music.bgm.load(noise)
	#music.bgm.play(0)
	music.channel[0].load(noisec)
	#music.channel[0].play(0)
	
	share.anime_img = image.Image("data/bin>anime.png")
	share.anime = animation.Animation(0.5, (
		image.SubImage(share.anime_img, i%5*192, i/5*192, 192, 192) for i in xrange(13)
	))
	share.anime.setScreenRectCenter()

def init():
	initFont()
	initTest()