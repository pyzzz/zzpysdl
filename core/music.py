#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import core
import movie
from sdl import MIX_CHANNELS
from sdl import MIX_DEFAULT_FREQUENCY, MIX_DEFAULT_FORMAT, MIX_DEFAULT_CHANNELS
from sdl import Mix_OpenAudio, Mix_HaltMusic, Mix_HaltChannel, Mix_CloseAudio
from sdl import Mix_LoadMUS, Mix_FreeMusic, Mix_LoadWAV, Mix_FreeChunk
from sdl import Mix_Playing, Mix_PlayingMusic, Mix_Paused, Mix_PausedMusic
from sdl import Mix_Pause, Mix_Resume, Mix_PlayChannel,Mix_FadeOutChannel
from sdl import Mix_PauseMusic, Mix_ResumeMusic, Mix_RewindMusic
from sdl import Mix_PlayMusic, Mix_FadeOutMusic
channel = [None]*MIX_CHANNELS
bgm = None
audioDeviceActive = False
#Segmentation fault if set both ...
#_channelDoneType = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int)
#_bgmDoneType = ctypes.CFUNCTYPE(ctypes.c_void_p)
#
#def _channelDone(channel_id):
#	global channel
#	core.logdebug("_channelDone", channel_id)
#	channel[channel_id].playing = False
#
#def _bgmDone():
#	global bgm
#	core.logdebug("_bgmDone")
#	bgm.playing = False

def openAudio():
	global audioDeviceActive
	if audioDeviceActive:
		return
	movie.stop() #if not call it, Mix_OpenAudio will failed after movie playing finish
	if Mix_OpenAudio(
		MIX_DEFAULT_FREQUENCY,
		MIX_DEFAULT_FORMAT,
		MIX_DEFAULT_CHANNELS,
		1024,
	) < 0: core.raisesdlerr()
	audioDeviceActive = True

def closeAudio():
	global audioDeviceActive
	if not audioDeviceActive:
		return
	Mix_HaltMusic()
	Mix_HaltChannel(-1) #stop all channel
	Mix_CloseAudio()
	audioDeviceActive = False

class Music:
	def __init__(self, path):
		self.path = path
		self.data = Mix_LoadMUS(path)
		if not self.data:
			core.logsdlerr(self)
	
	def __del__(self):
		core.logdebug("del music", self)
		Mix_FreeMusic(self.data)
	
	def __str__(self):
		return "%s[%s]"%(repr(self), self.path)

class Chunk:
	def __init__(self, path):
		self.path = path
		self.data = Mix_LoadWAV(path)
		if not self.data:
			core.logsdlerr(self)
	
	def __del__(self):
		core.logdebug("del chunk", self)
		Mix_FreeChunk(self.data)
	
	def __str__(self):
		return "%s[%s]"%(repr(self), self.path)

class _ChannelCore:
	def __init__(self, channel):
		if channel < 0 or channel >= MIX_CHANNELS:
			raise Exception("channel must in range [0..%s]"%MIX_CHANNELS)
		self.channel = channel
		self.chunk = None
	
	def __str__(self):
		return "%s[%s, %s, %s]"%(
			repr(self), self.chunk, self.channel, self.playing()
		)
	
	def paused(self):
		#Does not check if the channel has been halted after it was paused
		#Zero if the channel is not paused
		if Mix_Paused(self.channel) == 0:
			return False
		return True
	
	def playing(self):
		if not audioDeviceActive:
			return False
		#Segmentation fault if audio device closed
		if self.paused():
			return False
		#Does not check if the channel has been paused
		#Zero if the channel is not playing
		if Mix_Playing(self.channel) == 0:
			return False
		return True
	
	def load(self, chunk):
		if not isinstance(chunk, Chunk):
			core.logerr("not isinstance(chunk, Chunk)", chunk)
			return
		self.stop()
		self.chunk = chunk
	
	def play(self, loop):
		"""loop -1: infinite, 0: once"""
		if not self.chunk:
			core.logdebug("play canceled: not self.chunk", self)
			return
		if self.playing():
			core.logdebug("play canceled: playing", self)
			return
		if movie.playing():
			core.logdebug("play canceled: movie playing", self)
			return
		openAudio()
		if Mix_PlayChannel(self.channel, self.chunk.data, loop) < 0:
			core.logsdlerr(self)
			return
	
	def stop(self, fadeout_ms=0):
		"""bug:
			after Mix_FadeOutChannel or Mix_HaltChannel,
			Mix_Playing *maybe* still return 0.
			this bug look like not happen in _MusicCore.
		"""
		if not self.playing():
			return
		if fadeout_ms:
			Mix_FadeOutChannel(self.channel, fadeout_ms)
		else:
			Mix_HaltChannel(self.channel)
	
	def pause(self):
		Mix_Pause(self.channel)
	
	def unpause(self):
		Mix_Resume(self.channel)

class _MusicCore:
	def __init__(self):
		self.music = None
	
	def __str__(self):
		return "%s[%s, %s]"%(repr(self), self.music, self.playing())
	
	def paused(self):
		#Does not check if the channel has been halted after it was paused
		#Zero if the channel is not paused
		if Mix_PausedMusic() == 0:
			return False
		return True
	
	def playing(self):
		if not audioDeviceActive:
			return False
		#Segmentation fault if audio device closed
		if self.paused():
			return False
		#Does not check if the channel has been paused
		#Zero if the channel is not playing
		if Mix_PlayingMusic() == 0:
			return False
		return True
	
	def load(self, music):
		if not isinstance(music, Music):
			core.logerr("not isinstance(music, Music)", music)
			return
		self.stop()
		self.music = music
	
	def play(self, loop):
		"""loop -1: infinite, 0: once"""
		if not self.music:
			core.logdebug("play canceled: not self.music", self)
			return
		if self.playing():
			core.logdebug("play canceled: playing", self)
			return
		if movie.playing():
			core.logdebug("play canceled: movie playing", self)
			return
		openAudio()
		if Mix_PlayMusic(self.music.data, loop) < 0:
			core.logsdlerr(self)
			return
	
	def stop(self, fadeout_ms=0):
		if not self.playing():
			return
		if fadeout_ms:
			Mix_FadeOutMusic(fadeout_ms)
		else:
			Mix_HaltMusic()
	
	def pause(self):
		Mix_PauseMusic()
	
	def unpause(self):
		Mix_ResumeMusic()
	
	def restart(self):
		Mix_RewindMusic()
