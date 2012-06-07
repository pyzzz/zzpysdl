#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import sdl
import core
from ctypes import byref

class Widget:
	def __init__(self):
		self.surface = None
		self.rect = sdl.SDL_Rect()
		self.screen_rect = sdl.SDL_Rect()
	
	def __del__(self):
		core.logdebug("del widget", self)
		sdl.SDL_FreeSurface(self.surface)
	
	def setRect(self, x=0, y=0, w=None, h=None):
		self.rect.x = int(x)
		self.rect.y = int(y)
		self.rect.w = (w == None) and int(self.surface.contents.w) or w
		self.rect.h = (h == None) and int(self.surface.contents.h) or h
	
	def setScreenRect(self, x=None, y=None):
		self.screen_rect.x = (
			(x == None) and
			int((core.screen.contents.w - self.surface.contents.w)/2) or x
		)
		if self.screen_rect.x < 0:
			self.rect.x += abs(self.screen_rect.x)
			self.screen_rect.x = 0
		self.screen_rect.y = (
			(y == None) and
			int((core.screen.contents.h - self.surface.contents.h)/2) or y
		)
		if self.screen_rect.y < 0:
			self.rect.y += abs(self.screen_rect.y)
			self.screen_rect.y = 0
	
	def moveRect(self, xdiff=0, ydiff=0):
		self.rect.x += int(xdiff)
		self.rect.y += int(ydiff)
	
	def moveScreenRect(self, xdiff=0, ydiff=0):
		self.screen_rect.x += int(xdiff)
		self.screen_rect.y += int(ydiff)
		if self.screen_rect.x < 0:
			self.rect.x += abs(self.screen_rect.x)
			self.screen_rect.x = 0
		if self.screen_rect.y < 0:
			self.rect.y += abs(self.screen_rect.y)
			self.screen_rect.y = 0
	
	def draw(self):
		sdl.SDL_BlitSurface(
			self.surface, byref(self.rect),
			core.screen, byref(self.screen_rect),
		)