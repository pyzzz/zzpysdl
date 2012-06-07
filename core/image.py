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
		if scale == 1.0:
			self.surface = surface_orig
		else:
			self.surface = sdl.zoomSurface(surface_orig, scale, scale, True)
			sdl.SDL_FreeSurface(surface_orig)
		self.setRect()
		self.setScreenRect()
	def __str__(self):
		return "%s[%s]"%(repr(self), self.path)
