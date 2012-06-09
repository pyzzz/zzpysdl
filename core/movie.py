#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import sdl
import core
import music
import time
from ctypes import byref
from smpeg import SMPEG_status, SMPEG_PLAYING, SMPEG_Info
from smpeg import SMPEG_play, SMPEG_stop, SMPEG_new, SMPEG_delete, SMPEG_error
from smpeg import SMPEG_enableaudio, SMPEG_enablevideo, SMPEG_setvolume
from smpeg import SMPEG_setdisplay, SMPEG_DisplayCallback
from smpeg import SMPEG_move, SMPEG_scaleXY
info = None
mpeg = None
playDelay = 1.0

def playing():
	if mpeg:
		return (SMPEG_status(mpeg) == SMPEG_PLAYING)
	else:
		return False

def stop():
	global info, mpeg
	if mpeg:
		SMPEG_stop(mpeg) #should check playing or not ?
		SMPEG_delete(mpeg)
	info = None
	mpeg = None

def play(path, volume=100):
	#why not split load and play: smpeg need keep audio device open by itself ...
	global info, mpeg
	if playing():
		core.logdebug("movie play canceled: movie playing")
		return
	music.closeAudio()
	#stop()
	info = SMPEG_Info()
	mpeg = SMPEG_new(path, byref(info), 1)
	error = SMPEG_error(mpeg)
	if error:
		core.logdebug("movie play error:", error)
		stop()
		return
	SMPEG_enableaudio(mpeg, 1)
	SMPEG_enablevideo(mpeg, 1)
	SMPEG_setvolume(mpeg, volume)
	SMPEG_setdisplay(mpeg, core.screen, None, SMPEG_DisplayCallback())
	SMPEG_move(mpeg, 0, 0)
	SMPEG_scaleXY(mpeg, core.screen.contents.w, core.screen.contents.h)
	SMPEG_play(mpeg)
	#event queue will broken if stop before play start
	time.sleep(playDelay)
	core.clearEvent()