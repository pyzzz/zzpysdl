#!/usr/bin/env python
# -*- coding:utf-8 -*-
import core
import widget
from sdl import SDL_Color, TTF_RenderUTF8_Blended, SDL_FreeSurface

class Label(widget.Widget):
	def __init__(self, label, font, r=0, g=0, b=0):
		widget.Widget.__init__(self)
		self.label = label
		self.color = SDL_Color(int(r), int(g), int(b))
		#Solid, Quick and Dirty
		#Shaded, Slow and Nice, but with a Solid Box
		#Blended, Slow Slow Slow, but Ultra Nice over another image
		self.surface = TTF_RenderUTF8_Blended(
			font,
			label,
			self.color,
		)
		if not self.surface: core.raisesdlerr()
		
		#didn't need SDL_DisplayFormatAlpha
		self.resetSize()
		self.setRect()
		self.setScreenRect(0, 0)
	
	def __str__(self):
		return "%s[%s]"%(repr(self), self.label)
	
	def setLabel(self, label, font, r=0, g=0, b=0):
		color = SDL_Color(int(r), int(g), int(b))
		surface_prev = self.surface
		surface_next = TTF_RenderUTF8_Blended(
			font,
			label,
			color,
		)
		if not self.surface:
			logsdlerr()
			return
		self.label = label
		self.color = color
		self.surface = surface_next
		SDL_FreeSurface(surface_prev)
		self.resetSize()