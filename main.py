#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import traceback
import time
from ctypes import byref
from core import core
from core import sdl
from core import music
from core import movie
import init
import share
import define

def drawScreen():
	if movie.playing():
		time.sleep(define.playingDelay)
		return
	if not core.lockSurface(core.screen):
		return
	
	sdl.SDL_FillRect(core.screen, None, define.defaultBackGround)
	share.img.draw()
	share.label.draw()
	sdl.SDL_Flip(core.screen)
	
	core.unlockSurface(core.screen)

def mainLoop():
	while share.running:
		time.sleep(define.drawDelay)
		drawScreen()
		#if just pass to function should use ctypes.byref, it's fast than ctypes.pointer
		while sdl.SDL_PollEvent(byref(share.event)):
			evtype = share.event.type
			if evtype == sdl.SDL_QUIT:
				core.log("SDL_QUIT event")
				share.running = False
			elif evtype == sdl.SDL_KEYDOWN:
				key = share.event.key.keysym.sym
				core.log(key, sdl.SDL_GetKeyName(key))
				if key == sdl.SDLK_ESCAPE:
					share.running = False
				elif key == sdl.SDLK_s:
					movie.play("data/test.mpg")
				elif key == sdl.SDLK_d:
					movie.stop()
				elif key == sdl.SDLK_q:
					music.bgm.play(1)
				elif key == sdl.SDLK_w:
					music.bgm.pause()
				elif key == sdl.SDLK_z:
					core.logdebug(music.bgm)
					for channel in music.channel:
						core.logdebug(channel)
					core.logdebug(movie.mpeg, movie.playing())

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