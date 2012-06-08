#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sdl
import widget

class Image(widget.Widget):
	def __init__(self, path, scale=1.0):
		widget.Widget.__init__(self)
		self.path = path
		surface_orig = sdl.IMG_Load(path)
		if not surface_orig: raisesdlerr()
		
		#hasalpha = (surface_orig.contents.flags & sdl.SDL_SRCALPHA) == sdl.SDL_SRCALPHA
		#sdl.SDL_SetAlpha(surface_orig, sdl.SDL_SRCALPHA, sdl.SDL_ALPHA_TRANSPARENT)
		#performance increase
		surface_displayformat = sdl.SDL_DisplayFormatAlpha(surface_orig)
		if not surface_displayformat: raisesdlerr()
		sdl.SDL_FreeSurface(surface_orig)
		
		if scale == 1.0:
			self.surface = surface_displayformat
		else:
			self.surface = sdl.rotozoomSurface(surface_displayformat, scale, scale, 1)
			sdl.SDL_FreeSurface(surface_displayformat)
		
		self.setRect()
		self.setScreenRect()
	
	def __str__(self):
		return "%s[%s]"%(repr(self), self.path)
