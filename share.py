#!/usr/bin/env python
# -*- coding:utf-8 -*-
from core import sdl
running = True
event = sdl.SDL_Event()
font = None
font_outline = None

img = None
label = None
bgm = None
music = [None]*8