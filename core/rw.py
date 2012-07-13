#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import os
import core
import sdl
import zipfile
from sdl import SDL_RWFromConstMem, SDL_RWFromFile, SDL_FreeRW

def parsePath(path):
	path_unicode = core.getUnicode(path).replace("\\", "/")
	i = path_unicode.rfind(">")
	if i == -1:
		return (None, core.getStr(path_unicode))
	else:
		arc_path = core.getStr(path_unicode[:i])
		res_path = core.getStr(path_unicode[i+1:])
		if not os.path.isfile(arc_path):
			return (None, arc_path+"/"+res_path)
		else:
			return (arc_path, res_path)

def getArchiveData(arc_path, res_path):
	"""You may need replace this function to load different type archive"""
	arc = zipfile.ZipFile(arc_path, "r")
	try:
		data = arc.read(res_path)
	finally:
		arc.close()
	return data

class RW:
	"""Remind: leave a referrer to this object (self.data) to
	avoid segmentation fault,
	and use SDL_RWFromConstMem not SDL_RWFromMem.
	"""
	def __init__(self, path):
		self.path = path
		arc_path, res_path = parsePath(path)
		core.logdebug("RW", arc_path, res_path)
		if arc_path:
			self.data = getArchiveData(arc_path, res_path)
			self.obj = SDL_RWFromConstMem(self.data, len(self.data))
		else:
			self.data = None
			self.obj = SDL_RWFromFile(res_path, "rb")
		if not self.obj:
			core.raisesdlerr()
	
	def __str__(self):
		return "%s[%s]"%(repr(self), self.path)
	
	def __del__(self):
		core.logdebug("del rw", self)
		#corrupted double-linked list if set freesrc to 1 in loadXXX_RW
		#SDL_FreeRW(self.obj)