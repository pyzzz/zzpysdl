#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import traceback
import time
from core import core
#from core import sdl
from core import music
from core import movie
from core.sdl import SDL_QUIT, SDL_KEYDOWN, SDL_KEYUP
from core.sdl import SDL_GetKeyName
import init
import share
import define
import keyboard
import draw

def mainLoop():
	procStartTime = time.time()
	procEndTime = time.time()
	draw.updateScreen()
	while share.running:
		procEndTime = time.time()
		sleepTime = define.drawDelay-(procEndTime-procStartTime)
		#core.logdebug("sleep", sleepTime)
		if sleepTime > 0:
			time.sleep(define.drawDelay-(procEndTime-procStartTime))
		procStartTime = time.time()
		draw.drawScreen()
		keyboard.procKeypress()
		while core.pollEvent():
			evtype = core.event.type
			if evtype == SDL_QUIT:
				core.log("SDL_QUIT event")
				share.running = False
			elif evtype == SDL_KEYDOWN:
				#str(core.sdl.String)
				keyboard.keydown(str(SDL_GetKeyName(core.event.key.keysym.sym)))
			elif evtype == SDL_KEYUP:
				keyboard.keyup(str(SDL_GetKeyName(core.event.key.keysym.sym)))

if __name__ == "__main__":
	try:
		#switch work dir to script dir
		os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
		#core.screenVideoMode = sdl.SDL_SWSURFACE
		#core.screenVideoMode |= sdl.SDL_FULLSCREEN
		core.init(
			define.windowWidth,
			define.windowHeight,
			define.windowBpp,
			define.windowTitle,
		)
		init.init()
		keyboard.init()
		mainLoop()
	except:
		core.logtraceerr()
	core.exitapp()