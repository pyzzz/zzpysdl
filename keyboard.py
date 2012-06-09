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
#why not use SDLK_{name}: search member in namespace sdl will spend more time
#need split keypress{name} to keydown_{name} and keypress_{name} ?
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

def keypress_escape():
	share.running = False
	keyup("escape")

def keypress_s():
	movie.play("data/test.mpg")
	keyupAll()
	keyup("s")

def keypress_d():
	movie.stop()
	keyup("d")

def keypress_q():
	music.bgm.play(0)
	keyup("q")

def keypress_w():
	music.bgm.pause()
	keyup("w")

def keypress_z():
	core.logdebug(music.bgm)
	for channel in music.channel:
		core.logdebug(channel)
	core.logdebug(movie.mpeg, movie.playing())
	keyup("z")

def keyup_z():
	#test keyup
	core.logdebug("keyup_z")

def keypress_left():
	if pressed("up"): keypress_up(True)
	elif pressed("down"): keypress_down(True)
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

def keypress_up(slash=False):
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

def keypress_right():
	if pressed("left"): return
	if pressed("up"): keypress_up(True)
	elif pressed("down"): keypress_down(True)
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

def keypress_down(slash=False):
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
	core.logdebug(share.img.getRect(), share.img.getScreenRect())
	draw.updateScreen()

class Key:
	def __init__(self, name):
		self.name = name
		self.name_keypress = "keypress_"+self.name
		self.name_keyup = "keyup_"+self.name
		self.lastTime = 0
		self.pressed = False
	
	def __str__(self):
		return "%s[%s, %s]"%(repr(self), self.name, self.pressed)
	
	def keydown(self):
		core.logdebug(self, "down")
		self.pressed = True
		self.procKeypress()
	
	def keyup(self):
		core.logdebug(self, "up")
		self.lastTime = 0
		self.pressed = False
		event = ns.get(self.name_keyup)
		if event: event()
	
	def keypress(self):
		#core.logdebug(self, "press")
		event = ns.get(self.name_keypress)
		if event: event()
	
	def procKeydown(self):
		if self.pressed:
			return False
		self.keydown()
		return True
	
	def procKeyup(self):
		if not self.pressed:
			return False
		self.keyup()
		return True
	
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
	if not (keyobj and keyobj.procKeydown()):
		core.logdebug(keyname, "down")

def keyup(keyname):
	keyobj = key.get(keyname)
	if not (keyobj and keyobj.procKeyup()):
		core.logdebug(keyname, "up")

def keyupAll():
	for n in key.itervalues():
		n.procKeyup()

def procKeypress():
	for n in key.itervalues():
		n.procKeypress()

for n in keyList:
	key[n] = Key(n)