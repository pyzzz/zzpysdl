#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import sdl
import core
import smpeg
import music
from ctypes import byref
info = None
mpeg = None

def playing():
	if mpeg:
		return (smpeg.SMPEG_status(mpeg) == smpeg.SMPEG_PLAYING)
	else:
		return False

def stop():
	global info, mpeg
	if mpeg:
		smpeg.SMPEG_stop(mpeg)
		smpeg.SMPEG_delete(mpeg)
	info = None
	mpeg = None

def play(path, volume=100):
	#why not split load and play: smpeg need keep audio device open by itself ...
	global info, mpeg
	music.closeAudio()
	stop()
	info = smpeg.SMPEG_Info()
	mpeg = smpeg.SMPEG_new(path, byref(info), 1)
	error = smpeg.SMPEG_error(mpeg)
	if error:
		core.logdebug("movie play error:", error)
		stop()
		return
	smpeg.SMPEG_enableaudio(mpeg, 1)
	smpeg.SMPEG_enablevideo(mpeg, 1)
	smpeg.SMPEG_setvolume(mpeg, volume)
	smpeg.SMPEG_setdisplay(mpeg, core.screen, None, smpeg.SMPEG_DisplayCallback())
	smpeg.SMPEG_move(mpeg, 0, 0)
	smpeg.SMPEG_scaleXY(mpeg, core.screen.contents.w, core.screen.contents.h)
	smpeg.SMPEG_play(mpeg)