#!/usr/bin/env python
# -*- coding:utf-8 -*-
import widget
import core
from sdl import IMG_Load, SDL_DisplayFormatAlpha, SDL_FreeSurface, rotozoomSurface

class Image(widget.Widget):
	def __init__(self, path, scale=1.0):
		widget.Widget.__init__(self)
		self.path = path
		surface_orig = IMG_Load(path)
		if not surface_orig: core.raisesdlerr()
		
		#hasalpha = (surface_orig.contents.flags & SDL_SRCALPHA) == SDL_SRCALPHA
		#SDL_SetAlpha(surface_orig, SDL_SRCALPHA, SDL_ALPHA_TRANSPARENT)
		#performance increase
		surface_displayformat = SDL_DisplayFormatAlpha(surface_orig)
		if not surface_displayformat: core.raisesdlerr()
		SDL_FreeSurface(surface_orig)
		
		if scale == 1.0:
			self.surface = surface_displayformat
		else:
			self.surface = rotozoomSurface(surface_displayformat, scale, scale, 1)
			SDL_FreeSurface(surface_displayformat)
		
		self.setRect()
		self.setScreenRectCenter()
	
	def __str__(self):
		return "%s[%s]"%(repr(self), self.path)

class SubImage(widget.Widget):
	def __init__(self, master):
		if not isinstance(master, Image):
			raise Exception("not isinstance(master, Image) %s"%master)
		widget.Widget.__init__(self)
		self.master = master #reference count += 1
		self.surface = self.master.surface
		self.setRect()
		self.setScreenRectCenter()
	
	def __del__(self):
		"""replace Widget.__del__
		won't call SDL_FreeSurface
		master reference count -= 1
		"""
		core.logdebug("del widget without SDL_FreeSurface", self)
	
	def __str__(self):
		return "%s[%s]"%(repr(self), self.master)