#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sdl
import widget

class Label(widget.Widget):
	def __init__(self, label, font, r=0, g=0, b=0):
		widget.Widget.__init__(self)
		self.label = label
		self.color = sdl.SDL_Color(int(r), int(g), int(b))
		#Solid, Quick and Dirty
		#Shaded, Slow and Nice, but with a Solid Box
		#Blended, Slow Slow Slow, but Ultra Nice over another image
		self.surface = sdl.TTF_RenderUTF8_Blended(
			font,
			label,
			self.color,
		)
		if not self.surface: raisesdlerr()
		
		#didn't need SDL_DisplayFormatAlpha
		
		self.setRect()
		self.setScreenRect()
	def __str__(self):
		return "%s[%s]"%(repr(self), self.label)
