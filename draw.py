#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import traceback
import time
from core import core
from core import sdl
from core import movie
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