#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import core
#import threading
from ctypes import byref
#reduce search time (about 50%)
from sdl import SDL_BlitSurface, SDL_Rect, SDL_FreeSurface

class Widget:
	def __init__(self):
		self.surface = None
		#allow minus value
		self._rect = SDL_Rect()
		self._screen_rect = SDL_Rect()
		#convert _rect, _screen_rect to rect, screen_rect, repair minus value
		self.rect = SDL_Rect()
		self.screen_rect = SDL_Rect()
		#self.lock = threading.RLock() #include thread safe but performance decrease ?
	
	def __del__(self):
		core.logdebug("del widget", self)
		SDL_FreeSurface(self.surface)
	
	def _setupRect(self):
		self.rect.x = self._rect.x
		self.rect.y = self._rect.y
		self.rect.w = self._rect.w
		self.rect.h = self._rect.h
		self.screen_rect.x = self._screen_rect.x
		self.screen_rect.y = self._screen_rect.y
		#self.screen_rect.w = self._screen_rect.w
		#self.screen_rect.h = self._screen_rect.h
		if self.screen_rect.x < 0:
			self.rect.x += abs(self.screen_rect.x)
			self.screen_rect.x = 0
		if self.screen_rect.y < 0:
			self.rect.y += abs(self.screen_rect.y)
			self.screen_rect.y = 0
	
	def resetSize(self):
		#call when surface changed, don't call in SubImage
		self._rect.w = int(self.surface.contents.w)
		self._rect.h = int(self.surface.contents.h)
		self._setupRect()
	
	def setSize(self, w=None, h=None):
		if w != None: self._rect.w = int(w)
		if h != None: self._rect.h = int(h)
		self._setupRect()
	
	def setRect(self, x=None, y=None):
		if x != None: self._rect.x = int(x)
		if y != None: self._rect.y = int(y)
		self._setupRect()
	
	def setScreenRect(self, x=None, y=None):
		if x != None: self._screen_rect.x = int(x)
		if y != None: self._screen_rect.y = int(y)
		self._setupRect()
	
	def setScreenRectCenter(self, x=None, y=None):
		w, h = self.getSize()
		self._screen_rect.x = int((x == None) and (core.screen_w - w)/2 or x)
		self._screen_rect.y = int((y == None) and (core.screen_h - h)/2 or y)
		self._setupRect()
	
	def getRect(self):
		return (self._rect.x, self._rect.y)
	
	def getSize(self):
		return (self._rect.w, self._rect.h)
	
	def getScreenRect(self):
		return (self._screen_rect.x, self._screen_rect.y)
	
	def moveRect(self, xdiff=0, ydiff=0):
		self._rect.x += int(xdiff)
		self._rect.y += int(ydiff)
		self._setupRect()
	
	def moveScreenRect(self, xdiff=0, ydiff=0):
		self._screen_rect.x += int(xdiff)
		self._screen_rect.y += int(ydiff)
		self._setupRect()
	
	def draw(self):
		SDL_BlitSurface(
			self.surface, byref(self.rect),
			core.screen, byref(self.screen_rect),
		)