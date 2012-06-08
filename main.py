#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import traceback
import time
from core import core
from core import sdl
from core import music
from core import movie
import init
import share
import define

def updateScreen():
	share.screen_changed = True

def drawScreen():
	if movie.playing():
		time.sleep(define.playingDelay)
		return
	if not core.lockSurface(core.screen):
		return
	if share.screen_changed:
		sdl.SDL_FillRect(core.screen, None, define.defaultBackGround)
		share.img.draw()
		share.label.draw()
		share.screen_changed = False
	core.unlockSurface(core.screen)
	sdl.SDL_Flip(core.screen) #should not be called while screen is locked ?

def mainLoop():
	updateScreen()
	while share.running:
		time.sleep(define.drawDelay)
		drawScreen()
		while core.pollEvent():
			evtype = core.event.type
			if evtype == sdl.SDL_QUIT:
				core.log("SDL_QUIT event")
				share.running = False
			elif evtype == sdl.SDL_KEYDOWN:
				key = core.event.key.keysym.sym
				core.log(key, sdl.SDL_GetKeyName(key))
				if key == sdl.SDLK_ESCAPE:
					share.running = False
				elif key == sdl.SDLK_s:
					movie.play("data/test.mpg")
				elif key == sdl.SDLK_d:
					movie.stop()
				elif key == sdl.SDLK_q:
					music.bgm.play(0)
				elif key == sdl.SDLK_w:
					music.bgm.pause()
				elif key == sdl.SDLK_z:
					core.logdebug(music.bgm)
					for channel in music.channel:
						core.logdebug(channel)
					core.logdebug(movie.mpeg, movie.playing())
				elif key in (sdl.SDLK_LEFT, sdl.SDLK_UP,
						sdl.SDLK_RIGHT, sdl.SDLK_DOWN):
					if key == sdl.SDLK_LEFT: share.img.moveScreenRect(xdiff=100)
					elif key == sdl.SDLK_UP: share.img.moveScreenRect(ydiff=100)
					elif key == sdl.SDLK_RIGHT: share.img.moveScreenRect(xdiff=-100)
					elif key == sdl.SDLK_DOWN: share.img.moveScreenRect(ydiff=-100)
					core.logdebug(share.img.getRect(), share.img.getScreenRect())
					updateScreen()

if __name__ == "__main__":
	try:
		core.init(
			define.windowWidth,
			define.windowHeight,
			define.windowBpp,
			define.windowTitle,
		)
		init.init()
		mainLoop()
	except:
		core.logtraceerr()
	core.exitapp()