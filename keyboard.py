#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import time
from core import sdl
from core import image
from core import core
from core import music
from core import movie
import define
import share
import draw
key = {}
ns = globals()
keyList = (
	"escape",
	"s",
	"d",
	"q",
	"w",
	"z",
	"left",
	"up",
	"right",
	"down",
)

def press_escape():
	keyup("escape")
	share.running = False

def press_s():
	keyup("s")
	movie.play("data/test.mpg")

def press_d():
	keyup("d")
	movie.stop()

def press_q():
	keyup("q")
	music.bgm.play(0)

def press_w():
	keyup("w")
	music.bgm.pause()

def press_z():
	keyup("z")
	core.logdebug(music.bgm)
	for channel in music.channel:
		core.logdebug(channel)
	core.logdebug(movie.mpeg, movie.playing())

def press_left():
	if pressed("up"): press_up(True)
	elif pressed("down"): press_down(True)
	x, y = share.img.getScreenRect()
	ix, iy, iw, ih = share.img.getRect()
	maxx = max(0, define.windowWidth-iw)
	if x == maxx:
		return
	if x+define.moveDistance <= maxx:
		share.img.moveScreenRect(xdiff=define.moveDistance)
	else:
		share.img.setScreenRect(x=maxx)
	core.logdebug(share.img.getRect(), share.img.getScreenRect())
	draw.updateScreen()

def press_up(slash=False):
	if not slash and (pressed("left") or pressed("right")): return
	x, y = share.img.getScreenRect()
	ix, iy, iw, ih = share.img.getRect()
	maxy = max(0, define.windowHeight-ih)
	if y == maxy:
		return
	if y+define.moveDistance <= maxy:
		share.img.moveScreenRect(ydiff=define.moveDistance)
	else:
		share.img.setScreenRect(y=maxy)
	core.logdebug(share.img.getRect(), share.img.getScreenRect())
	draw.updateScreen()

def press_right():
	if pressed("left"): return
	if pressed("up"): press_up(True)
	elif pressed("down"): press_down(True)
	x, y = share.img.getScreenRect()
	ix, iy, iw, ih = share.img.getRect()
	minx = min(0, define.windowWidth-iw)
	if x == minx:
		return
	elif x-define.moveDistance >= minx:
		share.img.moveScreenRect(xdiff=-define.moveDistance)
	else:
		share.img.setScreenRect(x=minx)
	core.logdebug(share.img.getRect(), share.img.getScreenRect())
	draw.updateScreen()

def press_down(slash=False):
	if pressed("up"): return
	if not slash and (pressed("left") or pressed("right")): return
	x, y = share.img.getScreenRect()
	ix, iy, iw, ih = share.img.getRect()
	miny = min(0, define.windowHeight-ih)
	if y == miny:
		return
	elif y-define.moveDistance >= miny:
		share.img.moveScreenRect(ydiff=-define.moveDistance)
	else:
		share.img.setScreenRect(y=miny)
	#core.logdebug(share.img.getRect(), share.img.getScreenRect())
	draw.updateScreen()

class Key:
	def __init__(self, name):
		self.name = name
		self.name_event = "press_"+self.name
		self.lastTime = 0
		self.pressed = False
	
	def __str__(self):
		return "%s[%s, %s]"%(repr(self), self.name, self.pressed)
	
	def keydown(self):
		self.pressed = True
		self.procKeypress()
	
	def keyup(self):
		self.lastTime = 0
		self.pressed = False
	
	def keypress(self):
		event = ns.get(self.name_event)
		if event: event()
	
	def procKeypress(self):
		if not self.pressed:
			return
		if not self.lastTime:
			self.lastTime = time.time()
			self.keypress()
			return
		lasttime = time.time()
		while lasttime - self.lastTime > define.keyPressedDelay:
			self.lastTime += define.keyPressedDelay
			self.keypress()

def pressed(keyname):
	keyobj = key.get(keyname)
	if not keyobj:
		return None
	return keyobj.pressed

def keydown(keyname):
	keyobj = key.get(keyname)
	if keyobj:
		if keyobj.pressed:
			return
		keyobj.keydown()
		core.logdebug(keyobj, "down")
	else:
		core.logdebug(keyname, "down")

def keyup(keyname):
	keyobj = key.get(keyname)
	if keyobj:
		if not keyobj.pressed:
			return
		keyobj.keyup()
		core.logdebug(keyobj, "up")
	else:
		core.logdebug(keyname, "up")

def procKeypress():
	for n in key.itervalues():
		n.procKeypress()

for n in keyList:
	key[n] = Key(n)