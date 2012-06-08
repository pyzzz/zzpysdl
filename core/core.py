#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import sdl
import smpeg
import traceback
import music
import movie
from ctypes import byref
screen = None
event = sdl.SDL_Event()
screenVideoMode = sdl.SDL_HWSURFACE | sdl.SDL_DOUBLEBUF
coreVersion = (0, 1, 2)
sdlVersion = None
sdlIncludeVersion = None
ttfVersion = None
ttfIncludeVersion = None
gfxVersion = None
gfxIncludeVersion = None
imgVersion = None
imgIncludeVersion = None
mixVersion = None
mixIncludeVersion = None
mpgVersion = None
mpgIncludeVersion = None

def log(*args):
	if args: sys.stdout.write("[ Log ] %s\n"%" ".join(map(str, args)))

def logerr(*args):
	if args: sys.stderr.write("[Error] %s\n"%" ".join(map(str, args)))

def logdebug(*args):
	if args: sys.stdout.write("[Debug] %s\n"%" ".join(map(str, args)))

def logtraceerr(*args):
	logerr(traceback.format_exc(), *args)

def raisesdlerr(*args):
	raise Exception(
		" ".join((
			str(sdl.SDL_GetError()),
			" ".join(map(str, args)),
		))
	)

def logsdlerr(*args):
	logerr(sdl.SDL_GetError(), *args)

def exitproc():
	log("exitproc", os.name)
	if os.name == "posix":
		pass
		#dont't need, but just for now ...
		#import signal
		#os.kill(os.getpid(), signal.SIGKILL)
	elif os.name == "nt":
		#runtime error if smpeg imported ...
		from ctypes import windll
		kernel32 = windll.LoadLibrary("kernel32.dll")
		process = kernel32.OpenProcess(1, False, os.getpid())
		if process: kernel32.TerminateProcess(process, 0)
	os._exit(0) #no thread and __del__ error message

def exitapp(*args):
	if args:
		logerr(*args)
	global screen
	if screen:
		sdl.SDL_FreeSurface(screen)
		screen = None
	movie.stop()
	music.closeAudio()
	sdl.Mix_Quit() #if not call will abort
	sdl.IMG_Quit()
	sdl.TTF_Quit()
	sdl.SDL_Quit()
	exitproc()

def initVersionInfo():
	logdebug("core Version %s"%".".join(map(str, coreVersion)))
	global sdlVersion, sdlIncludeVersion
	ver = sdl.SDL_Linked_Version().contents
	sdlVersion = (ver.major, ver.minor, ver.patch)
	sdlIncludeVersion = (
		sdl.SDL_MAJOR_VERSION, sdl.SDL_MINOR_VERSION, sdl.SDL_PATCHLEVEL
	)
	logdebug("SDL Version [load %s] [include %s]"%(
			".".join(map(str, sdlVersion)),
			".".join(map(str, sdlIncludeVersion)),
		)
	)
	global ttfVersion, ttfIncludeVersion
	ver = sdl.TTF_Linked_Version().contents
	ttfVersion = (ver.major, ver.minor, ver.patch)
	ttfIncludeVersion = (
		sdl.SDL_TTF_MAJOR_VERSION, sdl.SDL_TTF_MINOR_VERSION, sdl.SDL_TTF_PATCHLEVEL
	)
	logdebug("SDL_ttf Version [load %s] [include %s]"%(
			".".join(map(str, ttfVersion)),
			".".join(map(str, ttfIncludeVersion)),
		)
	)
	global gfxVersion, gfxIncludeVersion
	gfxIncludeVersion = (
		sdl.SDL_GFXPRIMITIVES_MAJOR,
		sdl.SDL_GFXPRIMITIVES_MINOR,
		sdl.SDL_GFXPRIMITIVES_MICRO,
	)
	logdebug("SDL_gfx Version [load %s] [include %s]"%(
			"unknow",
			".".join(map(str, gfxIncludeVersion)),
		)
	)
	global imgVersion, imgIncludeVersion
	ver = sdl.IMG_Linked_Version().contents
	imgVersion = (ver.major, ver.minor, ver.patch)
	imgIncludeVersion = (
		sdl.SDL_IMAGE_MAJOR_VERSION,
		sdl.SDL_IMAGE_MINOR_VERSION,
		sdl.SDL_IMAGE_PATCHLEVEL,
	)
	logdebug("SDL_image Version [load %s] [include %s]"%(
			".".join(map(str, imgVersion)),
			".".join(map(str, imgIncludeVersion)),
		)
	)
	global mixVersion, mixIncludeVersion
	ver = sdl.Mix_Linked_Version().contents
	mixVersion = (ver.major, ver.minor, ver.patch)
	mixIncludeVersion = (
		sdl.SDL_MIXER_MAJOR_VERSION,
		sdl.SDL_MIXER_MINOR_VERSION,
		sdl.SDL_MIXER_PATCHLEVEL,
	)
	logdebug("SDL_mixer Version [load %s] [include %s]"%(
			".".join(map(str, mixVersion)),
			".".join(map(str, mixIncludeVersion)),
		)
	)
	global mpgVersion, mpgIncludeVersion
	mpgIncludeVersion = (
		smpeg.SMPEG_MAJOR_VERSION,
		smpeg.SMPEG_MINOR_VERSION,
		smpeg.SMPEG_PATCHLEVEL,
	)
	logdebug("SMPEG Version [load %s] [include %s]"%(
			"unknow",
			".".join(map(str, mpgIncludeVersion)),
		)
	)

def getScreenVideoModeString():
	mode = list(filter(
		lambda key: (screenVideoMode & getattr(sdl, key)), (
			#"SDL_SWSURFACE",
			"SDL_HWSURFACE",
			"SDL_ASYNCBLIT",
			"SDL_ANYFORMAT",
			"SDL_HWPALETTE",
			"SDL_DOUBLEBUF",
			"SDL_FULLSCREEN",
			"SDL_OPENGL",
			"SDL_OPENGLBLIT",
			"SDL_RESIZABLE",
			"SDL_NOFRAME",
			"SDL_HWACCEL",
			"SDL_SRCCOLORKEY",
			"SDL_RLEACCELOK",
			"SDL_RLEACCEL",
			"SDL_SRCALPHA",
			"SDL_PREALLOC",
		)
	))
	if not (screenVideoMode & sdl.SDL_HWSURFACE):
		mode.insert(0, "SDL_SWSURFACE")
	return mode

def init(w=0, h=0, bpp=0, title=""):
	initVersionInfo()
	os.putenv("SDL_VIDEO_WINDOW_POS", "center")
	os.putenv("SDL_VIDEO_CENTERED", "1")
	
	logdebug("start SDL_Init EVERYTHING")
	if sdl.SDL_Init(sdl.SDL_INIT_EVERYTHING) < 0: raisesdlerr()
	
	logdebug("start SDL_EnableUNICODE")
	sdl.SDL_EnableUNICODE(1)
	
	logdebug("start TTF_Init")
	if sdl.TTF_Init() < 0: raisesdlerr()
	
	logdebug("start IMG_Init JPG/PNG/TIF")
	if sdl.IMG_Init(
		sdl.IMG_INIT_JPG | sdl.IMG_INIT_PNG | sdl.IMG_INIT_TIF
	) < 0: raisesdlerr()
	
	logdebug("start Mix_Init FLAC/MOD/MP3/OGG")
	if sdl.Mix_Init(
		sdl.MIX_INIT_FLAC | sdl.MIX_INIT_MOD | sdl.MIX_INIT_MP3 | sdl.MIX_INIT_OGG
	) < 0: raisesdlerr()
	music.openAudio()
	music.bgm = music._MusicCore()
	for i in xrange(sdl.MIX_CHANNELS):
		music.channel[i] = music._ChannelCore(i)
	#Segmentation fault if set both ...
	#sdl.Mix_ChannelFinished(music._channelDoneType(music._channelDone))
	#sdl.Mix_HookMusicFinished(music._bgmDoneType(music._bgmDone))
	
	logdebug("start SDL_SetVideoMode", w, h, bpp, ", ".join(getScreenVideoModeString()))
	global screen
	screen = sdl.SDL_SetVideoMode(w, h, bpp, screenVideoMode)
	if not screen: raisesdlerr()
	
	logdebug("start SDL_WM_SetCaption", title)
	sdl.SDL_WM_SetCaption(title, title)

def lockSurface(surface):
	if sdl.SDL_MUSTLOCK(surface):
		if sdl.SDL_LockSurface(surface) < 0:
			return False
	return True

def unlockSurface(surface):
	if sdl.SDL_MUSTLOCK(surface):
		sdl.SDL_UnlockSurface(surface)

def pollEvent():
	#if just pass to function should use ctypes.byref, it's fast than ctypes.pointer
	return sdl.SDL_PollEvent(byref(event))

def clearEvent():
	while sdl.SDL_PollEvent(byref(event)):
		pass