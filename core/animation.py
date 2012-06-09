#!/usr/bin/env python
# -*- coding:utf-8 -*-
import widget
import core
import time

class Animation:
	def __init__(self, delay, widget_list):
		self.lastTime = 0
		self.index = 0
		self.widgetList = list(widget_list)
		self.length = len(self.widgetList)
		if hasattr(delay, "__iter__"):
			if len(delay) != length:
				raise Exception("len(delay) != length")
			self.delay = map(float, delay)
		else:
			self.delay = [float(delay)]*self.length
		self.playing = False
		self.loop = False
		self._needDraw = False
	
	def __str__(self):
		return "%s[%s, %s, %s, %s]"%(
			repr(self),
			self.playing,
			self.loop,
			self.widgetList,
			self.delay,
		)
	
	def setScreenRect(self, x=None, y=None):
		for w in self.widgetList:
			w.setScreenRect(x, y)
	
	def setScreenRectCenter(self, x=None, y=None):
		for w in self.widgetList:
			w.setScreenRectCenter(x, y)
	
	def moveScreenRect(self, xdiff=0, ydiff=0):
		for w in self.widgetList:
			w.moveScreenRect(xdiff, ydiff)
	
	def getWidget(self, index):
		return self.widgetList[index]
	
	def play(self, loop=False, index=0):
		if self.playing:
			core.logdebug("animation play canceled: playing")
			return
		index = int(index)
		if index < 0 or index >= self.length:
			raise IndexError("index %s not in [0..length], %s"%(index, widget))
		self.index = index
		self.loop = bool(loop)
		self.playing = True
		self._needDraw = True
		self.lastTime = time.time()
	
	def stop(self):
		if not self.playing:
			return
		self.playing = False
		self._needDraw = False
		self.lastTime = 0
	
	def next(self):
		if self.index == self.length-1:
			if self.loop:
				self.index = 0
				return True
			else:
				return False
		else:
			self.index += 1
			return True
	
	def needDraw(self):
		if not self.playing:
			return False
		if time.time() - self.lastTime > self.delay[self.index]:
			self._needDraw = True
		return self._needDraw
	
	def draw(self):
		if not self.playing:
			return
		self._needDraw = False
		lasttime = time.time()
		while True:
			delay = self.delay[self.index]
			if lasttime - self.lastTime > delay:
				self.lastTime += delay
				if not self.next():
					self.stop()
					return
			else:
				break
		#core.logdebug("draw", self.index)
		self.widgetList[self.index].draw()