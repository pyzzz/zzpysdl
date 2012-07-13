'''Wrapper for begin_code.h

Generated with:
ctypesgen.py -L/usr/lib -L/usr/lib64 -lSDL -lSDL_image -lSDL_gfx -lSDL_mixer -lSDL_ttf -I/usr/include/SDL/ /usr/include/SDL/begin_code.h /usr/include/SDL/close_code.h /usr/include/SDL/SDL_active.h /usr/include/SDL/SDL_audio.h /usr/include/SDL/SDL_byteorder.h /usr/include/SDL/SDL_cdrom.h /usr/include/SDL/SDL_config.h /usr/include/SDL/SDL_config-x86_64.h /usr/include/SDL/SDL_cpuinfo.h /usr/include/SDL/SDL_endian.h /usr/include/SDL/SDL_error.h /usr/include/SDL/SDL_events.h /usr/include/SDL/SDL_framerate.h /usr/include/SDL/SDL_getenv.h /usr/include/SDL/SDL_gfxBlitFunc.h /usr/include/SDL/SDL_gfxPrimitives_font.h /usr/include/SDL/SDL_gfxPrimitives.h /usr/include/SDL/SDL.h /usr/include/SDL/SDL_imageFilter.h /usr/include/SDL/SDL_image.h /usr/include/SDL/SDL_joystick.h /usr/include/SDL/SDL_keyboard.h /usr/include/SDL/SDL_keysym.h /usr/include/SDL/SDL_loadso.h /usr/include/SDL/SDL_main.h /usr/include/SDL/SDL_mixer.h /usr/include/SDL/SDL_mouse.h /usr/include/SDL/SDL_mutex.h /usr/include/SDL/SDL_name.h /usr/include/SDL/SDL_net.h /usr/include/SDL/SDL_opengl.h /usr/include/SDL/SDL_platform.h /usr/include/SDL/SDL_quit.h /usr/include/SDL/SDL_rotozoom.h /usr/include/SDL/SDL_rwops.h /usr/include/SDL/SDL_stdinc.h /usr/include/SDL/SDL_syswm.h /usr/include/SDL/SDL_thread.h /usr/include/SDL/SDL_timer.h /usr/include/SDL/SDL_ttf.h /usr/include/SDL/SDL_types.h /usr/include/SDL/SDL_version.h /usr/include/SDL/SDL_video.h -o sdl.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = ['/usr/lib', '/usr/lib64']

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs(['/usr/lib', '/usr/lib64'])

# Begin libraries

_libs["SDL"] = load_library("SDL")
_libs["SDL_image"] = load_library("SDL_image")
_libs["SDL_gfx"] = load_library("SDL_gfx")
_libs["SDL_mixer"] = load_library("SDL_mixer")
_libs["SDL_ttf"] = load_library("SDL_ttf")

# 5 libraries
# End libraries

# No modules

NULL = None # <built-in>

__off_t = c_long # /usr/include/bits/types.h: 141

__off64_t = c_long # /usr/include/bits/types.h: 142

# /usr/include/libio.h: 271
class struct__IO_FILE(Structure):
    pass

FILE = struct__IO_FILE # /usr/include/stdio.h: 49

_IO_lock_t = None # /usr/include/libio.h: 180

# /usr/include/libio.h: 186
class struct__IO_marker(Structure):
    pass

struct__IO_marker.__slots__ = [
    '_next',
    '_sbuf',
    '_pos',
]
struct__IO_marker._fields_ = [
    ('_next', POINTER(struct__IO_marker)),
    ('_sbuf', POINTER(struct__IO_FILE)),
    ('_pos', c_int),
]

struct__IO_FILE.__slots__ = [
    '_flags',
    '_IO_read_ptr',
    '_IO_read_end',
    '_IO_read_base',
    '_IO_write_base',
    '_IO_write_ptr',
    '_IO_write_end',
    '_IO_buf_base',
    '_IO_buf_end',
    '_IO_save_base',
    '_IO_backup_base',
    '_IO_save_end',
    '_markers',
    '_chain',
    '_fileno',
    '_flags2',
    '_old_offset',
    '_cur_column',
    '_vtable_offset',
    '_shortbuf',
    '_lock',
    '_offset',
    '__pad1',
    '__pad2',
    '__pad3',
    '__pad4',
    '__pad5',
    '_mode',
    '_unused2',
]
struct__IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', String),
    ('_IO_read_end', String),
    ('_IO_read_base', String),
    ('_IO_write_base', String),
    ('_IO_write_ptr', String),
    ('_IO_write_end', String),
    ('_IO_buf_base', String),
    ('_IO_buf_end', String),
    ('_IO_save_base', String),
    ('_IO_backup_base', String),
    ('_IO_save_end', String),
    ('_markers', POINTER(struct__IO_marker)),
    ('_chain', POINTER(struct__IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_char),
    ('_shortbuf', c_char * 1),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('__pad1', POINTER(None)),
    ('__pad2', POINTER(None)),
    ('__pad3', POINTER(None)),
    ('__pad4', POINTER(None)),
    ('__pad5', c_size_t),
    ('_mode', c_int),
    ('_unused2', c_char * (((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t))),
]

# /usr/include/stdio.h: 385
if hasattr(_libs['SDL'], 'snprintf'):
    _func = _libs['SDL'].snprintf
    _restype = c_int
    _argtypes = [String, c_size_t, String]
    snprintf = _variadic_function(_func,_restype,_argtypes)

# /usr/include/stdio.h: 437
if hasattr(_libs['SDL'], 'sscanf'):
    _func = _libs['SDL'].sscanf
    _restype = c_int
    _argtypes = [String, String]
    sscanf = _variadic_function(_func,_restype,_argtypes)

# /usr/include/stdlib.h: 145
if hasattr(_libs['SDL'], 'atof'):
    atof = _libs['SDL'].atof
    atof.argtypes = [String]
    atof.restype = c_double

# /usr/include/stdlib.h: 148
if hasattr(_libs['SDL'], 'atoi'):
    atoi = _libs['SDL'].atoi
    atoi.argtypes = [String]
    atoi.restype = c_int

# /usr/include/stdlib.h: 165
if hasattr(_libs['SDL'], 'strtod'):
    strtod = _libs['SDL'].strtod
    strtod.argtypes = [String, POINTER(POINTER(c_char))]
    strtod.restype = c_double

# /usr/include/stdlib.h: 184
if hasattr(_libs['SDL'], 'strtol'):
    strtol = _libs['SDL'].strtol
    strtol.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtol.restype = c_long

# /usr/include/stdlib.h: 188
if hasattr(_libs['SDL'], 'strtoul'):
    strtoul = _libs['SDL'].strtoul
    strtoul.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoul.restype = c_ulong

# /usr/include/stdlib.h: 210
if hasattr(_libs['SDL'], 'strtoll'):
    strtoll = _libs['SDL'].strtoll
    strtoll.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoll.restype = c_longlong

# /usr/include/stdlib.h: 215
if hasattr(_libs['SDL'], 'strtoull'):
    strtoull = _libs['SDL'].strtoull
    strtoull.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoull.restype = c_ulonglong

# /usr/include/stdlib.h: 471
if hasattr(_libs['SDL'], 'malloc'):
    malloc = _libs['SDL'].malloc
    malloc.argtypes = [c_size_t]
    malloc.restype = POINTER(None)

# /usr/include/stdlib.h: 473
if hasattr(_libs['SDL'], 'calloc'):
    calloc = _libs['SDL'].calloc
    calloc.argtypes = [c_size_t, c_size_t]
    calloc.restype = POINTER(None)

# /usr/include/stdlib.h: 485
if hasattr(_libs['SDL'], 'realloc'):
    realloc = _libs['SDL'].realloc
    realloc.argtypes = [POINTER(None), c_size_t]
    realloc.restype = POINTER(None)

# /usr/include/stdlib.h: 488
if hasattr(_libs['SDL'], 'free'):
    free = _libs['SDL'].free
    free.argtypes = [POINTER(None)]
    free.restype = None

# /usr/include/stdlib.h: 567
if hasattr(_libs['SDL'], 'getenv'):
    getenv = _libs['SDL'].getenv
    getenv.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        getenv.restype = ReturnString
    else:
        getenv.restype = String
        getenv.errcheck = ReturnString

# /usr/include/stdlib.h: 579
if hasattr(_libs['SDL'], 'putenv'):
    putenv = _libs['SDL'].putenv
    putenv.argtypes = [String]
    putenv.restype = c_int

__compar_fn_t = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None)) # /usr/include/stdlib.h: 742

# /usr/include/stdlib.h: 761
if hasattr(_libs['SDL'], 'qsort'):
    qsort = _libs['SDL'].qsort
    qsort.argtypes = [POINTER(None), c_size_t, c_size_t, __compar_fn_t]
    qsort.restype = None

# /usr/include/stdlib.h: 771
if hasattr(_libs['SDL'], 'abs'):
    abs = _libs['SDL'].abs
    abs.argtypes = [c_int]
    abs.restype = c_int

# /usr/include/string.h: 44
if hasattr(_libs['SDL'], 'memcpy'):
    memcpy = _libs['SDL'].memcpy
    memcpy.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memcpy.restype = POINTER(None)

# /usr/include/string.h: 49
if hasattr(_libs['SDL'], 'memmove'):
    memmove = _libs['SDL'].memmove
    memmove.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memmove.restype = POINTER(None)

# /usr/include/string.h: 65
if hasattr(_libs['SDL'], 'memset'):
    memset = _libs['SDL'].memset
    memset.argtypes = [POINTER(None), c_int, c_size_t]
    memset.restype = POINTER(None)

# /usr/include/string.h: 68
if hasattr(_libs['SDL'], 'memcmp'):
    memcmp = _libs['SDL'].memcmp
    memcmp.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memcmp.restype = c_int

# /usr/include/string.h: 143
if hasattr(_libs['SDL'], 'strcmp'):
    strcmp = _libs['SDL'].strcmp
    strcmp.argtypes = [String, String]
    strcmp.restype = c_int

# /usr/include/string.h: 146
if hasattr(_libs['SDL'], 'strncmp'):
    strncmp = _libs['SDL'].strncmp
    strncmp.argtypes = [String, String, c_size_t]
    strncmp.restype = c_int

# /usr/include/string.h: 175
if hasattr(_libs['SDL'], 'strdup'):
    strdup = _libs['SDL'].strdup
    strdup.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        strdup.restype = ReturnString
    else:
        strdup.restype = String
        strdup.errcheck = ReturnString

# /usr/include/string.h: 235
if hasattr(_libs['SDL'], 'strchr'):
    strchr = _libs['SDL'].strchr
    strchr.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        strchr.restype = ReturnString
    else:
        strchr.restype = String
        strchr.errcheck = ReturnString

# /usr/include/string.h: 262
if hasattr(_libs['SDL'], 'strrchr'):
    strrchr = _libs['SDL'].strrchr
    strrchr.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        strrchr.restype = ReturnString
    else:
        strrchr.restype = String
        strrchr.errcheck = ReturnString

# /usr/include/string.h: 342
if hasattr(_libs['SDL'], 'strstr'):
    strstr = _libs['SDL'].strstr
    strstr.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        strstr.restype = ReturnString
    else:
        strstr.restype = String
        strstr.errcheck = ReturnString

# /usr/include/string.h: 399
if hasattr(_libs['SDL'], 'strlen'):
    strlen = _libs['SDL'].strlen
    strlen.argtypes = [String]
    strlen.restype = c_size_t

# /usr/include/string.h: 536
if hasattr(_libs['SDL'], 'strcasecmp'):
    strcasecmp = _libs['SDL'].strcasecmp
    strcasecmp.argtypes = [String, String]
    strcasecmp.restype = c_int

# /usr/include/string.h: 540
if hasattr(_libs['SDL'], 'strncasecmp'):
    strncasecmp = _libs['SDL'].strncasecmp
    strncasecmp.argtypes = [String, String, c_size_t]
    strncasecmp.restype = c_int

# /usr/include/ctype.h: 105
if hasattr(_libs['SDL'], 'isdigit'):
    isdigit = _libs['SDL'].isdigit
    isdigit.argtypes = [c_int]
    isdigit.restype = c_int

# /usr/include/ctype.h: 110
if hasattr(_libs['SDL'], 'isspace'):
    isspace = _libs['SDL'].isspace
    isspace.argtypes = [c_int]
    isspace.restype = c_int

# /usr/include/ctype.h: 116
if hasattr(_libs['SDL'], 'tolower'):
    tolower = _libs['SDL'].tolower
    tolower.argtypes = [c_int]
    tolower.restype = c_int

# /usr/include/ctype.h: 119
if hasattr(_libs['SDL'], 'toupper'):
    toupper = _libs['SDL'].toupper
    toupper.argtypes = [c_int]
    toupper.restype = c_int

iconv_t = POINTER(None) # /usr/include/iconv.h: 30

# /usr/include/iconv.h: 38
if hasattr(_libs['SDL'], 'iconv_open'):
    iconv_open = _libs['SDL'].iconv_open
    iconv_open.argtypes = [String, String]
    iconv_open.restype = iconv_t

# /usr/include/iconv.h: 52
if hasattr(_libs['SDL'], 'iconv_close'):
    iconv_close = _libs['SDL'].iconv_close
    iconv_close.argtypes = [iconv_t]
    iconv_close.restype = c_int

enum_anon_26 = c_int # /usr/include/SDL/SDL_stdinc.h: 96

SDL_FALSE = 0 # /usr/include/SDL/SDL_stdinc.h: 96

SDL_TRUE = 1 # /usr/include/SDL/SDL_stdinc.h: 96

SDL_bool = enum_anon_26 # /usr/include/SDL/SDL_stdinc.h: 96

Sint8 = c_int8 # /usr/include/SDL/SDL_stdinc.h: 98

Uint8 = c_uint8 # /usr/include/SDL/SDL_stdinc.h: 99

Sint16 = c_int16 # /usr/include/SDL/SDL_stdinc.h: 100

Uint16 = c_uint16 # /usr/include/SDL/SDL_stdinc.h: 101

Sint32 = c_int32 # /usr/include/SDL/SDL_stdinc.h: 102

Uint32 = c_uint32 # /usr/include/SDL/SDL_stdinc.h: 103

Sint64 = c_int64 # /usr/include/SDL/SDL_stdinc.h: 106

Uint64 = c_uint64 # /usr/include/SDL/SDL_stdinc.h: 108

SDL_dummy_uint8 = c_int * (((sizeof(Uint8) == 1) * 2) - 1) # /usr/include/SDL/SDL_stdinc.h: 125

SDL_dummy_sint8 = c_int * (((sizeof(Sint8) == 1) * 2) - 1) # /usr/include/SDL/SDL_stdinc.h: 126

SDL_dummy_uint16 = c_int * (((sizeof(Uint16) == 2) * 2) - 1) # /usr/include/SDL/SDL_stdinc.h: 127

SDL_dummy_sint16 = c_int * (((sizeof(Sint16) == 2) * 2) - 1) # /usr/include/SDL/SDL_stdinc.h: 128

SDL_dummy_uint32 = c_int * (((sizeof(Uint32) == 4) * 2) - 1) # /usr/include/SDL/SDL_stdinc.h: 129

SDL_dummy_sint32 = c_int * (((sizeof(Sint32) == 4) * 2) - 1) # /usr/include/SDL/SDL_stdinc.h: 130

SDL_dummy_uint64 = c_int * (((sizeof(Uint64) == 8) * 2) - 1) # /usr/include/SDL/SDL_stdinc.h: 131

SDL_dummy_sint64 = c_int * (((sizeof(Sint64) == 8) * 2) - 1) # /usr/include/SDL/SDL_stdinc.h: 132

enum_anon_27 = c_int # /usr/include/SDL/SDL_stdinc.h: 148

DUMMY_ENUM_VALUE = 0 # /usr/include/SDL/SDL_stdinc.h: 148

SDL_DUMMY_ENUM = enum_anon_27 # /usr/include/SDL/SDL_stdinc.h: 148

SDL_dummy_enum = c_int * (((sizeof(SDL_DUMMY_ENUM) == sizeof(c_int)) * 2) - 1) # /usr/include/SDL/SDL_stdinc.h: 151

# /usr/include/SDL/SDL_stdinc.h: 370
if hasattr(_libs['SDL'], 'SDL_revcpy'):
    SDL_revcpy = _libs['SDL'].SDL_revcpy
    SDL_revcpy.argtypes = [POINTER(None), POINTER(None), c_size_t]
    SDL_revcpy.restype = POINTER(None)

# /usr/include/SDL/SDL_stdinc.h: 403
if hasattr(_libs['SDL'], 'SDL_strlcpy'):
    SDL_strlcpy = _libs['SDL'].SDL_strlcpy
    SDL_strlcpy.argtypes = [String, String, c_size_t]
    SDL_strlcpy.restype = c_size_t

# /usr/include/SDL/SDL_stdinc.h: 409
if hasattr(_libs['SDL'], 'SDL_strlcat'):
    SDL_strlcat = _libs['SDL'].SDL_strlcat
    SDL_strlcat.argtypes = [String, String, c_size_t]
    SDL_strlcat.restype = c_size_t

# /usr/include/SDL/SDL_stdinc.h: 421
if hasattr(_libs['SDL'], 'SDL_strrev'):
    SDL_strrev = _libs['SDL'].SDL_strrev
    SDL_strrev.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_strrev.restype = ReturnString
    else:
        SDL_strrev.restype = String
        SDL_strrev.errcheck = ReturnString

# /usr/include/SDL/SDL_stdinc.h: 427
if hasattr(_libs['SDL'], 'SDL_strupr'):
    SDL_strupr = _libs['SDL'].SDL_strupr
    SDL_strupr.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_strupr.restype = ReturnString
    else:
        SDL_strupr.restype = String
        SDL_strupr.errcheck = ReturnString

# /usr/include/SDL/SDL_stdinc.h: 433
if hasattr(_libs['SDL'], 'SDL_strlwr'):
    SDL_strlwr = _libs['SDL'].SDL_strlwr
    SDL_strlwr.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_strlwr.restype = ReturnString
    else:
        SDL_strlwr.restype = String
        SDL_strlwr.errcheck = ReturnString

# /usr/include/SDL/SDL_stdinc.h: 467
if hasattr(_libs['SDL'], 'SDL_ltoa'):
    SDL_ltoa = _libs['SDL'].SDL_ltoa
    SDL_ltoa.argtypes = [c_long, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_ltoa.restype = ReturnString
    else:
        SDL_ltoa.restype = String
        SDL_ltoa.errcheck = ReturnString

# /usr/include/SDL/SDL_stdinc.h: 479
if hasattr(_libs['SDL'], 'SDL_ultoa'):
    SDL_ultoa = _libs['SDL'].SDL_ultoa
    SDL_ultoa.argtypes = [c_ulong, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_ultoa.restype = ReturnString
    else:
        SDL_ultoa.restype = String
        SDL_ultoa.errcheck = ReturnString

# /usr/include/SDL/SDL_stdinc.h: 499
if hasattr(_libs['SDL'], 'SDL_lltoa'):
    SDL_lltoa = _libs['SDL'].SDL_lltoa
    SDL_lltoa.argtypes = [Sint64, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_lltoa.restype = ReturnString
    else:
        SDL_lltoa.restype = String
        SDL_lltoa.errcheck = ReturnString

# /usr/include/SDL/SDL_stdinc.h: 505
if hasattr(_libs['SDL'], 'SDL_ulltoa'):
    SDL_ulltoa = _libs['SDL'].SDL_ulltoa
    SDL_ulltoa.argtypes = [Uint64, String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_ulltoa.restype = ReturnString
    else:
        SDL_ulltoa.restype = String
        SDL_ulltoa.errcheck = ReturnString

# /usr/include/SDL/SDL_stdinc.h: 605
if hasattr(_libs['SDL'], 'SDL_iconv'):
    SDL_iconv = _libs['SDL'].SDL_iconv
    SDL_iconv.argtypes = [iconv_t, POINTER(POINTER(c_char)), POINTER(c_size_t), POINTER(POINTER(c_char)), POINTER(c_size_t)]
    SDL_iconv.restype = c_size_t

# /usr/include/SDL/SDL_stdinc.h: 609
if hasattr(_libs['SDL'], 'SDL_iconv_string'):
    SDL_iconv_string = _libs['SDL'].SDL_iconv_string
    SDL_iconv_string.argtypes = [String, String, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_iconv_string.restype = ReturnString
    else:
        SDL_iconv_string.restype = String
        SDL_iconv_string.errcheck = ReturnString

# /usr/include/SDL/SDL_error.h: 43
if hasattr(_libs['SDL'], 'SDL_SetError'):
    _func = _libs['SDL'].SDL_SetError
    _restype = None
    _argtypes = [String]
    SDL_SetError = _variadic_function(_func,_restype,_argtypes)

# /usr/include/SDL/SDL_error.h: 44
if hasattr(_libs['SDL'], 'SDL_GetError'):
    SDL_GetError = _libs['SDL'].SDL_GetError
    SDL_GetError.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_GetError.restype = ReturnString
    else:
        SDL_GetError.restype = String
        SDL_GetError.errcheck = ReturnString

# /usr/include/SDL/SDL_error.h: 45
if hasattr(_libs['SDL'], 'SDL_ClearError'):
    SDL_ClearError = _libs['SDL'].SDL_ClearError
    SDL_ClearError.argtypes = []
    SDL_ClearError.restype = None

enum_anon_28 = c_int # /usr/include/SDL/SDL_error.h: 62

SDL_ENOMEM = 0 # /usr/include/SDL/SDL_error.h: 62

SDL_EFREAD = (SDL_ENOMEM + 1) # /usr/include/SDL/SDL_error.h: 62

SDL_EFWRITE = (SDL_EFREAD + 1) # /usr/include/SDL/SDL_error.h: 62

SDL_EFSEEK = (SDL_EFWRITE + 1) # /usr/include/SDL/SDL_error.h: 62

SDL_UNSUPPORTED = (SDL_EFSEEK + 1) # /usr/include/SDL/SDL_error.h: 62

SDL_LASTERROR = (SDL_UNSUPPORTED + 1) # /usr/include/SDL/SDL_error.h: 62

SDL_errorcode = enum_anon_28 # /usr/include/SDL/SDL_error.h: 62

# /usr/include/SDL/SDL_error.h: 63
if hasattr(_libs['SDL'], 'SDL_Error'):
    SDL_Error = _libs['SDL'].SDL_Error
    SDL_Error.argtypes = [SDL_errorcode]
    SDL_Error.restype = None

# /usr/include/SDL/SDL_active.h: 54
if hasattr(_libs['SDL'], 'SDL_GetAppState'):
    SDL_GetAppState = _libs['SDL'].SDL_GetAppState
    SDL_GetAppState.argtypes = []
    SDL_GetAppState.restype = Uint8

# /usr/include/SDL/SDL_endian.h: 165
for _lib in _libs.values():
    try:
        hi = (Uint32).in_dll(_lib, 'hi')
        break
    except:
        pass

# /usr/include/SDL/SDL_endian.h: 165
for _lib in _libs.values():
    try:
        lo = (Uint32).in_dll(_lib, 'lo')
        break
    except:
        pass

# /usr/include/SDL/SDL_mutex.h: 55
class struct_SDL_mutex(Structure):
    pass

SDL_mutex = struct_SDL_mutex # /usr/include/SDL/SDL_mutex.h: 56

# /usr/include/SDL/SDL_mutex.h: 59
if hasattr(_libs['SDL'], 'SDL_CreateMutex'):
    SDL_CreateMutex = _libs['SDL'].SDL_CreateMutex
    SDL_CreateMutex.argtypes = []
    SDL_CreateMutex.restype = POINTER(SDL_mutex)

# /usr/include/SDL/SDL_mutex.h: 65
if hasattr(_libs['SDL'], 'SDL_mutexP'):
    SDL_mutexP = _libs['SDL'].SDL_mutexP
    SDL_mutexP.argtypes = [POINTER(SDL_mutex)]
    SDL_mutexP.restype = c_int

# /usr/include/SDL/SDL_mutex.h: 74
if hasattr(_libs['SDL'], 'SDL_mutexV'):
    SDL_mutexV = _libs['SDL'].SDL_mutexV
    SDL_mutexV.argtypes = [POINTER(SDL_mutex)]
    SDL_mutexV.restype = c_int

# /usr/include/SDL/SDL_mutex.h: 77
if hasattr(_libs['SDL'], 'SDL_DestroyMutex'):
    SDL_DestroyMutex = _libs['SDL'].SDL_DestroyMutex
    SDL_DestroyMutex.argtypes = [POINTER(SDL_mutex)]
    SDL_DestroyMutex.restype = None

# /usr/include/SDL/SDL_mutex.h: 86
class struct_SDL_semaphore(Structure):
    pass

SDL_sem = struct_SDL_semaphore # /usr/include/SDL/SDL_mutex.h: 87

# /usr/include/SDL/SDL_mutex.h: 90
if hasattr(_libs['SDL'], 'SDL_CreateSemaphore'):
    SDL_CreateSemaphore = _libs['SDL'].SDL_CreateSemaphore
    SDL_CreateSemaphore.argtypes = [Uint32]
    SDL_CreateSemaphore.restype = POINTER(SDL_sem)

# /usr/include/SDL/SDL_mutex.h: 93
if hasattr(_libs['SDL'], 'SDL_DestroySemaphore'):
    SDL_DestroySemaphore = _libs['SDL'].SDL_DestroySemaphore
    SDL_DestroySemaphore.argtypes = [POINTER(SDL_sem)]
    SDL_DestroySemaphore.restype = None

# /usr/include/SDL/SDL_mutex.h: 100
if hasattr(_libs['SDL'], 'SDL_SemWait'):
    SDL_SemWait = _libs['SDL'].SDL_SemWait
    SDL_SemWait.argtypes = [POINTER(SDL_sem)]
    SDL_SemWait.restype = c_int

# /usr/include/SDL/SDL_mutex.h: 106
if hasattr(_libs['SDL'], 'SDL_SemTryWait'):
    SDL_SemTryWait = _libs['SDL'].SDL_SemTryWait
    SDL_SemTryWait.argtypes = [POINTER(SDL_sem)]
    SDL_SemTryWait.restype = c_int

# /usr/include/SDL/SDL_mutex.h: 115
if hasattr(_libs['SDL'], 'SDL_SemWaitTimeout'):
    SDL_SemWaitTimeout = _libs['SDL'].SDL_SemWaitTimeout
    SDL_SemWaitTimeout.argtypes = [POINTER(SDL_sem), Uint32]
    SDL_SemWaitTimeout.restype = c_int

# /usr/include/SDL/SDL_mutex.h: 120
if hasattr(_libs['SDL'], 'SDL_SemPost'):
    SDL_SemPost = _libs['SDL'].SDL_SemPost
    SDL_SemPost.argtypes = [POINTER(SDL_sem)]
    SDL_SemPost.restype = c_int

# /usr/include/SDL/SDL_mutex.h: 123
if hasattr(_libs['SDL'], 'SDL_SemValue'):
    SDL_SemValue = _libs['SDL'].SDL_SemValue
    SDL_SemValue.argtypes = [POINTER(SDL_sem)]
    SDL_SemValue.restype = Uint32

# /usr/include/SDL/SDL_mutex.h: 133
class struct_SDL_cond(Structure):
    pass

SDL_cond = struct_SDL_cond # /usr/include/SDL/SDL_mutex.h: 134

# /usr/include/SDL/SDL_mutex.h: 138
if hasattr(_libs['SDL'], 'SDL_CreateCond'):
    SDL_CreateCond = _libs['SDL'].SDL_CreateCond
    SDL_CreateCond.argtypes = []
    SDL_CreateCond.restype = POINTER(SDL_cond)

# /usr/include/SDL/SDL_mutex.h: 141
if hasattr(_libs['SDL'], 'SDL_DestroyCond'):
    SDL_DestroyCond = _libs['SDL'].SDL_DestroyCond
    SDL_DestroyCond.argtypes = [POINTER(SDL_cond)]
    SDL_DestroyCond.restype = None

# /usr/include/SDL/SDL_mutex.h: 146
if hasattr(_libs['SDL'], 'SDL_CondSignal'):
    SDL_CondSignal = _libs['SDL'].SDL_CondSignal
    SDL_CondSignal.argtypes = [POINTER(SDL_cond)]
    SDL_CondSignal.restype = c_int

# /usr/include/SDL/SDL_mutex.h: 151
if hasattr(_libs['SDL'], 'SDL_CondBroadcast'):
    SDL_CondBroadcast = _libs['SDL'].SDL_CondBroadcast
    SDL_CondBroadcast.argtypes = [POINTER(SDL_cond)]
    SDL_CondBroadcast.restype = c_int

# /usr/include/SDL/SDL_mutex.h: 158
if hasattr(_libs['SDL'], 'SDL_CondWait'):
    SDL_CondWait = _libs['SDL'].SDL_CondWait
    SDL_CondWait.argtypes = [POINTER(SDL_cond), POINTER(SDL_mutex)]
    SDL_CondWait.restype = c_int

# /usr/include/SDL/SDL_mutex.h: 166
if hasattr(_libs['SDL'], 'SDL_CondWaitTimeout'):
    SDL_CondWaitTimeout = _libs['SDL'].SDL_CondWaitTimeout
    SDL_CondWaitTimeout.argtypes = [POINTER(SDL_cond), POINTER(SDL_mutex), Uint32]
    SDL_CondWaitTimeout.restype = c_int

# /usr/include/SDL/SDL_thread.h: 45
class struct_SDL_Thread(Structure):
    pass

SDL_Thread = struct_SDL_Thread # /usr/include/SDL/SDL_thread.h: 46

# /usr/include/SDL/SDL_thread.h: 93
if hasattr(_libs['SDL'], 'SDL_CreateThread'):
    SDL_CreateThread = _libs['SDL'].SDL_CreateThread
    SDL_CreateThread.argtypes = [CFUNCTYPE(UNCHECKED(c_int), POINTER(None)), POINTER(None)]
    SDL_CreateThread.restype = POINTER(SDL_Thread)

# /usr/include/SDL/SDL_thread.h: 97
if hasattr(_libs['SDL'], 'SDL_ThreadID'):
    SDL_ThreadID = _libs['SDL'].SDL_ThreadID
    SDL_ThreadID.argtypes = []
    SDL_ThreadID.restype = Uint32

# /usr/include/SDL/SDL_thread.h: 102
if hasattr(_libs['SDL'], 'SDL_GetThreadID'):
    SDL_GetThreadID = _libs['SDL'].SDL_GetThreadID
    SDL_GetThreadID.argtypes = [POINTER(SDL_Thread)]
    SDL_GetThreadID.restype = Uint32

# /usr/include/SDL/SDL_thread.h: 108
if hasattr(_libs['SDL'], 'SDL_WaitThread'):
    SDL_WaitThread = _libs['SDL'].SDL_WaitThread
    SDL_WaitThread.argtypes = [POINTER(SDL_Thread), POINTER(c_int)]
    SDL_WaitThread.restype = None

# /usr/include/SDL/SDL_thread.h: 111
if hasattr(_libs['SDL'], 'SDL_KillThread'):
    SDL_KillThread = _libs['SDL'].SDL_KillThread
    SDL_KillThread.argtypes = [POINTER(SDL_Thread)]
    SDL_KillThread.restype = None

# /usr/include/SDL/SDL_rwops.h: 42
class struct_SDL_RWops(Structure):
    pass

# /usr/include/SDL/SDL_rwops.h: 78
class struct_anon_29(Structure):
    pass

struct_anon_29.__slots__ = [
    'autoclose',
    'fp',
]
struct_anon_29._fields_ = [
    ('autoclose', c_int),
    ('fp', POINTER(FILE)),
]

# /usr/include/SDL/SDL_rwops.h: 83
class struct_anon_30(Structure):
    pass

struct_anon_30.__slots__ = [
    'base',
    'here',
    'stop',
]
struct_anon_30._fields_ = [
    ('base', POINTER(Uint8)),
    ('here', POINTER(Uint8)),
    ('stop', POINTER(Uint8)),
]

# /usr/include/SDL/SDL_rwops.h: 88
class struct_anon_31(Structure):
    pass

struct_anon_31.__slots__ = [
    'data1',
]
struct_anon_31._fields_ = [
    ('data1', POINTER(None)),
]

# /usr/include/SDL/SDL_rwops.h: 65
class union_anon_32(Union):
    pass

union_anon_32.__slots__ = [
    'stdio',
    'mem',
    'unknown',
]
union_anon_32._fields_ = [
    ('stdio', struct_anon_29),
    ('mem', struct_anon_30),
    ('unknown', struct_anon_31),
]

struct_SDL_RWops.__slots__ = [
    'seek',
    'read',
    'write',
    'close',
    'type',
    'hidden',
]
struct_SDL_RWops._fields_ = [
    ('seek', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_SDL_RWops), c_int, c_int)),
    ('read', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_SDL_RWops), POINTER(None), c_int, c_int)),
    ('write', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_SDL_RWops), POINTER(None), c_int, c_int)),
    ('close', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_SDL_RWops))),
    ('type', Uint32),
    ('hidden', union_anon_32),
]

SDL_RWops = struct_SDL_RWops # /usr/include/SDL/SDL_rwops.h: 93

# /usr/include/SDL/SDL_rwops.h: 99
if hasattr(_libs['SDL'], 'SDL_RWFromFile'):
    SDL_RWFromFile = _libs['SDL'].SDL_RWFromFile
    SDL_RWFromFile.argtypes = [String, String]
    SDL_RWFromFile.restype = POINTER(SDL_RWops)

# /usr/include/SDL/SDL_rwops.h: 102
if hasattr(_libs['SDL'], 'SDL_RWFromFP'):
    SDL_RWFromFP = _libs['SDL'].SDL_RWFromFP
    SDL_RWFromFP.argtypes = [POINTER(FILE), c_int]
    SDL_RWFromFP.restype = POINTER(SDL_RWops)

# /usr/include/SDL/SDL_rwops.h: 105
if hasattr(_libs['SDL'], 'SDL_RWFromMem'):
    SDL_RWFromMem = _libs['SDL'].SDL_RWFromMem
    SDL_RWFromMem.argtypes = [POINTER(None), c_int]
    SDL_RWFromMem.restype = POINTER(SDL_RWops)

# /usr/include/SDL/SDL_rwops.h: 106
if hasattr(_libs['SDL'], 'SDL_RWFromConstMem'):
    SDL_RWFromConstMem = _libs['SDL'].SDL_RWFromConstMem
    SDL_RWFromConstMem.argtypes = [POINTER(None), c_int]
    SDL_RWFromConstMem.restype = POINTER(SDL_RWops)

# /usr/include/SDL/SDL_rwops.h: 108
if hasattr(_libs['SDL'], 'SDL_AllocRW'):
    SDL_AllocRW = _libs['SDL'].SDL_AllocRW
    SDL_AllocRW.argtypes = []
    SDL_AllocRW.restype = POINTER(SDL_RWops)

# /usr/include/SDL/SDL_rwops.h: 109
if hasattr(_libs['SDL'], 'SDL_FreeRW'):
    SDL_FreeRW = _libs['SDL'].SDL_FreeRW
    SDL_FreeRW.argtypes = [POINTER(SDL_RWops)]
    SDL_FreeRW.restype = None

# /usr/include/SDL/SDL_rwops.h: 131
if hasattr(_libs['SDL'], 'SDL_ReadLE16'):
    SDL_ReadLE16 = _libs['SDL'].SDL_ReadLE16
    SDL_ReadLE16.argtypes = [POINTER(SDL_RWops)]
    SDL_ReadLE16.restype = Uint16

# /usr/include/SDL/SDL_rwops.h: 132
if hasattr(_libs['SDL'], 'SDL_ReadBE16'):
    SDL_ReadBE16 = _libs['SDL'].SDL_ReadBE16
    SDL_ReadBE16.argtypes = [POINTER(SDL_RWops)]
    SDL_ReadBE16.restype = Uint16

# /usr/include/SDL/SDL_rwops.h: 133
if hasattr(_libs['SDL'], 'SDL_ReadLE32'):
    SDL_ReadLE32 = _libs['SDL'].SDL_ReadLE32
    SDL_ReadLE32.argtypes = [POINTER(SDL_RWops)]
    SDL_ReadLE32.restype = Uint32

# /usr/include/SDL/SDL_rwops.h: 134
if hasattr(_libs['SDL'], 'SDL_ReadBE32'):
    SDL_ReadBE32 = _libs['SDL'].SDL_ReadBE32
    SDL_ReadBE32.argtypes = [POINTER(SDL_RWops)]
    SDL_ReadBE32.restype = Uint32

# /usr/include/SDL/SDL_rwops.h: 135
if hasattr(_libs['SDL'], 'SDL_ReadLE64'):
    SDL_ReadLE64 = _libs['SDL'].SDL_ReadLE64
    SDL_ReadLE64.argtypes = [POINTER(SDL_RWops)]
    SDL_ReadLE64.restype = Uint64

# /usr/include/SDL/SDL_rwops.h: 136
if hasattr(_libs['SDL'], 'SDL_ReadBE64'):
    SDL_ReadBE64 = _libs['SDL'].SDL_ReadBE64
    SDL_ReadBE64.argtypes = [POINTER(SDL_RWops)]
    SDL_ReadBE64.restype = Uint64

# /usr/include/SDL/SDL_rwops.h: 141
if hasattr(_libs['SDL'], 'SDL_WriteLE16'):
    SDL_WriteLE16 = _libs['SDL'].SDL_WriteLE16
    SDL_WriteLE16.argtypes = [POINTER(SDL_RWops), Uint16]
    SDL_WriteLE16.restype = c_int

# /usr/include/SDL/SDL_rwops.h: 142
if hasattr(_libs['SDL'], 'SDL_WriteBE16'):
    SDL_WriteBE16 = _libs['SDL'].SDL_WriteBE16
    SDL_WriteBE16.argtypes = [POINTER(SDL_RWops), Uint16]
    SDL_WriteBE16.restype = c_int

# /usr/include/SDL/SDL_rwops.h: 143
if hasattr(_libs['SDL'], 'SDL_WriteLE32'):
    SDL_WriteLE32 = _libs['SDL'].SDL_WriteLE32
    SDL_WriteLE32.argtypes = [POINTER(SDL_RWops), Uint32]
    SDL_WriteLE32.restype = c_int

# /usr/include/SDL/SDL_rwops.h: 144
if hasattr(_libs['SDL'], 'SDL_WriteBE32'):
    SDL_WriteBE32 = _libs['SDL'].SDL_WriteBE32
    SDL_WriteBE32.argtypes = [POINTER(SDL_RWops), Uint32]
    SDL_WriteBE32.restype = c_int

# /usr/include/SDL/SDL_rwops.h: 145
if hasattr(_libs['SDL'], 'SDL_WriteLE64'):
    SDL_WriteLE64 = _libs['SDL'].SDL_WriteLE64
    SDL_WriteLE64.argtypes = [POINTER(SDL_RWops), Uint64]
    SDL_WriteLE64.restype = c_int

# /usr/include/SDL/SDL_rwops.h: 146
if hasattr(_libs['SDL'], 'SDL_WriteBE64'):
    SDL_WriteBE64 = _libs['SDL'].SDL_WriteBE64
    SDL_WriteBE64.argtypes = [POINTER(SDL_RWops), Uint64]
    SDL_WriteBE64.restype = c_int

# /usr/include/SDL/SDL_audio.h: 93
class struct_SDL_AudioSpec(Structure):
    pass

struct_SDL_AudioSpec.__slots__ = [
    'freq',
    'format',
    'channels',
    'silence',
    'samples',
    'padding',
    'size',
    'callback',
    'userdata',
]
struct_SDL_AudioSpec._fields_ = [
    ('freq', c_int),
    ('format', Uint16),
    ('channels', Uint8),
    ('silence', Uint8),
    ('samples', Uint16),
    ('padding', Uint16),
    ('size', Uint32),
    ('callback', CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(Uint8), c_int)),
    ('userdata', POINTER(None)),
]

SDL_AudioSpec = struct_SDL_AudioSpec # /usr/include/SDL/SDL_audio.h: 93

# /usr/include/SDL/SDL_audio.h: 126
class struct_SDL_AudioCVT(Structure):
    pass

struct_SDL_AudioCVT.__slots__ = [
    'needed',
    'src_format',
    'dst_format',
    'rate_incr',
    'buf',
    'len',
    'len_cvt',
    'len_mult',
    'len_ratio',
    'filters',
    'filter_index',
]
struct_SDL_AudioCVT._fields_ = [
    ('needed', c_int),
    ('src_format', Uint16),
    ('dst_format', Uint16),
    ('rate_incr', c_double),
    ('buf', POINTER(Uint8)),
    ('len', c_int),
    ('len_cvt', c_int),
    ('len_mult', c_int),
    ('len_ratio', c_double),
    ('filters', POINTER(CFUNCTYPE(UNCHECKED(None), POINTER(struct_SDL_AudioCVT), Uint16)) * 10),
    ('filter_index', c_int),
]

SDL_AudioCVT = struct_SDL_AudioCVT # /usr/include/SDL/SDL_audio.h: 138

# /usr/include/SDL/SDL_audio.h: 150
if hasattr(_libs['SDL'], 'SDL_AudioInit'):
    SDL_AudioInit = _libs['SDL'].SDL_AudioInit
    SDL_AudioInit.argtypes = [String]
    SDL_AudioInit.restype = c_int

# /usr/include/SDL/SDL_audio.h: 151
if hasattr(_libs['SDL'], 'SDL_AudioQuit'):
    SDL_AudioQuit = _libs['SDL'].SDL_AudioQuit
    SDL_AudioQuit.argtypes = []
    SDL_AudioQuit.restype = None

# /usr/include/SDL/SDL_audio.h: 159
if hasattr(_libs['SDL'], 'SDL_AudioDriverName'):
    SDL_AudioDriverName = _libs['SDL'].SDL_AudioDriverName
    SDL_AudioDriverName.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_AudioDriverName.restype = ReturnString
    else:
        SDL_AudioDriverName.restype = String
        SDL_AudioDriverName.errcheck = ReturnString

# /usr/include/SDL/SDL_audio.h: 178
if hasattr(_libs['SDL'], 'SDL_OpenAudio'):
    SDL_OpenAudio = _libs['SDL'].SDL_OpenAudio
    SDL_OpenAudio.argtypes = [POINTER(SDL_AudioSpec), POINTER(SDL_AudioSpec)]
    SDL_OpenAudio.restype = c_int

enum_anon_33 = c_int # /usr/include/SDL/SDL_audio.h: 184

SDL_AUDIO_STOPPED = 0 # /usr/include/SDL/SDL_audio.h: 184

SDL_AUDIO_PLAYING = (SDL_AUDIO_STOPPED + 1) # /usr/include/SDL/SDL_audio.h: 184

SDL_AUDIO_PAUSED = (SDL_AUDIO_PLAYING + 1) # /usr/include/SDL/SDL_audio.h: 184

SDL_audiostatus = enum_anon_33 # /usr/include/SDL/SDL_audio.h: 184

# /usr/include/SDL/SDL_audio.h: 187
if hasattr(_libs['SDL'], 'SDL_GetAudioStatus'):
    SDL_GetAudioStatus = _libs['SDL'].SDL_GetAudioStatus
    SDL_GetAudioStatus.argtypes = []
    SDL_GetAudioStatus.restype = SDL_audiostatus

# /usr/include/SDL/SDL_audio.h: 196
if hasattr(_libs['SDL'], 'SDL_PauseAudio'):
    SDL_PauseAudio = _libs['SDL'].SDL_PauseAudio
    SDL_PauseAudio.argtypes = [c_int]
    SDL_PauseAudio.restype = None

# /usr/include/SDL/SDL_audio.h: 215
if hasattr(_libs['SDL'], 'SDL_LoadWAV_RW'):
    SDL_LoadWAV_RW = _libs['SDL'].SDL_LoadWAV_RW
    SDL_LoadWAV_RW.argtypes = [POINTER(SDL_RWops), c_int, POINTER(SDL_AudioSpec), POINTER(POINTER(Uint8)), POINTER(Uint32)]
    SDL_LoadWAV_RW.restype = POINTER(SDL_AudioSpec)

# /usr/include/SDL/SDL_audio.h: 224
if hasattr(_libs['SDL'], 'SDL_FreeWAV'):
    SDL_FreeWAV = _libs['SDL'].SDL_FreeWAV
    SDL_FreeWAV.argtypes = [POINTER(Uint8)]
    SDL_FreeWAV.restype = None

# /usr/include/SDL/SDL_audio.h: 234
if hasattr(_libs['SDL'], 'SDL_BuildAudioCVT'):
    SDL_BuildAudioCVT = _libs['SDL'].SDL_BuildAudioCVT
    SDL_BuildAudioCVT.argtypes = [POINTER(SDL_AudioCVT), Uint16, Uint8, c_int, Uint16, Uint8, c_int]
    SDL_BuildAudioCVT.restype = c_int

# /usr/include/SDL/SDL_audio.h: 247
if hasattr(_libs['SDL'], 'SDL_ConvertAudio'):
    SDL_ConvertAudio = _libs['SDL'].SDL_ConvertAudio
    SDL_ConvertAudio.argtypes = [POINTER(SDL_AudioCVT)]
    SDL_ConvertAudio.restype = c_int

# /usr/include/SDL/SDL_audio.h: 258
if hasattr(_libs['SDL'], 'SDL_MixAudio'):
    SDL_MixAudio = _libs['SDL'].SDL_MixAudio
    SDL_MixAudio.argtypes = [POINTER(Uint8), POINTER(Uint8), Uint32, c_int]
    SDL_MixAudio.restype = None

# /usr/include/SDL/SDL_audio.h: 268
if hasattr(_libs['SDL'], 'SDL_LockAudio'):
    SDL_LockAudio = _libs['SDL'].SDL_LockAudio
    SDL_LockAudio.argtypes = []
    SDL_LockAudio.restype = None

# /usr/include/SDL/SDL_audio.h: 269
if hasattr(_libs['SDL'], 'SDL_UnlockAudio'):
    SDL_UnlockAudio = _libs['SDL'].SDL_UnlockAudio
    SDL_UnlockAudio.argtypes = []
    SDL_UnlockAudio.restype = None

# /usr/include/SDL/SDL_audio.h: 275
if hasattr(_libs['SDL'], 'SDL_CloseAudio'):
    SDL_CloseAudio = _libs['SDL'].SDL_CloseAudio
    SDL_CloseAudio.argtypes = []
    SDL_CloseAudio.restype = None

enum_anon_34 = c_int # /usr/include/SDL/SDL_cdrom.h: 65

CD_TRAYEMPTY = 0 # /usr/include/SDL/SDL_cdrom.h: 65

CD_STOPPED = (CD_TRAYEMPTY + 1) # /usr/include/SDL/SDL_cdrom.h: 65

CD_PLAYING = (CD_STOPPED + 1) # /usr/include/SDL/SDL_cdrom.h: 65

CD_PAUSED = (CD_PLAYING + 1) # /usr/include/SDL/SDL_cdrom.h: 65

CD_ERROR = (-1) # /usr/include/SDL/SDL_cdrom.h: 65

CDstatus = enum_anon_34 # /usr/include/SDL/SDL_cdrom.h: 65

# /usr/include/SDL/SDL_cdrom.h: 76
class struct_SDL_CDtrack(Structure):
    pass

struct_SDL_CDtrack.__slots__ = [
    'id',
    'type',
    'unused',
    'length',
    'offset',
]
struct_SDL_CDtrack._fields_ = [
    ('id', Uint8),
    ('type', Uint8),
    ('unused', Uint16),
    ('length', Uint32),
    ('offset', Uint32),
]

SDL_CDtrack = struct_SDL_CDtrack # /usr/include/SDL/SDL_cdrom.h: 76

# /usr/include/SDL/SDL_cdrom.h: 90
class struct_SDL_CD(Structure):
    pass

struct_SDL_CD.__slots__ = [
    'id',
    'status',
    'numtracks',
    'cur_track',
    'cur_frame',
    'track',
]
struct_SDL_CD._fields_ = [
    ('id', c_int),
    ('status', CDstatus),
    ('numtracks', c_int),
    ('cur_track', c_int),
    ('cur_frame', c_int),
    ('track', SDL_CDtrack * (99 + 1)),
]

SDL_CD = struct_SDL_CD # /usr/include/SDL/SDL_cdrom.h: 90

# /usr/include/SDL/SDL_cdrom.h: 114
if hasattr(_libs['SDL'], 'SDL_CDNumDrives'):
    SDL_CDNumDrives = _libs['SDL'].SDL_CDNumDrives
    SDL_CDNumDrives.argtypes = []
    SDL_CDNumDrives.restype = c_int

# /usr/include/SDL/SDL_cdrom.h: 123
if hasattr(_libs['SDL'], 'SDL_CDName'):
    SDL_CDName = _libs['SDL'].SDL_CDName
    SDL_CDName.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_CDName.restype = ReturnString
    else:
        SDL_CDName.restype = String
        SDL_CDName.errcheck = ReturnString

# /usr/include/SDL/SDL_cdrom.h: 132
if hasattr(_libs['SDL'], 'SDL_CDOpen'):
    SDL_CDOpen = _libs['SDL'].SDL_CDOpen
    SDL_CDOpen.argtypes = [c_int]
    SDL_CDOpen.restype = POINTER(SDL_CD)

# /usr/include/SDL/SDL_cdrom.h: 139
if hasattr(_libs['SDL'], 'SDL_CDStatus'):
    SDL_CDStatus = _libs['SDL'].SDL_CDStatus
    SDL_CDStatus.argtypes = [POINTER(SDL_CD)]
    SDL_CDStatus.restype = CDstatus

# /usr/include/SDL/SDL_cdrom.h: 163
if hasattr(_libs['SDL'], 'SDL_CDPlayTracks'):
    SDL_CDPlayTracks = _libs['SDL'].SDL_CDPlayTracks
    SDL_CDPlayTracks.argtypes = [POINTER(SDL_CD), c_int, c_int, c_int, c_int]
    SDL_CDPlayTracks.restype = c_int

# /usr/include/SDL/SDL_cdrom.h: 170
if hasattr(_libs['SDL'], 'SDL_CDPlay'):
    SDL_CDPlay = _libs['SDL'].SDL_CDPlay
    SDL_CDPlay.argtypes = [POINTER(SDL_CD), c_int, c_int]
    SDL_CDPlay.restype = c_int

# /usr/include/SDL/SDL_cdrom.h: 175
if hasattr(_libs['SDL'], 'SDL_CDPause'):
    SDL_CDPause = _libs['SDL'].SDL_CDPause
    SDL_CDPause.argtypes = [POINTER(SDL_CD)]
    SDL_CDPause.restype = c_int

# /usr/include/SDL/SDL_cdrom.h: 180
if hasattr(_libs['SDL'], 'SDL_CDResume'):
    SDL_CDResume = _libs['SDL'].SDL_CDResume
    SDL_CDResume.argtypes = [POINTER(SDL_CD)]
    SDL_CDResume.restype = c_int

# /usr/include/SDL/SDL_cdrom.h: 185
if hasattr(_libs['SDL'], 'SDL_CDStop'):
    SDL_CDStop = _libs['SDL'].SDL_CDStop
    SDL_CDStop.argtypes = [POINTER(SDL_CD)]
    SDL_CDStop.restype = c_int

# /usr/include/SDL/SDL_cdrom.h: 190
if hasattr(_libs['SDL'], 'SDL_CDEject'):
    SDL_CDEject = _libs['SDL'].SDL_CDEject
    SDL_CDEject.argtypes = [POINTER(SDL_CD)]
    SDL_CDEject.restype = c_int

# /usr/include/SDL/SDL_cdrom.h: 193
if hasattr(_libs['SDL'], 'SDL_CDClose'):
    SDL_CDClose = _libs['SDL'].SDL_CDClose
    SDL_CDClose.argtypes = [POINTER(SDL_CD)]
    SDL_CDClose.restype = None

# /usr/include/SDL/SDL_cpuinfo.h: 40
if hasattr(_libs['SDL'], 'SDL_HasRDTSC'):
    SDL_HasRDTSC = _libs['SDL'].SDL_HasRDTSC
    SDL_HasRDTSC.argtypes = []
    SDL_HasRDTSC.restype = SDL_bool

# /usr/include/SDL/SDL_cpuinfo.h: 43
if hasattr(_libs['SDL'], 'SDL_HasMMX'):
    SDL_HasMMX = _libs['SDL'].SDL_HasMMX
    SDL_HasMMX.argtypes = []
    SDL_HasMMX.restype = SDL_bool

# /usr/include/SDL/SDL_cpuinfo.h: 46
if hasattr(_libs['SDL'], 'SDL_HasMMXExt'):
    SDL_HasMMXExt = _libs['SDL'].SDL_HasMMXExt
    SDL_HasMMXExt.argtypes = []
    SDL_HasMMXExt.restype = SDL_bool

# /usr/include/SDL/SDL_cpuinfo.h: 49
if hasattr(_libs['SDL'], 'SDL_Has3DNow'):
    SDL_Has3DNow = _libs['SDL'].SDL_Has3DNow
    SDL_Has3DNow.argtypes = []
    SDL_Has3DNow.restype = SDL_bool

# /usr/include/SDL/SDL_cpuinfo.h: 52
if hasattr(_libs['SDL'], 'SDL_Has3DNowExt'):
    SDL_Has3DNowExt = _libs['SDL'].SDL_Has3DNowExt
    SDL_Has3DNowExt.argtypes = []
    SDL_Has3DNowExt.restype = SDL_bool

# /usr/include/SDL/SDL_cpuinfo.h: 55
if hasattr(_libs['SDL'], 'SDL_HasSSE'):
    SDL_HasSSE = _libs['SDL'].SDL_HasSSE
    SDL_HasSSE.argtypes = []
    SDL_HasSSE.restype = SDL_bool

# /usr/include/SDL/SDL_cpuinfo.h: 58
if hasattr(_libs['SDL'], 'SDL_HasSSE2'):
    SDL_HasSSE2 = _libs['SDL'].SDL_HasSSE2
    SDL_HasSSE2.argtypes = []
    SDL_HasSSE2.restype = SDL_bool

# /usr/include/SDL/SDL_cpuinfo.h: 61
if hasattr(_libs['SDL'], 'SDL_HasAltiVec'):
    SDL_HasAltiVec = _libs['SDL'].SDL_HasAltiVec
    SDL_HasAltiVec.argtypes = []
    SDL_HasAltiVec.restype = SDL_bool

enum_anon_35 = c_int # /usr/include/SDL/SDL_keysym.h: 302

SDLK_UNKNOWN = 0 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_FIRST = 0 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_BACKSPACE = 8 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_TAB = 9 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_CLEAR = 12 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RETURN = 13 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_PAUSE = 19 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_ESCAPE = 27 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_SPACE = 32 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_EXCLAIM = 33 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_QUOTEDBL = 34 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_HASH = 35 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_DOLLAR = 36 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_AMPERSAND = 38 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_QUOTE = 39 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LEFTPAREN = 40 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RIGHTPAREN = 41 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_ASTERISK = 42 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_PLUS = 43 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_COMMA = 44 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_MINUS = 45 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_PERIOD = 46 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_SLASH = 47 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_0 = 48 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_1 = 49 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_2 = 50 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_3 = 51 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_4 = 52 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_5 = 53 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_6 = 54 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_7 = 55 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_8 = 56 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_9 = 57 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_COLON = 58 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_SEMICOLON = 59 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LESS = 60 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_EQUALS = 61 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_GREATER = 62 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_QUESTION = 63 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_AT = 64 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LEFTBRACKET = 91 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_BACKSLASH = 92 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RIGHTBRACKET = 93 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_CARET = 94 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_UNDERSCORE = 95 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_BACKQUOTE = 96 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_a = 97 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_b = 98 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_c = 99 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_d = 100 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_e = 101 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_f = 102 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_g = 103 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_h = 104 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_i = 105 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_j = 106 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_k = 107 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_l = 108 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_m = 109 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_n = 110 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_o = 111 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_p = 112 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_q = 113 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_r = 114 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_s = 115 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_t = 116 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_u = 117 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_v = 118 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_w = 119 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_x = 120 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_y = 121 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_z = 122 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_DELETE = 127 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_0 = 160 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_1 = 161 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_2 = 162 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_3 = 163 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_4 = 164 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_5 = 165 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_6 = 166 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_7 = 167 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_8 = 168 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_9 = 169 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_10 = 170 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_11 = 171 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_12 = 172 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_13 = 173 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_14 = 174 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_15 = 175 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_16 = 176 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_17 = 177 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_18 = 178 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_19 = 179 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_20 = 180 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_21 = 181 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_22 = 182 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_23 = 183 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_24 = 184 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_25 = 185 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_26 = 186 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_27 = 187 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_28 = 188 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_29 = 189 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_30 = 190 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_31 = 191 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_32 = 192 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_33 = 193 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_34 = 194 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_35 = 195 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_36 = 196 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_37 = 197 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_38 = 198 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_39 = 199 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_40 = 200 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_41 = 201 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_42 = 202 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_43 = 203 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_44 = 204 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_45 = 205 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_46 = 206 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_47 = 207 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_48 = 208 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_49 = 209 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_50 = 210 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_51 = 211 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_52 = 212 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_53 = 213 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_54 = 214 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_55 = 215 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_56 = 216 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_57 = 217 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_58 = 218 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_59 = 219 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_60 = 220 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_61 = 221 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_62 = 222 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_63 = 223 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_64 = 224 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_65 = 225 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_66 = 226 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_67 = 227 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_68 = 228 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_69 = 229 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_70 = 230 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_71 = 231 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_72 = 232 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_73 = 233 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_74 = 234 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_75 = 235 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_76 = 236 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_77 = 237 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_78 = 238 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_79 = 239 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_80 = 240 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_81 = 241 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_82 = 242 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_83 = 243 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_84 = 244 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_85 = 245 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_86 = 246 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_87 = 247 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_88 = 248 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_89 = 249 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_90 = 250 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_91 = 251 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_92 = 252 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_93 = 253 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_94 = 254 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_WORLD_95 = 255 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP0 = 256 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP1 = 257 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP2 = 258 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP3 = 259 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP4 = 260 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP5 = 261 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP6 = 262 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP7 = 263 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP8 = 264 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP9 = 265 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_PERIOD = 266 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_DIVIDE = 267 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_MULTIPLY = 268 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_MINUS = 269 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_PLUS = 270 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_ENTER = 271 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_KP_EQUALS = 272 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_UP = 273 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_DOWN = 274 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RIGHT = 275 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LEFT = 276 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_INSERT = 277 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_HOME = 278 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_END = 279 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_PAGEUP = 280 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_PAGEDOWN = 281 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F1 = 282 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F2 = 283 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F3 = 284 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F4 = 285 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F5 = 286 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F6 = 287 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F7 = 288 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F8 = 289 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F9 = 290 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F10 = 291 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F11 = 292 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F12 = 293 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F13 = 294 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F14 = 295 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_F15 = 296 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_NUMLOCK = 300 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_CAPSLOCK = 301 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_SCROLLOCK = 302 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RSHIFT = 303 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LSHIFT = 304 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RCTRL = 305 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LCTRL = 306 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RALT = 307 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LALT = 308 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RMETA = 309 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LMETA = 310 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LSUPER = 311 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_RSUPER = 312 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_MODE = 313 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_COMPOSE = 314 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_HELP = 315 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_PRINT = 316 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_SYSREQ = 317 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_BREAK = 318 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_MENU = 319 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_POWER = 320 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_EURO = 321 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_UNDO = 322 # /usr/include/SDL/SDL_keysym.h: 302

SDLK_LAST = (SDLK_UNDO + 1) # /usr/include/SDL/SDL_keysym.h: 302

SDLKey = enum_anon_35 # /usr/include/SDL/SDL_keysym.h: 302

enum_anon_36 = c_int # /usr/include/SDL/SDL_keysym.h: 319

KMOD_NONE = 0 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_LSHIFT = 1 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_RSHIFT = 2 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_LCTRL = 64 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_RCTRL = 128 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_LALT = 256 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_RALT = 512 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_LMETA = 1024 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_RMETA = 2048 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_NUM = 4096 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_CAPS = 8192 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_MODE = 16384 # /usr/include/SDL/SDL_keysym.h: 319

KMOD_RESERVED = 32768 # /usr/include/SDL/SDL_keysym.h: 319

SDLMod = enum_anon_36 # /usr/include/SDL/SDL_keysym.h: 319

# /usr/include/SDL/SDL_keyboard.h: 64
class struct_SDL_keysym(Structure):
    pass

struct_SDL_keysym.__slots__ = [
    'scancode',
    'sym',
    'mod',
    'unicode',
]
struct_SDL_keysym._fields_ = [
    ('scancode', Uint8),
    ('sym', SDLKey),
    ('mod', SDLMod),
    ('unicode', Uint16),
]

SDL_keysym = struct_SDL_keysym # /usr/include/SDL/SDL_keyboard.h: 64

# /usr/include/SDL/SDL_keyboard.h: 82
if hasattr(_libs['SDL'], 'SDL_EnableUNICODE'):
    SDL_EnableUNICODE = _libs['SDL'].SDL_EnableUNICODE
    SDL_EnableUNICODE.argtypes = [c_int]
    SDL_EnableUNICODE.restype = c_int

# /usr/include/SDL/SDL_keyboard.h: 98
if hasattr(_libs['SDL'], 'SDL_EnableKeyRepeat'):
    SDL_EnableKeyRepeat = _libs['SDL'].SDL_EnableKeyRepeat
    SDL_EnableKeyRepeat.argtypes = [c_int, c_int]
    SDL_EnableKeyRepeat.restype = c_int

# /usr/include/SDL/SDL_keyboard.h: 99
if hasattr(_libs['SDL'], 'SDL_GetKeyRepeat'):
    SDL_GetKeyRepeat = _libs['SDL'].SDL_GetKeyRepeat
    SDL_GetKeyRepeat.argtypes = [POINTER(c_int), POINTER(c_int)]
    SDL_GetKeyRepeat.restype = None

# /usr/include/SDL/SDL_keyboard.h: 110
if hasattr(_libs['SDL'], 'SDL_GetKeyState'):
    SDL_GetKeyState = _libs['SDL'].SDL_GetKeyState
    SDL_GetKeyState.argtypes = [POINTER(c_int)]
    SDL_GetKeyState.restype = POINTER(Uint8)

# /usr/include/SDL/SDL_keyboard.h: 115
if hasattr(_libs['SDL'], 'SDL_GetModState'):
    SDL_GetModState = _libs['SDL'].SDL_GetModState
    SDL_GetModState.argtypes = []
    SDL_GetModState.restype = SDLMod

# /usr/include/SDL/SDL_keyboard.h: 121
if hasattr(_libs['SDL'], 'SDL_SetModState'):
    SDL_SetModState = _libs['SDL'].SDL_SetModState
    SDL_SetModState.argtypes = [SDLMod]
    SDL_SetModState.restype = None

# /usr/include/SDL/SDL_keyboard.h: 126
if hasattr(_libs['SDL'], 'SDL_GetKeyName'):
    SDL_GetKeyName = _libs['SDL'].SDL_GetKeyName
    SDL_GetKeyName.argtypes = [SDLKey]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_GetKeyName.restype = ReturnString
    else:
        SDL_GetKeyName.restype = String
        SDL_GetKeyName.errcheck = ReturnString

# /usr/include/SDL/SDL_video.h: 53
class struct_SDL_Rect(Structure):
    pass

struct_SDL_Rect.__slots__ = [
    'x',
    'y',
    'w',
    'h',
]
struct_SDL_Rect._fields_ = [
    ('x', Sint16),
    ('y', Sint16),
    ('w', Uint16),
    ('h', Uint16),
]

SDL_Rect = struct_SDL_Rect # /usr/include/SDL/SDL_video.h: 53

# /usr/include/SDL/SDL_video.h: 60
class struct_SDL_Color(Structure):
    pass

struct_SDL_Color.__slots__ = [
    'r',
    'g',
    'b',
    'unused',
]
struct_SDL_Color._fields_ = [
    ('r', Uint8),
    ('g', Uint8),
    ('b', Uint8),
    ('unused', Uint8),
]

SDL_Color = struct_SDL_Color # /usr/include/SDL/SDL_video.h: 60

# /usr/include/SDL/SDL_video.h: 66
class struct_SDL_Palette(Structure):
    pass

struct_SDL_Palette.__slots__ = [
    'ncolors',
    'colors',
]
struct_SDL_Palette._fields_ = [
    ('ncolors', c_int),
    ('colors', POINTER(SDL_Color)),
]

SDL_Palette = struct_SDL_Palette # /usr/include/SDL/SDL_video.h: 66

# /usr/include/SDL/SDL_video.h: 91
class struct_SDL_PixelFormat(Structure):
    pass

struct_SDL_PixelFormat.__slots__ = [
    'palette',
    'BitsPerPixel',
    'BytesPerPixel',
    'Rloss',
    'Gloss',
    'Bloss',
    'Aloss',
    'Rshift',
    'Gshift',
    'Bshift',
    'Ashift',
    'Rmask',
    'Gmask',
    'Bmask',
    'Amask',
    'colorkey',
    'alpha',
]
struct_SDL_PixelFormat._fields_ = [
    ('palette', POINTER(SDL_Palette)),
    ('BitsPerPixel', Uint8),
    ('BytesPerPixel', Uint8),
    ('Rloss', Uint8),
    ('Gloss', Uint8),
    ('Bloss', Uint8),
    ('Aloss', Uint8),
    ('Rshift', Uint8),
    ('Gshift', Uint8),
    ('Bshift', Uint8),
    ('Ashift', Uint8),
    ('Rmask', Uint32),
    ('Gmask', Uint32),
    ('Bmask', Uint32),
    ('Amask', Uint32),
    ('colorkey', Uint32),
    ('alpha', Uint8),
]

SDL_PixelFormat = struct_SDL_PixelFormat # /usr/include/SDL/SDL_video.h: 91

# /usr/include/SDL/SDL_video.h: 105
class struct_private_hwdata(Structure):
    pass

# /usr/include/SDL/SDL_video.h: 115
class struct_SDL_BlitMap(Structure):
    pass

# /usr/include/SDL/SDL_video.h: 122
class struct_SDL_Surface(Structure):
    pass

struct_SDL_Surface.__slots__ = [
    'flags',
    'format',
    'w',
    'h',
    'pitch',
    'pixels',
    'offset',
    'hwdata',
    'clip_rect',
    'unused1',
    'locked',
    'map',
    'format_version',
    'refcount',
]
struct_SDL_Surface._fields_ = [
    ('flags', Uint32),
    ('format', POINTER(SDL_PixelFormat)),
    ('w', c_int),
    ('h', c_int),
    ('pitch', Uint16),
    ('pixels', POINTER(None)),
    ('offset', c_int),
    ('hwdata', POINTER(struct_private_hwdata)),
    ('clip_rect', SDL_Rect),
    ('unused1', Uint32),
    ('locked', Uint32),
    ('map', POINTER(struct_SDL_BlitMap)),
    ('format_version', c_uint),
    ('refcount', c_int),
]

SDL_Surface = struct_SDL_Surface # /usr/include/SDL/SDL_video.h: 122

SDL_blit = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_SDL_Surface), POINTER(SDL_Rect), POINTER(struct_SDL_Surface), POINTER(SDL_Rect)) # /usr/include/SDL/SDL_video.h: 166

# /usr/include/SDL/SDL_video.h: 188
class struct_SDL_VideoInfo(Structure):
    pass

struct_SDL_VideoInfo.__slots__ = [
    'hw_available',
    'wm_available',
    'UnusedBits1',
    'UnusedBits2',
    'blit_hw',
    'blit_hw_CC',
    'blit_hw_A',
    'blit_sw',
    'blit_sw_CC',
    'blit_sw_A',
    'blit_fill',
    'UnusedBits3',
    'video_mem',
    'vfmt',
    'current_w',
    'current_h',
]
struct_SDL_VideoInfo._fields_ = [
    ('hw_available', Uint32, 1),
    ('wm_available', Uint32, 1),
    ('UnusedBits1', Uint32, 6),
    ('UnusedBits2', Uint32, 1),
    ('blit_hw', Uint32, 1),
    ('blit_hw_CC', Uint32, 1),
    ('blit_hw_A', Uint32, 1),
    ('blit_sw', Uint32, 1),
    ('blit_sw_CC', Uint32, 1),
    ('blit_sw_A', Uint32, 1),
    ('blit_fill', Uint32, 1),
    ('UnusedBits3', Uint32, 16),
    ('video_mem', Uint32),
    ('vfmt', POINTER(SDL_PixelFormat)),
    ('current_w', c_int),
    ('current_h', c_int),
]

SDL_VideoInfo = struct_SDL_VideoInfo # /usr/include/SDL/SDL_video.h: 188

# /usr/include/SDL/SDL_video.h: 217
class struct_private_yuvhwfuncs(Structure):
    pass

# /usr/include/SDL/SDL_video.h: 218
class struct_private_yuvhwdata(Structure):
    pass

# /usr/include/SDL/SDL_video.h: 226
class struct_SDL_Overlay(Structure):
    pass

struct_SDL_Overlay.__slots__ = [
    'format',
    'w',
    'h',
    'planes',
    'pitches',
    'pixels',
    'hwfuncs',
    'hwdata',
    'hw_overlay',
    'UnusedBits',
]
struct_SDL_Overlay._fields_ = [
    ('format', Uint32),
    ('w', c_int),
    ('h', c_int),
    ('planes', c_int),
    ('pitches', POINTER(Uint16)),
    ('pixels', POINTER(POINTER(Uint8))),
    ('hwfuncs', POINTER(struct_private_yuvhwfuncs)),
    ('hwdata', POINTER(struct_private_yuvhwdata)),
    ('hw_overlay', Uint32, 1),
    ('UnusedBits', Uint32, 31),
]

SDL_Overlay = struct_SDL_Overlay # /usr/include/SDL/SDL_video.h: 226

enum_anon_37 = c_int # /usr/include/SDL/SDL_video.h: 248

SDL_GL_RED_SIZE = 0 # /usr/include/SDL/SDL_video.h: 248

SDL_GL_GREEN_SIZE = (SDL_GL_RED_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_BLUE_SIZE = (SDL_GL_GREEN_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_ALPHA_SIZE = (SDL_GL_BLUE_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_BUFFER_SIZE = (SDL_GL_ALPHA_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_DOUBLEBUFFER = (SDL_GL_BUFFER_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_DEPTH_SIZE = (SDL_GL_DOUBLEBUFFER + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_STENCIL_SIZE = (SDL_GL_DEPTH_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_ACCUM_RED_SIZE = (SDL_GL_STENCIL_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_ACCUM_GREEN_SIZE = (SDL_GL_ACCUM_RED_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_ACCUM_BLUE_SIZE = (SDL_GL_ACCUM_GREEN_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_ACCUM_ALPHA_SIZE = (SDL_GL_ACCUM_BLUE_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_STEREO = (SDL_GL_ACCUM_ALPHA_SIZE + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_MULTISAMPLEBUFFERS = (SDL_GL_STEREO + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_MULTISAMPLESAMPLES = (SDL_GL_MULTISAMPLEBUFFERS + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_ACCELERATED_VISUAL = (SDL_GL_MULTISAMPLESAMPLES + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GL_SWAP_CONTROL = (SDL_GL_ACCELERATED_VISUAL + 1) # /usr/include/SDL/SDL_video.h: 248

SDL_GLattr = enum_anon_37 # /usr/include/SDL/SDL_video.h: 248

# /usr/include/SDL/SDL_video.h: 275
if hasattr(_libs['SDL'], 'SDL_VideoInit'):
    SDL_VideoInit = _libs['SDL'].SDL_VideoInit
    SDL_VideoInit.argtypes = [String, Uint32]
    SDL_VideoInit.restype = c_int

# /usr/include/SDL/SDL_video.h: 276
if hasattr(_libs['SDL'], 'SDL_VideoQuit'):
    SDL_VideoQuit = _libs['SDL'].SDL_VideoQuit
    SDL_VideoQuit.argtypes = []
    SDL_VideoQuit.restype = None

# /usr/include/SDL/SDL_video.h: 284
if hasattr(_libs['SDL'], 'SDL_VideoDriverName'):
    SDL_VideoDriverName = _libs['SDL'].SDL_VideoDriverName
    SDL_VideoDriverName.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_VideoDriverName.restype = ReturnString
    else:
        SDL_VideoDriverName.restype = String
        SDL_VideoDriverName.errcheck = ReturnString

# /usr/include/SDL/SDL_video.h: 292
if hasattr(_libs['SDL'], 'SDL_GetVideoSurface'):
    SDL_GetVideoSurface = _libs['SDL'].SDL_GetVideoSurface
    SDL_GetVideoSurface.argtypes = []
    SDL_GetVideoSurface.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 300
if hasattr(_libs['SDL'], 'SDL_GetVideoInfo'):
    SDL_GetVideoInfo = _libs['SDL'].SDL_GetVideoInfo
    SDL_GetVideoInfo.argtypes = []
    SDL_GetVideoInfo.restype = POINTER(SDL_VideoInfo)

# /usr/include/SDL/SDL_video.h: 313
if hasattr(_libs['SDL'], 'SDL_VideoModeOK'):
    SDL_VideoModeOK = _libs['SDL'].SDL_VideoModeOK
    SDL_VideoModeOK.argtypes = [c_int, c_int, c_int, Uint32]
    SDL_VideoModeOK.restype = c_int

# /usr/include/SDL/SDL_video.h: 324
if hasattr(_libs['SDL'], 'SDL_ListModes'):
    SDL_ListModes = _libs['SDL'].SDL_ListModes
    SDL_ListModes.argtypes = [POINTER(SDL_PixelFormat), Uint32]
    SDL_ListModes.restype = POINTER(POINTER(SDL_Rect))

# /usr/include/SDL/SDL_video.h: 384
if hasattr(_libs['SDL'], 'SDL_SetVideoMode'):
    SDL_SetVideoMode = _libs['SDL'].SDL_SetVideoMode
    SDL_SetVideoMode.argtypes = [c_int, c_int, c_int, Uint32]
    SDL_SetVideoMode.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 394
if hasattr(_libs['SDL'], 'SDL_UpdateRects'):
    SDL_UpdateRects = _libs['SDL'].SDL_UpdateRects
    SDL_UpdateRects.argtypes = [POINTER(SDL_Surface), c_int, POINTER(SDL_Rect)]
    SDL_UpdateRects.restype = None

# /usr/include/SDL/SDL_video.h: 400
if hasattr(_libs['SDL'], 'SDL_UpdateRect'):
    SDL_UpdateRect = _libs['SDL'].SDL_UpdateRect
    SDL_UpdateRect.argtypes = [POINTER(SDL_Surface), Sint32, Sint32, Uint32, Uint32]
    SDL_UpdateRect.restype = None

# /usr/include/SDL/SDL_video.h: 414
if hasattr(_libs['SDL'], 'SDL_Flip'):
    SDL_Flip = _libs['SDL'].SDL_Flip
    SDL_Flip.argtypes = [POINTER(SDL_Surface)]
    SDL_Flip.restype = c_int

# /usr/include/SDL/SDL_video.h: 424
if hasattr(_libs['SDL'], 'SDL_SetGamma'):
    SDL_SetGamma = _libs['SDL'].SDL_SetGamma
    SDL_SetGamma.argtypes = [c_float, c_float, c_float]
    SDL_SetGamma.restype = c_int

# /usr/include/SDL/SDL_video.h: 438
if hasattr(_libs['SDL'], 'SDL_SetGammaRamp'):
    SDL_SetGammaRamp = _libs['SDL'].SDL_SetGammaRamp
    SDL_SetGammaRamp.argtypes = [POINTER(Uint16), POINTER(Uint16), POINTER(Uint16)]
    SDL_SetGammaRamp.restype = c_int

# /usr/include/SDL/SDL_video.h: 449
if hasattr(_libs['SDL'], 'SDL_GetGammaRamp'):
    SDL_GetGammaRamp = _libs['SDL'].SDL_GetGammaRamp
    SDL_GetGammaRamp.argtypes = [POINTER(Uint16), POINTER(Uint16), POINTER(Uint16)]
    SDL_GetGammaRamp.restype = c_int

# /usr/include/SDL/SDL_video.h: 466
if hasattr(_libs['SDL'], 'SDL_SetColors'):
    SDL_SetColors = _libs['SDL'].SDL_SetColors
    SDL_SetColors.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Color), c_int, c_int]
    SDL_SetColors.restype = c_int

# /usr/include/SDL/SDL_video.h: 485
if hasattr(_libs['SDL'], 'SDL_SetPalette'):
    SDL_SetPalette = _libs['SDL'].SDL_SetPalette
    SDL_SetPalette.argtypes = [POINTER(SDL_Surface), c_int, POINTER(SDL_Color), c_int, c_int]
    SDL_SetPalette.restype = c_int

# /usr/include/SDL/SDL_video.h: 492
if hasattr(_libs['SDL'], 'SDL_MapRGB'):
    SDL_MapRGB = _libs['SDL'].SDL_MapRGB
    SDL_MapRGB.argtypes = [POINTER(SDL_PixelFormat), Uint8, Uint8, Uint8]
    SDL_MapRGB.restype = Uint32

# /usr/include/SDL/SDL_video.h: 499
if hasattr(_libs['SDL'], 'SDL_MapRGBA'):
    SDL_MapRGBA = _libs['SDL'].SDL_MapRGBA
    SDL_MapRGBA.argtypes = [POINTER(SDL_PixelFormat), Uint8, Uint8, Uint8, Uint8]
    SDL_MapRGBA.restype = Uint32

# /usr/include/SDL/SDL_video.h: 506
if hasattr(_libs['SDL'], 'SDL_GetRGB'):
    SDL_GetRGB = _libs['SDL'].SDL_GetRGB
    SDL_GetRGB.argtypes = [Uint32, POINTER(SDL_PixelFormat), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8)]
    SDL_GetRGB.restype = None

# /usr/include/SDL/SDL_video.h: 513
if hasattr(_libs['SDL'], 'SDL_GetRGBA'):
    SDL_GetRGBA = _libs['SDL'].SDL_GetRGBA
    SDL_GetRGBA.argtypes = [Uint32, POINTER(SDL_PixelFormat), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8), POINTER(Uint8)]
    SDL_GetRGBA.restype = None

# /usr/include/SDL/SDL_video.h: 553
if hasattr(_libs['SDL'], 'SDL_CreateRGBSurface'):
    SDL_CreateRGBSurface = _libs['SDL'].SDL_CreateRGBSurface
    SDL_CreateRGBSurface.argtypes = [Uint32, c_int, c_int, c_int, Uint32, Uint32, Uint32, Uint32]
    SDL_CreateRGBSurface.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 557
if hasattr(_libs['SDL'], 'SDL_CreateRGBSurfaceFrom'):
    SDL_CreateRGBSurfaceFrom = _libs['SDL'].SDL_CreateRGBSurfaceFrom
    SDL_CreateRGBSurfaceFrom.argtypes = [POINTER(None), c_int, c_int, c_int, c_int, Uint32, Uint32, Uint32, Uint32]
    SDL_CreateRGBSurfaceFrom.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 560
if hasattr(_libs['SDL'], 'SDL_FreeSurface'):
    SDL_FreeSurface = _libs['SDL'].SDL_FreeSurface
    SDL_FreeSurface.argtypes = [POINTER(SDL_Surface)]
    SDL_FreeSurface.restype = None

# /usr/include/SDL/SDL_video.h: 580
if hasattr(_libs['SDL'], 'SDL_LockSurface'):
    SDL_LockSurface = _libs['SDL'].SDL_LockSurface
    SDL_LockSurface.argtypes = [POINTER(SDL_Surface)]
    SDL_LockSurface.restype = c_int

# /usr/include/SDL/SDL_video.h: 581
if hasattr(_libs['SDL'], 'SDL_UnlockSurface'):
    SDL_UnlockSurface = _libs['SDL'].SDL_UnlockSurface
    SDL_UnlockSurface.argtypes = [POINTER(SDL_Surface)]
    SDL_UnlockSurface.restype = None

# /usr/include/SDL/SDL_video.h: 589
if hasattr(_libs['SDL'], 'SDL_LoadBMP_RW'):
    SDL_LoadBMP_RW = _libs['SDL'].SDL_LoadBMP_RW
    SDL_LoadBMP_RW.argtypes = [POINTER(SDL_RWops), c_int]
    SDL_LoadBMP_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 599
if hasattr(_libs['SDL'], 'SDL_SaveBMP_RW'):
    SDL_SaveBMP_RW = _libs['SDL'].SDL_SaveBMP_RW
    SDL_SaveBMP_RW.argtypes = [POINTER(SDL_Surface), POINTER(SDL_RWops), c_int]
    SDL_SaveBMP_RW.restype = c_int

# /usr/include/SDL/SDL_video.h: 615
if hasattr(_libs['SDL'], 'SDL_SetColorKey'):
    SDL_SetColorKey = _libs['SDL'].SDL_SetColorKey
    SDL_SetColorKey.argtypes = [POINTER(SDL_Surface), Uint32, Uint32]
    SDL_SetColorKey.restype = c_int

# /usr/include/SDL/SDL_video.h: 633
if hasattr(_libs['SDL'], 'SDL_SetAlpha'):
    SDL_SetAlpha = _libs['SDL'].SDL_SetAlpha
    SDL_SetAlpha.argtypes = [POINTER(SDL_Surface), Uint32, Uint8]
    SDL_SetAlpha.restype = c_int

# /usr/include/SDL/SDL_video.h: 647
if hasattr(_libs['SDL'], 'SDL_SetClipRect'):
    SDL_SetClipRect = _libs['SDL'].SDL_SetClipRect
    SDL_SetClipRect.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect)]
    SDL_SetClipRect.restype = SDL_bool

# /usr/include/SDL/SDL_video.h: 654
if hasattr(_libs['SDL'], 'SDL_GetClipRect'):
    SDL_GetClipRect = _libs['SDL'].SDL_GetClipRect
    SDL_GetClipRect.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect)]
    SDL_GetClipRect.restype = None

# /usr/include/SDL/SDL_video.h: 668
if hasattr(_libs['SDL'], 'SDL_ConvertSurface'):
    SDL_ConvertSurface = _libs['SDL'].SDL_ConvertSurface
    SDL_ConvertSurface.argtypes = [POINTER(SDL_Surface), POINTER(SDL_PixelFormat), Uint32]
    SDL_ConvertSurface.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 748
if hasattr(_libs['SDL'], 'SDL_UpperBlit'):
    SDL_UpperBlit = _libs['SDL'].SDL_UpperBlit
    SDL_UpperBlit.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect)]
    SDL_UpperBlit.restype = c_int

# /usr/include/SDL/SDL_video.h: 754
if hasattr(_libs['SDL'], 'SDL_LowerBlit'):
    SDL_LowerBlit = _libs['SDL'].SDL_LowerBlit
    SDL_LowerBlit.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect)]
    SDL_LowerBlit.restype = c_int

# /usr/include/SDL/SDL_video.h: 767
if hasattr(_libs['SDL'], 'SDL_FillRect'):
    SDL_FillRect = _libs['SDL'].SDL_FillRect
    SDL_FillRect.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), Uint32]
    SDL_FillRect.restype = c_int

# /usr/include/SDL/SDL_video.h: 781
if hasattr(_libs['SDL'], 'SDL_DisplayFormat'):
    SDL_DisplayFormat = _libs['SDL'].SDL_DisplayFormat
    SDL_DisplayFormat.argtypes = [POINTER(SDL_Surface)]
    SDL_DisplayFormat.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 795
if hasattr(_libs['SDL'], 'SDL_DisplayFormatAlpha'):
    SDL_DisplayFormatAlpha = _libs['SDL'].SDL_DisplayFormatAlpha
    SDL_DisplayFormatAlpha.argtypes = [POINTER(SDL_Surface)]
    SDL_DisplayFormatAlpha.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_video.h: 807
if hasattr(_libs['SDL'], 'SDL_CreateYUVOverlay'):
    SDL_CreateYUVOverlay = _libs['SDL'].SDL_CreateYUVOverlay
    SDL_CreateYUVOverlay.argtypes = [c_int, c_int, Uint32, POINTER(SDL_Surface)]
    SDL_CreateYUVOverlay.restype = POINTER(SDL_Overlay)

# /usr/include/SDL/SDL_video.h: 811
if hasattr(_libs['SDL'], 'SDL_LockYUVOverlay'):
    SDL_LockYUVOverlay = _libs['SDL'].SDL_LockYUVOverlay
    SDL_LockYUVOverlay.argtypes = [POINTER(SDL_Overlay)]
    SDL_LockYUVOverlay.restype = c_int

# /usr/include/SDL/SDL_video.h: 812
if hasattr(_libs['SDL'], 'SDL_UnlockYUVOverlay'):
    SDL_UnlockYUVOverlay = _libs['SDL'].SDL_UnlockYUVOverlay
    SDL_UnlockYUVOverlay.argtypes = [POINTER(SDL_Overlay)]
    SDL_UnlockYUVOverlay.restype = None

# /usr/include/SDL/SDL_video.h: 820
if hasattr(_libs['SDL'], 'SDL_DisplayYUVOverlay'):
    SDL_DisplayYUVOverlay = _libs['SDL'].SDL_DisplayYUVOverlay
    SDL_DisplayYUVOverlay.argtypes = [POINTER(SDL_Overlay), POINTER(SDL_Rect)]
    SDL_DisplayYUVOverlay.restype = c_int

# /usr/include/SDL/SDL_video.h: 823
if hasattr(_libs['SDL'], 'SDL_FreeYUVOverlay'):
    SDL_FreeYUVOverlay = _libs['SDL'].SDL_FreeYUVOverlay
    SDL_FreeYUVOverlay.argtypes = [POINTER(SDL_Overlay)]
    SDL_FreeYUVOverlay.restype = None

# /usr/include/SDL/SDL_video.h: 837
if hasattr(_libs['SDL'], 'SDL_GL_LoadLibrary'):
    SDL_GL_LoadLibrary = _libs['SDL'].SDL_GL_LoadLibrary
    SDL_GL_LoadLibrary.argtypes = [String]
    SDL_GL_LoadLibrary.restype = c_int

# /usr/include/SDL/SDL_video.h: 842
if hasattr(_libs['SDL'], 'SDL_GL_GetProcAddress'):
    SDL_GL_GetProcAddress = _libs['SDL'].SDL_GL_GetProcAddress
    SDL_GL_GetProcAddress.argtypes = [String]
    SDL_GL_GetProcAddress.restype = POINTER(None)

# /usr/include/SDL/SDL_video.h: 847
if hasattr(_libs['SDL'], 'SDL_GL_SetAttribute'):
    SDL_GL_SetAttribute = _libs['SDL'].SDL_GL_SetAttribute
    SDL_GL_SetAttribute.argtypes = [SDL_GLattr, c_int]
    SDL_GL_SetAttribute.restype = c_int

# /usr/include/SDL/SDL_video.h: 858
if hasattr(_libs['SDL'], 'SDL_GL_GetAttribute'):
    SDL_GL_GetAttribute = _libs['SDL'].SDL_GL_GetAttribute
    SDL_GL_GetAttribute.argtypes = [SDL_GLattr, POINTER(c_int)]
    SDL_GL_GetAttribute.restype = c_int

# /usr/include/SDL/SDL_video.h: 863
if hasattr(_libs['SDL'], 'SDL_GL_SwapBuffers'):
    SDL_GL_SwapBuffers = _libs['SDL'].SDL_GL_SwapBuffers
    SDL_GL_SwapBuffers.argtypes = []
    SDL_GL_SwapBuffers.restype = None

# /usr/include/SDL/SDL_video.h: 870
if hasattr(_libs['SDL'], 'SDL_GL_UpdateRects'):
    SDL_GL_UpdateRects = _libs['SDL'].SDL_GL_UpdateRects
    SDL_GL_UpdateRects.argtypes = [c_int, POINTER(SDL_Rect)]
    SDL_GL_UpdateRects.restype = None

# /usr/include/SDL/SDL_video.h: 871
if hasattr(_libs['SDL'], 'SDL_GL_Lock'):
    SDL_GL_Lock = _libs['SDL'].SDL_GL_Lock
    SDL_GL_Lock.argtypes = []
    SDL_GL_Lock.restype = None

# /usr/include/SDL/SDL_video.h: 872
if hasattr(_libs['SDL'], 'SDL_GL_Unlock'):
    SDL_GL_Unlock = _libs['SDL'].SDL_GL_Unlock
    SDL_GL_Unlock.argtypes = []
    SDL_GL_Unlock.restype = None

# /usr/include/SDL/SDL_video.h: 885
if hasattr(_libs['SDL'], 'SDL_WM_SetCaption'):
    SDL_WM_SetCaption = _libs['SDL'].SDL_WM_SetCaption
    SDL_WM_SetCaption.argtypes = [String, String]
    SDL_WM_SetCaption.restype = None

# /usr/include/SDL/SDL_video.h: 889
if hasattr(_libs['SDL'], 'SDL_WM_GetCaption'):
    SDL_WM_GetCaption = _libs['SDL'].SDL_WM_GetCaption
    SDL_WM_GetCaption.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    SDL_WM_GetCaption.restype = None

# /usr/include/SDL/SDL_video.h: 897
if hasattr(_libs['SDL'], 'SDL_WM_SetIcon'):
    SDL_WM_SetIcon = _libs['SDL'].SDL_WM_SetIcon
    SDL_WM_SetIcon.argtypes = [POINTER(SDL_Surface), POINTER(Uint8)]
    SDL_WM_SetIcon.restype = None

# /usr/include/SDL/SDL_video.h: 904
if hasattr(_libs['SDL'], 'SDL_WM_IconifyWindow'):
    SDL_WM_IconifyWindow = _libs['SDL'].SDL_WM_IconifyWindow
    SDL_WM_IconifyWindow.argtypes = []
    SDL_WM_IconifyWindow.restype = c_int

# /usr/include/SDL/SDL_video.h: 921
if hasattr(_libs['SDL'], 'SDL_WM_ToggleFullScreen'):
    SDL_WM_ToggleFullScreen = _libs['SDL'].SDL_WM_ToggleFullScreen
    SDL_WM_ToggleFullScreen.argtypes = [POINTER(SDL_Surface)]
    SDL_WM_ToggleFullScreen.restype = c_int

enum_anon_38 = c_int # /usr/include/SDL/SDL_video.h: 928

SDL_GRAB_QUERY = (-1) # /usr/include/SDL/SDL_video.h: 928

SDL_GRAB_OFF = 0 # /usr/include/SDL/SDL_video.h: 928

SDL_GRAB_ON = 1 # /usr/include/SDL/SDL_video.h: 928

SDL_GRAB_FULLSCREEN = (SDL_GRAB_ON + 1) # /usr/include/SDL/SDL_video.h: 928

SDL_GrabMode = enum_anon_38 # /usr/include/SDL/SDL_video.h: 928

# /usr/include/SDL/SDL_video.h: 937
if hasattr(_libs['SDL'], 'SDL_WM_GrabInput'):
    SDL_WM_GrabInput = _libs['SDL'].SDL_WM_GrabInput
    SDL_WM_GrabInput.argtypes = [SDL_GrabMode]
    SDL_WM_GrabInput.restype = SDL_GrabMode

# /usr/include/SDL/SDL_video.h: 942
if hasattr(_libs['SDL'], 'SDL_SoftStretch'):
    SDL_SoftStretch = _libs['SDL'].SDL_SoftStretch
    SDL_SoftStretch.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect)]
    SDL_SoftStretch.restype = c_int

# /usr/include/SDL/SDL_mouse.h: 40
class struct_WMcursor(Structure):
    pass

WMcursor = struct_WMcursor # /usr/include/SDL/SDL_mouse.h: 40

# /usr/include/SDL/SDL_mouse.h: 48
class struct_SDL_Cursor(Structure):
    pass

struct_SDL_Cursor.__slots__ = [
    'area',
    'hot_x',
    'hot_y',
    'data',
    'mask',
    'save',
    'wm_cursor',
]
struct_SDL_Cursor._fields_ = [
    ('area', SDL_Rect),
    ('hot_x', Sint16),
    ('hot_y', Sint16),
    ('data', POINTER(Uint8)),
    ('mask', POINTER(Uint8)),
    ('save', POINTER(Uint8) * 2),
    ('wm_cursor', POINTER(WMcursor)),
]

SDL_Cursor = struct_SDL_Cursor # /usr/include/SDL/SDL_mouse.h: 48

# /usr/include/SDL/SDL_mouse.h: 57
if hasattr(_libs['SDL'], 'SDL_GetMouseState'):
    SDL_GetMouseState = _libs['SDL'].SDL_GetMouseState
    SDL_GetMouseState.argtypes = [POINTER(c_int), POINTER(c_int)]
    SDL_GetMouseState.restype = Uint8

# /usr/include/SDL/SDL_mouse.h: 65
if hasattr(_libs['SDL'], 'SDL_GetRelativeMouseState'):
    SDL_GetRelativeMouseState = _libs['SDL'].SDL_GetRelativeMouseState
    SDL_GetRelativeMouseState.argtypes = [POINTER(c_int), POINTER(c_int)]
    SDL_GetRelativeMouseState.restype = Uint8

# /usr/include/SDL/SDL_mouse.h: 70
if hasattr(_libs['SDL'], 'SDL_WarpMouse'):
    SDL_WarpMouse = _libs['SDL'].SDL_WarpMouse
    SDL_WarpMouse.argtypes = [Uint16, Uint16]
    SDL_WarpMouse.restype = None

# /usr/include/SDL/SDL_mouse.h: 85
if hasattr(_libs['SDL'], 'SDL_CreateCursor'):
    SDL_CreateCursor = _libs['SDL'].SDL_CreateCursor
    SDL_CreateCursor.argtypes = [POINTER(Uint8), POINTER(Uint8), c_int, c_int, c_int, c_int]
    SDL_CreateCursor.restype = POINTER(SDL_Cursor)

# /usr/include/SDL/SDL_mouse.h: 93
if hasattr(_libs['SDL'], 'SDL_SetCursor'):
    SDL_SetCursor = _libs['SDL'].SDL_SetCursor
    SDL_SetCursor.argtypes = [POINTER(SDL_Cursor)]
    SDL_SetCursor.restype = None

# /usr/include/SDL/SDL_mouse.h: 98
if hasattr(_libs['SDL'], 'SDL_GetCursor'):
    SDL_GetCursor = _libs['SDL'].SDL_GetCursor
    SDL_GetCursor.argtypes = []
    SDL_GetCursor.restype = POINTER(SDL_Cursor)

# /usr/include/SDL/SDL_mouse.h: 103
if hasattr(_libs['SDL'], 'SDL_FreeCursor'):
    SDL_FreeCursor = _libs['SDL'].SDL_FreeCursor
    SDL_FreeCursor.argtypes = [POINTER(SDL_Cursor)]
    SDL_FreeCursor.restype = None

# /usr/include/SDL/SDL_mouse.h: 112
if hasattr(_libs['SDL'], 'SDL_ShowCursor'):
    SDL_ShowCursor = _libs['SDL'].SDL_ShowCursor
    SDL_ShowCursor.argtypes = [c_int]
    SDL_ShowCursor.restype = c_int

# /usr/include/SDL/SDL_joystick.h: 46
class struct__SDL_Joystick(Structure):
    pass

SDL_Joystick = struct__SDL_Joystick # /usr/include/SDL/SDL_joystick.h: 47

# /usr/include/SDL/SDL_joystick.h: 53
if hasattr(_libs['SDL'], 'SDL_NumJoysticks'):
    SDL_NumJoysticks = _libs['SDL'].SDL_NumJoysticks
    SDL_NumJoysticks.argtypes = []
    SDL_NumJoysticks.restype = c_int

# /usr/include/SDL/SDL_joystick.h: 61
if hasattr(_libs['SDL'], 'SDL_JoystickName'):
    SDL_JoystickName = _libs['SDL'].SDL_JoystickName
    SDL_JoystickName.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        SDL_JoystickName.restype = ReturnString
    else:
        SDL_JoystickName.restype = String
        SDL_JoystickName.errcheck = ReturnString

# /usr/include/SDL/SDL_joystick.h: 73
if hasattr(_libs['SDL'], 'SDL_JoystickOpen'):
    SDL_JoystickOpen = _libs['SDL'].SDL_JoystickOpen
    SDL_JoystickOpen.argtypes = [c_int]
    SDL_JoystickOpen.restype = POINTER(SDL_Joystick)

# /usr/include/SDL/SDL_joystick.h: 78
if hasattr(_libs['SDL'], 'SDL_JoystickOpened'):
    SDL_JoystickOpened = _libs['SDL'].SDL_JoystickOpened
    SDL_JoystickOpened.argtypes = [c_int]
    SDL_JoystickOpened.restype = c_int

# /usr/include/SDL/SDL_joystick.h: 83
if hasattr(_libs['SDL'], 'SDL_JoystickIndex'):
    SDL_JoystickIndex = _libs['SDL'].SDL_JoystickIndex
    SDL_JoystickIndex.argtypes = [POINTER(SDL_Joystick)]
    SDL_JoystickIndex.restype = c_int

# /usr/include/SDL/SDL_joystick.h: 88
if hasattr(_libs['SDL'], 'SDL_JoystickNumAxes'):
    SDL_JoystickNumAxes = _libs['SDL'].SDL_JoystickNumAxes
    SDL_JoystickNumAxes.argtypes = [POINTER(SDL_Joystick)]
    SDL_JoystickNumAxes.restype = c_int

# /usr/include/SDL/SDL_joystick.h: 96
if hasattr(_libs['SDL'], 'SDL_JoystickNumBalls'):
    SDL_JoystickNumBalls = _libs['SDL'].SDL_JoystickNumBalls
    SDL_JoystickNumBalls.argtypes = [POINTER(SDL_Joystick)]
    SDL_JoystickNumBalls.restype = c_int

# /usr/include/SDL/SDL_joystick.h: 101
if hasattr(_libs['SDL'], 'SDL_JoystickNumHats'):
    SDL_JoystickNumHats = _libs['SDL'].SDL_JoystickNumHats
    SDL_JoystickNumHats.argtypes = [POINTER(SDL_Joystick)]
    SDL_JoystickNumHats.restype = c_int

# /usr/include/SDL/SDL_joystick.h: 106
if hasattr(_libs['SDL'], 'SDL_JoystickNumButtons'):
    SDL_JoystickNumButtons = _libs['SDL'].SDL_JoystickNumButtons
    SDL_JoystickNumButtons.argtypes = [POINTER(SDL_Joystick)]
    SDL_JoystickNumButtons.restype = c_int

# /usr/include/SDL/SDL_joystick.h: 114
if hasattr(_libs['SDL'], 'SDL_JoystickUpdate'):
    SDL_JoystickUpdate = _libs['SDL'].SDL_JoystickUpdate
    SDL_JoystickUpdate.argtypes = []
    SDL_JoystickUpdate.restype = None

# /usr/include/SDL/SDL_joystick.h: 125
if hasattr(_libs['SDL'], 'SDL_JoystickEventState'):
    SDL_JoystickEventState = _libs['SDL'].SDL_JoystickEventState
    SDL_JoystickEventState.argtypes = [c_int]
    SDL_JoystickEventState.restype = c_int

# /usr/include/SDL/SDL_joystick.h: 134
if hasattr(_libs['SDL'], 'SDL_JoystickGetAxis'):
    SDL_JoystickGetAxis = _libs['SDL'].SDL_JoystickGetAxis
    SDL_JoystickGetAxis.argtypes = [POINTER(SDL_Joystick), c_int]
    SDL_JoystickGetAxis.restype = Sint16

# /usr/include/SDL/SDL_joystick.h: 157
if hasattr(_libs['SDL'], 'SDL_JoystickGetHat'):
    SDL_JoystickGetHat = _libs['SDL'].SDL_JoystickGetHat
    SDL_JoystickGetHat.argtypes = [POINTER(SDL_Joystick), c_int]
    SDL_JoystickGetHat.restype = Uint8

# /usr/include/SDL/SDL_joystick.h: 166
if hasattr(_libs['SDL'], 'SDL_JoystickGetBall'):
    SDL_JoystickGetBall = _libs['SDL'].SDL_JoystickGetBall
    SDL_JoystickGetBall.argtypes = [POINTER(SDL_Joystick), c_int, POINTER(c_int), POINTER(c_int)]
    SDL_JoystickGetBall.restype = c_int

# /usr/include/SDL/SDL_joystick.h: 173
if hasattr(_libs['SDL'], 'SDL_JoystickGetButton'):
    SDL_JoystickGetButton = _libs['SDL'].SDL_JoystickGetButton
    SDL_JoystickGetButton.argtypes = [POINTER(SDL_Joystick), c_int]
    SDL_JoystickGetButton.restype = Uint8

# /usr/include/SDL/SDL_joystick.h: 178
if hasattr(_libs['SDL'], 'SDL_JoystickClose'):
    SDL_JoystickClose = _libs['SDL'].SDL_JoystickClose
    SDL_JoystickClose.argtypes = [POINTER(SDL_Joystick)]
    SDL_JoystickClose.restype = None

enum_anon_39 = c_int # /usr/include/SDL/SDL_events.h: 83

SDL_NOEVENT = 0 # /usr/include/SDL/SDL_events.h: 83

SDL_ACTIVEEVENT = (SDL_NOEVENT + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_KEYDOWN = (SDL_ACTIVEEVENT + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_KEYUP = (SDL_KEYDOWN + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_MOUSEMOTION = (SDL_KEYUP + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_MOUSEBUTTONDOWN = (SDL_MOUSEMOTION + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_MOUSEBUTTONUP = (SDL_MOUSEBUTTONDOWN + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_JOYAXISMOTION = (SDL_MOUSEBUTTONUP + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_JOYBALLMOTION = (SDL_JOYAXISMOTION + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_JOYHATMOTION = (SDL_JOYBALLMOTION + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_JOYBUTTONDOWN = (SDL_JOYHATMOTION + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_JOYBUTTONUP = (SDL_JOYBUTTONDOWN + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_QUIT = (SDL_JOYBUTTONUP + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_SYSWMEVENT = (SDL_QUIT + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVEDA = (SDL_SYSWMEVENT + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVEDB = (SDL_EVENT_RESERVEDA + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_VIDEORESIZE = (SDL_EVENT_RESERVEDB + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_VIDEOEXPOSE = (SDL_VIDEORESIZE + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVED2 = (SDL_VIDEOEXPOSE + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVED3 = (SDL_EVENT_RESERVED2 + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVED4 = (SDL_EVENT_RESERVED3 + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVED5 = (SDL_EVENT_RESERVED4 + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVED6 = (SDL_EVENT_RESERVED5 + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_EVENT_RESERVED7 = (SDL_EVENT_RESERVED6 + 1) # /usr/include/SDL/SDL_events.h: 83

SDL_USEREVENT = 24 # /usr/include/SDL/SDL_events.h: 83

SDL_NUMEVENTS = 32 # /usr/include/SDL/SDL_events.h: 83

SDL_EventType = enum_anon_39 # /usr/include/SDL/SDL_events.h: 83

enum_anon_40 = c_int # /usr/include/SDL/SDL_events.h: 114

SDL_ACTIVEEVENTMASK = (1 << SDL_ACTIVEEVENT) # /usr/include/SDL/SDL_events.h: 114

SDL_KEYDOWNMASK = (1 << SDL_KEYDOWN) # /usr/include/SDL/SDL_events.h: 114

SDL_KEYUPMASK = (1 << SDL_KEYUP) # /usr/include/SDL/SDL_events.h: 114

SDL_KEYEVENTMASK = ((1 << SDL_KEYDOWN) | (1 << SDL_KEYUP)) # /usr/include/SDL/SDL_events.h: 114

SDL_MOUSEMOTIONMASK = (1 << SDL_MOUSEMOTION) # /usr/include/SDL/SDL_events.h: 114

SDL_MOUSEBUTTONDOWNMASK = (1 << SDL_MOUSEBUTTONDOWN) # /usr/include/SDL/SDL_events.h: 114

SDL_MOUSEBUTTONUPMASK = (1 << SDL_MOUSEBUTTONUP) # /usr/include/SDL/SDL_events.h: 114

SDL_MOUSEEVENTMASK = (((1 << SDL_MOUSEMOTION) | (1 << SDL_MOUSEBUTTONDOWN)) | (1 << SDL_MOUSEBUTTONUP)) # /usr/include/SDL/SDL_events.h: 114

SDL_JOYAXISMOTIONMASK = (1 << SDL_JOYAXISMOTION) # /usr/include/SDL/SDL_events.h: 114

SDL_JOYBALLMOTIONMASK = (1 << SDL_JOYBALLMOTION) # /usr/include/SDL/SDL_events.h: 114

SDL_JOYHATMOTIONMASK = (1 << SDL_JOYHATMOTION) # /usr/include/SDL/SDL_events.h: 114

SDL_JOYBUTTONDOWNMASK = (1 << SDL_JOYBUTTONDOWN) # /usr/include/SDL/SDL_events.h: 114

SDL_JOYBUTTONUPMASK = (1 << SDL_JOYBUTTONUP) # /usr/include/SDL/SDL_events.h: 114

SDL_JOYEVENTMASK = (((((1 << SDL_JOYAXISMOTION) | (1 << SDL_JOYBALLMOTION)) | (1 << SDL_JOYHATMOTION)) | (1 << SDL_JOYBUTTONDOWN)) | (1 << SDL_JOYBUTTONUP)) # /usr/include/SDL/SDL_events.h: 114

SDL_VIDEORESIZEMASK = (1 << SDL_VIDEORESIZE) # /usr/include/SDL/SDL_events.h: 114

SDL_VIDEOEXPOSEMASK = (1 << SDL_VIDEOEXPOSE) # /usr/include/SDL/SDL_events.h: 114

SDL_QUITMASK = (1 << SDL_QUIT) # /usr/include/SDL/SDL_events.h: 114

SDL_SYSWMEVENTMASK = (1 << SDL_SYSWMEVENT) # /usr/include/SDL/SDL_events.h: 114

SDL_EventMask = enum_anon_40 # /usr/include/SDL/SDL_events.h: 114

# /usr/include/SDL/SDL_events.h: 123
class struct_SDL_ActiveEvent(Structure):
    pass

struct_SDL_ActiveEvent.__slots__ = [
    'type',
    'gain',
    'state',
]
struct_SDL_ActiveEvent._fields_ = [
    ('type', Uint8),
    ('gain', Uint8),
    ('state', Uint8),
]

SDL_ActiveEvent = struct_SDL_ActiveEvent # /usr/include/SDL/SDL_events.h: 123

# /usr/include/SDL/SDL_events.h: 131
class struct_SDL_KeyboardEvent(Structure):
    pass

struct_SDL_KeyboardEvent.__slots__ = [
    'type',
    'which',
    'state',
    'keysym',
]
struct_SDL_KeyboardEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('state', Uint8),
    ('keysym', SDL_keysym),
]

SDL_KeyboardEvent = struct_SDL_KeyboardEvent # /usr/include/SDL/SDL_events.h: 131

# /usr/include/SDL/SDL_events.h: 141
class struct_SDL_MouseMotionEvent(Structure):
    pass

struct_SDL_MouseMotionEvent.__slots__ = [
    'type',
    'which',
    'state',
    'x',
    'y',
    'xrel',
    'yrel',
]
struct_SDL_MouseMotionEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('state', Uint8),
    ('x', Uint16),
    ('y', Uint16),
    ('xrel', Sint16),
    ('yrel', Sint16),
]

SDL_MouseMotionEvent = struct_SDL_MouseMotionEvent # /usr/include/SDL/SDL_events.h: 141

# /usr/include/SDL/SDL_events.h: 150
class struct_SDL_MouseButtonEvent(Structure):
    pass

struct_SDL_MouseButtonEvent.__slots__ = [
    'type',
    'which',
    'button',
    'state',
    'x',
    'y',
]
struct_SDL_MouseButtonEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('button', Uint8),
    ('state', Uint8),
    ('x', Uint16),
    ('y', Uint16),
]

SDL_MouseButtonEvent = struct_SDL_MouseButtonEvent # /usr/include/SDL/SDL_events.h: 150

# /usr/include/SDL/SDL_events.h: 158
class struct_SDL_JoyAxisEvent(Structure):
    pass

struct_SDL_JoyAxisEvent.__slots__ = [
    'type',
    'which',
    'axis',
    'value',
]
struct_SDL_JoyAxisEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('axis', Uint8),
    ('value', Sint16),
]

SDL_JoyAxisEvent = struct_SDL_JoyAxisEvent # /usr/include/SDL/SDL_events.h: 158

# /usr/include/SDL/SDL_events.h: 167
class struct_SDL_JoyBallEvent(Structure):
    pass

struct_SDL_JoyBallEvent.__slots__ = [
    'type',
    'which',
    'ball',
    'xrel',
    'yrel',
]
struct_SDL_JoyBallEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('ball', Uint8),
    ('xrel', Sint16),
    ('yrel', Sint16),
]

SDL_JoyBallEvent = struct_SDL_JoyBallEvent # /usr/include/SDL/SDL_events.h: 167

# /usr/include/SDL/SDL_events.h: 180
class struct_SDL_JoyHatEvent(Structure):
    pass

struct_SDL_JoyHatEvent.__slots__ = [
    'type',
    'which',
    'hat',
    'value',
]
struct_SDL_JoyHatEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('hat', Uint8),
    ('value', Uint8),
]

SDL_JoyHatEvent = struct_SDL_JoyHatEvent # /usr/include/SDL/SDL_events.h: 180

# /usr/include/SDL/SDL_events.h: 188
class struct_SDL_JoyButtonEvent(Structure):
    pass

struct_SDL_JoyButtonEvent.__slots__ = [
    'type',
    'which',
    'button',
    'state',
]
struct_SDL_JoyButtonEvent._fields_ = [
    ('type', Uint8),
    ('which', Uint8),
    ('button', Uint8),
    ('state', Uint8),
]

SDL_JoyButtonEvent = struct_SDL_JoyButtonEvent # /usr/include/SDL/SDL_events.h: 188

# /usr/include/SDL/SDL_events.h: 198
class struct_SDL_ResizeEvent(Structure):
    pass

struct_SDL_ResizeEvent.__slots__ = [
    'type',
    'w',
    'h',
]
struct_SDL_ResizeEvent._fields_ = [
    ('type', Uint8),
    ('w', c_int),
    ('h', c_int),
]

SDL_ResizeEvent = struct_SDL_ResizeEvent # /usr/include/SDL/SDL_events.h: 198

# /usr/include/SDL/SDL_events.h: 203
class struct_SDL_ExposeEvent(Structure):
    pass

struct_SDL_ExposeEvent.__slots__ = [
    'type',
]
struct_SDL_ExposeEvent._fields_ = [
    ('type', Uint8),
]

SDL_ExposeEvent = struct_SDL_ExposeEvent # /usr/include/SDL/SDL_events.h: 203

# /usr/include/SDL/SDL_events.h: 208
class struct_SDL_QuitEvent(Structure):
    pass

struct_SDL_QuitEvent.__slots__ = [
    'type',
]
struct_SDL_QuitEvent._fields_ = [
    ('type', Uint8),
]

SDL_QuitEvent = struct_SDL_QuitEvent # /usr/include/SDL/SDL_events.h: 208

# /usr/include/SDL/SDL_events.h: 216
class struct_SDL_UserEvent(Structure):
    pass

struct_SDL_UserEvent.__slots__ = [
    'type',
    'code',
    'data1',
    'data2',
]
struct_SDL_UserEvent._fields_ = [
    ('type', Uint8),
    ('code', c_int),
    ('data1', POINTER(None)),
    ('data2', POINTER(None)),
]

SDL_UserEvent = struct_SDL_UserEvent # /usr/include/SDL/SDL_events.h: 216

# /usr/include/SDL/SDL_syswm.h: 72
class struct_SDL_SysWMmsg(Structure):
    pass

SDL_SysWMmsg = struct_SDL_SysWMmsg # /usr/include/SDL/SDL_events.h: 220

# /usr/include/SDL/SDL_events.h: 224
class struct_SDL_SysWMEvent(Structure):
    pass

struct_SDL_SysWMEvent.__slots__ = [
    'type',
    'msg',
]
struct_SDL_SysWMEvent._fields_ = [
    ('type', Uint8),
    ('msg', POINTER(SDL_SysWMmsg)),
]

SDL_SysWMEvent = struct_SDL_SysWMEvent # /usr/include/SDL/SDL_events.h: 224

# /usr/include/SDL/SDL_events.h: 242
class union_SDL_Event(Union):
    pass

union_SDL_Event.__slots__ = [
    'type',
    'active',
    'key',
    'motion',
    'button',
    'jaxis',
    'jball',
    'jhat',
    'jbutton',
    'resize',
    'expose',
    'quit',
    'user',
    'syswm',
]
union_SDL_Event._fields_ = [
    ('type', Uint8),
    ('active', SDL_ActiveEvent),
    ('key', SDL_KeyboardEvent),
    ('motion', SDL_MouseMotionEvent),
    ('button', SDL_MouseButtonEvent),
    ('jaxis', SDL_JoyAxisEvent),
    ('jball', SDL_JoyBallEvent),
    ('jhat', SDL_JoyHatEvent),
    ('jbutton', SDL_JoyButtonEvent),
    ('resize', SDL_ResizeEvent),
    ('expose', SDL_ExposeEvent),
    ('quit', SDL_QuitEvent),
    ('user', SDL_UserEvent),
    ('syswm', SDL_SysWMEvent),
]

SDL_Event = union_SDL_Event # /usr/include/SDL/SDL_events.h: 242

# /usr/include/SDL/SDL_events.h: 251
if hasattr(_libs['SDL'], 'SDL_PumpEvents'):
    SDL_PumpEvents = _libs['SDL'].SDL_PumpEvents
    SDL_PumpEvents.argtypes = []
    SDL_PumpEvents.restype = None

enum_anon_41 = c_int # /usr/include/SDL/SDL_events.h: 257

SDL_ADDEVENT = 0 # /usr/include/SDL/SDL_events.h: 257

SDL_PEEKEVENT = (SDL_ADDEVENT + 1) # /usr/include/SDL/SDL_events.h: 257

SDL_GETEVENT = (SDL_PEEKEVENT + 1) # /usr/include/SDL/SDL_events.h: 257

SDL_eventaction = enum_anon_41 # /usr/include/SDL/SDL_events.h: 257

# /usr/include/SDL/SDL_events.h: 277
if hasattr(_libs['SDL'], 'SDL_PeepEvents'):
    SDL_PeepEvents = _libs['SDL'].SDL_PeepEvents
    SDL_PeepEvents.argtypes = [POINTER(SDL_Event), c_int, SDL_eventaction, Uint32]
    SDL_PeepEvents.restype = c_int

# /usr/include/SDL/SDL_events.h: 284
if hasattr(_libs['SDL'], 'SDL_PollEvent'):
    SDL_PollEvent = _libs['SDL'].SDL_PollEvent
    SDL_PollEvent.argtypes = [POINTER(SDL_Event)]
    SDL_PollEvent.restype = c_int

# /usr/include/SDL/SDL_events.h: 290
if hasattr(_libs['SDL'], 'SDL_WaitEvent'):
    SDL_WaitEvent = _libs['SDL'].SDL_WaitEvent
    SDL_WaitEvent.argtypes = [POINTER(SDL_Event)]
    SDL_WaitEvent.restype = c_int

# /usr/include/SDL/SDL_events.h: 296
if hasattr(_libs['SDL'], 'SDL_PushEvent'):
    SDL_PushEvent = _libs['SDL'].SDL_PushEvent
    SDL_PushEvent.argtypes = [POINTER(SDL_Event)]
    SDL_PushEvent.restype = c_int

SDL_EventFilter = CFUNCTYPE(UNCHECKED(c_int), POINTER(SDL_Event)) # /usr/include/SDL/SDL_events.h: 300

# /usr/include/SDL/SDL_events.h: 323
if hasattr(_libs['SDL'], 'SDL_SetEventFilter'):
    SDL_SetEventFilter = _libs['SDL'].SDL_SetEventFilter
    SDL_SetEventFilter.argtypes = [SDL_EventFilter]
    SDL_SetEventFilter.restype = None

# /usr/include/SDL/SDL_events.h: 329
if hasattr(_libs['SDL'], 'SDL_GetEventFilter'):
    SDL_GetEventFilter = _libs['SDL'].SDL_GetEventFilter
    SDL_GetEventFilter.argtypes = []
    SDL_GetEventFilter.restype = SDL_EventFilter

# /usr/include/SDL/SDL_events.h: 348
if hasattr(_libs['SDL'], 'SDL_EventState'):
    SDL_EventState = _libs['SDL'].SDL_EventState
    SDL_EventState.argtypes = [Uint8, c_int]
    SDL_EventState.restype = Uint8

# /usr/include/SDL/SDL_loadso.h: 60
if hasattr(_libs['SDL'], 'SDL_LoadObject'):
    SDL_LoadObject = _libs['SDL'].SDL_LoadObject
    SDL_LoadObject.argtypes = [String]
    SDL_LoadObject.restype = POINTER(None)

# /usr/include/SDL/SDL_loadso.h: 67
if hasattr(_libs['SDL'], 'SDL_LoadFunction'):
    SDL_LoadFunction = _libs['SDL'].SDL_LoadFunction
    SDL_LoadFunction.argtypes = [POINTER(None), String]
    SDL_LoadFunction.restype = POINTER(None)

# /usr/include/SDL/SDL_loadso.h: 70
if hasattr(_libs['SDL'], 'SDL_UnloadObject'):
    SDL_UnloadObject = _libs['SDL'].SDL_UnloadObject
    SDL_UnloadObject.argtypes = [POINTER(None)]
    SDL_UnloadObject.restype = None

# /usr/include/SDL/SDL_timer.h: 49
if hasattr(_libs['SDL'], 'SDL_GetTicks'):
    SDL_GetTicks = _libs['SDL'].SDL_GetTicks
    SDL_GetTicks.argtypes = []
    SDL_GetTicks.restype = Uint32

# /usr/include/SDL/SDL_timer.h: 52
if hasattr(_libs['SDL'], 'SDL_Delay'):
    SDL_Delay = _libs['SDL'].SDL_Delay
    SDL_Delay.argtypes = [Uint32]
    SDL_Delay.restype = None

SDL_TimerCallback = CFUNCTYPE(UNCHECKED(Uint32), Uint32) # /usr/include/SDL/SDL_timer.h: 55

# /usr/include/SDL/SDL_timer.h: 86
if hasattr(_libs['SDL'], 'SDL_SetTimer'):
    SDL_SetTimer = _libs['SDL'].SDL_SetTimer
    SDL_SetTimer.argtypes = [Uint32, SDL_TimerCallback]
    SDL_SetTimer.restype = c_int

SDL_NewTimerCallback = CFUNCTYPE(UNCHECKED(Uint32), Uint32, POINTER(None)) # /usr/include/SDL/SDL_timer.h: 101

# /usr/include/SDL/SDL_timer.h: 104
class struct__SDL_TimerID(Structure):
    pass

SDL_TimerID = POINTER(struct__SDL_TimerID) # /usr/include/SDL/SDL_timer.h: 104

# /usr/include/SDL/SDL_timer.h: 109
if hasattr(_libs['SDL'], 'SDL_AddTimer'):
    SDL_AddTimer = _libs['SDL'].SDL_AddTimer
    SDL_AddTimer.argtypes = [Uint32, SDL_NewTimerCallback, POINTER(None)]
    SDL_AddTimer.restype = SDL_TimerID

# /usr/include/SDL/SDL_timer.h: 115
if hasattr(_libs['SDL'], 'SDL_RemoveTimer'):
    SDL_RemoveTimer = _libs['SDL'].SDL_RemoveTimer
    SDL_RemoveTimer.argtypes = [SDL_TimerID]
    SDL_RemoveTimer.restype = SDL_bool

# /usr/include/SDL/SDL_version.h: 51
class struct_SDL_version(Structure):
    pass

struct_SDL_version.__slots__ = [
    'major',
    'minor',
    'patch',
]
struct_SDL_version._fields_ = [
    ('major', Uint8),
    ('minor', Uint8),
    ('patch', Uint8),
]

SDL_version = struct_SDL_version # /usr/include/SDL/SDL_version.h: 51

# /usr/include/SDL/SDL_version.h: 83
if hasattr(_libs['SDL'], 'SDL_Linked_Version'):
    SDL_Linked_Version = _libs['SDL'].SDL_Linked_Version
    SDL_Linked_Version.argtypes = []
    SDL_Linked_Version.restype = POINTER(SDL_version)

# /usr/include/SDL/SDL.h: 76
if hasattr(_libs['SDL'], 'SDL_Init'):
    SDL_Init = _libs['SDL'].SDL_Init
    SDL_Init.argtypes = [Uint32]
    SDL_Init.restype = c_int

# /usr/include/SDL/SDL.h: 79
if hasattr(_libs['SDL'], 'SDL_InitSubSystem'):
    SDL_InitSubSystem = _libs['SDL'].SDL_InitSubSystem
    SDL_InitSubSystem.argtypes = [Uint32]
    SDL_InitSubSystem.restype = c_int

# /usr/include/SDL/SDL.h: 82
if hasattr(_libs['SDL'], 'SDL_QuitSubSystem'):
    SDL_QuitSubSystem = _libs['SDL'].SDL_QuitSubSystem
    SDL_QuitSubSystem.argtypes = [Uint32]
    SDL_QuitSubSystem.restype = None

# /usr/include/SDL/SDL.h: 88
if hasattr(_libs['SDL'], 'SDL_WasInit'):
    SDL_WasInit = _libs['SDL'].SDL_WasInit
    SDL_WasInit.argtypes = [Uint32]
    SDL_WasInit.restype = Uint32

# /usr/include/SDL/SDL.h: 93
if hasattr(_libs['SDL'], 'SDL_Quit'):
    SDL_Quit = _libs['SDL'].SDL_Quit
    SDL_Quit.argtypes = []
    SDL_Quit.restype = None

# /usr/include/SDL/SDL_framerate.h: 47
class struct_anon_42(Structure):
    pass

struct_anon_42.__slots__ = [
    'framecount',
    'rateticks',
    'lastticks',
    'rate',
]
struct_anon_42._fields_ = [
    ('framecount', Uint32),
    ('rateticks', c_float),
    ('lastticks', Uint32),
    ('rate', Uint32),
]

FPSmanager = struct_anon_42 # /usr/include/SDL/SDL_framerate.h: 47

# /usr/include/SDL/SDL_framerate.h: 66
if hasattr(_libs['SDL_gfx'], 'SDL_initFramerate'):
    SDL_initFramerate = _libs['SDL_gfx'].SDL_initFramerate
    SDL_initFramerate.argtypes = [POINTER(FPSmanager)]
    SDL_initFramerate.restype = None

# /usr/include/SDL/SDL_framerate.h: 67
if hasattr(_libs['SDL_gfx'], 'SDL_setFramerate'):
    SDL_setFramerate = _libs['SDL_gfx'].SDL_setFramerate
    SDL_setFramerate.argtypes = [POINTER(FPSmanager), c_int]
    SDL_setFramerate.restype = c_int

# /usr/include/SDL/SDL_framerate.h: 68
if hasattr(_libs['SDL_gfx'], 'SDL_getFramerate'):
    SDL_getFramerate = _libs['SDL_gfx'].SDL_getFramerate
    SDL_getFramerate.argtypes = [POINTER(FPSmanager)]
    SDL_getFramerate.restype = c_int

# /usr/include/SDL/SDL_framerate.h: 69
if hasattr(_libs['SDL_gfx'], 'SDL_getFramecount'):
    SDL_getFramecount = _libs['SDL_gfx'].SDL_getFramecount
    SDL_getFramecount.argtypes = [POINTER(FPSmanager)]
    SDL_getFramecount.restype = c_int

# /usr/include/SDL/SDL_framerate.h: 70
if hasattr(_libs['SDL_gfx'], 'SDL_framerateDelay'):
    SDL_framerateDelay = _libs['SDL_gfx'].SDL_framerateDelay
    SDL_framerateDelay.argtypes = [POINTER(FPSmanager)]
    SDL_framerateDelay.restype = None

# /usr/include/SDL/SDL_gfxBlitFunc.h: 39
if hasattr(_libs['SDL_gfx'], 'SDL_gfxBlitRGBA'):
    SDL_gfxBlitRGBA = _libs['SDL_gfx'].SDL_gfxBlitRGBA
    SDL_gfxBlitRGBA.argtypes = [POINTER(SDL_Surface), POINTER(SDL_Rect), POINTER(SDL_Surface), POINTER(SDL_Rect)]
    SDL_gfxBlitRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxBlitFunc.h: 41
if hasattr(_libs['SDL_gfx'], 'SDL_gfxSetAlpha'):
    SDL_gfxSetAlpha = _libs['SDL_gfx'].SDL_gfxSetAlpha
    SDL_gfxSetAlpha.argtypes = [POINTER(SDL_Surface), Uint8]
    SDL_gfxSetAlpha.restype = c_int

# /usr/include/SDL/SDL_gfxBlitFunc.h: 43
if hasattr(_libs['SDL_gfx'], 'SDL_gfxMultiplyAlpha'):
    SDL_gfxMultiplyAlpha = _libs['SDL_gfx'].SDL_gfxMultiplyAlpha
    SDL_gfxMultiplyAlpha.argtypes = [POINTER(SDL_Surface), Uint8]
    SDL_gfxMultiplyAlpha.restype = c_int

# /usr/include/SDL/SDL_gfxBlitFunc.h: 66
class struct_anon_43(Structure):
    pass

struct_anon_43.__slots__ = [
    's_pixels',
    's_width',
    's_height',
    's_skip',
    'd_pixels',
    'd_width',
    'd_height',
    'd_skip',
    'aux_data',
    'src',
    'table',
    'dst',
]
struct_anon_43._fields_ = [
    ('s_pixels', POINTER(Uint8)),
    ('s_width', c_int),
    ('s_height', c_int),
    ('s_skip', c_int),
    ('d_pixels', POINTER(Uint8)),
    ('d_width', c_int),
    ('d_height', c_int),
    ('d_skip', c_int),
    ('aux_data', POINTER(None)),
    ('src', POINTER(SDL_PixelFormat)),
    ('table', POINTER(Uint8)),
    ('dst', POINTER(SDL_PixelFormat)),
]

SDL_gfxBlitInfo = struct_anon_43 # /usr/include/SDL/SDL_gfxBlitFunc.h: 66

# /usr/include/SDL/SDL_gfxPrimitives.h: 50
if hasattr(_libs['SDL_gfx'], 'pixelColor'):
    pixelColor = _libs['SDL_gfx'].pixelColor
    pixelColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Uint32]
    pixelColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 51
if hasattr(_libs['SDL_gfx'], 'pixelRGBA'):
    pixelRGBA = _libs['SDL_gfx'].pixelRGBA
    pixelRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    pixelRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 55
if hasattr(_libs['SDL_gfx'], 'hlineColor'):
    hlineColor = _libs['SDL_gfx'].hlineColor
    hlineColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Uint32]
    hlineColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 56
if hasattr(_libs['SDL_gfx'], 'hlineRGBA'):
    hlineRGBA = _libs['SDL_gfx'].hlineRGBA
    hlineRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    hlineRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 60
if hasattr(_libs['SDL_gfx'], 'vlineColor'):
    vlineColor = _libs['SDL_gfx'].vlineColor
    vlineColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Uint32]
    vlineColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 61
if hasattr(_libs['SDL_gfx'], 'vlineRGBA'):
    vlineRGBA = _libs['SDL_gfx'].vlineRGBA
    vlineRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    vlineRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 65
if hasattr(_libs['SDL_gfx'], 'rectangleColor'):
    rectangleColor = _libs['SDL_gfx'].rectangleColor
    rectangleColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint32]
    rectangleColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 66
if hasattr(_libs['SDL_gfx'], 'rectangleRGBA'):
    rectangleRGBA = _libs['SDL_gfx'].rectangleRGBA
    rectangleRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    rectangleRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 71
if hasattr(_libs['SDL_gfx'], 'roundedRectangleColor'):
    roundedRectangleColor = _libs['SDL_gfx'].roundedRectangleColor
    roundedRectangleColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Uint32]
    roundedRectangleColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 72
if hasattr(_libs['SDL_gfx'], 'roundedRectangleRGBA'):
    roundedRectangleRGBA = _libs['SDL_gfx'].roundedRectangleRGBA
    roundedRectangleRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    roundedRectangleRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 77
if hasattr(_libs['SDL_gfx'], 'boxColor'):
    boxColor = _libs['SDL_gfx'].boxColor
    boxColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint32]
    boxColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 78
if hasattr(_libs['SDL_gfx'], 'boxRGBA'):
    boxRGBA = _libs['SDL_gfx'].boxRGBA
    boxRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    boxRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 83
if hasattr(_libs['SDL_gfx'], 'roundedBoxColor'):
    roundedBoxColor = _libs['SDL_gfx'].roundedBoxColor
    roundedBoxColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Uint32]
    roundedBoxColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 84
if hasattr(_libs['SDL_gfx'], 'roundedBoxRGBA'):
    roundedBoxRGBA = _libs['SDL_gfx'].roundedBoxRGBA
    roundedBoxRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    roundedBoxRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 89
if hasattr(_libs['SDL_gfx'], 'lineColor'):
    lineColor = _libs['SDL_gfx'].lineColor
    lineColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint32]
    lineColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 90
if hasattr(_libs['SDL_gfx'], 'lineRGBA'):
    lineRGBA = _libs['SDL_gfx'].lineRGBA
    lineRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    lineRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 95
if hasattr(_libs['SDL_gfx'], 'aalineColor'):
    aalineColor = _libs['SDL_gfx'].aalineColor
    aalineColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint32]
    aalineColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 96
if hasattr(_libs['SDL_gfx'], 'aalineRGBA'):
    aalineRGBA = _libs['SDL_gfx'].aalineRGBA
    aalineRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    aalineRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 100
if hasattr(_libs['SDL_gfx'], 'thickLineColor'):
    thickLineColor = _libs['SDL_gfx'].thickLineColor
    thickLineColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint8, Uint32]
    thickLineColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 102
if hasattr(_libs['SDL_gfx'], 'thickLineRGBA'):
    thickLineRGBA = _libs['SDL_gfx'].thickLineRGBA
    thickLineRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8, Uint8]
    thickLineRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 107
if hasattr(_libs['SDL_gfx'], 'circleColor'):
    circleColor = _libs['SDL_gfx'].circleColor
    circleColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Uint32]
    circleColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 108
if hasattr(_libs['SDL_gfx'], 'circleRGBA'):
    circleRGBA = _libs['SDL_gfx'].circleRGBA
    circleRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    circleRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 112
if hasattr(_libs['SDL_gfx'], 'arcColor'):
    arcColor = _libs['SDL_gfx'].arcColor
    arcColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Uint32]
    arcColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 113
if hasattr(_libs['SDL_gfx'], 'arcRGBA'):
    arcRGBA = _libs['SDL_gfx'].arcRGBA
    arcRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    arcRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 118
if hasattr(_libs['SDL_gfx'], 'aacircleColor'):
    aacircleColor = _libs['SDL_gfx'].aacircleColor
    aacircleColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Uint32]
    aacircleColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 119
if hasattr(_libs['SDL_gfx'], 'aacircleRGBA'):
    aacircleRGBA = _libs['SDL_gfx'].aacircleRGBA
    aacircleRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    aacircleRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 124
if hasattr(_libs['SDL_gfx'], 'filledCircleColor'):
    filledCircleColor = _libs['SDL_gfx'].filledCircleColor
    filledCircleColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Uint32]
    filledCircleColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 125
if hasattr(_libs['SDL_gfx'], 'filledCircleRGBA'):
    filledCircleRGBA = _libs['SDL_gfx'].filledCircleRGBA
    filledCircleRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    filledCircleRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 130
if hasattr(_libs['SDL_gfx'], 'ellipseColor'):
    ellipseColor = _libs['SDL_gfx'].ellipseColor
    ellipseColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint32]
    ellipseColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 131
if hasattr(_libs['SDL_gfx'], 'ellipseRGBA'):
    ellipseRGBA = _libs['SDL_gfx'].ellipseRGBA
    ellipseRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    ellipseRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 136
if hasattr(_libs['SDL_gfx'], 'aaellipseColor'):
    aaellipseColor = _libs['SDL_gfx'].aaellipseColor
    aaellipseColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint32]
    aaellipseColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 137
if hasattr(_libs['SDL_gfx'], 'aaellipseRGBA'):
    aaellipseRGBA = _libs['SDL_gfx'].aaellipseRGBA
    aaellipseRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    aaellipseRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 142
if hasattr(_libs['SDL_gfx'], 'filledEllipseColor'):
    filledEllipseColor = _libs['SDL_gfx'].filledEllipseColor
    filledEllipseColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint32]
    filledEllipseColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 143
if hasattr(_libs['SDL_gfx'], 'filledEllipseRGBA'):
    filledEllipseRGBA = _libs['SDL_gfx'].filledEllipseRGBA
    filledEllipseRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    filledEllipseRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 148
if hasattr(_libs['SDL_gfx'], 'pieColor'):
    pieColor = _libs['SDL_gfx'].pieColor
    pieColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Uint32]
    pieColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 150
if hasattr(_libs['SDL_gfx'], 'pieRGBA'):
    pieRGBA = _libs['SDL_gfx'].pieRGBA
    pieRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    pieRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 155
if hasattr(_libs['SDL_gfx'], 'filledPieColor'):
    filledPieColor = _libs['SDL_gfx'].filledPieColor
    filledPieColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Uint32]
    filledPieColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 157
if hasattr(_libs['SDL_gfx'], 'filledPieRGBA'):
    filledPieRGBA = _libs['SDL_gfx'].filledPieRGBA
    filledPieRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    filledPieRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 162
if hasattr(_libs['SDL_gfx'], 'trigonColor'):
    trigonColor = _libs['SDL_gfx'].trigonColor
    trigonColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Sint16, Uint32]
    trigonColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 163
if hasattr(_libs['SDL_gfx'], 'trigonRGBA'):
    trigonRGBA = _libs['SDL_gfx'].trigonRGBA
    trigonRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    trigonRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 168
if hasattr(_libs['SDL_gfx'], 'aatrigonColor'):
    aatrigonColor = _libs['SDL_gfx'].aatrigonColor
    aatrigonColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Sint16, Uint32]
    aatrigonColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 169
if hasattr(_libs['SDL_gfx'], 'aatrigonRGBA'):
    aatrigonRGBA = _libs['SDL_gfx'].aatrigonRGBA
    aatrigonRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    aatrigonRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 174
if hasattr(_libs['SDL_gfx'], 'filledTrigonColor'):
    filledTrigonColor = _libs['SDL_gfx'].filledTrigonColor
    filledTrigonColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Sint16, Uint32]
    filledTrigonColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 175
if hasattr(_libs['SDL_gfx'], 'filledTrigonRGBA'):
    filledTrigonRGBA = _libs['SDL_gfx'].filledTrigonRGBA
    filledTrigonRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, Sint16, Sint16, Sint16, Sint16, Uint8, Uint8, Uint8, Uint8]
    filledTrigonRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 180
if hasattr(_libs['SDL_gfx'], 'polygonColor'):
    polygonColor = _libs['SDL_gfx'].polygonColor
    polygonColor.argtypes = [POINTER(SDL_Surface), POINTER(Sint16), POINTER(Sint16), c_int, Uint32]
    polygonColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 181
if hasattr(_libs['SDL_gfx'], 'polygonRGBA'):
    polygonRGBA = _libs['SDL_gfx'].polygonRGBA
    polygonRGBA.argtypes = [POINTER(SDL_Surface), POINTER(Sint16), POINTER(Sint16), c_int, Uint8, Uint8, Uint8, Uint8]
    polygonRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 186
if hasattr(_libs['SDL_gfx'], 'aapolygonColor'):
    aapolygonColor = _libs['SDL_gfx'].aapolygonColor
    aapolygonColor.argtypes = [POINTER(SDL_Surface), POINTER(Sint16), POINTER(Sint16), c_int, Uint32]
    aapolygonColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 187
if hasattr(_libs['SDL_gfx'], 'aapolygonRGBA'):
    aapolygonRGBA = _libs['SDL_gfx'].aapolygonRGBA
    aapolygonRGBA.argtypes = [POINTER(SDL_Surface), POINTER(Sint16), POINTER(Sint16), c_int, Uint8, Uint8, Uint8, Uint8]
    aapolygonRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 192
if hasattr(_libs['SDL_gfx'], 'filledPolygonColor'):
    filledPolygonColor = _libs['SDL_gfx'].filledPolygonColor
    filledPolygonColor.argtypes = [POINTER(SDL_Surface), POINTER(Sint16), POINTER(Sint16), c_int, Uint32]
    filledPolygonColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 193
if hasattr(_libs['SDL_gfx'], 'filledPolygonRGBA'):
    filledPolygonRGBA = _libs['SDL_gfx'].filledPolygonRGBA
    filledPolygonRGBA.argtypes = [POINTER(SDL_Surface), POINTER(Sint16), POINTER(Sint16), c_int, Uint8, Uint8, Uint8, Uint8]
    filledPolygonRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 195
if hasattr(_libs['SDL_gfx'], 'texturedPolygon'):
    texturedPolygon = _libs['SDL_gfx'].texturedPolygon
    texturedPolygon.argtypes = [POINTER(SDL_Surface), POINTER(Sint16), POINTER(Sint16), c_int, POINTER(SDL_Surface), c_int, c_int]
    texturedPolygon.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 199
if hasattr(_libs['SDL_gfx'], 'filledPolygonColorMT'):
    filledPolygonColorMT = _libs['SDL_gfx'].filledPolygonColorMT
    filledPolygonColorMT.argtypes = [POINTER(SDL_Surface), POINTER(Sint16), POINTER(Sint16), c_int, Uint32, POINTER(POINTER(c_int)), POINTER(c_int)]
    filledPolygonColorMT.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 200
if hasattr(_libs['SDL_gfx'], 'filledPolygonRGBAMT'):
    filledPolygonRGBAMT = _libs['SDL_gfx'].filledPolygonRGBAMT
    filledPolygonRGBAMT.argtypes = [POINTER(SDL_Surface), POINTER(Sint16), POINTER(Sint16), c_int, Uint8, Uint8, Uint8, Uint8, POINTER(POINTER(c_int)), POINTER(c_int)]
    filledPolygonRGBAMT.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 203
if hasattr(_libs['SDL_gfx'], 'texturedPolygonMT'):
    texturedPolygonMT = _libs['SDL_gfx'].texturedPolygonMT
    texturedPolygonMT.argtypes = [POINTER(SDL_Surface), POINTER(Sint16), POINTER(Sint16), c_int, POINTER(SDL_Surface), c_int, c_int, POINTER(POINTER(c_int)), POINTER(c_int)]
    texturedPolygonMT.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 207
if hasattr(_libs['SDL_gfx'], 'bezierColor'):
    bezierColor = _libs['SDL_gfx'].bezierColor
    bezierColor.argtypes = [POINTER(SDL_Surface), POINTER(Sint16), POINTER(Sint16), c_int, c_int, Uint32]
    bezierColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 208
if hasattr(_libs['SDL_gfx'], 'bezierRGBA'):
    bezierRGBA = _libs['SDL_gfx'].bezierRGBA
    bezierRGBA.argtypes = [POINTER(SDL_Surface), POINTER(Sint16), POINTER(Sint16), c_int, c_int, Uint8, Uint8, Uint8, Uint8]
    bezierRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 213
if hasattr(_libs['SDL_gfx'], 'gfxPrimitivesSetFont'):
    gfxPrimitivesSetFont = _libs['SDL_gfx'].gfxPrimitivesSetFont
    gfxPrimitivesSetFont.argtypes = [POINTER(None), Uint32, Uint32]
    gfxPrimitivesSetFont.restype = None

# /usr/include/SDL/SDL_gfxPrimitives.h: 214
if hasattr(_libs['SDL_gfx'], 'gfxPrimitivesSetFontRotation'):
    gfxPrimitivesSetFontRotation = _libs['SDL_gfx'].gfxPrimitivesSetFontRotation
    gfxPrimitivesSetFontRotation.argtypes = [Uint32]
    gfxPrimitivesSetFontRotation.restype = None

# /usr/include/SDL/SDL_gfxPrimitives.h: 215
if hasattr(_libs['SDL_gfx'], 'characterColor'):
    characterColor = _libs['SDL_gfx'].characterColor
    characterColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, c_char, Uint32]
    characterColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 216
if hasattr(_libs['SDL_gfx'], 'characterRGBA'):
    characterRGBA = _libs['SDL_gfx'].characterRGBA
    characterRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, c_char, Uint8, Uint8, Uint8, Uint8]
    characterRGBA.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 217
if hasattr(_libs['SDL_gfx'], 'stringColor'):
    stringColor = _libs['SDL_gfx'].stringColor
    stringColor.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, String, Uint32]
    stringColor.restype = c_int

# /usr/include/SDL/SDL_gfxPrimitives.h: 218
if hasattr(_libs['SDL_gfx'], 'stringRGBA'):
    stringRGBA = _libs['SDL_gfx'].stringRGBA
    stringRGBA.argtypes = [POINTER(SDL_Surface), Sint16, Sint16, String, Uint8, Uint8, Uint8, Uint8]
    stringRGBA.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 39
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterMMXdetect'):
    SDL_imageFilterMMXdetect = _libs['SDL_gfx'].SDL_imageFilterMMXdetect
    SDL_imageFilterMMXdetect.argtypes = []
    SDL_imageFilterMMXdetect.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 42
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterMMXoff'):
    SDL_imageFilterMMXoff = _libs['SDL_gfx'].SDL_imageFilterMMXoff
    SDL_imageFilterMMXoff.argtypes = []
    SDL_imageFilterMMXoff.restype = None

# /usr/include/SDL/SDL_imageFilter.h: 43
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterMMXon'):
    SDL_imageFilterMMXon = _libs['SDL_gfx'].SDL_imageFilterMMXon
    SDL_imageFilterMMXon.argtypes = []
    SDL_imageFilterMMXon.restype = None

# /usr/include/SDL/SDL_imageFilter.h: 52
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterAdd'):
    SDL_imageFilterAdd = _libs['SDL_gfx'].SDL_imageFilterAdd
    SDL_imageFilterAdd.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_uint]
    SDL_imageFilterAdd.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 55
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterMean'):
    SDL_imageFilterMean = _libs['SDL_gfx'].SDL_imageFilterMean
    SDL_imageFilterMean.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_uint]
    SDL_imageFilterMean.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 58
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterSub'):
    SDL_imageFilterSub = _libs['SDL_gfx'].SDL_imageFilterSub
    SDL_imageFilterSub.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_uint]
    SDL_imageFilterSub.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 61
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterAbsDiff'):
    SDL_imageFilterAbsDiff = _libs['SDL_gfx'].SDL_imageFilterAbsDiff
    SDL_imageFilterAbsDiff.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_uint]
    SDL_imageFilterAbsDiff.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 64
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterMult'):
    SDL_imageFilterMult = _libs['SDL_gfx'].SDL_imageFilterMult
    SDL_imageFilterMult.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_uint]
    SDL_imageFilterMult.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 67
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterMultNor'):
    SDL_imageFilterMultNor = _libs['SDL_gfx'].SDL_imageFilterMultNor
    SDL_imageFilterMultNor.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_uint]
    SDL_imageFilterMultNor.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 70
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterMultDivby2'):
    SDL_imageFilterMultDivby2 = _libs['SDL_gfx'].SDL_imageFilterMultDivby2
    SDL_imageFilterMultDivby2.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_uint]
    SDL_imageFilterMultDivby2.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 74
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterMultDivby4'):
    SDL_imageFilterMultDivby4 = _libs['SDL_gfx'].SDL_imageFilterMultDivby4
    SDL_imageFilterMultDivby4.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_uint]
    SDL_imageFilterMultDivby4.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 78
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterBitAnd'):
    SDL_imageFilterBitAnd = _libs['SDL_gfx'].SDL_imageFilterBitAnd
    SDL_imageFilterBitAnd.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_uint]
    SDL_imageFilterBitAnd.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 81
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterBitOr'):
    SDL_imageFilterBitOr = _libs['SDL_gfx'].SDL_imageFilterBitOr
    SDL_imageFilterBitOr.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_uint]
    SDL_imageFilterBitOr.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 84
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterDiv'):
    SDL_imageFilterDiv = _libs['SDL_gfx'].SDL_imageFilterDiv
    SDL_imageFilterDiv.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_uint]
    SDL_imageFilterDiv.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 87
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterBitNegation'):
    SDL_imageFilterBitNegation = _libs['SDL_gfx'].SDL_imageFilterBitNegation
    SDL_imageFilterBitNegation.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint]
    SDL_imageFilterBitNegation.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 90
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterAddByte'):
    SDL_imageFilterAddByte = _libs['SDL_gfx'].SDL_imageFilterAddByte
    SDL_imageFilterAddByte.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_ubyte]
    SDL_imageFilterAddByte.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 93
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterAddUint'):
    SDL_imageFilterAddUint = _libs['SDL_gfx'].SDL_imageFilterAddUint
    SDL_imageFilterAddUint.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_uint]
    SDL_imageFilterAddUint.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 96
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterAddByteToHalf'):
    SDL_imageFilterAddByteToHalf = _libs['SDL_gfx'].SDL_imageFilterAddByteToHalf
    SDL_imageFilterAddByteToHalf.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_ubyte]
    SDL_imageFilterAddByteToHalf.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 100
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterSubByte'):
    SDL_imageFilterSubByte = _libs['SDL_gfx'].SDL_imageFilterSubByte
    SDL_imageFilterSubByte.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_ubyte]
    SDL_imageFilterSubByte.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 103
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterSubUint'):
    SDL_imageFilterSubUint = _libs['SDL_gfx'].SDL_imageFilterSubUint
    SDL_imageFilterSubUint.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_uint]
    SDL_imageFilterSubUint.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 106
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterShiftRight'):
    SDL_imageFilterShiftRight = _libs['SDL_gfx'].SDL_imageFilterShiftRight
    SDL_imageFilterShiftRight.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_ubyte]
    SDL_imageFilterShiftRight.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 109
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterShiftRightUint'):
    SDL_imageFilterShiftRightUint = _libs['SDL_gfx'].SDL_imageFilterShiftRightUint
    SDL_imageFilterShiftRightUint.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_ubyte]
    SDL_imageFilterShiftRightUint.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 112
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterMultByByte'):
    SDL_imageFilterMultByByte = _libs['SDL_gfx'].SDL_imageFilterMultByByte
    SDL_imageFilterMultByByte.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_ubyte]
    SDL_imageFilterMultByByte.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 115
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterShiftRightAndMultByByte'):
    SDL_imageFilterShiftRightAndMultByByte = _libs['SDL_gfx'].SDL_imageFilterShiftRightAndMultByByte
    SDL_imageFilterShiftRightAndMultByByte.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_ubyte, c_ubyte]
    SDL_imageFilterShiftRightAndMultByByte.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 119
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterShiftLeftByte'):
    SDL_imageFilterShiftLeftByte = _libs['SDL_gfx'].SDL_imageFilterShiftLeftByte
    SDL_imageFilterShiftLeftByte.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_ubyte]
    SDL_imageFilterShiftLeftByte.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 123
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterShiftLeftUint'):
    SDL_imageFilterShiftLeftUint = _libs['SDL_gfx'].SDL_imageFilterShiftLeftUint
    SDL_imageFilterShiftLeftUint.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_ubyte]
    SDL_imageFilterShiftLeftUint.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 127
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterShiftLeft'):
    SDL_imageFilterShiftLeft = _libs['SDL_gfx'].SDL_imageFilterShiftLeft
    SDL_imageFilterShiftLeft.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_ubyte]
    SDL_imageFilterShiftLeft.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 130
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterBinarizeUsingThreshold'):
    SDL_imageFilterBinarizeUsingThreshold = _libs['SDL_gfx'].SDL_imageFilterBinarizeUsingThreshold
    SDL_imageFilterBinarizeUsingThreshold.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_ubyte]
    SDL_imageFilterBinarizeUsingThreshold.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 134
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterClipToRange'):
    SDL_imageFilterClipToRange = _libs['SDL_gfx'].SDL_imageFilterClipToRange
    SDL_imageFilterClipToRange.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_ubyte, c_ubyte]
    SDL_imageFilterClipToRange.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 138
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterNormalizeLinear'):
    SDL_imageFilterNormalizeLinear = _libs['SDL_gfx'].SDL_imageFilterNormalizeLinear
    SDL_imageFilterNormalizeLinear.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_int, c_int, c_int, c_int]
    SDL_imageFilterNormalizeLinear.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 144
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterConvolveKernel3x3Divide'):
    SDL_imageFilterConvolveKernel3x3Divide = _libs['SDL_gfx'].SDL_imageFilterConvolveKernel3x3Divide
    SDL_imageFilterConvolveKernel3x3Divide.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, c_int, POINTER(c_short), c_ubyte]
    SDL_imageFilterConvolveKernel3x3Divide.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 148
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterConvolveKernel5x5Divide'):
    SDL_imageFilterConvolveKernel5x5Divide = _libs['SDL_gfx'].SDL_imageFilterConvolveKernel5x5Divide
    SDL_imageFilterConvolveKernel5x5Divide.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, c_int, POINTER(c_short), c_ubyte]
    SDL_imageFilterConvolveKernel5x5Divide.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 152
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterConvolveKernel7x7Divide'):
    SDL_imageFilterConvolveKernel7x7Divide = _libs['SDL_gfx'].SDL_imageFilterConvolveKernel7x7Divide
    SDL_imageFilterConvolveKernel7x7Divide.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, c_int, POINTER(c_short), c_ubyte]
    SDL_imageFilterConvolveKernel7x7Divide.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 156
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterConvolveKernel9x9Divide'):
    SDL_imageFilterConvolveKernel9x9Divide = _libs['SDL_gfx'].SDL_imageFilterConvolveKernel9x9Divide
    SDL_imageFilterConvolveKernel9x9Divide.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, c_int, POINTER(c_short), c_ubyte]
    SDL_imageFilterConvolveKernel9x9Divide.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 160
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterConvolveKernel3x3ShiftRight'):
    SDL_imageFilterConvolveKernel3x3ShiftRight = _libs['SDL_gfx'].SDL_imageFilterConvolveKernel3x3ShiftRight
    SDL_imageFilterConvolveKernel3x3ShiftRight.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, c_int, POINTER(c_short), c_ubyte]
    SDL_imageFilterConvolveKernel3x3ShiftRight.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 165
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterConvolveKernel5x5ShiftRight'):
    SDL_imageFilterConvolveKernel5x5ShiftRight = _libs['SDL_gfx'].SDL_imageFilterConvolveKernel5x5ShiftRight
    SDL_imageFilterConvolveKernel5x5ShiftRight.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, c_int, POINTER(c_short), c_ubyte]
    SDL_imageFilterConvolveKernel5x5ShiftRight.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 170
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterConvolveKernel7x7ShiftRight'):
    SDL_imageFilterConvolveKernel7x7ShiftRight = _libs['SDL_gfx'].SDL_imageFilterConvolveKernel7x7ShiftRight
    SDL_imageFilterConvolveKernel7x7ShiftRight.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, c_int, POINTER(c_short), c_ubyte]
    SDL_imageFilterConvolveKernel7x7ShiftRight.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 175
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterConvolveKernel9x9ShiftRight'):
    SDL_imageFilterConvolveKernel9x9ShiftRight = _libs['SDL_gfx'].SDL_imageFilterConvolveKernel9x9ShiftRight
    SDL_imageFilterConvolveKernel9x9ShiftRight.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, c_int, POINTER(c_short), c_ubyte]
    SDL_imageFilterConvolveKernel9x9ShiftRight.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 180
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterSobelX'):
    SDL_imageFilterSobelX = _libs['SDL_gfx'].SDL_imageFilterSobelX
    SDL_imageFilterSobelX.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, c_int]
    SDL_imageFilterSobelX.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 183
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterSobelXShiftRight'):
    SDL_imageFilterSobelXShiftRight = _libs['SDL_gfx'].SDL_imageFilterSobelXShiftRight
    SDL_imageFilterSobelXShiftRight.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_int, c_int, c_ubyte]
    SDL_imageFilterSobelXShiftRight.restype = c_int

# /usr/include/SDL/SDL_imageFilter.h: 187
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterAlignStack'):
    SDL_imageFilterAlignStack = _libs['SDL_gfx'].SDL_imageFilterAlignStack
    SDL_imageFilterAlignStack.argtypes = []
    SDL_imageFilterAlignStack.restype = None

# /usr/include/SDL/SDL_imageFilter.h: 188
if hasattr(_libs['SDL_gfx'], 'SDL_imageFilterRestoreStack'):
    SDL_imageFilterRestoreStack = _libs['SDL_gfx'].SDL_imageFilterRestoreStack
    SDL_imageFilterRestoreStack.argtypes = []
    SDL_imageFilterRestoreStack.restype = None

# /usr/include/SDL/SDL_image.h: 57
if hasattr(_libs['SDL_image'], 'IMG_Linked_Version'):
    IMG_Linked_Version = _libs['SDL_image'].IMG_Linked_Version
    IMG_Linked_Version.argtypes = []
    IMG_Linked_Version.restype = POINTER(SDL_version)

enum_anon_49 = c_int # /usr/include/SDL/SDL_image.h: 64

IMG_INIT_JPG = 1 # /usr/include/SDL/SDL_image.h: 64

IMG_INIT_PNG = 2 # /usr/include/SDL/SDL_image.h: 64

IMG_INIT_TIF = 4 # /usr/include/SDL/SDL_image.h: 64

IMG_InitFlags = enum_anon_49 # /usr/include/SDL/SDL_image.h: 64

# /usr/include/SDL/SDL_image.h: 70
if hasattr(_libs['SDL_image'], 'IMG_Init'):
    IMG_Init = _libs['SDL_image'].IMG_Init
    IMG_Init.argtypes = [c_int]
    IMG_Init.restype = c_int

# /usr/include/SDL/SDL_image.h: 73
if hasattr(_libs['SDL_image'], 'IMG_Quit'):
    IMG_Quit = _libs['SDL_image'].IMG_Quit
    IMG_Quit.argtypes = []
    IMG_Quit.restype = None

# /usr/include/SDL/SDL_image.h: 83
if hasattr(_libs['SDL_image'], 'IMG_LoadTyped_RW'):
    IMG_LoadTyped_RW = _libs['SDL_image'].IMG_LoadTyped_RW
    IMG_LoadTyped_RW.argtypes = [POINTER(SDL_RWops), c_int, String]
    IMG_LoadTyped_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 85
if hasattr(_libs['SDL_image'], 'IMG_Load'):
    IMG_Load = _libs['SDL_image'].IMG_Load
    IMG_Load.argtypes = [String]
    IMG_Load.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 86
if hasattr(_libs['SDL_image'], 'IMG_Load_RW'):
    IMG_Load_RW = _libs['SDL_image'].IMG_Load_RW
    IMG_Load_RW.argtypes = [POINTER(SDL_RWops), c_int]
    IMG_Load_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 91
if hasattr(_libs['SDL_image'], 'IMG_InvertAlpha'):
    IMG_InvertAlpha = _libs['SDL_image'].IMG_InvertAlpha
    IMG_InvertAlpha.argtypes = [c_int]
    IMG_InvertAlpha.restype = c_int

# /usr/include/SDL/SDL_image.h: 94
if hasattr(_libs['SDL_image'], 'IMG_isICO'):
    IMG_isICO = _libs['SDL_image'].IMG_isICO
    IMG_isICO.argtypes = [POINTER(SDL_RWops)]
    IMG_isICO.restype = c_int

# /usr/include/SDL/SDL_image.h: 95
if hasattr(_libs['SDL_image'], 'IMG_isCUR'):
    IMG_isCUR = _libs['SDL_image'].IMG_isCUR
    IMG_isCUR.argtypes = [POINTER(SDL_RWops)]
    IMG_isCUR.restype = c_int

# /usr/include/SDL/SDL_image.h: 96
if hasattr(_libs['SDL_image'], 'IMG_isBMP'):
    IMG_isBMP = _libs['SDL_image'].IMG_isBMP
    IMG_isBMP.argtypes = [POINTER(SDL_RWops)]
    IMG_isBMP.restype = c_int

# /usr/include/SDL/SDL_image.h: 97
if hasattr(_libs['SDL_image'], 'IMG_isGIF'):
    IMG_isGIF = _libs['SDL_image'].IMG_isGIF
    IMG_isGIF.argtypes = [POINTER(SDL_RWops)]
    IMG_isGIF.restype = c_int

# /usr/include/SDL/SDL_image.h: 98
if hasattr(_libs['SDL_image'], 'IMG_isJPG'):
    IMG_isJPG = _libs['SDL_image'].IMG_isJPG
    IMG_isJPG.argtypes = [POINTER(SDL_RWops)]
    IMG_isJPG.restype = c_int

# /usr/include/SDL/SDL_image.h: 99
if hasattr(_libs['SDL_image'], 'IMG_isLBM'):
    IMG_isLBM = _libs['SDL_image'].IMG_isLBM
    IMG_isLBM.argtypes = [POINTER(SDL_RWops)]
    IMG_isLBM.restype = c_int

# /usr/include/SDL/SDL_image.h: 100
if hasattr(_libs['SDL_image'], 'IMG_isPCX'):
    IMG_isPCX = _libs['SDL_image'].IMG_isPCX
    IMG_isPCX.argtypes = [POINTER(SDL_RWops)]
    IMG_isPCX.restype = c_int

# /usr/include/SDL/SDL_image.h: 101
if hasattr(_libs['SDL_image'], 'IMG_isPNG'):
    IMG_isPNG = _libs['SDL_image'].IMG_isPNG
    IMG_isPNG.argtypes = [POINTER(SDL_RWops)]
    IMG_isPNG.restype = c_int

# /usr/include/SDL/SDL_image.h: 102
if hasattr(_libs['SDL_image'], 'IMG_isPNM'):
    IMG_isPNM = _libs['SDL_image'].IMG_isPNM
    IMG_isPNM.argtypes = [POINTER(SDL_RWops)]
    IMG_isPNM.restype = c_int

# /usr/include/SDL/SDL_image.h: 103
if hasattr(_libs['SDL_image'], 'IMG_isTIF'):
    IMG_isTIF = _libs['SDL_image'].IMG_isTIF
    IMG_isTIF.argtypes = [POINTER(SDL_RWops)]
    IMG_isTIF.restype = c_int

# /usr/include/SDL/SDL_image.h: 104
if hasattr(_libs['SDL_image'], 'IMG_isXCF'):
    IMG_isXCF = _libs['SDL_image'].IMG_isXCF
    IMG_isXCF.argtypes = [POINTER(SDL_RWops)]
    IMG_isXCF.restype = c_int

# /usr/include/SDL/SDL_image.h: 105
if hasattr(_libs['SDL_image'], 'IMG_isXPM'):
    IMG_isXPM = _libs['SDL_image'].IMG_isXPM
    IMG_isXPM.argtypes = [POINTER(SDL_RWops)]
    IMG_isXPM.restype = c_int

# /usr/include/SDL/SDL_image.h: 106
if hasattr(_libs['SDL_image'], 'IMG_isXV'):
    IMG_isXV = _libs['SDL_image'].IMG_isXV
    IMG_isXV.argtypes = [POINTER(SDL_RWops)]
    IMG_isXV.restype = c_int

# /usr/include/SDL/SDL_image.h: 109
if hasattr(_libs['SDL_image'], 'IMG_LoadICO_RW'):
    IMG_LoadICO_RW = _libs['SDL_image'].IMG_LoadICO_RW
    IMG_LoadICO_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadICO_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 110
if hasattr(_libs['SDL_image'], 'IMG_LoadCUR_RW'):
    IMG_LoadCUR_RW = _libs['SDL_image'].IMG_LoadCUR_RW
    IMG_LoadCUR_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadCUR_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 111
if hasattr(_libs['SDL_image'], 'IMG_LoadBMP_RW'):
    IMG_LoadBMP_RW = _libs['SDL_image'].IMG_LoadBMP_RW
    IMG_LoadBMP_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadBMP_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 112
if hasattr(_libs['SDL_image'], 'IMG_LoadGIF_RW'):
    IMG_LoadGIF_RW = _libs['SDL_image'].IMG_LoadGIF_RW
    IMG_LoadGIF_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadGIF_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 113
if hasattr(_libs['SDL_image'], 'IMG_LoadJPG_RW'):
    IMG_LoadJPG_RW = _libs['SDL_image'].IMG_LoadJPG_RW
    IMG_LoadJPG_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadJPG_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 114
if hasattr(_libs['SDL_image'], 'IMG_LoadLBM_RW'):
    IMG_LoadLBM_RW = _libs['SDL_image'].IMG_LoadLBM_RW
    IMG_LoadLBM_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadLBM_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 115
if hasattr(_libs['SDL_image'], 'IMG_LoadPCX_RW'):
    IMG_LoadPCX_RW = _libs['SDL_image'].IMG_LoadPCX_RW
    IMG_LoadPCX_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadPCX_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 116
if hasattr(_libs['SDL_image'], 'IMG_LoadPNG_RW'):
    IMG_LoadPNG_RW = _libs['SDL_image'].IMG_LoadPNG_RW
    IMG_LoadPNG_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadPNG_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 117
if hasattr(_libs['SDL_image'], 'IMG_LoadPNM_RW'):
    IMG_LoadPNM_RW = _libs['SDL_image'].IMG_LoadPNM_RW
    IMG_LoadPNM_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadPNM_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 118
if hasattr(_libs['SDL_image'], 'IMG_LoadTGA_RW'):
    IMG_LoadTGA_RW = _libs['SDL_image'].IMG_LoadTGA_RW
    IMG_LoadTGA_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadTGA_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 119
if hasattr(_libs['SDL_image'], 'IMG_LoadTIF_RW'):
    IMG_LoadTIF_RW = _libs['SDL_image'].IMG_LoadTIF_RW
    IMG_LoadTIF_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadTIF_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 120
if hasattr(_libs['SDL_image'], 'IMG_LoadXCF_RW'):
    IMG_LoadXCF_RW = _libs['SDL_image'].IMG_LoadXCF_RW
    IMG_LoadXCF_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadXCF_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 121
if hasattr(_libs['SDL_image'], 'IMG_LoadXPM_RW'):
    IMG_LoadXPM_RW = _libs['SDL_image'].IMG_LoadXPM_RW
    IMG_LoadXPM_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadXPM_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 122
if hasattr(_libs['SDL_image'], 'IMG_LoadXV_RW'):
    IMG_LoadXV_RW = _libs['SDL_image'].IMG_LoadXV_RW
    IMG_LoadXV_RW.argtypes = [POINTER(SDL_RWops)]
    IMG_LoadXV_RW.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_image.h: 124
if hasattr(_libs['SDL_image'], 'IMG_ReadXPMFromArray'):
    IMG_ReadXPMFromArray = _libs['SDL_image'].IMG_ReadXPMFromArray
    IMG_ReadXPMFromArray.argtypes = [POINTER(POINTER(c_char))]
    IMG_ReadXPMFromArray.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_mixer.h: 66
if hasattr(_libs['SDL_mixer'], 'Mix_Linked_Version'):
    Mix_Linked_Version = _libs['SDL_mixer'].Mix_Linked_Version
    Mix_Linked_Version.argtypes = []
    Mix_Linked_Version.restype = POINTER(SDL_version)

enum_anon_50 = c_int # /usr/include/SDL/SDL_mixer.h: 74

MIX_INIT_FLAC = 1 # /usr/include/SDL/SDL_mixer.h: 74

MIX_INIT_MOD = 2 # /usr/include/SDL/SDL_mixer.h: 74

MIX_INIT_MP3 = 4 # /usr/include/SDL/SDL_mixer.h: 74

MIX_INIT_OGG = 8 # /usr/include/SDL/SDL_mixer.h: 74

MIX_InitFlags = enum_anon_50 # /usr/include/SDL/SDL_mixer.h: 74

# /usr/include/SDL/SDL_mixer.h: 80
if hasattr(_libs['SDL_mixer'], 'Mix_Init'):
    Mix_Init = _libs['SDL_mixer'].Mix_Init
    Mix_Init.argtypes = [c_int]
    Mix_Init.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 83
if hasattr(_libs['SDL_mixer'], 'Mix_Quit'):
    Mix_Quit = _libs['SDL_mixer'].Mix_Quit
    Mix_Quit.argtypes = []
    Mix_Quit.restype = None

# /usr/include/SDL/SDL_mixer.h: 107
class struct_Mix_Chunk(Structure):
    pass

struct_Mix_Chunk.__slots__ = [
    'allocated',
    'abuf',
    'alen',
    'volume',
]
struct_Mix_Chunk._fields_ = [
    ('allocated', c_int),
    ('abuf', POINTER(Uint8)),
    ('alen', Uint32),
    ('volume', Uint8),
]

Mix_Chunk = struct_Mix_Chunk # /usr/include/SDL/SDL_mixer.h: 107

enum_anon_51 = c_int # /usr/include/SDL/SDL_mixer.h: 114

MIX_NO_FADING = 0 # /usr/include/SDL/SDL_mixer.h: 114

MIX_FADING_OUT = (MIX_NO_FADING + 1) # /usr/include/SDL/SDL_mixer.h: 114

MIX_FADING_IN = (MIX_FADING_OUT + 1) # /usr/include/SDL/SDL_mixer.h: 114

Mix_Fading = enum_anon_51 # /usr/include/SDL/SDL_mixer.h: 114

enum_anon_52 = c_int # /usr/include/SDL/SDL_mixer.h: 126

MUS_NONE = 0 # /usr/include/SDL/SDL_mixer.h: 126

MUS_CMD = (MUS_NONE + 1) # /usr/include/SDL/SDL_mixer.h: 126

MUS_WAV = (MUS_CMD + 1) # /usr/include/SDL/SDL_mixer.h: 126

MUS_MOD = (MUS_WAV + 1) # /usr/include/SDL/SDL_mixer.h: 126

MUS_MID = (MUS_MOD + 1) # /usr/include/SDL/SDL_mixer.h: 126

MUS_OGG = (MUS_MID + 1) # /usr/include/SDL/SDL_mixer.h: 126

MUS_MP3 = (MUS_OGG + 1) # /usr/include/SDL/SDL_mixer.h: 126

MUS_MP3_MAD = (MUS_MP3 + 1) # /usr/include/SDL/SDL_mixer.h: 126

MUS_FLAC = (MUS_MP3_MAD + 1) # /usr/include/SDL/SDL_mixer.h: 126

Mix_MusicType = enum_anon_52 # /usr/include/SDL/SDL_mixer.h: 126

# /usr/include/SDL/SDL_mixer.h: 129
class struct__Mix_Music(Structure):
    pass

Mix_Music = struct__Mix_Music # /usr/include/SDL/SDL_mixer.h: 129

# /usr/include/SDL/SDL_mixer.h: 132
if hasattr(_libs['SDL_mixer'], 'Mix_OpenAudio'):
    Mix_OpenAudio = _libs['SDL_mixer'].Mix_OpenAudio
    Mix_OpenAudio.argtypes = [c_int, Uint16, c_int, c_int]
    Mix_OpenAudio.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 140
if hasattr(_libs['SDL_mixer'], 'Mix_AllocateChannels'):
    Mix_AllocateChannels = _libs['SDL_mixer'].Mix_AllocateChannels
    Mix_AllocateChannels.argtypes = [c_int]
    Mix_AllocateChannels.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 145
if hasattr(_libs['SDL_mixer'], 'Mix_QuerySpec'):
    Mix_QuerySpec = _libs['SDL_mixer'].Mix_QuerySpec
    Mix_QuerySpec.argtypes = [POINTER(c_int), POINTER(Uint16), POINTER(c_int)]
    Mix_QuerySpec.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 148
if hasattr(_libs['SDL_mixer'], 'Mix_LoadWAV_RW'):
    Mix_LoadWAV_RW = _libs['SDL_mixer'].Mix_LoadWAV_RW
    Mix_LoadWAV_RW.argtypes = [POINTER(SDL_RWops), c_int]
    Mix_LoadWAV_RW.restype = POINTER(Mix_Chunk)

# /usr/include/SDL/SDL_mixer.h: 150
if hasattr(_libs['SDL_mixer'], 'Mix_LoadMUS'):
    Mix_LoadMUS = _libs['SDL_mixer'].Mix_LoadMUS
    Mix_LoadMUS.argtypes = [String]
    Mix_LoadMUS.restype = POINTER(Mix_Music)

# /usr/include/SDL/SDL_mixer.h: 154
if hasattr(_libs['SDL_mixer'], 'Mix_LoadMUS_RW'):
    Mix_LoadMUS_RW = _libs['SDL_mixer'].Mix_LoadMUS_RW
    Mix_LoadMUS_RW.argtypes = [POINTER(SDL_RWops)]
    Mix_LoadMUS_RW.restype = POINTER(Mix_Music)

# /usr/include/SDL/SDL_mixer.h: 157
if hasattr(_libs['SDL_mixer'], 'Mix_QuickLoad_WAV'):
    Mix_QuickLoad_WAV = _libs['SDL_mixer'].Mix_QuickLoad_WAV
    Mix_QuickLoad_WAV.argtypes = [POINTER(Uint8)]
    Mix_QuickLoad_WAV.restype = POINTER(Mix_Chunk)

# /usr/include/SDL/SDL_mixer.h: 160
if hasattr(_libs['SDL_mixer'], 'Mix_QuickLoad_RAW'):
    Mix_QuickLoad_RAW = _libs['SDL_mixer'].Mix_QuickLoad_RAW
    Mix_QuickLoad_RAW.argtypes = [POINTER(Uint8), Uint32]
    Mix_QuickLoad_RAW.restype = POINTER(Mix_Chunk)

# /usr/include/SDL/SDL_mixer.h: 163
if hasattr(_libs['SDL_mixer'], 'Mix_FreeChunk'):
    Mix_FreeChunk = _libs['SDL_mixer'].Mix_FreeChunk
    Mix_FreeChunk.argtypes = [POINTER(Mix_Chunk)]
    Mix_FreeChunk.restype = None

# /usr/include/SDL/SDL_mixer.h: 164
if hasattr(_libs['SDL_mixer'], 'Mix_FreeMusic'):
    Mix_FreeMusic = _libs['SDL_mixer'].Mix_FreeMusic
    Mix_FreeMusic.argtypes = [POINTER(Mix_Music)]
    Mix_FreeMusic.restype = None

# /usr/include/SDL/SDL_mixer.h: 185
if hasattr(_libs['SDL_mixer'], 'Mix_GetNumChunkDecoders'):
    Mix_GetNumChunkDecoders = _libs['SDL_mixer'].Mix_GetNumChunkDecoders
    Mix_GetNumChunkDecoders.argtypes = []
    Mix_GetNumChunkDecoders.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 186
if hasattr(_libs['SDL_mixer'], 'Mix_GetChunkDecoder'):
    Mix_GetChunkDecoder = _libs['SDL_mixer'].Mix_GetChunkDecoder
    Mix_GetChunkDecoder.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        Mix_GetChunkDecoder.restype = ReturnString
    else:
        Mix_GetChunkDecoder.restype = String
        Mix_GetChunkDecoder.errcheck = ReturnString

# /usr/include/SDL/SDL_mixer.h: 187
if hasattr(_libs['SDL_mixer'], 'Mix_GetNumMusicDecoders'):
    Mix_GetNumMusicDecoders = _libs['SDL_mixer'].Mix_GetNumMusicDecoders
    Mix_GetNumMusicDecoders.argtypes = []
    Mix_GetNumMusicDecoders.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 188
if hasattr(_libs['SDL_mixer'], 'Mix_GetMusicDecoder'):
    Mix_GetMusicDecoder = _libs['SDL_mixer'].Mix_GetMusicDecoder
    Mix_GetMusicDecoder.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        Mix_GetMusicDecoder.restype = ReturnString
    else:
        Mix_GetMusicDecoder.restype = String
        Mix_GetMusicDecoder.errcheck = ReturnString

# /usr/include/SDL/SDL_mixer.h: 193
if hasattr(_libs['SDL_mixer'], 'Mix_GetMusicType'):
    Mix_GetMusicType = _libs['SDL_mixer'].Mix_GetMusicType
    Mix_GetMusicType.argtypes = [POINTER(Mix_Music)]
    Mix_GetMusicType.restype = Mix_MusicType

# /usr/include/SDL/SDL_mixer.h: 199
if hasattr(_libs['SDL_mixer'], 'Mix_SetPostMix'):
    Mix_SetPostMix = _libs['SDL_mixer'].Mix_SetPostMix
    Mix_SetPostMix.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(Uint8), c_int), POINTER(None)]
    Mix_SetPostMix.restype = None

# /usr/include/SDL/SDL_mixer.h: 205
if hasattr(_libs['SDL_mixer'], 'Mix_HookMusic'):
    Mix_HookMusic = _libs['SDL_mixer'].Mix_HookMusic
    Mix_HookMusic.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(Uint8), c_int), POINTER(None)]
    Mix_HookMusic.restype = None

# /usr/include/SDL/SDL_mixer.h: 211
if hasattr(_libs['SDL_mixer'], 'Mix_HookMusicFinished'):
    Mix_HookMusicFinished = _libs['SDL_mixer'].Mix_HookMusicFinished
    Mix_HookMusicFinished.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    Mix_HookMusicFinished.restype = None

# /usr/include/SDL/SDL_mixer.h: 214
if hasattr(_libs['SDL_mixer'], 'Mix_GetMusicHookData'):
    Mix_GetMusicHookData = _libs['SDL_mixer'].Mix_GetMusicHookData
    Mix_GetMusicHookData.argtypes = []
    Mix_GetMusicHookData.restype = POINTER(None)

# /usr/include/SDL/SDL_mixer.h: 224
if hasattr(_libs['SDL_mixer'], 'Mix_ChannelFinished'):
    Mix_ChannelFinished = _libs['SDL_mixer'].Mix_ChannelFinished
    Mix_ChannelFinished.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int)]
    Mix_ChannelFinished.restype = None

Mix_EffectFunc_t = CFUNCTYPE(UNCHECKED(None), c_int, POINTER(None), c_int, POINTER(None)) # /usr/include/SDL/SDL_mixer.h: 248

Mix_EffectDone_t = CFUNCTYPE(UNCHECKED(None), c_int, POINTER(None)) # /usr/include/SDL/SDL_mixer.h: 259

# /usr/include/SDL/SDL_mixer.h: 308
if hasattr(_libs['SDL_mixer'], 'Mix_RegisterEffect'):
    Mix_RegisterEffect = _libs['SDL_mixer'].Mix_RegisterEffect
    Mix_RegisterEffect.argtypes = [c_int, Mix_EffectFunc_t, Mix_EffectDone_t, POINTER(None)]
    Mix_RegisterEffect.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 320
if hasattr(_libs['SDL_mixer'], 'Mix_UnregisterEffect'):
    Mix_UnregisterEffect = _libs['SDL_mixer'].Mix_UnregisterEffect
    Mix_UnregisterEffect.argtypes = [c_int, Mix_EffectFunc_t]
    Mix_UnregisterEffect.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 334
if hasattr(_libs['SDL_mixer'], 'Mix_UnregisterAllEffects'):
    Mix_UnregisterAllEffects = _libs['SDL_mixer'].Mix_UnregisterAllEffects
    Mix_UnregisterAllEffects.argtypes = [c_int]
    Mix_UnregisterAllEffects.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 374
if hasattr(_libs['SDL_mixer'], 'Mix_SetPanning'):
    Mix_SetPanning = _libs['SDL_mixer'].Mix_SetPanning
    Mix_SetPanning.argtypes = [c_int, Uint8, Uint8]
    Mix_SetPanning.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 414
if hasattr(_libs['SDL_mixer'], 'Mix_SetPosition'):
    Mix_SetPosition = _libs['SDL_mixer'].Mix_SetPosition
    Mix_SetPosition.argtypes = [c_int, Sint16, Uint8]
    Mix_SetPosition.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 444
if hasattr(_libs['SDL_mixer'], 'Mix_SetDistance'):
    Mix_SetDistance = _libs['SDL_mixer'].Mix_SetDistance
    Mix_SetDistance.argtypes = [c_int, Uint8]
    Mix_SetDistance.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 491
if hasattr(_libs['SDL_mixer'], 'Mix_SetReverseStereo'):
    Mix_SetReverseStereo = _libs['SDL_mixer'].Mix_SetReverseStereo
    Mix_SetReverseStereo.argtypes = [c_int, c_int]
    Mix_SetReverseStereo.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 500
if hasattr(_libs['SDL_mixer'], 'Mix_ReserveChannels'):
    Mix_ReserveChannels = _libs['SDL_mixer'].Mix_ReserveChannels
    Mix_ReserveChannels.argtypes = [c_int]
    Mix_ReserveChannels.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 510
if hasattr(_libs['SDL_mixer'], 'Mix_GroupChannel'):
    Mix_GroupChannel = _libs['SDL_mixer'].Mix_GroupChannel
    Mix_GroupChannel.argtypes = [c_int, c_int]
    Mix_GroupChannel.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 512
if hasattr(_libs['SDL_mixer'], 'Mix_GroupChannels'):
    Mix_GroupChannels = _libs['SDL_mixer'].Mix_GroupChannels
    Mix_GroupChannels.argtypes = [c_int, c_int, c_int]
    Mix_GroupChannels.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 516
if hasattr(_libs['SDL_mixer'], 'Mix_GroupAvailable'):
    Mix_GroupAvailable = _libs['SDL_mixer'].Mix_GroupAvailable
    Mix_GroupAvailable.argtypes = [c_int]
    Mix_GroupAvailable.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 520
if hasattr(_libs['SDL_mixer'], 'Mix_GroupCount'):
    Mix_GroupCount = _libs['SDL_mixer'].Mix_GroupCount
    Mix_GroupCount.argtypes = [c_int]
    Mix_GroupCount.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 522
if hasattr(_libs['SDL_mixer'], 'Mix_GroupOldest'):
    Mix_GroupOldest = _libs['SDL_mixer'].Mix_GroupOldest
    Mix_GroupOldest.argtypes = [c_int]
    Mix_GroupOldest.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 524
if hasattr(_libs['SDL_mixer'], 'Mix_GroupNewer'):
    Mix_GroupNewer = _libs['SDL_mixer'].Mix_GroupNewer
    Mix_GroupNewer.argtypes = [c_int]
    Mix_GroupNewer.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 534
if hasattr(_libs['SDL_mixer'], 'Mix_PlayChannelTimed'):
    Mix_PlayChannelTimed = _libs['SDL_mixer'].Mix_PlayChannelTimed
    Mix_PlayChannelTimed.argtypes = [c_int, POINTER(Mix_Chunk), c_int, c_int]
    Mix_PlayChannelTimed.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 535
if hasattr(_libs['SDL_mixer'], 'Mix_PlayMusic'):
    Mix_PlayMusic = _libs['SDL_mixer'].Mix_PlayMusic
    Mix_PlayMusic.argtypes = [POINTER(Mix_Music), c_int]
    Mix_PlayMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 538
if hasattr(_libs['SDL_mixer'], 'Mix_FadeInMusic'):
    Mix_FadeInMusic = _libs['SDL_mixer'].Mix_FadeInMusic
    Mix_FadeInMusic.argtypes = [POINTER(Mix_Music), c_int, c_int]
    Mix_FadeInMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 539
if hasattr(_libs['SDL_mixer'], 'Mix_FadeInMusicPos'):
    Mix_FadeInMusicPos = _libs['SDL_mixer'].Mix_FadeInMusicPos
    Mix_FadeInMusicPos.argtypes = [POINTER(Mix_Music), c_int, c_int, c_double]
    Mix_FadeInMusicPos.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 541
if hasattr(_libs['SDL_mixer'], 'Mix_FadeInChannelTimed'):
    Mix_FadeInChannelTimed = _libs['SDL_mixer'].Mix_FadeInChannelTimed
    Mix_FadeInChannelTimed.argtypes = [c_int, POINTER(Mix_Chunk), c_int, c_int, c_int]
    Mix_FadeInChannelTimed.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 548
if hasattr(_libs['SDL_mixer'], 'Mix_Volume'):
    Mix_Volume = _libs['SDL_mixer'].Mix_Volume
    Mix_Volume.argtypes = [c_int, c_int]
    Mix_Volume.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 549
if hasattr(_libs['SDL_mixer'], 'Mix_VolumeChunk'):
    Mix_VolumeChunk = _libs['SDL_mixer'].Mix_VolumeChunk
    Mix_VolumeChunk.argtypes = [POINTER(Mix_Chunk), c_int]
    Mix_VolumeChunk.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 550
if hasattr(_libs['SDL_mixer'], 'Mix_VolumeMusic'):
    Mix_VolumeMusic = _libs['SDL_mixer'].Mix_VolumeMusic
    Mix_VolumeMusic.argtypes = [c_int]
    Mix_VolumeMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 553
if hasattr(_libs['SDL_mixer'], 'Mix_HaltChannel'):
    Mix_HaltChannel = _libs['SDL_mixer'].Mix_HaltChannel
    Mix_HaltChannel.argtypes = [c_int]
    Mix_HaltChannel.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 554
if hasattr(_libs['SDL_mixer'], 'Mix_HaltGroup'):
    Mix_HaltGroup = _libs['SDL_mixer'].Mix_HaltGroup
    Mix_HaltGroup.argtypes = [c_int]
    Mix_HaltGroup.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 555
if hasattr(_libs['SDL_mixer'], 'Mix_HaltMusic'):
    Mix_HaltMusic = _libs['SDL_mixer'].Mix_HaltMusic
    Mix_HaltMusic.argtypes = []
    Mix_HaltMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 561
if hasattr(_libs['SDL_mixer'], 'Mix_ExpireChannel'):
    Mix_ExpireChannel = _libs['SDL_mixer'].Mix_ExpireChannel
    Mix_ExpireChannel.argtypes = [c_int, c_int]
    Mix_ExpireChannel.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 567
if hasattr(_libs['SDL_mixer'], 'Mix_FadeOutChannel'):
    Mix_FadeOutChannel = _libs['SDL_mixer'].Mix_FadeOutChannel
    Mix_FadeOutChannel.argtypes = [c_int, c_int]
    Mix_FadeOutChannel.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 568
if hasattr(_libs['SDL_mixer'], 'Mix_FadeOutGroup'):
    Mix_FadeOutGroup = _libs['SDL_mixer'].Mix_FadeOutGroup
    Mix_FadeOutGroup.argtypes = [c_int, c_int]
    Mix_FadeOutGroup.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 569
if hasattr(_libs['SDL_mixer'], 'Mix_FadeOutMusic'):
    Mix_FadeOutMusic = _libs['SDL_mixer'].Mix_FadeOutMusic
    Mix_FadeOutMusic.argtypes = [c_int]
    Mix_FadeOutMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 572
if hasattr(_libs['SDL_mixer'], 'Mix_FadingMusic'):
    Mix_FadingMusic = _libs['SDL_mixer'].Mix_FadingMusic
    Mix_FadingMusic.argtypes = []
    Mix_FadingMusic.restype = Mix_Fading

# /usr/include/SDL/SDL_mixer.h: 573
if hasattr(_libs['SDL_mixer'], 'Mix_FadingChannel'):
    Mix_FadingChannel = _libs['SDL_mixer'].Mix_FadingChannel
    Mix_FadingChannel.argtypes = [c_int]
    Mix_FadingChannel.restype = Mix_Fading

# /usr/include/SDL/SDL_mixer.h: 576
if hasattr(_libs['SDL_mixer'], 'Mix_Pause'):
    Mix_Pause = _libs['SDL_mixer'].Mix_Pause
    Mix_Pause.argtypes = [c_int]
    Mix_Pause.restype = None

# /usr/include/SDL/SDL_mixer.h: 577
if hasattr(_libs['SDL_mixer'], 'Mix_Resume'):
    Mix_Resume = _libs['SDL_mixer'].Mix_Resume
    Mix_Resume.argtypes = [c_int]
    Mix_Resume.restype = None

# /usr/include/SDL/SDL_mixer.h: 578
if hasattr(_libs['SDL_mixer'], 'Mix_Paused'):
    Mix_Paused = _libs['SDL_mixer'].Mix_Paused
    Mix_Paused.argtypes = [c_int]
    Mix_Paused.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 581
if hasattr(_libs['SDL_mixer'], 'Mix_PauseMusic'):
    Mix_PauseMusic = _libs['SDL_mixer'].Mix_PauseMusic
    Mix_PauseMusic.argtypes = []
    Mix_PauseMusic.restype = None

# /usr/include/SDL/SDL_mixer.h: 582
if hasattr(_libs['SDL_mixer'], 'Mix_ResumeMusic'):
    Mix_ResumeMusic = _libs['SDL_mixer'].Mix_ResumeMusic
    Mix_ResumeMusic.argtypes = []
    Mix_ResumeMusic.restype = None

# /usr/include/SDL/SDL_mixer.h: 583
if hasattr(_libs['SDL_mixer'], 'Mix_RewindMusic'):
    Mix_RewindMusic = _libs['SDL_mixer'].Mix_RewindMusic
    Mix_RewindMusic.argtypes = []
    Mix_RewindMusic.restype = None

# /usr/include/SDL/SDL_mixer.h: 584
if hasattr(_libs['SDL_mixer'], 'Mix_PausedMusic'):
    Mix_PausedMusic = _libs['SDL_mixer'].Mix_PausedMusic
    Mix_PausedMusic.argtypes = []
    Mix_PausedMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 592
if hasattr(_libs['SDL_mixer'], 'Mix_SetMusicPosition'):
    Mix_SetMusicPosition = _libs['SDL_mixer'].Mix_SetMusicPosition
    Mix_SetMusicPosition.argtypes = [c_double]
    Mix_SetMusicPosition.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 597
if hasattr(_libs['SDL_mixer'], 'Mix_Playing'):
    Mix_Playing = _libs['SDL_mixer'].Mix_Playing
    Mix_Playing.argtypes = [c_int]
    Mix_Playing.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 598
if hasattr(_libs['SDL_mixer'], 'Mix_PlayingMusic'):
    Mix_PlayingMusic = _libs['SDL_mixer'].Mix_PlayingMusic
    Mix_PlayingMusic.argtypes = []
    Mix_PlayingMusic.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 601
if hasattr(_libs['SDL_mixer'], 'Mix_SetMusicCMD'):
    Mix_SetMusicCMD = _libs['SDL_mixer'].Mix_SetMusicCMD
    Mix_SetMusicCMD.argtypes = [String]
    Mix_SetMusicCMD.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 604
if hasattr(_libs['SDL_mixer'], 'Mix_SetSynchroValue'):
    Mix_SetSynchroValue = _libs['SDL_mixer'].Mix_SetSynchroValue
    Mix_SetSynchroValue.argtypes = [c_int]
    Mix_SetSynchroValue.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 605
if hasattr(_libs['SDL_mixer'], 'Mix_GetSynchroValue'):
    Mix_GetSynchroValue = _libs['SDL_mixer'].Mix_GetSynchroValue
    Mix_GetSynchroValue.argtypes = []
    Mix_GetSynchroValue.restype = c_int

# /usr/include/SDL/SDL_mixer.h: 610
if hasattr(_libs['SDL_mixer'], 'Mix_GetChunk'):
    Mix_GetChunk = _libs['SDL_mixer'].Mix_GetChunk
    Mix_GetChunk.argtypes = [c_int]
    Mix_GetChunk.restype = POINTER(Mix_Chunk)

# /usr/include/SDL/SDL_mixer.h: 613
if hasattr(_libs['SDL_mixer'], 'Mix_CloseAudio'):
    Mix_CloseAudio = _libs['SDL_mixer'].Mix_CloseAudio
    Mix_CloseAudio.argtypes = []
    Mix_CloseAudio.restype = None

# /usr/include/SDL/SDL_net.h: 60
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_Linked_Version'):
        continue
    SDLNet_Linked_Version = _lib.SDLNet_Linked_Version
    SDLNet_Linked_Version.argtypes = []
    SDLNet_Linked_Version.restype = POINTER(SDL_version)
    break

# /usr/include/SDL/SDL_net.h: 66
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_Init'):
        continue
    SDLNet_Init = _lib.SDLNet_Init
    SDLNet_Init.argtypes = []
    SDLNet_Init.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 67
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_Quit'):
        continue
    SDLNet_Quit = _lib.SDLNet_Quit
    SDLNet_Quit.argtypes = []
    SDLNet_Quit.restype = None
    break

# /usr/include/SDL/SDL_net.h: 76
class struct_anon_53(Structure):
    pass

struct_anon_53.__slots__ = [
    'host',
    'port',
]
struct_anon_53._fields_ = [
    ('host', Uint32),
    ('port', Uint16),
]

IPaddress = struct_anon_53 # /usr/include/SDL/SDL_net.h: 76

# /usr/include/SDL/SDL_net.h: 93
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_ResolveHost'):
        continue
    SDLNet_ResolveHost = _lib.SDLNet_ResolveHost
    SDLNet_ResolveHost.argtypes = [POINTER(IPaddress), String, Uint16]
    SDLNet_ResolveHost.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 100
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_ResolveIP'):
        continue
    SDLNet_ResolveIP = _lib.SDLNet_ResolveIP
    SDLNet_ResolveIP.argtypes = [POINTER(IPaddress)]
    if sizeof(c_int) == sizeof(c_void_p):
        SDLNet_ResolveIP.restype = ReturnString
    else:
        SDLNet_ResolveIP.restype = String
        SDLNet_ResolveIP.errcheck = ReturnString
    break

# /usr/include/SDL/SDL_net.h: 107
class struct__TCPsocket(Structure):
    pass

TCPsocket = POINTER(struct__TCPsocket) # /usr/include/SDL/SDL_net.h: 107

# /usr/include/SDL/SDL_net.h: 117
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_TCP_Open'):
        continue
    SDLNet_TCP_Open = _lib.SDLNet_TCP_Open
    SDLNet_TCP_Open.argtypes = [POINTER(IPaddress)]
    SDLNet_TCP_Open.restype = TCPsocket
    break

# /usr/include/SDL/SDL_net.h: 122
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_TCP_Accept'):
        continue
    SDLNet_TCP_Accept = _lib.SDLNet_TCP_Accept
    SDLNet_TCP_Accept.argtypes = [TCPsocket]
    SDLNet_TCP_Accept.restype = TCPsocket
    break

# /usr/include/SDL/SDL_net.h: 127
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_TCP_GetPeerAddress'):
        continue
    SDLNet_TCP_GetPeerAddress = _lib.SDLNet_TCP_GetPeerAddress
    SDLNet_TCP_GetPeerAddress.argtypes = [TCPsocket]
    SDLNet_TCP_GetPeerAddress.restype = POINTER(IPaddress)
    break

# /usr/include/SDL/SDL_net.h: 134
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_TCP_Send'):
        continue
    SDLNet_TCP_Send = _lib.SDLNet_TCP_Send
    SDLNet_TCP_Send.argtypes = [TCPsocket, POINTER(None), c_int]
    SDLNet_TCP_Send.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 143
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_TCP_Recv'):
        continue
    SDLNet_TCP_Recv = _lib.SDLNet_TCP_Recv
    SDLNet_TCP_Recv.argtypes = [TCPsocket, POINTER(None), c_int]
    SDLNet_TCP_Recv.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 146
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_TCP_Close'):
        continue
    SDLNet_TCP_Close = _lib.SDLNet_TCP_Close
    SDLNet_TCP_Close.argtypes = [TCPsocket]
    SDLNet_TCP_Close.restype = None
    break

# /usr/include/SDL/SDL_net.h: 158
class struct__UDPsocket(Structure):
    pass

UDPsocket = POINTER(struct__UDPsocket) # /usr/include/SDL/SDL_net.h: 158

# /usr/include/SDL/SDL_net.h: 166
class struct_anon_54(Structure):
    pass

struct_anon_54.__slots__ = [
    'channel',
    'data',
    'len',
    'maxlen',
    'status',
    'address',
]
struct_anon_54._fields_ = [
    ('channel', c_int),
    ('data', POINTER(Uint8)),
    ('len', c_int),
    ('maxlen', c_int),
    ('status', c_int),
    ('address', IPaddress),
]

UDPpacket = struct_anon_54 # /usr/include/SDL/SDL_net.h: 166

# /usr/include/SDL/SDL_net.h: 171
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_AllocPacket'):
        continue
    SDLNet_AllocPacket = _lib.SDLNet_AllocPacket
    SDLNet_AllocPacket.argtypes = [c_int]
    SDLNet_AllocPacket.restype = POINTER(UDPpacket)
    break

# /usr/include/SDL/SDL_net.h: 172
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_ResizePacket'):
        continue
    SDLNet_ResizePacket = _lib.SDLNet_ResizePacket
    SDLNet_ResizePacket.argtypes = [POINTER(UDPpacket), c_int]
    SDLNet_ResizePacket.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 173
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_FreePacket'):
        continue
    SDLNet_FreePacket = _lib.SDLNet_FreePacket
    SDLNet_FreePacket.argtypes = [POINTER(UDPpacket)]
    SDLNet_FreePacket.restype = None
    break

# /usr/include/SDL/SDL_net.h: 180
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_AllocPacketV'):
        continue
    SDLNet_AllocPacketV = _lib.SDLNet_AllocPacketV
    SDLNet_AllocPacketV.argtypes = [c_int, c_int]
    SDLNet_AllocPacketV.restype = POINTER(POINTER(UDPpacket))
    break

# /usr/include/SDL/SDL_net.h: 181
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_FreePacketV'):
        continue
    SDLNet_FreePacketV = _lib.SDLNet_FreePacketV
    SDLNet_FreePacketV.argtypes = [POINTER(POINTER(UDPpacket))]
    SDLNet_FreePacketV.restype = None
    break

# /usr/include/SDL/SDL_net.h: 190
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_UDP_Open'):
        continue
    SDLNet_UDP_Open = _lib.SDLNet_UDP_Open
    SDLNet_UDP_Open.argtypes = [Uint16]
    SDLNet_UDP_Open.restype = UDPsocket
    break

# /usr/include/SDL/SDL_net.h: 201
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_UDP_Bind'):
        continue
    SDLNet_UDP_Bind = _lib.SDLNet_UDP_Bind
    SDLNet_UDP_Bind.argtypes = [UDPsocket, c_int, POINTER(IPaddress)]
    SDLNet_UDP_Bind.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 204
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_UDP_Unbind'):
        continue
    SDLNet_UDP_Unbind = _lib.SDLNet_UDP_Unbind
    SDLNet_UDP_Unbind.argtypes = [UDPsocket, c_int]
    SDLNet_UDP_Unbind.restype = None
    break

# /usr/include/SDL/SDL_net.h: 212
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_UDP_GetPeerAddress'):
        continue
    SDLNet_UDP_GetPeerAddress = _lib.SDLNet_UDP_GetPeerAddress
    SDLNet_UDP_GetPeerAddress.argtypes = [UDPsocket, c_int]
    SDLNet_UDP_GetPeerAddress.restype = POINTER(IPaddress)
    break

# /usr/include/SDL/SDL_net.h: 221
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_UDP_SendV'):
        continue
    SDLNet_UDP_SendV = _lib.SDLNet_UDP_SendV
    SDLNet_UDP_SendV.argtypes = [UDPsocket, POINTER(POINTER(UDPpacket)), c_int]
    SDLNet_UDP_SendV.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 235
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_UDP_Send'):
        continue
    SDLNet_UDP_Send = _lib.SDLNet_UDP_Send
    SDLNet_UDP_Send.argtypes = [UDPsocket, c_int, POINTER(UDPpacket)]
    SDLNet_UDP_Send.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 247
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_UDP_RecvV'):
        continue
    SDLNet_UDP_RecvV = _lib.SDLNet_UDP_RecvV
    SDLNet_UDP_RecvV.argtypes = [UDPsocket, POINTER(POINTER(UDPpacket))]
    SDLNet_UDP_RecvV.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 259
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_UDP_Recv'):
        continue
    SDLNet_UDP_Recv = _lib.SDLNet_UDP_Recv
    SDLNet_UDP_Recv.argtypes = [UDPsocket, POINTER(UDPpacket)]
    SDLNet_UDP_Recv.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 262
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_UDP_Close'):
        continue
    SDLNet_UDP_Close = _lib.SDLNet_UDP_Close
    SDLNet_UDP_Close.argtypes = [UDPsocket]
    SDLNet_UDP_Close.restype = None
    break

# /usr/include/SDL/SDL_net.h: 269
class struct__SDLNet_SocketSet(Structure):
    pass

SDLNet_SocketSet = POINTER(struct__SDLNet_SocketSet) # /usr/include/SDL/SDL_net.h: 269

# /usr/include/SDL/SDL_net.h: 272
class struct_anon_55(Structure):
    pass

struct_anon_55.__slots__ = [
    'ready',
]
struct_anon_55._fields_ = [
    ('ready', c_int),
]

SDLNet_GenericSocket = POINTER(struct_anon_55) # /usr/include/SDL/SDL_net.h: 274

# /usr/include/SDL/SDL_net.h: 280
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_AllocSocketSet'):
        continue
    SDLNet_AllocSocketSet = _lib.SDLNet_AllocSocketSet
    SDLNet_AllocSocketSet.argtypes = [c_int]
    SDLNet_AllocSocketSet.restype = SDLNet_SocketSet
    break

# /usr/include/SDL/SDL_net.h: 287
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_AddSocket'):
        continue
    SDLNet_AddSocket = _lib.SDLNet_AddSocket
    SDLNet_AddSocket.argtypes = [SDLNet_SocketSet, SDLNet_GenericSocket]
    SDLNet_AddSocket.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 294
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_DelSocket'):
        continue
    SDLNet_DelSocket = _lib.SDLNet_DelSocket
    SDLNet_DelSocket.argtypes = [SDLNet_SocketSet, SDLNet_GenericSocket]
    SDLNet_DelSocket.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 303
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_CheckSockets'):
        continue
    SDLNet_CheckSockets = _lib.SDLNet_CheckSockets
    SDLNet_CheckSockets.argtypes = [SDLNet_SocketSet, Uint32]
    SDLNet_CheckSockets.restype = c_int
    break

# /usr/include/SDL/SDL_net.h: 313
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_FreeSocketSet'):
        continue
    SDLNet_FreeSocketSet = _lib.SDLNet_FreeSocketSet
    SDLNet_FreeSocketSet.argtypes = [SDLNet_SocketSet]
    SDLNet_FreeSocketSet.restype = None
    break

# /usr/include/SDL/SDL_net.h: 321
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_Write16'):
        continue
    SDLNet_Write16 = _lib.SDLNet_Write16
    SDLNet_Write16.argtypes = [Uint16, POINTER(None)]
    SDLNet_Write16.restype = None
    break

# /usr/include/SDL/SDL_net.h: 322
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_Write32'):
        continue
    SDLNet_Write32 = _lib.SDLNet_Write32
    SDLNet_Write32.argtypes = [Uint32, POINTER(None)]
    SDLNet_Write32.restype = None
    break

# /usr/include/SDL/SDL_net.h: 325
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_Read16'):
        continue
    SDLNet_Read16 = _lib.SDLNet_Read16
    SDLNet_Read16.argtypes = [POINTER(None)]
    SDLNet_Read16.restype = Uint16
    break

# /usr/include/SDL/SDL_net.h: 326
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SDLNet_Read32'):
        continue
    SDLNet_Read32 = _lib.SDLNet_Read32
    SDLNet_Read32.argtypes = [POINTER(None)]
    SDLNet_Read32.restype = Uint32
    break

GLenum = c_uint # /usr/include/GL/gl.h: 155

GLboolean = c_ubyte # /usr/include/GL/gl.h: 156

GLbitfield = c_uint # /usr/include/GL/gl.h: 157

GLvoid = None # /usr/include/GL/gl.h: 158

GLbyte = c_char # /usr/include/GL/gl.h: 159

GLshort = c_short # /usr/include/GL/gl.h: 160

GLint = c_int # /usr/include/GL/gl.h: 161

GLubyte = c_ubyte # /usr/include/GL/gl.h: 162

GLushort = c_ushort # /usr/include/GL/gl.h: 163

GLuint = c_uint # /usr/include/GL/gl.h: 164

GLsizei = c_int # /usr/include/GL/gl.h: 165

GLfloat = c_float # /usr/include/GL/gl.h: 166

GLclampf = c_float # /usr/include/GL/gl.h: 167

GLdouble = c_double # /usr/include/GL/gl.h: 168

GLclampd = c_double # /usr/include/GL/gl.h: 169

GLchar = c_char # /usr/include/SDL/SDL_opengl.h: 3106

GLintptr = c_ptrdiff_t # /usr/include/SDL/SDL_opengl.h: 3111

GLsizeiptr = c_ptrdiff_t # /usr/include/SDL/SDL_opengl.h: 3112

GLintptrARB = c_ptrdiff_t # /usr/include/SDL/SDL_opengl.h: 3117

GLsizeiptrARB = c_ptrdiff_t # /usr/include/SDL/SDL_opengl.h: 3118

GLcharARB = c_char # /usr/include/SDL/SDL_opengl.h: 3123

GLhandleARB = c_uint # /usr/include/SDL/SDL_opengl.h: 3124

GLhalfARB = c_ushort # /usr/include/SDL/SDL_opengl.h: 3129

GLhalfNV = c_ushort # /usr/include/SDL/SDL_opengl.h: 3133

PFNGLBLENDFUNCSEPARATEPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 3365

PFNGLFOGCOORDFPROC = CFUNCTYPE(UNCHECKED(None), GLfloat) # /usr/include/SDL/SDL_opengl.h: 3366

PFNGLFOGCOORDFVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3367

PFNGLFOGCOORDDPROC = CFUNCTYPE(UNCHECKED(None), GLdouble) # /usr/include/SDL/SDL_opengl.h: 3368

PFNGLFOGCOORDDVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3369

PFNGLFOGCOORDPOINTERPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3370

PFNGLMULTIDRAWARRAYSPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint), POINTER(GLsizei), GLsizei) # /usr/include/SDL/SDL_opengl.h: 3371

PFNGLMULTIDRAWELEMENTSPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLsizei), GLenum, POINTER(POINTER(GLvoid)), GLsizei) # /usr/include/SDL/SDL_opengl.h: 3372

PFNGLPOINTPARAMETERFPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3373

PFNGLPOINTPARAMETERFVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3374

PFNGLPOINTPARAMETERIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 3375

PFNGLPOINTPARAMETERIVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3376

PFNGLSECONDARYCOLOR3BPROC = CFUNCTYPE(UNCHECKED(None), GLbyte, GLbyte, GLbyte) # /usr/include/SDL/SDL_opengl.h: 3377

PFNGLSECONDARYCOLOR3BVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLbyte)) # /usr/include/SDL/SDL_opengl.h: 3378

PFNGLSECONDARYCOLOR3DPROC = CFUNCTYPE(UNCHECKED(None), GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3379

PFNGLSECONDARYCOLOR3DVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3380

PFNGLSECONDARYCOLOR3FPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3381

PFNGLSECONDARYCOLOR3FVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3382

PFNGLSECONDARYCOLOR3IPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 3383

PFNGLSECONDARYCOLOR3IVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3384

PFNGLSECONDARYCOLOR3SPROC = CFUNCTYPE(UNCHECKED(None), GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 3385

PFNGLSECONDARYCOLOR3SVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3386

PFNGLSECONDARYCOLOR3UBPROC = CFUNCTYPE(UNCHECKED(None), GLubyte, GLubyte, GLubyte) # /usr/include/SDL/SDL_opengl.h: 3387

PFNGLSECONDARYCOLOR3UBVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 3388

PFNGLSECONDARYCOLOR3UIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 3389

PFNGLSECONDARYCOLOR3UIVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3390

PFNGLSECONDARYCOLOR3USPROC = CFUNCTYPE(UNCHECKED(None), GLushort, GLushort, GLushort) # /usr/include/SDL/SDL_opengl.h: 3391

PFNGLSECONDARYCOLOR3USVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLushort)) # /usr/include/SDL/SDL_opengl.h: 3392

PFNGLSECONDARYCOLORPOINTERPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3393

PFNGLWINDOWPOS2DPROC = CFUNCTYPE(UNCHECKED(None), GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3394

PFNGLWINDOWPOS2DVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3395

PFNGLWINDOWPOS2FPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3396

PFNGLWINDOWPOS2FVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3397

PFNGLWINDOWPOS2IPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 3398

PFNGLWINDOWPOS2IVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3399

PFNGLWINDOWPOS2SPROC = CFUNCTYPE(UNCHECKED(None), GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 3400

PFNGLWINDOWPOS2SVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3401

PFNGLWINDOWPOS3DPROC = CFUNCTYPE(UNCHECKED(None), GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3402

PFNGLWINDOWPOS3DVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3403

PFNGLWINDOWPOS3FPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3404

PFNGLWINDOWPOS3FVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3405

PFNGLWINDOWPOS3IPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 3406

PFNGLWINDOWPOS3IVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3407

PFNGLWINDOWPOS3SPROC = CFUNCTYPE(UNCHECKED(None), GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 3408

PFNGLWINDOWPOS3SVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3409

PFNGLGENQUERIESPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3435

PFNGLDELETEQUERIESPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3436

PFNGLISQUERYPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 3437

PFNGLBEGINQUERYPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 3438

PFNGLENDQUERYPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 3439

PFNGLGETQUERYIVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3440

PFNGLGETQUERYOBJECTIVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3441

PFNGLGETQUERYOBJECTUIVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3442

PFNGLBINDBUFFERPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 3443

PFNGLDELETEBUFFERSPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3444

PFNGLGENBUFFERSPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3445

PFNGLISBUFFERPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 3446

PFNGLBUFFERDATAPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizeiptr, POINTER(GLvoid), GLenum) # /usr/include/SDL/SDL_opengl.h: 3447

PFNGLBUFFERSUBDATAPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLintptr, GLsizeiptr, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3448

PFNGLGETBUFFERSUBDATAPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLintptr, GLsizeiptr, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3449

PFNGLMAPBUFFERPROC = CFUNCTYPE(UNCHECKED(POINTER(GLvoid)), GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 3450

PFNGLUNMAPBUFFERPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLenum) # /usr/include/SDL/SDL_opengl.h: 3451

PFNGLGETBUFFERPARAMETERIVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3452

PFNGLGETBUFFERPOINTERVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(POINTER(GLvoid))) # /usr/include/SDL/SDL_opengl.h: 3453

PFNGLBLENDEQUATIONSEPARATEPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 3553

PFNGLDRAWBUFFERSPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLenum)) # /usr/include/SDL/SDL_opengl.h: 3554

PFNGLSTENCILOPSEPARATEPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 3555

PFNGLSTENCILFUNCSEPARATEPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLint, GLuint) # /usr/include/SDL/SDL_opengl.h: 3556

PFNGLSTENCILMASKSEPARATEPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 3557

PFNGLATTACHSHADERPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 3558

PFNGLBINDATTRIBLOCATIONPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint, POINTER(GLchar)) # /usr/include/SDL/SDL_opengl.h: 3559

PFNGLCOMPILESHADERPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 3560

PFNGLCREATEPROGRAMPROC = CFUNCTYPE(UNCHECKED(GLuint), ) # /usr/include/SDL/SDL_opengl.h: 3561

PFNGLCREATESHADERPROC = CFUNCTYPE(UNCHECKED(GLuint), GLenum) # /usr/include/SDL/SDL_opengl.h: 3562

PFNGLDELETEPROGRAMPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 3563

PFNGLDELETESHADERPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 3564

PFNGLDETACHSHADERPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 3565

PFNGLDISABLEVERTEXATTRIBARRAYPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 3566

PFNGLENABLEVERTEXATTRIBARRAYPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 3567

PFNGLGETACTIVEATTRIBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint, GLsizei, POINTER(GLsizei), POINTER(GLint), POINTER(GLenum), POINTER(GLchar)) # /usr/include/SDL/SDL_opengl.h: 3568

PFNGLGETACTIVEUNIFORMPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint, GLsizei, POINTER(GLsizei), POINTER(GLint), POINTER(GLenum), POINTER(GLchar)) # /usr/include/SDL/SDL_opengl.h: 3569

PFNGLGETATTACHEDSHADERSPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLsizei), POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3570

PFNGLGETATTRIBLOCATIONPROC = CFUNCTYPE(UNCHECKED(GLint), GLuint, POINTER(GLchar)) # /usr/include/SDL/SDL_opengl.h: 3571

PFNGLGETPROGRAMIVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3572

PFNGLGETPROGRAMINFOLOGPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLsizei), POINTER(GLchar)) # /usr/include/SDL/SDL_opengl.h: 3573

PFNGLGETSHADERIVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3574

PFNGLGETSHADERINFOLOGPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLsizei), POINTER(GLchar)) # /usr/include/SDL/SDL_opengl.h: 3575

PFNGLGETSHADERSOURCEPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLsizei), POINTER(GLchar)) # /usr/include/SDL/SDL_opengl.h: 3576

PFNGLGETUNIFORMLOCATIONPROC = CFUNCTYPE(UNCHECKED(GLint), GLuint, POINTER(GLchar)) # /usr/include/SDL/SDL_opengl.h: 3577

PFNGLGETUNIFORMFVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3578

PFNGLGETUNIFORMIVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLint, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3579

PFNGLGETVERTEXATTRIBDVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3580

PFNGLGETVERTEXATTRIBFVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3581

PFNGLGETVERTEXATTRIBIVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3582

PFNGLGETVERTEXATTRIBPOINTERVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(POINTER(GLvoid))) # /usr/include/SDL/SDL_opengl.h: 3583

PFNGLISPROGRAMPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 3584

PFNGLISSHADERPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 3585

PFNGLLINKPROGRAMPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 3586

PFNGLSHADERSOURCEPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(POINTER(GLchar)), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3587

PFNGLUSEPROGRAMPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 3588

PFNGLUNIFORM1FPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3589

PFNGLUNIFORM2FPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3590

PFNGLUNIFORM3FPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3591

PFNGLUNIFORM4FPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3592

PFNGLUNIFORM1IPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 3593

PFNGLUNIFORM2IPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 3594

PFNGLUNIFORM3IPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 3595

PFNGLUNIFORM4IPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 3596

PFNGLUNIFORM1FVPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3597

PFNGLUNIFORM2FVPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3598

PFNGLUNIFORM3FVPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3599

PFNGLUNIFORM4FVPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3600

PFNGLUNIFORM1IVPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3601

PFNGLUNIFORM2IVPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3602

PFNGLUNIFORM3IVPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3603

PFNGLUNIFORM4IVPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3604

PFNGLUNIFORMMATRIX2FVPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, GLboolean, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3605

PFNGLUNIFORMMATRIX3FVPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, GLboolean, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3606

PFNGLUNIFORMMATRIX4FVPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, GLboolean, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3607

PFNGLVALIDATEPROGRAMPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 3608

PFNGLVERTEXATTRIB1DPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3609

PFNGLVERTEXATTRIB1DVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3610

PFNGLVERTEXATTRIB1FPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3611

PFNGLVERTEXATTRIB1FVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3612

PFNGLVERTEXATTRIB1SPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLshort) # /usr/include/SDL/SDL_opengl.h: 3613

PFNGLVERTEXATTRIB1SVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3614

PFNGLVERTEXATTRIB2DPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3615

PFNGLVERTEXATTRIB2DVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3616

PFNGLVERTEXATTRIB2FPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3617

PFNGLVERTEXATTRIB2FVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3618

PFNGLVERTEXATTRIB2SPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 3619

PFNGLVERTEXATTRIB2SVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3620

PFNGLVERTEXATTRIB3DPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3621

PFNGLVERTEXATTRIB3DVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3622

PFNGLVERTEXATTRIB3FPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3623

PFNGLVERTEXATTRIB3FVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3624

PFNGLVERTEXATTRIB3SPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 3625

PFNGLVERTEXATTRIB3SVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3626

PFNGLVERTEXATTRIB4NBVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLbyte)) # /usr/include/SDL/SDL_opengl.h: 3627

PFNGLVERTEXATTRIB4NIVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3628

PFNGLVERTEXATTRIB4NSVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3629

PFNGLVERTEXATTRIB4NUBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLubyte, GLubyte, GLubyte, GLubyte) # /usr/include/SDL/SDL_opengl.h: 3630

PFNGLVERTEXATTRIB4NUBVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 3631

PFNGLVERTEXATTRIB4NUIVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3632

PFNGLVERTEXATTRIB4NUSVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLushort)) # /usr/include/SDL/SDL_opengl.h: 3633

PFNGLVERTEXATTRIB4BVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLbyte)) # /usr/include/SDL/SDL_opengl.h: 3634

PFNGLVERTEXATTRIB4DPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLdouble, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3635

PFNGLVERTEXATTRIB4DVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3636

PFNGLVERTEXATTRIB4FPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3637

PFNGLVERTEXATTRIB4FVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3638

PFNGLVERTEXATTRIB4IVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3639

PFNGLVERTEXATTRIB4SPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLshort, GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 3640

PFNGLVERTEXATTRIB4SVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3641

PFNGLVERTEXATTRIB4UBVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 3642

PFNGLVERTEXATTRIB4UIVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3643

PFNGLVERTEXATTRIB4USVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLushort)) # /usr/include/SDL/SDL_opengl.h: 3644

PFNGLVERTEXATTRIBPOINTERPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLint, GLenum, GLboolean, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3645

PFNGLLOADTRANSPOSEMATRIXFARBPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3730

PFNGLLOADTRANSPOSEMATRIXDARBPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3731

PFNGLMULTTRANSPOSEMATRIXFARBPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3732

PFNGLMULTTRANSPOSEMATRIXDARBPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3733

PFNGLSAMPLECOVERAGEARBPROC = CFUNCTYPE(UNCHECKED(None), GLclampf, GLboolean) # /usr/include/SDL/SDL_opengl.h: 3741

PFNGLCOMPRESSEDTEXIMAGE3DARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3763

PFNGLCOMPRESSEDTEXIMAGE2DARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3764

PFNGLCOMPRESSEDTEXIMAGE1DARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLenum, GLsizei, GLint, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3765

PFNGLCOMPRESSEDTEXSUBIMAGE3DARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3766

PFNGLCOMPRESSEDTEXSUBIMAGE2DARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3767

PFNGLCOMPRESSEDTEXSUBIMAGE1DARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLsizei, GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3768

PFNGLGETCOMPRESSEDTEXIMAGEARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3769

PFNGLPOINTPARAMETERFARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3782

PFNGLPOINTPARAMETERFVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3783

PFNGLWEIGHTBVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, POINTER(GLbyte)) # /usr/include/SDL/SDL_opengl.h: 3800

PFNGLWEIGHTSVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3801

PFNGLWEIGHTIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3802

PFNGLWEIGHTFVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3803

PFNGLWEIGHTDVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3804

PFNGLWEIGHTUBVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 3805

PFNGLWEIGHTUSVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, POINTER(GLushort)) # /usr/include/SDL/SDL_opengl.h: 3806

PFNGLWEIGHTUIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3807

PFNGLWEIGHTPOINTERARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3808

PFNGLVERTEXBLENDARBPROC = CFUNCTYPE(UNCHECKED(None), GLint) # /usr/include/SDL/SDL_opengl.h: 3809

PFNGLCURRENTPALETTEMATRIXARBPROC = CFUNCTYPE(UNCHECKED(None), GLint) # /usr/include/SDL/SDL_opengl.h: 3821

PFNGLMATRIXINDEXUBVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 3822

PFNGLMATRIXINDEXUSVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, POINTER(GLushort)) # /usr/include/SDL/SDL_opengl.h: 3823

PFNGLMATRIXINDEXUIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3824

PFNGLMATRIXINDEXPOINTERARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3825

PFNGLWINDOWPOS2DARBPROC = CFUNCTYPE(UNCHECKED(None), GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3876

PFNGLWINDOWPOS2DVARBPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3877

PFNGLWINDOWPOS2FARBPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3878

PFNGLWINDOWPOS2FVARBPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3879

PFNGLWINDOWPOS2IARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 3880

PFNGLWINDOWPOS2IVARBPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3881

PFNGLWINDOWPOS2SARBPROC = CFUNCTYPE(UNCHECKED(None), GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 3882

PFNGLWINDOWPOS2SVARBPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3883

PFNGLWINDOWPOS3DARBPROC = CFUNCTYPE(UNCHECKED(None), GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3884

PFNGLWINDOWPOS3DVARBPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3885

PFNGLWINDOWPOS3FARBPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3886

PFNGLWINDOWPOS3FVARBPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3887

PFNGLWINDOWPOS3IARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 3888

PFNGLWINDOWPOS3IVARBPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3889

PFNGLWINDOWPOS3SARBPROC = CFUNCTYPE(UNCHECKED(None), GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 3890

PFNGLWINDOWPOS3SVARBPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3891

PFNGLVERTEXATTRIB1DARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3960

PFNGLVERTEXATTRIB1DVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3961

PFNGLVERTEXATTRIB1FARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3962

PFNGLVERTEXATTRIB1FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3963

PFNGLVERTEXATTRIB1SARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLshort) # /usr/include/SDL/SDL_opengl.h: 3964

PFNGLVERTEXATTRIB1SVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3965

PFNGLVERTEXATTRIB2DARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3966

PFNGLVERTEXATTRIB2DVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3967

PFNGLVERTEXATTRIB2FARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3968

PFNGLVERTEXATTRIB2FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3969

PFNGLVERTEXATTRIB2SARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 3970

PFNGLVERTEXATTRIB2SVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3971

PFNGLVERTEXATTRIB3DARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3972

PFNGLVERTEXATTRIB3DVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3973

PFNGLVERTEXATTRIB3FARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3974

PFNGLVERTEXATTRIB3FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3975

PFNGLVERTEXATTRIB3SARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 3976

PFNGLVERTEXATTRIB3SVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3977

PFNGLVERTEXATTRIB4NBVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLbyte)) # /usr/include/SDL/SDL_opengl.h: 3978

PFNGLVERTEXATTRIB4NIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3979

PFNGLVERTEXATTRIB4NSVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3980

PFNGLVERTEXATTRIB4NUBARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLubyte, GLubyte, GLubyte, GLubyte) # /usr/include/SDL/SDL_opengl.h: 3981

PFNGLVERTEXATTRIB4NUBVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 3982

PFNGLVERTEXATTRIB4NUIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3983

PFNGLVERTEXATTRIB4NUSVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLushort)) # /usr/include/SDL/SDL_opengl.h: 3984

PFNGLVERTEXATTRIB4BVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLbyte)) # /usr/include/SDL/SDL_opengl.h: 3985

PFNGLVERTEXATTRIB4DARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLdouble, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 3986

PFNGLVERTEXATTRIB4DVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 3987

PFNGLVERTEXATTRIB4FARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 3988

PFNGLVERTEXATTRIB4FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 3989

PFNGLVERTEXATTRIB4IVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 3990

PFNGLVERTEXATTRIB4SARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLshort, GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 3991

PFNGLVERTEXATTRIB4SVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 3992

PFNGLVERTEXATTRIB4UBVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 3993

PFNGLVERTEXATTRIB4UIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 3994

PFNGLVERTEXATTRIB4USVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLushort)) # /usr/include/SDL/SDL_opengl.h: 3995

PFNGLVERTEXATTRIBPOINTERARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLint, GLenum, GLboolean, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3996

PFNGLENABLEVERTEXATTRIBARRAYARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 3997

PFNGLDISABLEVERTEXATTRIBARRAYARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 3998

PFNGLPROGRAMSTRINGARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 3999

PFNGLBINDPROGRAMARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 4000

PFNGLDELETEPROGRAMSARBPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 4001

PFNGLGENPROGRAMSARBPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 4002

PFNGLPROGRAMENVPARAMETER4DARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLdouble, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 4003

PFNGLPROGRAMENVPARAMETER4DVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 4004

PFNGLPROGRAMENVPARAMETER4FARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4005

PFNGLPROGRAMENVPARAMETER4FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4006

PFNGLPROGRAMLOCALPARAMETER4DARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLdouble, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 4007

PFNGLPROGRAMLOCALPARAMETER4DVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 4008

PFNGLPROGRAMLOCALPARAMETER4FARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4009

PFNGLPROGRAMLOCALPARAMETER4FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4010

PFNGLGETPROGRAMENVPARAMETERDVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 4011

PFNGLGETPROGRAMENVPARAMETERFVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4012

PFNGLGETPROGRAMLOCALPARAMETERDVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 4013

PFNGLGETPROGRAMLOCALPARAMETERFVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4014

PFNGLGETPROGRAMIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4015

PFNGLGETPROGRAMSTRINGARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4016

PFNGLGETVERTEXATTRIBDVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 4017

PFNGLGETVERTEXATTRIBFVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4018

PFNGLGETVERTEXATTRIBIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4019

PFNGLGETVERTEXATTRIBPOINTERVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(POINTER(GLvoid))) # /usr/include/SDL/SDL_opengl.h: 4020

PFNGLISPROGRAMARBPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 4021

PFNGLBINDBUFFERARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 4044

PFNGLDELETEBUFFERSARBPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 4045

PFNGLGENBUFFERSARBPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 4046

PFNGLISBUFFERARBPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 4047

PFNGLBUFFERDATAARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizeiptrARB, POINTER(GLvoid), GLenum) # /usr/include/SDL/SDL_opengl.h: 4048

PFNGLBUFFERSUBDATAARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLintptrARB, GLsizeiptrARB, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4049

PFNGLGETBUFFERSUBDATAARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLintptrARB, GLsizeiptrARB, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4050

PFNGLMAPBUFFERARBPROC = CFUNCTYPE(UNCHECKED(POINTER(GLvoid)), GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 4051

PFNGLUNMAPBUFFERARBPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLenum) # /usr/include/SDL/SDL_opengl.h: 4052

PFNGLGETBUFFERPARAMETERIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4053

PFNGLGETBUFFERPOINTERVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(POINTER(GLvoid))) # /usr/include/SDL/SDL_opengl.h: 4054

PFNGLGENQUERIESARBPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 4069

PFNGLDELETEQUERIESARBPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 4070

PFNGLISQUERYARBPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 4071

PFNGLBEGINQUERYARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 4072

PFNGLENDQUERYARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 4073

PFNGLGETQUERYIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4074

PFNGLGETQUERYOBJECTIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4075

PFNGLGETQUERYOBJECTUIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 4076

PFNGLDELETEOBJECTARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB) # /usr/include/SDL/SDL_opengl.h: 4122

PFNGLGETHANDLEARBPROC = CFUNCTYPE(UNCHECKED(GLhandleARB), GLenum) # /usr/include/SDL/SDL_opengl.h: 4123

PFNGLDETACHOBJECTARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLhandleARB) # /usr/include/SDL/SDL_opengl.h: 4124

PFNGLCREATESHADEROBJECTARBPROC = CFUNCTYPE(UNCHECKED(GLhandleARB), GLenum) # /usr/include/SDL/SDL_opengl.h: 4125

PFNGLSHADERSOURCEARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLsizei, POINTER(POINTER(GLcharARB)), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4126

PFNGLCOMPILESHADERARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB) # /usr/include/SDL/SDL_opengl.h: 4127

PFNGLCREATEPROGRAMOBJECTARBPROC = CFUNCTYPE(UNCHECKED(GLhandleARB), ) # /usr/include/SDL/SDL_opengl.h: 4128

PFNGLATTACHOBJECTARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLhandleARB) # /usr/include/SDL/SDL_opengl.h: 4129

PFNGLLINKPROGRAMARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB) # /usr/include/SDL/SDL_opengl.h: 4130

PFNGLUSEPROGRAMOBJECTARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB) # /usr/include/SDL/SDL_opengl.h: 4131

PFNGLVALIDATEPROGRAMARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB) # /usr/include/SDL/SDL_opengl.h: 4132

PFNGLUNIFORM1FARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4133

PFNGLUNIFORM2FARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4134

PFNGLUNIFORM3FARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4135

PFNGLUNIFORM4FARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4136

PFNGLUNIFORM1IARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 4137

PFNGLUNIFORM2IARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 4138

PFNGLUNIFORM3IARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 4139

PFNGLUNIFORM4IARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 4140

PFNGLUNIFORM1FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4141

PFNGLUNIFORM2FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4142

PFNGLUNIFORM3FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4143

PFNGLUNIFORM4FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4144

PFNGLUNIFORM1IVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4145

PFNGLUNIFORM2IVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4146

PFNGLUNIFORM3IVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4147

PFNGLUNIFORM4IVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4148

PFNGLUNIFORMMATRIX2FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, GLboolean, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4149

PFNGLUNIFORMMATRIX3FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, GLboolean, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4150

PFNGLUNIFORMMATRIX4FVARBPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei, GLboolean, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4151

PFNGLGETOBJECTPARAMETERFVARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4152

PFNGLGETOBJECTPARAMETERIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4153

PFNGLGETINFOLOGARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLsizei, POINTER(GLsizei), POINTER(GLcharARB)) # /usr/include/SDL/SDL_opengl.h: 4154

PFNGLGETATTACHEDOBJECTSARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLsizei, POINTER(GLsizei), POINTER(GLhandleARB)) # /usr/include/SDL/SDL_opengl.h: 4155

PFNGLGETUNIFORMLOCATIONARBPROC = CFUNCTYPE(UNCHECKED(GLint), GLhandleARB, POINTER(GLcharARB)) # /usr/include/SDL/SDL_opengl.h: 4156

PFNGLGETACTIVEUNIFORMARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLuint, GLsizei, POINTER(GLsizei), POINTER(GLint), POINTER(GLenum), POINTER(GLcharARB)) # /usr/include/SDL/SDL_opengl.h: 4157

PFNGLGETUNIFORMFVARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4158

PFNGLGETUNIFORMIVARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLint, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4159

PFNGLGETSHADERSOURCEARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLsizei, POINTER(GLsizei), POINTER(GLcharARB)) # /usr/include/SDL/SDL_opengl.h: 4160

PFNGLBINDATTRIBLOCATIONARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLuint, POINTER(GLcharARB)) # /usr/include/SDL/SDL_opengl.h: 4170

PFNGLGETACTIVEATTRIBARBPROC = CFUNCTYPE(UNCHECKED(None), GLhandleARB, GLuint, GLsizei, POINTER(GLsizei), POINTER(GLint), POINTER(GLenum), POINTER(GLcharARB)) # /usr/include/SDL/SDL_opengl.h: 4171

PFNGLGETATTRIBLOCATIONARBPROC = CFUNCTYPE(UNCHECKED(GLint), GLhandleARB, POINTER(GLcharARB)) # /usr/include/SDL/SDL_opengl.h: 4172

PFNGLDRAWBUFFERSARBPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLenum)) # /usr/include/SDL/SDL_opengl.h: 4200

PFNGLCLAMPCOLORARBPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 4212

PFNGLBLENDCOLOREXTPROC = CFUNCTYPE(UNCHECKED(None), GLclampf, GLclampf, GLclampf, GLclampf) # /usr/include/SDL/SDL_opengl.h: 4236

PFNGLPOLYGONOFFSETEXTPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4244

PFNGLTEXIMAGE3DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4257

PFNGLTEXSUBIMAGE3DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4258

PFNGLGETTEXFILTERFUNCSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4267

PFNGLTEXFILTERFUNCSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4268

PFNGLTEXSUBIMAGE1DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLsizei, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4277

PFNGLTEXSUBIMAGE2DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4278

PFNGLCOPYTEXIMAGE1DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLint) # /usr/include/SDL/SDL_opengl.h: 4290

PFNGLCOPYTEXIMAGE2DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint) # /usr/include/SDL/SDL_opengl.h: 4291

PFNGLCOPYTEXSUBIMAGE1DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLint, GLint, GLsizei) # /usr/include/SDL/SDL_opengl.h: 4292

PFNGLCOPYTEXSUBIMAGE2DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei) # /usr/include/SDL/SDL_opengl.h: 4293

PFNGLCOPYTEXSUBIMAGE3DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei) # /usr/include/SDL/SDL_opengl.h: 4294

PFNGLGETHISTOGRAMEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLboolean, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4311

PFNGLGETHISTOGRAMPARAMETERFVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4312

PFNGLGETHISTOGRAMPARAMETERIVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4313

PFNGLGETMINMAXEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLboolean, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4314

PFNGLGETMINMAXPARAMETERFVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4315

PFNGLGETMINMAXPARAMETERIVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4316

PFNGLHISTOGRAMEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, GLenum, GLboolean) # /usr/include/SDL/SDL_opengl.h: 4317

PFNGLMINMAXEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLboolean) # /usr/include/SDL/SDL_opengl.h: 4318

PFNGLRESETHISTOGRAMEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 4319

PFNGLRESETMINMAXEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 4320

PFNGLCONVOLUTIONFILTER1DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLsizei, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4340

PFNGLCONVOLUTIONFILTER2DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4341

PFNGLCONVOLUTIONPARAMETERFEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4342

PFNGLCONVOLUTIONPARAMETERFVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4343

PFNGLCONVOLUTIONPARAMETERIEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 4344

PFNGLCONVOLUTIONPARAMETERIVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4345

PFNGLCOPYCONVOLUTIONFILTER1DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLint, GLint, GLsizei) # /usr/include/SDL/SDL_opengl.h: 4346

PFNGLCOPYCONVOLUTIONFILTER2DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLint, GLint, GLsizei, GLsizei) # /usr/include/SDL/SDL_opengl.h: 4347

PFNGLGETCONVOLUTIONFILTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4348

PFNGLGETCONVOLUTIONPARAMETERFVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4349

PFNGLGETCONVOLUTIONPARAMETERIVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4350

PFNGLGETSEPARABLEFILTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, POINTER(GLvoid), POINTER(GLvoid), POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4351

PFNGLSEPARABLEFILTER2DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid), POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4352

PFNGLCOLORTABLESGIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLsizei, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4370

PFNGLCOLORTABLEPARAMETERFVSGIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4371

PFNGLCOLORTABLEPARAMETERIVSGIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4372

PFNGLCOPYCOLORTABLESGIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLint, GLint, GLsizei) # /usr/include/SDL/SDL_opengl.h: 4373

PFNGLGETCOLORTABLESGIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4374

PFNGLGETCOLORTABLEPARAMETERFVSGIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4375

PFNGLGETCOLORTABLEPARAMETERIVSGIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4376

PFNGLPIXELTEXGENSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 4384

PFNGLPIXELTEXGENPARAMETERISGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 4397

PFNGLPIXELTEXGENPARAMETERIVSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4398

PFNGLPIXELTEXGENPARAMETERFSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4399

PFNGLPIXELTEXGENPARAMETERFVSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4400

PFNGLGETPIXELTEXGENPARAMETERIVSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4401

PFNGLGETPIXELTEXGENPARAMETERFVSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4402

PFNGLTEXIMAGE4DSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4411

PFNGLTEXSUBIMAGE4DSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4412

PFNGLARETEXTURESRESIDENTEXTPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLsizei, POINTER(GLuint), POINTER(GLboolean)) # /usr/include/SDL/SDL_opengl.h: 4433

PFNGLBINDTEXTUREEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 4434

PFNGLDELETETEXTURESEXTPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 4435

PFNGLGENTEXTURESEXTPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 4436

PFNGLISTEXTUREEXTPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 4437

PFNGLPRIORITIZETEXTURESEXTPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint), POINTER(GLclampf)) # /usr/include/SDL/SDL_opengl.h: 4438

PFNGLDETAILTEXFUNCSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4447

PFNGLGETDETAILTEXFUNCSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4448

PFNGLSHARPENTEXFUNCSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4457

PFNGLGETSHARPENTEXFUNCSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4458

PFNGLSAMPLEMASKSGISPROC = CFUNCTYPE(UNCHECKED(None), GLclampf, GLboolean) # /usr/include/SDL/SDL_opengl.h: 4475

PFNGLSAMPLEPATTERNSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 4476

PFNGLARRAYELEMENTEXTPROC = CFUNCTYPE(UNCHECKED(None), GLint) # /usr/include/SDL/SDL_opengl.h: 4496

PFNGLCOLORPOINTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, GLsizei, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4497

PFNGLDRAWARRAYSEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLsizei) # /usr/include/SDL/SDL_opengl.h: 4498

PFNGLEDGEFLAGPOINTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, GLsizei, POINTER(GLboolean)) # /usr/include/SDL/SDL_opengl.h: 4499

PFNGLGETPOINTERVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(POINTER(GLvoid))) # /usr/include/SDL/SDL_opengl.h: 4500

PFNGLINDEXPOINTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4501

PFNGLNORMALPOINTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4502

PFNGLTEXCOORDPOINTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, GLsizei, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4503

PFNGLVERTEXPOINTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, GLsizei, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4504

PFNGLBLENDEQUATIONEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 4536

PFNGLSPRITEPARAMETERFSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4567

PFNGLSPRITEPARAMETERFVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4568

PFNGLSPRITEPARAMETERISGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 4569

PFNGLSPRITEPARAMETERIVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4570

PFNGLPOINTPARAMETERFEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4583

PFNGLPOINTPARAMETERFVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4584

PFNGLPOINTPARAMETERFSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4593

PFNGLPOINTPARAMETERFVSGISPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4594

PFNGLGETINSTRUMENTSSGIXPROC = CFUNCTYPE(UNCHECKED(GLint), ) # /usr/include/SDL/SDL_opengl.h: 4607

PFNGLINSTRUMENTSBUFFERSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4608

PFNGLPOLLINSTRUMENTSSGIXPROC = CFUNCTYPE(UNCHECKED(GLint), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4609

PFNGLREADINSTRUMENTSSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLint) # /usr/include/SDL/SDL_opengl.h: 4610

PFNGLSTARTINSTRUMENTSSGIXPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 4611

PFNGLSTOPINSTRUMENTSSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLint) # /usr/include/SDL/SDL_opengl.h: 4612

PFNGLFRAMEZOOMSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLint) # /usr/include/SDL/SDL_opengl.h: 4624

PFNGLTAGSAMPLEBUFFERSGIXPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 4632

PFNGLDEFORMATIONMAP3DSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble, GLint, GLint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 4643

PFNGLDEFORMATIONMAP3FSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat, GLfloat, GLint, GLint, GLfloat, GLfloat, GLint, GLint, GLfloat, GLfloat, GLint, GLint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4644

PFNGLDEFORMSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLbitfield) # /usr/include/SDL/SDL_opengl.h: 4645

PFNGLLOADIDENTITYDEFORMATIONMAPSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLbitfield) # /usr/include/SDL/SDL_opengl.h: 4646

PFNGLREFERENCEPLANESGIXPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 4654

PFNGLFLUSHRASTERSGIXPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 4662

PFNGLFOGFUNCSGISPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4675

PFNGLGETFOGFUNCSGISPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4676

PFNGLIMAGETRANSFORMPARAMETERIHPPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 4693

PFNGLIMAGETRANSFORMPARAMETERFHPPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4694

PFNGLIMAGETRANSFORMPARAMETERIVHPPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4695

PFNGLIMAGETRANSFORMPARAMETERFVHPPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4696

PFNGLGETIMAGETRANSFORMPARAMETERIVHPPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4697

PFNGLGETIMAGETRANSFORMPARAMETERFVHPPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4698

PFNGLCOLORSUBTABLEEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4715

PFNGLCOPYCOLORSUBTABLEEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, GLint, GLint, GLsizei) # /usr/include/SDL/SDL_opengl.h: 4716

PFNGLHINTPGIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 4728

PFNGLCOLORTABLEEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLsizei, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4739

PFNGLGETCOLORTABLEEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4740

PFNGLGETCOLORTABLEPARAMETERIVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4741

PFNGLGETCOLORTABLEPARAMETERFVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4742

PFNGLGETLISTPARAMETERFVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4759

PFNGLGETLISTPARAMETERIVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4760

PFNGLLISTPARAMETERFSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4761

PFNGLLISTPARAMETERFVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4762

PFNGLLISTPARAMETERISGIXPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 4763

PFNGLLISTPARAMETERIVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4764

PFNGLINDEXMATERIALEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 4792

PFNGLINDEXFUNCEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLclampf) # /usr/include/SDL/SDL_opengl.h: 4800

PFNGLLOCKARRAYSEXTPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLsizei) # /usr/include/SDL/SDL_opengl.h: 4813

PFNGLUNLOCKARRAYSEXTPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 4814

PFNGLCULLPARAMETERDVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 4823

PFNGLCULLPARAMETERFVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4824

PFNGLFRAGMENTCOLORMATERIALSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 4853

PFNGLFRAGMENTLIGHTFSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4854

PFNGLFRAGMENTLIGHTFVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4855

PFNGLFRAGMENTLIGHTISGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 4856

PFNGLFRAGMENTLIGHTIVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4857

PFNGLFRAGMENTLIGHTMODELFSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4858

PFNGLFRAGMENTLIGHTMODELFVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4859

PFNGLFRAGMENTLIGHTMODELISGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 4860

PFNGLFRAGMENTLIGHTMODELIVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4861

PFNGLFRAGMENTMATERIALFSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4862

PFNGLFRAGMENTMATERIALFVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4863

PFNGLFRAGMENTMATERIALISGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 4864

PFNGLFRAGMENTMATERIALIVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4865

PFNGLGETFRAGMENTLIGHTFVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4866

PFNGLGETFRAGMENTLIGHTIVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4867

PFNGLGETFRAGMENTMATERIALFVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4868

PFNGLGETFRAGMENTMATERIALIVSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4869

PFNGLLIGHTENVISGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 4870

PFNGLDRAWRANGEELEMENTSEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, GLsizei, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 4886

PFNGLAPPLYTEXTUREEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 4904

PFNGLTEXTURELIGHTEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 4905

PFNGLTEXTUREMATERIALEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 4906

PFNGLASYNCMARKERSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 4927

PFNGLFINISHASYNCSGIXPROC = CFUNCTYPE(UNCHECKED(GLint), POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 4928

PFNGLPOLLASYNCSGIXPROC = CFUNCTYPE(UNCHECKED(GLint), POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 4929

PFNGLGENASYNCMARKERSSGIXPROC = CFUNCTYPE(UNCHECKED(GLuint), GLsizei) # /usr/include/SDL/SDL_opengl.h: 4930

PFNGLDELETEASYNCMARKERSSGIXPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei) # /usr/include/SDL/SDL_opengl.h: 4931

PFNGLISASYNCMARKERSGIXPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 4932

PFNGLVERTEXPOINTERVINTELPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, POINTER(POINTER(GLvoid))) # /usr/include/SDL/SDL_opengl.h: 4951

PFNGLNORMALPOINTERVINTELPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(POINTER(GLvoid))) # /usr/include/SDL/SDL_opengl.h: 4952

PFNGLCOLORPOINTERVINTELPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, POINTER(POINTER(GLvoid))) # /usr/include/SDL/SDL_opengl.h: 4953

PFNGLTEXCOORDPOINTERVINTELPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, POINTER(POINTER(GLvoid))) # /usr/include/SDL/SDL_opengl.h: 4954

PFNGLPIXELTRANSFORMPARAMETERIEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 4969

PFNGLPIXELTRANSFORMPARAMETERFEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 4970

PFNGLPIXELTRANSFORMPARAMETERIVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 4971

PFNGLPIXELTRANSFORMPARAMETERFVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 4972

PFNGLSECONDARYCOLOR3BEXTPROC = CFUNCTYPE(UNCHECKED(None), GLbyte, GLbyte, GLbyte) # /usr/include/SDL/SDL_opengl.h: 5008

PFNGLSECONDARYCOLOR3BVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLbyte)) # /usr/include/SDL/SDL_opengl.h: 5009

PFNGLSECONDARYCOLOR3DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 5010

PFNGLSECONDARYCOLOR3DVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5011

PFNGLSECONDARYCOLOR3FEXTPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5012

PFNGLSECONDARYCOLOR3FVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5013

PFNGLSECONDARYCOLOR3IEXTPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 5014

PFNGLSECONDARYCOLOR3IVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5015

PFNGLSECONDARYCOLOR3SEXTPROC = CFUNCTYPE(UNCHECKED(None), GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 5016

PFNGLSECONDARYCOLOR3SVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5017

PFNGLSECONDARYCOLOR3UBEXTPROC = CFUNCTYPE(UNCHECKED(None), GLubyte, GLubyte, GLubyte) # /usr/include/SDL/SDL_opengl.h: 5018

PFNGLSECONDARYCOLOR3UBVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 5019

PFNGLSECONDARYCOLOR3UIEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5020

PFNGLSECONDARYCOLOR3UIVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 5021

PFNGLSECONDARYCOLOR3USEXTPROC = CFUNCTYPE(UNCHECKED(None), GLushort, GLushort, GLushort) # /usr/include/SDL/SDL_opengl.h: 5022

PFNGLSECONDARYCOLOR3USVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLushort)) # /usr/include/SDL/SDL_opengl.h: 5023

PFNGLSECONDARYCOLORPOINTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5024

PFNGLTEXTURENORMALEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 5032

PFNGLMULTIDRAWARRAYSEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint), POINTER(GLsizei), GLsizei) # /usr/include/SDL/SDL_opengl.h: 5041

PFNGLMULTIDRAWELEMENTSEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLsizei), GLenum, POINTER(POINTER(GLvoid)), GLsizei) # /usr/include/SDL/SDL_opengl.h: 5042

PFNGLFOGCOORDFEXTPROC = CFUNCTYPE(UNCHECKED(None), GLfloat) # /usr/include/SDL/SDL_opengl.h: 5054

PFNGLFOGCOORDFVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5055

PFNGLFOGCOORDDEXTPROC = CFUNCTYPE(UNCHECKED(None), GLdouble) # /usr/include/SDL/SDL_opengl.h: 5056

PFNGLFOGCOORDDVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5057

PFNGLFOGCOORDPOINTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5058

PFNGLTANGENT3BEXTPROC = CFUNCTYPE(UNCHECKED(None), GLbyte, GLbyte, GLbyte) # /usr/include/SDL/SDL_opengl.h: 5091

PFNGLTANGENT3BVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLbyte)) # /usr/include/SDL/SDL_opengl.h: 5092

PFNGLTANGENT3DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 5093

PFNGLTANGENT3DVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5094

PFNGLTANGENT3FEXTPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5095

PFNGLTANGENT3FVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5096

PFNGLTANGENT3IEXTPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 5097

PFNGLTANGENT3IVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5098

PFNGLTANGENT3SEXTPROC = CFUNCTYPE(UNCHECKED(None), GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 5099

PFNGLTANGENT3SVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5100

PFNGLBINORMAL3BEXTPROC = CFUNCTYPE(UNCHECKED(None), GLbyte, GLbyte, GLbyte) # /usr/include/SDL/SDL_opengl.h: 5101

PFNGLBINORMAL3BVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLbyte)) # /usr/include/SDL/SDL_opengl.h: 5102

PFNGLBINORMAL3DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 5103

PFNGLBINORMAL3DVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5104

PFNGLBINORMAL3FEXTPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5105

PFNGLBINORMAL3FVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5106

PFNGLBINORMAL3IEXTPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 5107

PFNGLBINORMAL3IVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5108

PFNGLBINORMAL3SEXTPROC = CFUNCTYPE(UNCHECKED(None), GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 5109

PFNGLBINORMAL3SVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5110

PFNGLTANGENTPOINTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5111

PFNGLBINORMALPOINTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5112

PFNGLFINISHTEXTURESUNXPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 5136

PFNGLGLOBALALPHAFACTORBSUNPROC = CFUNCTYPE(UNCHECKED(None), GLbyte) # /usr/include/SDL/SDL_opengl.h: 5151

PFNGLGLOBALALPHAFACTORSSUNPROC = CFUNCTYPE(UNCHECKED(None), GLshort) # /usr/include/SDL/SDL_opengl.h: 5152

PFNGLGLOBALALPHAFACTORISUNPROC = CFUNCTYPE(UNCHECKED(None), GLint) # /usr/include/SDL/SDL_opengl.h: 5153

PFNGLGLOBALALPHAFACTORFSUNPROC = CFUNCTYPE(UNCHECKED(None), GLfloat) # /usr/include/SDL/SDL_opengl.h: 5154

PFNGLGLOBALALPHAFACTORDSUNPROC = CFUNCTYPE(UNCHECKED(None), GLdouble) # /usr/include/SDL/SDL_opengl.h: 5155

PFNGLGLOBALALPHAFACTORUBSUNPROC = CFUNCTYPE(UNCHECKED(None), GLubyte) # /usr/include/SDL/SDL_opengl.h: 5156

PFNGLGLOBALALPHAFACTORUSSUNPROC = CFUNCTYPE(UNCHECKED(None), GLushort) # /usr/include/SDL/SDL_opengl.h: 5157

PFNGLGLOBALALPHAFACTORUISUNPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 5158

PFNGLREPLACEMENTCODEUISUNPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 5172

PFNGLREPLACEMENTCODEUSSUNPROC = CFUNCTYPE(UNCHECKED(None), GLushort) # /usr/include/SDL/SDL_opengl.h: 5173

PFNGLREPLACEMENTCODEUBSUNPROC = CFUNCTYPE(UNCHECKED(None), GLubyte) # /usr/include/SDL/SDL_opengl.h: 5174

PFNGLREPLACEMENTCODEUIVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 5175

PFNGLREPLACEMENTCODEUSVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLushort)) # /usr/include/SDL/SDL_opengl.h: 5176

PFNGLREPLACEMENTCODEUBVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 5177

PFNGLREPLACEMENTCODEPOINTERSUNPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, POINTER(POINTER(GLvoid))) # /usr/include/SDL/SDL_opengl.h: 5178

PFNGLCOLOR4UBVERTEX2FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLubyte, GLubyte, GLubyte, GLubyte, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5225

PFNGLCOLOR4UBVERTEX2FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLubyte), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5226

PFNGLCOLOR4UBVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLubyte, GLubyte, GLubyte, GLubyte, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5227

PFNGLCOLOR4UBVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLubyte), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5228

PFNGLCOLOR3FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5229

PFNGLCOLOR3FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5230

PFNGLNORMAL3FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5231

PFNGLNORMAL3FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5232

PFNGLCOLOR4FNORMAL3FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5233

PFNGLCOLOR4FNORMAL3FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5234

PFNGLTEXCOORD2FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5235

PFNGLTEXCOORD2FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5236

PFNGLTEXCOORD4FVERTEX4FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5237

PFNGLTEXCOORD4FVERTEX4FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5238

PFNGLTEXCOORD2FCOLOR4UBVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLubyte, GLubyte, GLubyte, GLubyte, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5239

PFNGLTEXCOORD2FCOLOR4UBVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat), POINTER(GLubyte), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5240

PFNGLTEXCOORD2FCOLOR3FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5241

PFNGLTEXCOORD2FCOLOR3FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5242

PFNGLTEXCOORD2FNORMAL3FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5243

PFNGLTEXCOORD2FNORMAL3FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5244

PFNGLTEXCOORD2FCOLOR4FNORMAL3FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5245

PFNGLTEXCOORD2FCOLOR4FNORMAL3FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5246

PFNGLTEXCOORD4FCOLOR4FNORMAL3FVERTEX4FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5247

PFNGLTEXCOORD4FCOLOR4FNORMAL3FVERTEX4FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5248

PFNGLREPLACEMENTCODEUIVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5249

PFNGLREPLACEMENTCODEUIVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLuint), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5250

PFNGLREPLACEMENTCODEUICOLOR4UBVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLubyte, GLubyte, GLubyte, GLubyte, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5251

PFNGLREPLACEMENTCODEUICOLOR4UBVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLuint), POINTER(GLubyte), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5252

PFNGLREPLACEMENTCODEUICOLOR3FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5253

PFNGLREPLACEMENTCODEUICOLOR3FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLuint), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5254

PFNGLREPLACEMENTCODEUINORMAL3FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5255

PFNGLREPLACEMENTCODEUINORMAL3FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLuint), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5256

PFNGLREPLACEMENTCODEUICOLOR4FNORMAL3FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5257

PFNGLREPLACEMENTCODEUICOLOR4FNORMAL3FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLuint), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5258

PFNGLREPLACEMENTCODEUITEXCOORD2FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5259

PFNGLREPLACEMENTCODEUITEXCOORD2FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLuint), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5260

PFNGLREPLACEMENTCODEUITEXCOORD2FNORMAL3FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5261

PFNGLREPLACEMENTCODEUITEXCOORD2FNORMAL3FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLuint), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5262

PFNGLREPLACEMENTCODEUITEXCOORD2FCOLOR4FNORMAL3FVERTEX3FSUNPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5263

PFNGLREPLACEMENTCODEUITEXCOORD2FCOLOR4FNORMAL3FVERTEX3FVSUNPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLuint), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5264

PFNGLBLENDFUNCSEPARATEEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 5272

PFNGLBLENDFUNCSEPARATEINGRPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 5280

PFNGLVERTEXWEIGHTFEXTPROC = CFUNCTYPE(UNCHECKED(None), GLfloat) # /usr/include/SDL/SDL_opengl.h: 5326

PFNGLVERTEXWEIGHTFVEXTPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5327

PFNGLVERTEXWEIGHTPOINTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5328

PFNGLFLUSHVERTEXARRAYRANGENVPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 5341

PFNGLVERTEXARRAYRANGENVPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5342

PFNGLCOMBINERPARAMETERFVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5362

PFNGLCOMBINERPARAMETERFNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5363

PFNGLCOMBINERPARAMETERIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5364

PFNGLCOMBINERPARAMETERINVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 5365

PFNGLCOMBINERINPUTNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLenum, GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 5366

PFNGLCOMBINEROUTPUTNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLenum, GLenum, GLenum, GLenum, GLboolean, GLboolean, GLboolean) # /usr/include/SDL/SDL_opengl.h: 5367

PFNGLFINALCOMBINERINPUTNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 5368

PFNGLGETCOMBINERINPUTPARAMETERFVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5369

PFNGLGETCOMBINERINPUTPARAMETERIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5370

PFNGLGETCOMBINEROUTPUTPARAMETERFVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5371

PFNGLGETCOMBINEROUTPUTPARAMETERIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5372

PFNGLGETFINALCOMBINERINPUTPARAMETERFVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5373

PFNGLGETFINALCOMBINERINPUTPARAMETERIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5374

PFNGLRESIZEBUFFERSMESAPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 5398

PFNGLWINDOWPOS2DMESAPROC = CFUNCTYPE(UNCHECKED(None), GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 5429

PFNGLWINDOWPOS2DVMESAPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5430

PFNGLWINDOWPOS2FMESAPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5431

PFNGLWINDOWPOS2FVMESAPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5432

PFNGLWINDOWPOS2IMESAPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 5433

PFNGLWINDOWPOS2IVMESAPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5434

PFNGLWINDOWPOS2SMESAPROC = CFUNCTYPE(UNCHECKED(None), GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 5435

PFNGLWINDOWPOS2SVMESAPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5436

PFNGLWINDOWPOS3DMESAPROC = CFUNCTYPE(UNCHECKED(None), GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 5437

PFNGLWINDOWPOS3DVMESAPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5438

PFNGLWINDOWPOS3FMESAPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5439

PFNGLWINDOWPOS3FVMESAPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5440

PFNGLWINDOWPOS3IMESAPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 5441

PFNGLWINDOWPOS3IVMESAPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5442

PFNGLWINDOWPOS3SMESAPROC = CFUNCTYPE(UNCHECKED(None), GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 5443

PFNGLWINDOWPOS3SVMESAPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5444

PFNGLWINDOWPOS4DMESAPROC = CFUNCTYPE(UNCHECKED(None), GLdouble, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 5445

PFNGLWINDOWPOS4DVMESAPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5446

PFNGLWINDOWPOS4FMESAPROC = CFUNCTYPE(UNCHECKED(None), GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5447

PFNGLWINDOWPOS4FVMESAPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5448

PFNGLWINDOWPOS4IMESAPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 5449

PFNGLWINDOWPOS4IVMESAPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5450

PFNGLWINDOWPOS4SMESAPROC = CFUNCTYPE(UNCHECKED(None), GLshort, GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 5451

PFNGLWINDOWPOS4SVMESAPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5452

PFNGLMULTIMODEDRAWARRAYSIBMPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLenum), POINTER(GLint), POINTER(GLsizei), GLsizei, GLint) # /usr/include/SDL/SDL_opengl.h: 5465

PFNGLMULTIMODEDRAWELEMENTSIBMPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLenum), POINTER(GLsizei), GLenum, POINTER(POINTER(GLvoid)), GLsizei, GLint) # /usr/include/SDL/SDL_opengl.h: 5466

PFNGLCOLORPOINTERLISTIBMPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, GLint, POINTER(POINTER(GLvoid)), GLint) # /usr/include/SDL/SDL_opengl.h: 5481

PFNGLSECONDARYCOLORPOINTERLISTIBMPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, GLint, POINTER(POINTER(GLvoid)), GLint) # /usr/include/SDL/SDL_opengl.h: 5482

PFNGLEDGEFLAGPOINTERLISTIBMPROC = CFUNCTYPE(UNCHECKED(None), GLint, POINTER(POINTER(GLboolean)), GLint) # /usr/include/SDL/SDL_opengl.h: 5483

PFNGLFOGCOORDPOINTERLISTIBMPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, POINTER(POINTER(GLvoid)), GLint) # /usr/include/SDL/SDL_opengl.h: 5484

PFNGLINDEXPOINTERLISTIBMPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, POINTER(POINTER(GLvoid)), GLint) # /usr/include/SDL/SDL_opengl.h: 5485

PFNGLNORMALPOINTERLISTIBMPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, POINTER(POINTER(GLvoid)), GLint) # /usr/include/SDL/SDL_opengl.h: 5486

PFNGLTEXCOORDPOINTERLISTIBMPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, GLint, POINTER(POINTER(GLvoid)), GLint) # /usr/include/SDL/SDL_opengl.h: 5487

PFNGLVERTEXPOINTERLISTIBMPROC = CFUNCTYPE(UNCHECKED(None), GLint, GLenum, GLint, POINTER(POINTER(GLvoid)), GLint) # /usr/include/SDL/SDL_opengl.h: 5488

PFNGLTBUFFERMASK3DFXPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 5520

PFNGLSAMPLEMASKEXTPROC = CFUNCTYPE(UNCHECKED(None), GLclampf, GLboolean) # /usr/include/SDL/SDL_opengl.h: 5529

PFNGLSAMPLEPATTERNEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 5530

PFNGLTEXTURECOLORMASKSGISPROC = CFUNCTYPE(UNCHECKED(None), GLboolean, GLboolean, GLboolean, GLboolean) # /usr/include/SDL/SDL_opengl.h: 5554

PFNGLIGLOOINTERFACESGIXPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5562

PFNGLDELETEFENCESNVPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 5584

PFNGLGENFENCESNVPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 5585

PFNGLISFENCENVPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 5586

PFNGLTESTFENCENVPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 5587

PFNGLGETFENCEIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5588

PFNGLFINISHFENCENVPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 5589

PFNGLSETFENCENVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum) # /usr/include/SDL/SDL_opengl.h: 5590

PFNGLMAPCONTROLPOINTSNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLenum, GLsizei, GLsizei, GLint, GLint, GLboolean, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5606

PFNGLMAPPARAMETERIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5607

PFNGLMAPPARAMETERFVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5608

PFNGLGETMAPCONTROLPOINTSNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLenum, GLsizei, GLsizei, GLboolean, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5609

PFNGLGETMAPPARAMETERIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5610

PFNGLGETMAPPARAMETERFVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5611

PFNGLGETMAPATTRIBPARAMETERIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5612

PFNGLGETMAPATTRIBPARAMETERFVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5613

PFNGLEVALMAPSNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 5614

PFNGLCOMBINERSTAGEPARAMETERFVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5627

PFNGLGETCOMBINERSTAGEPARAMETERFVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5628

PFNGLAREPROGRAMSRESIDENTNVPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLsizei, POINTER(GLuint), POINTER(GLboolean)) # /usr/include/SDL/SDL_opengl.h: 5719

PFNGLBINDPROGRAMNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 5720

PFNGLDELETEPROGRAMSNVPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 5721

PFNGLEXECUTEPROGRAMNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5722

PFNGLGENPROGRAMSNVPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 5723

PFNGLGETPROGRAMPARAMETERDVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLenum, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5724

PFNGLGETPROGRAMPARAMETERFVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5725

PFNGLGETPROGRAMIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5726

PFNGLGETPROGRAMSTRINGNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 5727

PFNGLGETTRACKMATRIXIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5728

PFNGLGETVERTEXATTRIBDVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5729

PFNGLGETVERTEXATTRIBFVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5730

PFNGLGETVERTEXATTRIBIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5731

PFNGLGETVERTEXATTRIBPOINTERVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(POINTER(GLvoid))) # /usr/include/SDL/SDL_opengl.h: 5732

PFNGLISPROGRAMNVPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 5733

PFNGLLOADPROGRAMNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLsizei, POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 5734

PFNGLPROGRAMPARAMETER4DNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLdouble, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 5735

PFNGLPROGRAMPARAMETER4DVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5736

PFNGLPROGRAMPARAMETER4FNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5737

PFNGLPROGRAMPARAMETER4FVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5738

PFNGLPROGRAMPARAMETERS4DVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5739

PFNGLPROGRAMPARAMETERS4FVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5740

PFNGLREQUESTRESIDENTPROGRAMSNVPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 5741

PFNGLTRACKMATRIXNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 5742

PFNGLVERTEXATTRIBPOINTERNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLint, GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5743

PFNGLVERTEXATTRIB1DNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLdouble) # /usr/include/SDL/SDL_opengl.h: 5744

PFNGLVERTEXATTRIB1DVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5745

PFNGLVERTEXATTRIB1FNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5746

PFNGLVERTEXATTRIB1FVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5747

PFNGLVERTEXATTRIB1SNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLshort) # /usr/include/SDL/SDL_opengl.h: 5748

PFNGLVERTEXATTRIB1SVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5749

PFNGLVERTEXATTRIB2DNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 5750

PFNGLVERTEXATTRIB2DVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5751

PFNGLVERTEXATTRIB2FNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5752

PFNGLVERTEXATTRIB2FVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5753

PFNGLVERTEXATTRIB2SNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 5754

PFNGLVERTEXATTRIB2SVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5755

PFNGLVERTEXATTRIB3DNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 5756

PFNGLVERTEXATTRIB3DVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5757

PFNGLVERTEXATTRIB3FNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5758

PFNGLVERTEXATTRIB3FVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5759

PFNGLVERTEXATTRIB3SNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 5760

PFNGLVERTEXATTRIB3SVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5761

PFNGLVERTEXATTRIB4DNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLdouble, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 5762

PFNGLVERTEXATTRIB4DVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5763

PFNGLVERTEXATTRIB4FNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5764

PFNGLVERTEXATTRIB4FVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5765

PFNGLVERTEXATTRIB4SNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLshort, GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 5766

PFNGLVERTEXATTRIB4SVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5767

PFNGLVERTEXATTRIB4UBNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLubyte, GLubyte, GLubyte, GLubyte) # /usr/include/SDL/SDL_opengl.h: 5768

PFNGLVERTEXATTRIB4UBVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 5769

PFNGLVERTEXATTRIBS1DVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5770

PFNGLVERTEXATTRIBS1FVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5771

PFNGLVERTEXATTRIBS1SVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5772

PFNGLVERTEXATTRIBS2DVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5773

PFNGLVERTEXATTRIBS2FVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5774

PFNGLVERTEXATTRIBS2SVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5775

PFNGLVERTEXATTRIBS3DVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5776

PFNGLVERTEXATTRIBS3FVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5777

PFNGLVERTEXATTRIBS3SVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5778

PFNGLVERTEXATTRIBS4DVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5779

PFNGLVERTEXATTRIBS4FVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5780

PFNGLVERTEXATTRIBS4SVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5781

PFNGLVERTEXATTRIBS4UBVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 5782

PFNGLTEXBUMPPARAMETERIVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5817

PFNGLTEXBUMPPARAMETERFVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5818

PFNGLGETTEXBUMPPARAMETERIVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5819

PFNGLGETTEXBUMPPARAMETERFVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5820

PFNGLGENFRAGMENTSHADERSATIPROC = CFUNCTYPE(UNCHECKED(GLuint), GLuint) # /usr/include/SDL/SDL_opengl.h: 5841

PFNGLBINDFRAGMENTSHADERATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 5842

PFNGLDELETEFRAGMENTSHADERATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 5843

PFNGLBEGINFRAGMENTSHADERATIPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 5844

PFNGLENDFRAGMENTSHADERATIPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 5845

PFNGLPASSTEXCOORDATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint, GLenum) # /usr/include/SDL/SDL_opengl.h: 5846

PFNGLSAMPLEMAPATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint, GLenum) # /usr/include/SDL/SDL_opengl.h: 5847

PFNGLCOLORFRAGMENTOP1ATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5848

PFNGLCOLORFRAGMENTOP2ATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5849

PFNGLCOLORFRAGMENTOP3ATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5850

PFNGLALPHAFRAGMENTOP1ATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, GLuint, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5851

PFNGLALPHAFRAGMENTOP2ATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5852

PFNGLALPHAFRAGMENTOP3ATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5853

PFNGLSETFRAGMENTSHADERCONSTANTATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5854

PFNGLPNTRIANGLESIATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 5863

PFNGLPNTRIANGLESFATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 5864

PFNGLNEWOBJECTBUFFERATIPROC = CFUNCTYPE(UNCHECKED(GLuint), GLsizei, POINTER(GLvoid), GLenum) # /usr/include/SDL/SDL_opengl.h: 5883

PFNGLISOBJECTBUFFERATIPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 5884

PFNGLUPDATEOBJECTBUFFERATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint, GLsizei, POINTER(GLvoid), GLenum) # /usr/include/SDL/SDL_opengl.h: 5885

PFNGLGETOBJECTBUFFERFVATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5886

PFNGLGETOBJECTBUFFERIVATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5887

PFNGLFREEOBJECTBUFFERATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 5888

PFNGLARRAYOBJECTATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLenum, GLsizei, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5889

PFNGLGETARRAYOBJECTFVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5890

PFNGLGETARRAYOBJECTIVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5891

PFNGLVARIANTARRAYOBJECTATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, GLsizei, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5892

PFNGLGETVARIANTARRAYOBJECTFVATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5893

PFNGLGETVARIANTARRAYOBJECTIVATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5894

PFNGLBEGINVERTEXSHADEREXTPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 5943

PFNGLENDVERTEXSHADEREXTPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 5944

PFNGLBINDVERTEXSHADEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 5945

PFNGLGENVERTEXSHADERSEXTPROC = CFUNCTYPE(UNCHECKED(GLuint), GLuint) # /usr/include/SDL/SDL_opengl.h: 5946

PFNGLDELETEVERTEXSHADEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 5947

PFNGLSHADEROP1EXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5948

PFNGLSHADEROP2EXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5949

PFNGLSHADEROP3EXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5950

PFNGLSWIZZLEEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint, GLenum, GLenum, GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 5951

PFNGLWRITEMASKEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint, GLenum, GLenum, GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 5952

PFNGLINSERTCOMPONENTEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5953

PFNGLEXTRACTCOMPONENTEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 5954

PFNGLGENSYMBOLSEXTPROC = CFUNCTYPE(UNCHECKED(GLuint), GLenum, GLenum, GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 5955

PFNGLSETINVARIANTEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5956

PFNGLSETLOCALCONSTANTEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5957

PFNGLVARIANTBVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLbyte)) # /usr/include/SDL/SDL_opengl.h: 5958

PFNGLVARIANTSVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 5959

PFNGLVARIANTIVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5960

PFNGLVARIANTFVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5961

PFNGLVARIANTDVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 5962

PFNGLVARIANTUBVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLubyte)) # /usr/include/SDL/SDL_opengl.h: 5963

PFNGLVARIANTUSVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLushort)) # /usr/include/SDL/SDL_opengl.h: 5964

PFNGLVARIANTUIVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 5965

PFNGLVARIANTPOINTEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, GLuint, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 5966

PFNGLENABLEVARIANTCLIENTSTATEEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 5967

PFNGLDISABLEVARIANTCLIENTSTATEEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 5968

PFNGLBINDLIGHTPARAMETEREXTPROC = CFUNCTYPE(UNCHECKED(GLuint), GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 5969

PFNGLBINDMATERIALPARAMETEREXTPROC = CFUNCTYPE(UNCHECKED(GLuint), GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 5970

PFNGLBINDTEXGENPARAMETEREXTPROC = CFUNCTYPE(UNCHECKED(GLuint), GLenum, GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 5971

PFNGLBINDTEXTUREUNITPARAMETEREXTPROC = CFUNCTYPE(UNCHECKED(GLuint), GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 5972

PFNGLBINDPARAMETEREXTPROC = CFUNCTYPE(UNCHECKED(GLuint), GLenum) # /usr/include/SDL/SDL_opengl.h: 5973

PFNGLISVARIANTENABLEDEXTPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint, GLenum) # /usr/include/SDL/SDL_opengl.h: 5974

PFNGLGETVARIANTBOOLEANVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLboolean)) # /usr/include/SDL/SDL_opengl.h: 5975

PFNGLGETVARIANTINTEGERVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5976

PFNGLGETVARIANTFLOATVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5977

PFNGLGETVARIANTPOINTERVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(POINTER(GLvoid))) # /usr/include/SDL/SDL_opengl.h: 5978

PFNGLGETINVARIANTBOOLEANVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLboolean)) # /usr/include/SDL/SDL_opengl.h: 5979

PFNGLGETINVARIANTINTEGERVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5980

PFNGLGETINVARIANTFLOATVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5981

PFNGLGETLOCALCONSTANTBOOLEANVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLboolean)) # /usr/include/SDL/SDL_opengl.h: 5982

PFNGLGETLOCALCONSTANTINTEGERVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 5983

PFNGLGETLOCALCONSTANTFLOATVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 5984

PFNGLVERTEXSTREAM1SATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLshort) # /usr/include/SDL/SDL_opengl.h: 6036

PFNGLVERTEXSTREAM1SVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 6037

PFNGLVERTEXSTREAM1IATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 6038

PFNGLVERTEXSTREAM1IVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 6039

PFNGLVERTEXSTREAM1FATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 6040

PFNGLVERTEXSTREAM1FVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 6041

PFNGLVERTEXSTREAM1DATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLdouble) # /usr/include/SDL/SDL_opengl.h: 6042

PFNGLVERTEXSTREAM1DVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 6043

PFNGLVERTEXSTREAM2SATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 6044

PFNGLVERTEXSTREAM2SVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 6045

PFNGLVERTEXSTREAM2IATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 6046

PFNGLVERTEXSTREAM2IVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 6047

PFNGLVERTEXSTREAM2FATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 6048

PFNGLVERTEXSTREAM2FVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 6049

PFNGLVERTEXSTREAM2DATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 6050

PFNGLVERTEXSTREAM2DVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 6051

PFNGLVERTEXSTREAM3SATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 6052

PFNGLVERTEXSTREAM3SVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 6053

PFNGLVERTEXSTREAM3IATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 6054

PFNGLVERTEXSTREAM3IVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 6055

PFNGLVERTEXSTREAM3FATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 6056

PFNGLVERTEXSTREAM3FVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 6057

PFNGLVERTEXSTREAM3DATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 6058

PFNGLVERTEXSTREAM3DVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 6059

PFNGLVERTEXSTREAM4SATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLshort, GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 6060

PFNGLVERTEXSTREAM4SVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 6061

PFNGLVERTEXSTREAM4IATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 6062

PFNGLVERTEXSTREAM4IVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 6063

PFNGLVERTEXSTREAM4FATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 6064

PFNGLVERTEXSTREAM4FVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 6065

PFNGLVERTEXSTREAM4DATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLdouble, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 6066

PFNGLVERTEXSTREAM4DVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 6067

PFNGLNORMALSTREAM3BATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLbyte, GLbyte, GLbyte) # /usr/include/SDL/SDL_opengl.h: 6068

PFNGLNORMALSTREAM3BVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLbyte)) # /usr/include/SDL/SDL_opengl.h: 6069

PFNGLNORMALSTREAM3SATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLshort, GLshort, GLshort) # /usr/include/SDL/SDL_opengl.h: 6070

PFNGLNORMALSTREAM3SVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLshort)) # /usr/include/SDL/SDL_opengl.h: 6071

PFNGLNORMALSTREAM3IATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 6072

PFNGLNORMALSTREAM3IVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 6073

PFNGLNORMALSTREAM3FATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 6074

PFNGLNORMALSTREAM3FVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 6075

PFNGLNORMALSTREAM3DATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 6076

PFNGLNORMALSTREAM3DVATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 6077

PFNGLCLIENTACTIVEVERTEXSTREAMATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 6078

PFNGLVERTEXBLENDENVIATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 6079

PFNGLVERTEXBLENDENVFATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLfloat) # /usr/include/SDL/SDL_opengl.h: 6080

PFNGLELEMENTPOINTERATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 6090

PFNGLDRAWELEMENTARRAYATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei) # /usr/include/SDL/SDL_opengl.h: 6091

PFNGLDRAWRANGEELEMENTARRAYATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, GLsizei) # /usr/include/SDL/SDL_opengl.h: 6092

PFNGLDRAWMESHARRAYSSUNPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLsizei, GLsizei) # /usr/include/SDL/SDL_opengl.h: 6100

PFNGLGENOCCLUSIONQUERIESNVPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 6126

PFNGLDELETEOCCLUSIONQUERIESNVPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 6127

PFNGLISOCCLUSIONQUERYNVPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 6128

PFNGLBEGINOCCLUSIONQUERYNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 6129

PFNGLENDOCCLUSIONQUERYNVPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 6130

PFNGLGETOCCLUSIONQUERYIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 6131

PFNGLGETOCCLUSIONQUERYUIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 6132

PFNGLPOINTPARAMETERINVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 6141

PFNGLPOINTPARAMETERIVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 6142

PFNGLACTIVESTENCILFACEEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 6162

PFNGLELEMENTPOINTERAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 6182

PFNGLDRAWELEMENTARRAYAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint, GLsizei) # /usr/include/SDL/SDL_opengl.h: 6183

PFNGLDRAWRANGEELEMENTARRAYAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, GLint, GLsizei) # /usr/include/SDL/SDL_opengl.h: 6184

PFNGLMULTIDRAWELEMENTARRAYAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLint), POINTER(GLsizei), GLsizei) # /usr/include/SDL/SDL_opengl.h: 6185

PFNGLMULTIDRAWRANGEELEMENTARRAYAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint, GLuint, POINTER(GLint), POINTER(GLsizei), GLsizei) # /usr/include/SDL/SDL_opengl.h: 6186

PFNGLGENFENCESAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 6201

PFNGLDELETEFENCESAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 6202

PFNGLSETFENCEAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 6203

PFNGLISFENCEAPPLEPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 6204

PFNGLTESTFENCEAPPLEPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 6205

PFNGLFINISHFENCEAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 6206

PFNGLTESTOBJECTAPPLEPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 6207

PFNGLFINISHOBJECTAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 6208

PFNGLBINDVERTEXARRAYAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 6219

PFNGLDELETEVERTEXARRAYSAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 6220

PFNGLGENVERTEXARRAYSAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 6221

PFNGLISVERTEXARRAYAPPLEPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 6222

PFNGLVERTEXARRAYRANGEAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 6232

PFNGLFLUSHVERTEXARRAYRANGEAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 6233

PFNGLVERTEXARRAYPARAMETERIAPPLEPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLint) # /usr/include/SDL/SDL_opengl.h: 6234

PFNGLDRAWBUFFERSATIPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLenum)) # /usr/include/SDL/SDL_opengl.h: 6250

PFNGLPROGRAMNAMEDPARAMETER4FNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLubyte), GLfloat, GLfloat, GLfloat, GLfloat) # /usr/include/SDL/SDL_opengl.h: 6283

PFNGLPROGRAMNAMEDPARAMETER4DNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLubyte), GLdouble, GLdouble, GLdouble, GLdouble) # /usr/include/SDL/SDL_opengl.h: 6284

PFNGLPROGRAMNAMEDPARAMETER4FVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLubyte), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 6285

PFNGLPROGRAMNAMEDPARAMETER4DVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLubyte), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 6286

PFNGLGETPROGRAMNAMEDPARAMETERFVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLubyte), POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 6287

PFNGLGETPROGRAMNAMEDPARAMETERDVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLubyte), POINTER(GLdouble)) # /usr/include/SDL/SDL_opengl.h: 6288

PFNGLVERTEX2HNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6341

PFNGLVERTEX2HVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6342

PFNGLVERTEX3HNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6343

PFNGLVERTEX3HVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6344

PFNGLVERTEX4HNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV, GLhalfNV, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6345

PFNGLVERTEX4HVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6346

PFNGLNORMAL3HNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6347

PFNGLNORMAL3HVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6348

PFNGLCOLOR3HNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6349

PFNGLCOLOR3HVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6350

PFNGLCOLOR4HNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV, GLhalfNV, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6351

PFNGLCOLOR4HVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6352

PFNGLTEXCOORD1HNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6353

PFNGLTEXCOORD1HVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6354

PFNGLTEXCOORD2HNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6355

PFNGLTEXCOORD2HVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6356

PFNGLTEXCOORD3HNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6357

PFNGLTEXCOORD3HVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6358

PFNGLTEXCOORD4HNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV, GLhalfNV, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6359

PFNGLTEXCOORD4HVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6360

PFNGLMULTITEXCOORD1HNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6361

PFNGLMULTITEXCOORD1HVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6362

PFNGLMULTITEXCOORD2HNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6363

PFNGLMULTITEXCOORD2HVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6364

PFNGLMULTITEXCOORD3HNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLhalfNV, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6365

PFNGLMULTITEXCOORD3HVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6366

PFNGLMULTITEXCOORD4HNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLhalfNV, GLhalfNV, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6367

PFNGLMULTITEXCOORD4HVNVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6368

PFNGLFOGCOORDHNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6369

PFNGLFOGCOORDHVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6370

PFNGLSECONDARYCOLOR3HNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6371

PFNGLSECONDARYCOLOR3HVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6372

PFNGLVERTEXWEIGHTHNVPROC = CFUNCTYPE(UNCHECKED(None), GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6373

PFNGLVERTEXWEIGHTHVNVPROC = CFUNCTYPE(UNCHECKED(None), POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6374

PFNGLVERTEXATTRIB1HNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6375

PFNGLVERTEXATTRIB1HVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6376

PFNGLVERTEXATTRIB2HNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6377

PFNGLVERTEXATTRIB2HVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6378

PFNGLVERTEXATTRIB3HNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLhalfNV, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6379

PFNGLVERTEXATTRIB3HVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6380

PFNGLVERTEXATTRIB4HNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLhalfNV, GLhalfNV, GLhalfNV, GLhalfNV) # /usr/include/SDL/SDL_opengl.h: 6381

PFNGLVERTEXATTRIB4HVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6382

PFNGLVERTEXATTRIBS1HVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6383

PFNGLVERTEXATTRIBS2HVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6384

PFNGLVERTEXATTRIBS3HVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6385

PFNGLVERTEXATTRIBS4HVNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLsizei, POINTER(GLhalfNV)) # /usr/include/SDL/SDL_opengl.h: 6386

PFNGLPIXELDATARANGENVPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 6395

PFNGLFLUSHPIXELDATARANGENVPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 6396

PFNGLPRIMITIVERESTARTNVPROC = CFUNCTYPE(UNCHECKED(None), ) # /usr/include/SDL/SDL_opengl.h: 6405

PFNGLPRIMITIVERESTARTINDEXNVPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 6406

PFNGLMAPOBJECTBUFFERATIPROC = CFUNCTYPE(UNCHECKED(POINTER(GLvoid)), GLuint) # /usr/include/SDL/SDL_opengl.h: 6423

PFNGLUNMAPOBJECTBUFFERATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint) # /usr/include/SDL/SDL_opengl.h: 6424

PFNGLSTENCILOPSEPARATEATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 6433

PFNGLSTENCILFUNCSEPARATEATIPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLint, GLuint) # /usr/include/SDL/SDL_opengl.h: 6434

PFNGLVERTEXATTRIBARRAYOBJECTATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLint, GLenum, GLboolean, GLsizei, GLuint, GLuint) # /usr/include/SDL/SDL_opengl.h: 6444

PFNGLGETVERTEXATTRIBARRAYOBJECTFVATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLfloat)) # /usr/include/SDL/SDL_opengl.h: 6445

PFNGLGETVERTEXATTRIBARRAYOBJECTIVATIPROC = CFUNCTYPE(UNCHECKED(None), GLuint, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 6446

PFNGLDEPTHBOUNDSEXTPROC = CFUNCTYPE(UNCHECKED(None), GLclampd, GLclampd) # /usr/include/SDL/SDL_opengl.h: 6458

PFNGLBLENDEQUATIONSEPARATEEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum) # /usr/include/SDL/SDL_opengl.h: 6470

PFNGLISRENDERBUFFEREXTPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 6522

PFNGLBINDRENDERBUFFEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 6523

PFNGLDELETERENDERBUFFERSEXTPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 6524

PFNGLGENRENDERBUFFERSEXTPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 6525

PFNGLRENDERBUFFERSTORAGEEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLsizei, GLsizei) # /usr/include/SDL/SDL_opengl.h: 6526

PFNGLGETRENDERBUFFERPARAMETERIVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 6527

PFNGLISFRAMEBUFFEREXTPROC = CFUNCTYPE(UNCHECKED(GLboolean), GLuint) # /usr/include/SDL/SDL_opengl.h: 6528

PFNGLBINDFRAMEBUFFEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 6529

PFNGLDELETEFRAMEBUFFERSEXTPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 6530

PFNGLGENFRAMEBUFFERSEXTPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLuint)) # /usr/include/SDL/SDL_opengl.h: 6531

PFNGLCHECKFRAMEBUFFERSTATUSEXTPROC = CFUNCTYPE(UNCHECKED(GLenum), GLenum) # /usr/include/SDL/SDL_opengl.h: 6532

PFNGLFRAMEBUFFERTEXTURE1DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLuint, GLint) # /usr/include/SDL/SDL_opengl.h: 6533

PFNGLFRAMEBUFFERTEXTURE2DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLuint, GLint) # /usr/include/SDL/SDL_opengl.h: 6534

PFNGLFRAMEBUFFERTEXTURE3DEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLuint, GLint, GLint) # /usr/include/SDL/SDL_opengl.h: 6535

PFNGLFRAMEBUFFERRENDERBUFFEREXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, GLuint) # /usr/include/SDL/SDL_opengl.h: 6536

PFNGLGETFRAMEBUFFERATTACHMENTPARAMETERIVEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum, GLenum, GLenum, POINTER(GLint)) # /usr/include/SDL/SDL_opengl.h: 6537

PFNGLGENERATEMIPMAPEXTPROC = CFUNCTYPE(UNCHECKED(None), GLenum) # /usr/include/SDL/SDL_opengl.h: 6538

PFNGLSTRINGMARKERGREMEDYPROC = CFUNCTYPE(UNCHECKED(None), GLsizei, POINTER(GLvoid)) # /usr/include/SDL/SDL_opengl.h: 6546

# /usr/include/SDL/SDL_rotozoom.h: 59
if hasattr(_libs['SDL_gfx'], 'rotozoomSurface'):
    rotozoomSurface = _libs['SDL_gfx'].rotozoomSurface
    rotozoomSurface.argtypes = [POINTER(SDL_Surface), c_double, c_double, c_int]
    rotozoomSurface.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_rotozoom.h: 61
if hasattr(_libs['SDL_gfx'], 'rotozoomSurfaceXY'):
    rotozoomSurfaceXY = _libs['SDL_gfx'].rotozoomSurfaceXY
    rotozoomSurfaceXY.argtypes = [POINTER(SDL_Surface), c_double, c_double, c_double, c_int]
    rotozoomSurfaceXY.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_rotozoom.h: 65
if hasattr(_libs['SDL_gfx'], 'rotozoomSurfaceSize'):
    rotozoomSurfaceSize = _libs['SDL_gfx'].rotozoomSurfaceSize
    rotozoomSurfaceSize.argtypes = [c_int, c_int, c_double, c_double, POINTER(c_int), POINTER(c_int)]
    rotozoomSurfaceSize.restype = None

# /usr/include/SDL/SDL_rotozoom.h: 68
if hasattr(_libs['SDL_gfx'], 'rotozoomSurfaceSizeXY'):
    rotozoomSurfaceSizeXY = _libs['SDL_gfx'].rotozoomSurfaceSizeXY
    rotozoomSurfaceSizeXY.argtypes = [c_int, c_int, c_double, c_double, c_double, POINTER(c_int), POINTER(c_int)]
    rotozoomSurfaceSizeXY.restype = None

# /usr/include/SDL/SDL_rotozoom.h: 78
if hasattr(_libs['SDL_gfx'], 'zoomSurface'):
    zoomSurface = _libs['SDL_gfx'].zoomSurface
    zoomSurface.argtypes = [POINTER(SDL_Surface), c_double, c_double, c_int]
    zoomSurface.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_rotozoom.h: 80
if hasattr(_libs['SDL_gfx'], 'zoomSurfaceSize'):
    zoomSurfaceSize = _libs['SDL_gfx'].zoomSurfaceSize
    zoomSurfaceSize.argtypes = [c_int, c_int, c_double, c_double, POINTER(c_int), POINTER(c_int)]
    zoomSurfaceSize.restype = None

# /usr/include/SDL/SDL_rotozoom.h: 88
if hasattr(_libs['SDL_gfx'], 'shrinkSurface'):
    shrinkSurface = _libs['SDL_gfx'].shrinkSurface
    shrinkSurface.argtypes = [POINTER(SDL_Surface), c_int, c_int]
    shrinkSurface.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_rotozoom.h: 96
if hasattr(_libs['SDL_gfx'], 'rotateSurface90Degrees'):
    rotateSurface90Degrees = _libs['SDL_gfx'].rotateSurface90Degrees
    rotateSurface90Degrees.argtypes = [POINTER(SDL_Surface), c_int]
    rotateSurface90Degrees.restype = POINTER(SDL_Surface)

XID = c_ulong # /usr/include/X11/X.h: 66

Atom = c_ulong # /usr/include/X11/X.h: 74

Time = c_ulong # /usr/include/X11/X.h: 77

Window = XID # /usr/include/X11/X.h: 96

Drawable = XID # /usr/include/X11/X.h: 97

Colormap = XID # /usr/include/X11/X.h: 104

# /usr/include/X11/Xlib.h: 266
class struct__XDisplay(Structure):
    pass

Display = struct__XDisplay # /usr/include/X11/Xlib.h: 498

# /usr/include/X11/Xlib.h: 582
class struct_anon_78(Structure):
    pass

struct_anon_78.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'root',
    'subwindow',
    'time',
    'x',
    'y',
    'x_root',
    'y_root',
    'state',
    'keycode',
    'same_screen',
]
struct_anon_78._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('root', Window),
    ('subwindow', Window),
    ('time', Time),
    ('x', c_int),
    ('y', c_int),
    ('x_root', c_int),
    ('y_root', c_int),
    ('state', c_uint),
    ('keycode', c_uint),
    ('same_screen', c_int),
]

XKeyEvent = struct_anon_78 # /usr/include/X11/Xlib.h: 582

# /usr/include/X11/Xlib.h: 600
class struct_anon_79(Structure):
    pass

struct_anon_79.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'root',
    'subwindow',
    'time',
    'x',
    'y',
    'x_root',
    'y_root',
    'state',
    'button',
    'same_screen',
]
struct_anon_79._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('root', Window),
    ('subwindow', Window),
    ('time', Time),
    ('x', c_int),
    ('y', c_int),
    ('x_root', c_int),
    ('y_root', c_int),
    ('state', c_uint),
    ('button', c_uint),
    ('same_screen', c_int),
]

XButtonEvent = struct_anon_79 # /usr/include/X11/Xlib.h: 600

# /usr/include/X11/Xlib.h: 618
class struct_anon_80(Structure):
    pass

struct_anon_80.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'root',
    'subwindow',
    'time',
    'x',
    'y',
    'x_root',
    'y_root',
    'state',
    'is_hint',
    'same_screen',
]
struct_anon_80._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('root', Window),
    ('subwindow', Window),
    ('time', Time),
    ('x', c_int),
    ('y', c_int),
    ('x_root', c_int),
    ('y_root', c_int),
    ('state', c_uint),
    ('is_hint', c_char),
    ('same_screen', c_int),
]

XMotionEvent = struct_anon_80 # /usr/include/X11/Xlib.h: 618

# /usr/include/X11/Xlib.h: 641
class struct_anon_81(Structure):
    pass

struct_anon_81.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'root',
    'subwindow',
    'time',
    'x',
    'y',
    'x_root',
    'y_root',
    'mode',
    'detail',
    'same_screen',
    'focus',
    'state',
]
struct_anon_81._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('root', Window),
    ('subwindow', Window),
    ('time', Time),
    ('x', c_int),
    ('y', c_int),
    ('x_root', c_int),
    ('y_root', c_int),
    ('mode', c_int),
    ('detail', c_int),
    ('same_screen', c_int),
    ('focus', c_int),
    ('state', c_uint),
]

XCrossingEvent = struct_anon_81 # /usr/include/X11/Xlib.h: 641

# /usr/include/X11/Xlib.h: 659
class struct_anon_82(Structure):
    pass

struct_anon_82.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'mode',
    'detail',
]
struct_anon_82._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('mode', c_int),
    ('detail', c_int),
]

XFocusChangeEvent = struct_anon_82 # /usr/include/X11/Xlib.h: 659

# /usr/include/X11/Xlib.h: 671
class struct_anon_83(Structure):
    pass

struct_anon_83.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'key_vector',
]
struct_anon_83._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('key_vector', c_char * 32),
]

XKeymapEvent = struct_anon_83 # /usr/include/X11/Xlib.h: 671

# /usr/include/X11/Xlib.h: 682
class struct_anon_84(Structure):
    pass

struct_anon_84.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'x',
    'y',
    'width',
    'height',
    'count',
]
struct_anon_84._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
    ('count', c_int),
]

XExposeEvent = struct_anon_84 # /usr/include/X11/Xlib.h: 682

# /usr/include/X11/Xlib.h: 695
class struct_anon_85(Structure):
    pass

struct_anon_85.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'drawable',
    'x',
    'y',
    'width',
    'height',
    'count',
    'major_code',
    'minor_code',
]
struct_anon_85._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('drawable', Drawable),
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
    ('count', c_int),
    ('major_code', c_int),
    ('minor_code', c_int),
]

XGraphicsExposeEvent = struct_anon_85 # /usr/include/X11/Xlib.h: 695

# /usr/include/X11/Xlib.h: 705
class struct_anon_86(Structure):
    pass

struct_anon_86.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'drawable',
    'major_code',
    'minor_code',
]
struct_anon_86._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('drawable', Drawable),
    ('major_code', c_int),
    ('minor_code', c_int),
]

XNoExposeEvent = struct_anon_86 # /usr/include/X11/Xlib.h: 705

# /usr/include/X11/Xlib.h: 714
class struct_anon_87(Structure):
    pass

struct_anon_87.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'state',
]
struct_anon_87._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('state', c_int),
]

XVisibilityEvent = struct_anon_87 # /usr/include/X11/Xlib.h: 714

# /usr/include/X11/Xlib.h: 727
class struct_anon_88(Structure):
    pass

struct_anon_88.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'parent',
    'window',
    'x',
    'y',
    'width',
    'height',
    'border_width',
    'override_redirect',
]
struct_anon_88._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('parent', Window),
    ('window', Window),
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
    ('border_width', c_int),
    ('override_redirect', c_int),
]

XCreateWindowEvent = struct_anon_88 # /usr/include/X11/Xlib.h: 727

# /usr/include/X11/Xlib.h: 736
class struct_anon_89(Structure):
    pass

struct_anon_89.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'event',
    'window',
]
struct_anon_89._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('event', Window),
    ('window', Window),
]

XDestroyWindowEvent = struct_anon_89 # /usr/include/X11/Xlib.h: 736

# /usr/include/X11/Xlib.h: 746
class struct_anon_90(Structure):
    pass

struct_anon_90.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'event',
    'window',
    'from_configure',
]
struct_anon_90._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('event', Window),
    ('window', Window),
    ('from_configure', c_int),
]

XUnmapEvent = struct_anon_90 # /usr/include/X11/Xlib.h: 746

# /usr/include/X11/Xlib.h: 756
class struct_anon_91(Structure):
    pass

struct_anon_91.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'event',
    'window',
    'override_redirect',
]
struct_anon_91._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('event', Window),
    ('window', Window),
    ('override_redirect', c_int),
]

XMapEvent = struct_anon_91 # /usr/include/X11/Xlib.h: 756

# /usr/include/X11/Xlib.h: 765
class struct_anon_92(Structure):
    pass

struct_anon_92.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'parent',
    'window',
]
struct_anon_92._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('parent', Window),
    ('window', Window),
]

XMapRequestEvent = struct_anon_92 # /usr/include/X11/Xlib.h: 765

# /usr/include/X11/Xlib.h: 777
class struct_anon_93(Structure):
    pass

struct_anon_93.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'event',
    'window',
    'parent',
    'x',
    'y',
    'override_redirect',
]
struct_anon_93._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('event', Window),
    ('window', Window),
    ('parent', Window),
    ('x', c_int),
    ('y', c_int),
    ('override_redirect', c_int),
]

XReparentEvent = struct_anon_93 # /usr/include/X11/Xlib.h: 777

# /usr/include/X11/Xlib.h: 791
class struct_anon_94(Structure):
    pass

struct_anon_94.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'event',
    'window',
    'x',
    'y',
    'width',
    'height',
    'border_width',
    'above',
    'override_redirect',
]
struct_anon_94._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('event', Window),
    ('window', Window),
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
    ('border_width', c_int),
    ('above', Window),
    ('override_redirect', c_int),
]

XConfigureEvent = struct_anon_94 # /usr/include/X11/Xlib.h: 791

# /usr/include/X11/Xlib.h: 801
class struct_anon_95(Structure):
    pass

struct_anon_95.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'event',
    'window',
    'x',
    'y',
]
struct_anon_95._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('event', Window),
    ('window', Window),
    ('x', c_int),
    ('y', c_int),
]

XGravityEvent = struct_anon_95 # /usr/include/X11/Xlib.h: 801

# /usr/include/X11/Xlib.h: 810
class struct_anon_96(Structure):
    pass

struct_anon_96.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'width',
    'height',
]
struct_anon_96._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('width', c_int),
    ('height', c_int),
]

XResizeRequestEvent = struct_anon_96 # /usr/include/X11/Xlib.h: 810

# /usr/include/X11/Xlib.h: 825
class struct_anon_97(Structure):
    pass

struct_anon_97.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'parent',
    'window',
    'x',
    'y',
    'width',
    'height',
    'border_width',
    'above',
    'detail',
    'value_mask',
]
struct_anon_97._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('parent', Window),
    ('window', Window),
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
    ('border_width', c_int),
    ('above', Window),
    ('detail', c_int),
    ('value_mask', c_ulong),
]

XConfigureRequestEvent = struct_anon_97 # /usr/include/X11/Xlib.h: 825

# /usr/include/X11/Xlib.h: 835
class struct_anon_98(Structure):
    pass

struct_anon_98.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'event',
    'window',
    'place',
]
struct_anon_98._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('event', Window),
    ('window', Window),
    ('place', c_int),
]

XCirculateEvent = struct_anon_98 # /usr/include/X11/Xlib.h: 835

# /usr/include/X11/Xlib.h: 845
class struct_anon_99(Structure):
    pass

struct_anon_99.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'parent',
    'window',
    'place',
]
struct_anon_99._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('parent', Window),
    ('window', Window),
    ('place', c_int),
]

XCirculateRequestEvent = struct_anon_99 # /usr/include/X11/Xlib.h: 845

# /usr/include/X11/Xlib.h: 856
class struct_anon_100(Structure):
    pass

struct_anon_100.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'atom',
    'time',
    'state',
]
struct_anon_100._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('atom', Atom),
    ('time', Time),
    ('state', c_int),
]

XPropertyEvent = struct_anon_100 # /usr/include/X11/Xlib.h: 856

# /usr/include/X11/Xlib.h: 866
class struct_anon_101(Structure):
    pass

struct_anon_101.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'selection',
    'time',
]
struct_anon_101._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('selection', Atom),
    ('time', Time),
]

XSelectionClearEvent = struct_anon_101 # /usr/include/X11/Xlib.h: 866

# /usr/include/X11/Xlib.h: 879
class struct_anon_102(Structure):
    pass

struct_anon_102.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'owner',
    'requestor',
    'selection',
    'target',
    'property',
    'time',
]
struct_anon_102._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('owner', Window),
    ('requestor', Window),
    ('selection', Atom),
    ('target', Atom),
    ('property', Atom),
    ('time', Time),
]

XSelectionRequestEvent = struct_anon_102 # /usr/include/X11/Xlib.h: 879

# /usr/include/X11/Xlib.h: 891
class struct_anon_103(Structure):
    pass

struct_anon_103.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'requestor',
    'selection',
    'target',
    'property',
    'time',
]
struct_anon_103._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('requestor', Window),
    ('selection', Atom),
    ('target', Atom),
    ('property', Atom),
    ('time', Time),
]

XSelectionEvent = struct_anon_103 # /usr/include/X11/Xlib.h: 891

# /usr/include/X11/Xlib.h: 906
class struct_anon_104(Structure):
    pass

struct_anon_104.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'colormap',
    'new',
    'state',
]
struct_anon_104._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('colormap', Colormap),
    ('new', c_int),
    ('state', c_int),
]

XColormapEvent = struct_anon_104 # /usr/include/X11/Xlib.h: 906

# /usr/include/X11/Xlib.h: 916
class union_anon_105(Union):
    pass

union_anon_105.__slots__ = [
    'b',
    's',
    'l',
]
union_anon_105._fields_ = [
    ('b', c_char * 20),
    ('s', c_short * 10),
    ('l', c_long * 5),
]

# /usr/include/X11/Xlib.h: 921
class struct_anon_106(Structure):
    pass

struct_anon_106.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'message_type',
    'format',
    'data',
]
struct_anon_106._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('message_type', Atom),
    ('format', c_int),
    ('data', union_anon_105),
]

XClientMessageEvent = struct_anon_106 # /usr/include/X11/Xlib.h: 921

# /usr/include/X11/Xlib.h: 933
class struct_anon_107(Structure):
    pass

struct_anon_107.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
    'request',
    'first_keycode',
    'count',
]
struct_anon_107._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
    ('request', c_int),
    ('first_keycode', c_int),
    ('count', c_int),
]

XMappingEvent = struct_anon_107 # /usr/include/X11/Xlib.h: 933

# /usr/include/X11/Xlib.h: 943
class struct_anon_108(Structure):
    pass

struct_anon_108.__slots__ = [
    'type',
    'display',
    'resourceid',
    'serial',
    'error_code',
    'request_code',
    'minor_code',
]
struct_anon_108._fields_ = [
    ('type', c_int),
    ('display', POINTER(Display)),
    ('resourceid', XID),
    ('serial', c_ulong),
    ('error_code', c_ubyte),
    ('request_code', c_ubyte),
    ('minor_code', c_ubyte),
]

XErrorEvent = struct_anon_108 # /usr/include/X11/Xlib.h: 943

# /usr/include/X11/Xlib.h: 951
class struct_anon_109(Structure):
    pass

struct_anon_109.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'window',
]
struct_anon_109._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('window', Window),
]

XAnyEvent = struct_anon_109 # /usr/include/X11/Xlib.h: 951

# /usr/include/X11/Xlib.h: 967
class struct_anon_110(Structure):
    pass

struct_anon_110.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'extension',
    'evtype',
]
struct_anon_110._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('extension', c_int),
    ('evtype', c_int),
]

XGenericEvent = struct_anon_110 # /usr/include/X11/Xlib.h: 967

# /usr/include/X11/Xlib.h: 978
class struct_anon_111(Structure):
    pass

struct_anon_111.__slots__ = [
    'type',
    'serial',
    'send_event',
    'display',
    'extension',
    'evtype',
    'cookie',
    'data',
]
struct_anon_111._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('extension', c_int),
    ('evtype', c_int),
    ('cookie', c_uint),
    ('data', POINTER(None)),
]

XGenericEventCookie = struct_anon_111 # /usr/include/X11/Xlib.h: 978

# /usr/include/X11/Xlib.h: 1020
class union__XEvent(Union):
    pass

union__XEvent.__slots__ = [
    'type',
    'xany',
    'xkey',
    'xbutton',
    'xmotion',
    'xcrossing',
    'xfocus',
    'xexpose',
    'xgraphicsexpose',
    'xnoexpose',
    'xvisibility',
    'xcreatewindow',
    'xdestroywindow',
    'xunmap',
    'xmap',
    'xmaprequest',
    'xreparent',
    'xconfigure',
    'xgravity',
    'xresizerequest',
    'xconfigurerequest',
    'xcirculate',
    'xcirculaterequest',
    'xproperty',
    'xselectionclear',
    'xselectionrequest',
    'xselection',
    'xcolormap',
    'xclient',
    'xmapping',
    'xerror',
    'xkeymap',
    'xgeneric',
    'xcookie',
    'pad',
]
union__XEvent._fields_ = [
    ('type', c_int),
    ('xany', XAnyEvent),
    ('xkey', XKeyEvent),
    ('xbutton', XButtonEvent),
    ('xmotion', XMotionEvent),
    ('xcrossing', XCrossingEvent),
    ('xfocus', XFocusChangeEvent),
    ('xexpose', XExposeEvent),
    ('xgraphicsexpose', XGraphicsExposeEvent),
    ('xnoexpose', XNoExposeEvent),
    ('xvisibility', XVisibilityEvent),
    ('xcreatewindow', XCreateWindowEvent),
    ('xdestroywindow', XDestroyWindowEvent),
    ('xunmap', XUnmapEvent),
    ('xmap', XMapEvent),
    ('xmaprequest', XMapRequestEvent),
    ('xreparent', XReparentEvent),
    ('xconfigure', XConfigureEvent),
    ('xgravity', XGravityEvent),
    ('xresizerequest', XResizeRequestEvent),
    ('xconfigurerequest', XConfigureRequestEvent),
    ('xcirculate', XCirculateEvent),
    ('xcirculaterequest', XCirculateRequestEvent),
    ('xproperty', XPropertyEvent),
    ('xselectionclear', XSelectionClearEvent),
    ('xselectionrequest', XSelectionRequestEvent),
    ('xselection', XSelectionEvent),
    ('xcolormap', XColormapEvent),
    ('xclient', XClientMessageEvent),
    ('xmapping', XMappingEvent),
    ('xerror', XErrorEvent),
    ('xkeymap', XKeymapEvent),
    ('xgeneric', XGenericEvent),
    ('xcookie', XGenericEventCookie),
    ('pad', c_long * 24),
]

XEvent = union__XEvent # /usr/include/X11/Xlib.h: 1020

enum_anon_136 = c_int # /usr/include/SDL/SDL_syswm.h: 69

SDL_SYSWM_X11 = 0 # /usr/include/SDL/SDL_syswm.h: 69

SDL_SYSWM_TYPE = enum_anon_136 # /usr/include/SDL/SDL_syswm.h: 69

# /usr/include/SDL/SDL_syswm.h: 75
class union_anon_137(Union):
    pass

union_anon_137.__slots__ = [
    'xevent',
]
union_anon_137._fields_ = [
    ('xevent', XEvent),
]

struct_SDL_SysWMmsg.__slots__ = [
    'version',
    'subsystem',
    'event',
]
struct_SDL_SysWMmsg._fields_ = [
    ('version', SDL_version),
    ('subsystem', SDL_SYSWM_TYPE),
    ('event', union_anon_137),
]

# /usr/include/SDL/SDL_syswm.h: 88
class struct_anon_138(Structure):
    pass

struct_anon_138.__slots__ = [
    'display',
    'window',
    'lock_func',
    'unlock_func',
    'fswindow',
    'wmwindow',
    'gfxdisplay',
]
struct_anon_138._fields_ = [
    ('display', POINTER(Display)),
    ('window', Window),
    ('lock_func', CFUNCTYPE(UNCHECKED(None), )),
    ('unlock_func', CFUNCTYPE(UNCHECKED(None), )),
    ('fswindow', Window),
    ('wmwindow', Window),
    ('gfxdisplay', POINTER(Display)),
]

# /usr/include/SDL/SDL_syswm.h: 87
class union_anon_139(Union):
    pass

union_anon_139.__slots__ = [
    'x11',
]
union_anon_139._fields_ = [
    ('x11', struct_anon_138),
]

# /usr/include/SDL/SDL_syswm.h: 114
class struct_SDL_SysWMinfo(Structure):
    pass

struct_SDL_SysWMinfo.__slots__ = [
    'version',
    'subsystem',
    'info',
]
struct_SDL_SysWMinfo._fields_ = [
    ('version', SDL_version),
    ('subsystem', SDL_SYSWM_TYPE),
    ('info', union_anon_139),
]

SDL_SysWMinfo = struct_SDL_SysWMinfo # /usr/include/SDL/SDL_syswm.h: 114

# /usr/include/SDL/SDL_syswm.h: 216
if hasattr(_libs['SDL'], 'SDL_GetWMInfo'):
    SDL_GetWMInfo = _libs['SDL'].SDL_GetWMInfo
    SDL_GetWMInfo.argtypes = [POINTER(SDL_SysWMinfo)]
    SDL_GetWMInfo.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 64
if hasattr(_libs['SDL_ttf'], 'TTF_Linked_Version'):
    TTF_Linked_Version = _libs['SDL_ttf'].TTF_Linked_Version
    TTF_Linked_Version.argtypes = []
    TTF_Linked_Version.restype = POINTER(SDL_version)

# /usr/include/SDL/SDL_ttf.h: 74
if hasattr(_libs['SDL_ttf'], 'TTF_ByteSwappedUNICODE'):
    TTF_ByteSwappedUNICODE = _libs['SDL_ttf'].TTF_ByteSwappedUNICODE
    TTF_ByteSwappedUNICODE.argtypes = [c_int]
    TTF_ByteSwappedUNICODE.restype = None

# /usr/include/SDL/SDL_ttf.h: 77
class struct__TTF_Font(Structure):
    pass

TTF_Font = struct__TTF_Font # /usr/include/SDL/SDL_ttf.h: 77

# /usr/include/SDL/SDL_ttf.h: 80
if hasattr(_libs['SDL_ttf'], 'TTF_Init'):
    TTF_Init = _libs['SDL_ttf'].TTF_Init
    TTF_Init.argtypes = []
    TTF_Init.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 86
if hasattr(_libs['SDL_ttf'], 'TTF_OpenFont'):
    TTF_OpenFont = _libs['SDL_ttf'].TTF_OpenFont
    TTF_OpenFont.argtypes = [String, c_int]
    TTF_OpenFont.restype = POINTER(TTF_Font)

# /usr/include/SDL/SDL_ttf.h: 87
if hasattr(_libs['SDL_ttf'], 'TTF_OpenFontIndex'):
    TTF_OpenFontIndex = _libs['SDL_ttf'].TTF_OpenFontIndex
    TTF_OpenFontIndex.argtypes = [String, c_int, c_long]
    TTF_OpenFontIndex.restype = POINTER(TTF_Font)

# /usr/include/SDL/SDL_ttf.h: 88
if hasattr(_libs['SDL_ttf'], 'TTF_OpenFontRW'):
    TTF_OpenFontRW = _libs['SDL_ttf'].TTF_OpenFontRW
    TTF_OpenFontRW.argtypes = [POINTER(SDL_RWops), c_int, c_int]
    TTF_OpenFontRW.restype = POINTER(TTF_Font)

# /usr/include/SDL/SDL_ttf.h: 89
if hasattr(_libs['SDL_ttf'], 'TTF_OpenFontIndexRW'):
    TTF_OpenFontIndexRW = _libs['SDL_ttf'].TTF_OpenFontIndexRW
    TTF_OpenFontIndexRW.argtypes = [POINTER(SDL_RWops), c_int, c_int, c_long]
    TTF_OpenFontIndexRW.restype = POINTER(TTF_Font)

# /usr/include/SDL/SDL_ttf.h: 97
if hasattr(_libs['SDL_ttf'], 'TTF_GetFontStyle'):
    TTF_GetFontStyle = _libs['SDL_ttf'].TTF_GetFontStyle
    TTF_GetFontStyle.argtypes = [POINTER(TTF_Font)]
    TTF_GetFontStyle.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 98
if hasattr(_libs['SDL_ttf'], 'TTF_SetFontStyle'):
    TTF_SetFontStyle = _libs['SDL_ttf'].TTF_SetFontStyle
    TTF_SetFontStyle.argtypes = [POINTER(TTF_Font), c_int]
    TTF_SetFontStyle.restype = None

# /usr/include/SDL/SDL_ttf.h: 99
if hasattr(_libs['SDL_ttf'], 'TTF_GetFontOutline'):
    TTF_GetFontOutline = _libs['SDL_ttf'].TTF_GetFontOutline
    TTF_GetFontOutline.argtypes = [POINTER(TTF_Font)]
    TTF_GetFontOutline.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 100
if hasattr(_libs['SDL_ttf'], 'TTF_SetFontOutline'):
    TTF_SetFontOutline = _libs['SDL_ttf'].TTF_SetFontOutline
    TTF_SetFontOutline.argtypes = [POINTER(TTF_Font), c_int]
    TTF_SetFontOutline.restype = None

# /usr/include/SDL/SDL_ttf.h: 107
if hasattr(_libs['SDL_ttf'], 'TTF_GetFontHinting'):
    TTF_GetFontHinting = _libs['SDL_ttf'].TTF_GetFontHinting
    TTF_GetFontHinting.argtypes = [POINTER(TTF_Font)]
    TTF_GetFontHinting.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 108
if hasattr(_libs['SDL_ttf'], 'TTF_SetFontHinting'):
    TTF_SetFontHinting = _libs['SDL_ttf'].TTF_SetFontHinting
    TTF_SetFontHinting.argtypes = [POINTER(TTF_Font), c_int]
    TTF_SetFontHinting.restype = None

# /usr/include/SDL/SDL_ttf.h: 111
if hasattr(_libs['SDL_ttf'], 'TTF_FontHeight'):
    TTF_FontHeight = _libs['SDL_ttf'].TTF_FontHeight
    TTF_FontHeight.argtypes = [POINTER(TTF_Font)]
    TTF_FontHeight.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 116
if hasattr(_libs['SDL_ttf'], 'TTF_FontAscent'):
    TTF_FontAscent = _libs['SDL_ttf'].TTF_FontAscent
    TTF_FontAscent.argtypes = [POINTER(TTF_Font)]
    TTF_FontAscent.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 121
if hasattr(_libs['SDL_ttf'], 'TTF_FontDescent'):
    TTF_FontDescent = _libs['SDL_ttf'].TTF_FontDescent
    TTF_FontDescent.argtypes = [POINTER(TTF_Font)]
    TTF_FontDescent.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 124
if hasattr(_libs['SDL_ttf'], 'TTF_FontLineSkip'):
    TTF_FontLineSkip = _libs['SDL_ttf'].TTF_FontLineSkip
    TTF_FontLineSkip.argtypes = [POINTER(TTF_Font)]
    TTF_FontLineSkip.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 127
if hasattr(_libs['SDL_ttf'], 'TTF_GetFontKerning'):
    TTF_GetFontKerning = _libs['SDL_ttf'].TTF_GetFontKerning
    TTF_GetFontKerning.argtypes = [POINTER(TTF_Font)]
    TTF_GetFontKerning.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 128
if hasattr(_libs['SDL_ttf'], 'TTF_SetFontKerning'):
    TTF_SetFontKerning = _libs['SDL_ttf'].TTF_SetFontKerning
    TTF_SetFontKerning.argtypes = [POINTER(TTF_Font), c_int]
    TTF_SetFontKerning.restype = None

# /usr/include/SDL/SDL_ttf.h: 131
if hasattr(_libs['SDL_ttf'], 'TTF_FontFaces'):
    TTF_FontFaces = _libs['SDL_ttf'].TTF_FontFaces
    TTF_FontFaces.argtypes = [POINTER(TTF_Font)]
    TTF_FontFaces.restype = c_long

# /usr/include/SDL/SDL_ttf.h: 134
if hasattr(_libs['SDL_ttf'], 'TTF_FontFaceIsFixedWidth'):
    TTF_FontFaceIsFixedWidth = _libs['SDL_ttf'].TTF_FontFaceIsFixedWidth
    TTF_FontFaceIsFixedWidth.argtypes = [POINTER(TTF_Font)]
    TTF_FontFaceIsFixedWidth.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 135
if hasattr(_libs['SDL_ttf'], 'TTF_FontFaceFamilyName'):
    TTF_FontFaceFamilyName = _libs['SDL_ttf'].TTF_FontFaceFamilyName
    TTF_FontFaceFamilyName.argtypes = [POINTER(TTF_Font)]
    if sizeof(c_int) == sizeof(c_void_p):
        TTF_FontFaceFamilyName.restype = ReturnString
    else:
        TTF_FontFaceFamilyName.restype = String
        TTF_FontFaceFamilyName.errcheck = ReturnString

# /usr/include/SDL/SDL_ttf.h: 136
if hasattr(_libs['SDL_ttf'], 'TTF_FontFaceStyleName'):
    TTF_FontFaceStyleName = _libs['SDL_ttf'].TTF_FontFaceStyleName
    TTF_FontFaceStyleName.argtypes = [POINTER(TTF_Font)]
    if sizeof(c_int) == sizeof(c_void_p):
        TTF_FontFaceStyleName.restype = ReturnString
    else:
        TTF_FontFaceStyleName.restype = String
        TTF_FontFaceStyleName.errcheck = ReturnString

# /usr/include/SDL/SDL_ttf.h: 139
if hasattr(_libs['SDL_ttf'], 'TTF_GlyphIsProvided'):
    TTF_GlyphIsProvided = _libs['SDL_ttf'].TTF_GlyphIsProvided
    TTF_GlyphIsProvided.argtypes = [POINTER(TTF_Font), Uint16]
    TTF_GlyphIsProvided.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 145
if hasattr(_libs['SDL_ttf'], 'TTF_GlyphMetrics'):
    TTF_GlyphMetrics = _libs['SDL_ttf'].TTF_GlyphMetrics
    TTF_GlyphMetrics.argtypes = [POINTER(TTF_Font), Uint16, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    TTF_GlyphMetrics.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 150
if hasattr(_libs['SDL_ttf'], 'TTF_SizeText'):
    TTF_SizeText = _libs['SDL_ttf'].TTF_SizeText
    TTF_SizeText.argtypes = [POINTER(TTF_Font), String, POINTER(c_int), POINTER(c_int)]
    TTF_SizeText.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 151
if hasattr(_libs['SDL_ttf'], 'TTF_SizeUTF8'):
    TTF_SizeUTF8 = _libs['SDL_ttf'].TTF_SizeUTF8
    TTF_SizeUTF8.argtypes = [POINTER(TTF_Font), String, POINTER(c_int), POINTER(c_int)]
    TTF_SizeUTF8.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 152
if hasattr(_libs['SDL_ttf'], 'TTF_SizeUNICODE'):
    TTF_SizeUNICODE = _libs['SDL_ttf'].TTF_SizeUNICODE
    TTF_SizeUNICODE.argtypes = [POINTER(TTF_Font), POINTER(Uint16), POINTER(c_int), POINTER(c_int)]
    TTF_SizeUNICODE.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 160
if hasattr(_libs['SDL_ttf'], 'TTF_RenderText_Solid'):
    TTF_RenderText_Solid = _libs['SDL_ttf'].TTF_RenderText_Solid
    TTF_RenderText_Solid.argtypes = [POINTER(TTF_Font), String, SDL_Color]
    TTF_RenderText_Solid.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 162
if hasattr(_libs['SDL_ttf'], 'TTF_RenderUTF8_Solid'):
    TTF_RenderUTF8_Solid = _libs['SDL_ttf'].TTF_RenderUTF8_Solid
    TTF_RenderUTF8_Solid.argtypes = [POINTER(TTF_Font), String, SDL_Color]
    TTF_RenderUTF8_Solid.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 164
if hasattr(_libs['SDL_ttf'], 'TTF_RenderUNICODE_Solid'):
    TTF_RenderUNICODE_Solid = _libs['SDL_ttf'].TTF_RenderUNICODE_Solid
    TTF_RenderUNICODE_Solid.argtypes = [POINTER(TTF_Font), POINTER(Uint16), SDL_Color]
    TTF_RenderUNICODE_Solid.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 174
if hasattr(_libs['SDL_ttf'], 'TTF_RenderGlyph_Solid'):
    TTF_RenderGlyph_Solid = _libs['SDL_ttf'].TTF_RenderGlyph_Solid
    TTF_RenderGlyph_Solid.argtypes = [POINTER(TTF_Font), Uint16, SDL_Color]
    TTF_RenderGlyph_Solid.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 182
if hasattr(_libs['SDL_ttf'], 'TTF_RenderText_Shaded'):
    TTF_RenderText_Shaded = _libs['SDL_ttf'].TTF_RenderText_Shaded
    TTF_RenderText_Shaded.argtypes = [POINTER(TTF_Font), String, SDL_Color, SDL_Color]
    TTF_RenderText_Shaded.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 184
if hasattr(_libs['SDL_ttf'], 'TTF_RenderUTF8_Shaded'):
    TTF_RenderUTF8_Shaded = _libs['SDL_ttf'].TTF_RenderUTF8_Shaded
    TTF_RenderUTF8_Shaded.argtypes = [POINTER(TTF_Font), String, SDL_Color, SDL_Color]
    TTF_RenderUTF8_Shaded.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 186
if hasattr(_libs['SDL_ttf'], 'TTF_RenderUNICODE_Shaded'):
    TTF_RenderUNICODE_Shaded = _libs['SDL_ttf'].TTF_RenderUNICODE_Shaded
    TTF_RenderUNICODE_Shaded.argtypes = [POINTER(TTF_Font), POINTER(Uint16), SDL_Color, SDL_Color]
    TTF_RenderUNICODE_Shaded.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 196
if hasattr(_libs['SDL_ttf'], 'TTF_RenderGlyph_Shaded'):
    TTF_RenderGlyph_Shaded = _libs['SDL_ttf'].TTF_RenderGlyph_Shaded
    TTF_RenderGlyph_Shaded.argtypes = [POINTER(TTF_Font), Uint16, SDL_Color, SDL_Color]
    TTF_RenderGlyph_Shaded.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 203
if hasattr(_libs['SDL_ttf'], 'TTF_RenderText_Blended'):
    TTF_RenderText_Blended = _libs['SDL_ttf'].TTF_RenderText_Blended
    TTF_RenderText_Blended.argtypes = [POINTER(TTF_Font), String, SDL_Color]
    TTF_RenderText_Blended.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 205
if hasattr(_libs['SDL_ttf'], 'TTF_RenderUTF8_Blended'):
    TTF_RenderUTF8_Blended = _libs['SDL_ttf'].TTF_RenderUTF8_Blended
    TTF_RenderUTF8_Blended.argtypes = [POINTER(TTF_Font), String, SDL_Color]
    TTF_RenderUTF8_Blended.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 207
if hasattr(_libs['SDL_ttf'], 'TTF_RenderUNICODE_Blended'):
    TTF_RenderUNICODE_Blended = _libs['SDL_ttf'].TTF_RenderUNICODE_Blended
    TTF_RenderUNICODE_Blended.argtypes = [POINTER(TTF_Font), POINTER(Uint16), SDL_Color]
    TTF_RenderUNICODE_Blended.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 216
if hasattr(_libs['SDL_ttf'], 'TTF_RenderGlyph_Blended'):
    TTF_RenderGlyph_Blended = _libs['SDL_ttf'].TTF_RenderGlyph_Blended
    TTF_RenderGlyph_Blended.argtypes = [POINTER(TTF_Font), Uint16, SDL_Color]
    TTF_RenderGlyph_Blended.restype = POINTER(SDL_Surface)

# /usr/include/SDL/SDL_ttf.h: 228
if hasattr(_libs['SDL_ttf'], 'TTF_CloseFont'):
    TTF_CloseFont = _libs['SDL_ttf'].TTF_CloseFont
    TTF_CloseFont.argtypes = [POINTER(TTF_Font)]
    TTF_CloseFont.restype = None

# /usr/include/SDL/SDL_ttf.h: 231
if hasattr(_libs['SDL_ttf'], 'TTF_Quit'):
    TTF_Quit = _libs['SDL_ttf'].TTF_Quit
    TTF_Quit.argtypes = []
    TTF_Quit.restype = None

# /usr/include/SDL/SDL_ttf.h: 234
if hasattr(_libs['SDL_ttf'], 'TTF_WasInit'):
    TTF_WasInit = _libs['SDL_ttf'].TTF_WasInit
    TTF_WasInit.argtypes = []
    TTF_WasInit.restype = c_int

# /usr/include/SDL/SDL_ttf.h: 237
if hasattr(_libs['SDL_ttf'], 'TTF_GetFontKerningSize'):
    TTF_GetFontKerningSize = _libs['SDL_ttf'].TTF_GetFontKerningSize
    TTF_GetFontKerningSize.argtypes = [POINTER(TTF_Font), c_int, c_int]
    TTF_GetFontKerningSize.restype = c_int

# /usr/include/SDL/SDL_platform.h: 68
try:
    __LINUX__ = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 53
try:
    SDL_HAS_64BIT_TYPE = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 56
try:
    SDL_BYTEORDER = 1234
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 59
try:
    HAVE_LIBC = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 63
try:
    HAVE_ALLOCA_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 64
try:
    HAVE_SYS_TYPES_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 65
try:
    HAVE_STDIO_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 66
try:
    STDC_HEADERS = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 67
try:
    HAVE_STDLIB_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 68
try:
    HAVE_STDARG_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 69
try:
    HAVE_MALLOC_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 70
try:
    HAVE_MEMORY_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 71
try:
    HAVE_STRING_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 72
try:
    HAVE_STRINGS_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 73
try:
    HAVE_INTTYPES_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 74
try:
    HAVE_STDINT_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 75
try:
    HAVE_CTYPE_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 76
try:
    HAVE_MATH_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 77
try:
    HAVE_ICONV_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 78
try:
    HAVE_SIGNAL_H = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 82
try:
    HAVE_MALLOC = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 83
try:
    HAVE_CALLOC = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 84
try:
    HAVE_REALLOC = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 85
try:
    HAVE_FREE = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 86
try:
    HAVE_ALLOCA = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 88
try:
    HAVE_GETENV = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 89
try:
    HAVE_PUTENV = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 90
try:
    HAVE_UNSETENV = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 92
try:
    HAVE_QSORT = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 93
try:
    HAVE_ABS = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 94
try:
    HAVE_BCOPY = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 95
try:
    HAVE_MEMSET = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 96
try:
    HAVE_MEMCPY = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 97
try:
    HAVE_MEMMOVE = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 98
try:
    HAVE_MEMCMP = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 99
try:
    HAVE_STRLEN = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 102
try:
    HAVE_STRDUP = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 108
try:
    HAVE_STRCHR = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 109
try:
    HAVE_STRRCHR = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 110
try:
    HAVE_STRSTR = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 115
try:
    HAVE_STRTOL = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 116
try:
    HAVE_STRTOUL = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 119
try:
    HAVE_STRTOLL = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 120
try:
    HAVE_STRTOULL = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 121
try:
    HAVE_STRTOD = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 122
try:
    HAVE_ATOI = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 123
try:
    HAVE_ATOF = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 124
try:
    HAVE_STRCMP = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 125
try:
    HAVE_STRNCMP = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 127
try:
    HAVE_STRCASECMP = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 129
try:
    HAVE_STRNCASECMP = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 130
try:
    HAVE_SSCANF = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 131
try:
    HAVE_SNPRINTF = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 132
try:
    HAVE_VSNPRINTF = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 133
try:
    HAVE_ICONV = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 134
try:
    HAVE_SIGACTION = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 135
try:
    HAVE_SETJMP = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 136
try:
    HAVE_NANOSLEEP = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 138
try:
    HAVE_GETPAGESIZE = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 139
try:
    HAVE_MPROTECT = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 159
try:
    SDL_AUDIO_DRIVER_ALSA = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 160
try:
    SDL_AUDIO_DRIVER_ALSA_DYNAMIC = 'libasound.so.2'
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 161
try:
    SDL_AUDIO_DRIVER_ARTS = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 162
try:
    SDL_AUDIO_DRIVER_ARTS_DYNAMIC = 'libartsc.so.0'
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 168
try:
    SDL_AUDIO_DRIVER_DISK = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 169
try:
    SDL_AUDIO_DRIVER_DUMMY = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 172
try:
    SDL_AUDIO_DRIVER_PULSE = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 173
try:
    SDL_AUDIO_DRIVER_PULSE_DYNAMIC = 'libpulse-simple.so.0'
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 174
try:
    SDL_AUDIO_DRIVER_ESD = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 175
try:
    SDL_AUDIO_DRIVER_ESD_DYNAMIC = 'libesd.so.0'
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 180
try:
    SDL_AUDIO_DRIVER_OSS = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 195
try:
    SDL_CDROM_LINUX = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 206
try:
    SDL_INPUT_LINUXEV = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 212
try:
    SDL_JOYSTICK_LINUX = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 224
try:
    SDL_LOADSO_DLOPEN = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 236
try:
    SDL_THREAD_PTHREAD = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 237
try:
    SDL_THREAD_PTHREAD_RECURSIVE_MUTEX = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 250
try:
    SDL_TIMER_UNIX = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 260
try:
    SDL_VIDEO_DRIVER_DGA = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 263
try:
    SDL_VIDEO_DRIVER_DUMMY = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 264
try:
    SDL_VIDEO_DRIVER_FBCON = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 283
try:
    SDL_VIDEO_DRIVER_X11 = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 284
try:
    SDL_VIDEO_DRIVER_X11_DGAMOUSE = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 285
try:
    SDL_VIDEO_DRIVER_X11_DYNAMIC = 'libX11.so.6'
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 286
try:
    SDL_VIDEO_DRIVER_X11_DYNAMIC_XEXT = 'libXext.so.6'
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 287
try:
    SDL_VIDEO_DRIVER_X11_DYNAMIC_XRANDR = 'libXrandr.so.2'
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 288
try:
    SDL_VIDEO_DRIVER_X11_DYNAMIC_XRENDER = 'libXrender.so.1'
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 289
try:
    SDL_VIDEO_DRIVER_X11_VIDMODE = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 290
try:
    SDL_VIDEO_DRIVER_X11_XINERAMA = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 291
try:
    SDL_VIDEO_DRIVER_X11_XME = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 292
try:
    SDL_VIDEO_DRIVER_X11_XRANDR = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 293
try:
    SDL_VIDEO_DRIVER_X11_XV = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 297
try:
    SDL_VIDEO_OPENGL = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 298
try:
    SDL_VIDEO_OPENGL_GLX = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 304
try:
    SDL_VIDEO_DISABLE_SCREENSAVER = 1
except:
    pass

# /usr/include/SDL/SDL_config-x86_64.h: 307
try:
    SDL_ASSEMBLY_ROUTINES = 1
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 78
def SDL_arraysize(array):
    return (sizeof(array) / sizeof((array [0])))

# /usr/include/SDL/SDL_stdinc.h: 79
def SDL_TABLESIZE(table):
    return (SDL_arraysize (table))

# /usr/include/SDL/SDL_stdinc.h: 87
def SDL_reinterpret_cast(type, expression):
    return (type (expression))

# /usr/include/SDL/SDL_stdinc.h: 88
def SDL_static_cast(type, expression):
    return (type (expression))

# /usr/include/SDL/SDL_stdinc.h: 162
try:
    SDL_malloc = malloc
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 168
try:
    SDL_calloc = calloc
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 174
try:
    SDL_realloc = realloc
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 180
try:
    SDL_free = free
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 216
try:
    SDL_getenv = getenv
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 222
try:
    SDL_putenv = putenv
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 228
try:
    SDL_qsort = qsort
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 235
try:
    SDL_abs = abs
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 240
def SDL_min(x, y):
    return (x < y) and x or y

# /usr/include/SDL/SDL_stdinc.h: 241
def SDL_max(x, y):
    return (x > y) and x or y

# /usr/include/SDL/SDL_stdinc.h: 244
def SDL_isdigit(X):
    return (isdigit (X))

# /usr/include/SDL/SDL_stdinc.h: 245
def SDL_isspace(X):
    return (isspace (X))

# /usr/include/SDL/SDL_stdinc.h: 246
def SDL_toupper(X):
    return (toupper (X))

# /usr/include/SDL/SDL_stdinc.h: 247
def SDL_tolower(X):
    return (tolower (X))

# /usr/include/SDL/SDL_stdinc.h: 256
try:
    SDL_memset = memset
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 315
try:
    SDL_memcpy = memcpy
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 339
def SDL_memcpy4(dst, src, len):
    return (SDL_memcpy (dst, src, (len << 2)))

# /usr/include/SDL/SDL_stdinc.h: 374
try:
    SDL_memmove = memmove
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 389
try:
    SDL_memcmp = memcmp
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 395
try:
    SDL_strlen = strlen
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 413
try:
    SDL_strdup = strdup
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 437
try:
    SDL_strchr = strchr
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 445
try:
    SDL_strrchr = strrchr
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 453
try:
    SDL_strstr = strstr
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 461
def SDL_itoa(value, string, radix):
    return (SDL_ltoa (value, string, radix))

# /usr/include/SDL/SDL_stdinc.h: 473
def SDL_uitoa(value, string, radix):
    return (SDL_ultoa (value, string, radix))

# /usr/include/SDL/SDL_stdinc.h: 483
try:
    SDL_strtol = strtol
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 489
try:
    SDL_strtoul = strtoul
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 509
try:
    SDL_strtoll = strtoll
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 515
try:
    SDL_strtoull = strtoull
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 523
try:
    SDL_strtod = strtod
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 529
try:
    SDL_atoi = atoi
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 535
try:
    SDL_atof = atof
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 541
try:
    SDL_strcmp = strcmp
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 547
try:
    SDL_strncmp = strncmp
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 553
try:
    SDL_strcasecmp = strcasecmp
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 561
try:
    SDL_strncasecmp = strncasecmp
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 569
try:
    SDL_sscanf = sscanf
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 575
try:
    SDL_snprintf = snprintf
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 590
try:
    SDL_ICONV_ERROR = (-1)
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 591
try:
    SDL_ICONV_E2BIG = (-2)
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 592
try:
    SDL_ICONV_EILSEQ = (-3)
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 593
try:
    SDL_ICONV_EINVAL = (-4)
except:
    pass

SDL_iconv_t = iconv_t # /usr/include/SDL/SDL_stdinc.h: 597

# /usr/include/SDL/SDL_stdinc.h: 598
try:
    SDL_iconv_open = iconv_open
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 599
try:
    SDL_iconv_close = iconv_close
except:
    pass

# /usr/include/SDL/SDL_stdinc.h: 610
def SDL_iconv_utf8_locale(S):
    return (SDL_iconv_string ('', 'UTF-8', S, (((SDL_strlen (S)).value) + 1)))

# /usr/include/SDL/SDL_stdinc.h: 611
def SDL_iconv_utf8_ucs2(S):
    return (SDL_iconv_string ('UCS-2', 'UTF-8', S, (((SDL_strlen (S)).value) + 1)))

# /usr/include/SDL/SDL_stdinc.h: 612
def SDL_iconv_utf8_ucs4(S):
    return (SDL_iconv_string ('UCS-4', 'UTF-8', S, (((SDL_strlen (S)).value) + 1)))

# /usr/include/SDL/SDL_error.h: 53
try:
    SDL_OutOfMemory = (SDL_Error (SDL_ENOMEM))
except:
    pass

# /usr/include/SDL/SDL_error.h: 54
try:
    SDL_Unsupported = (SDL_Error (SDL_UNSUPPORTED))
except:
    pass

# /usr/include/SDL/SDL_active.h: 42
try:
    SDL_APPMOUSEFOCUS = 1
except:
    pass

# /usr/include/SDL/SDL_active.h: 43
try:
    SDL_APPINPUTFOCUS = 2
except:
    pass

# /usr/include/SDL/SDL_active.h: 44
try:
    SDL_APPACTIVE = 4
except:
    pass

# /usr/include/SDL/SDL_endian.h: 37
try:
    SDL_LIL_ENDIAN = 1234
except:
    pass

# /usr/include/SDL/SDL_endian.h: 38
try:
    SDL_BIG_ENDIAN = 4321
except:
    pass

# /usr/include/SDL/SDL_endian.h: 192
def SDL_SwapLE16(X):
    return X

# /usr/include/SDL/SDL_endian.h: 193
def SDL_SwapLE32(X):
    return X

# /usr/include/SDL/SDL_endian.h: 194
def SDL_SwapLE64(X):
    return X

# /usr/include/SDL/SDL_mutex.h: 44
try:
    SDL_MUTEX_TIMEDOUT = 1
except:
    pass

# /usr/include/SDL/SDL_mutex.h: 47
try:
    SDL_MUTEX_MAXWAIT = (~0)
except:
    pass

# /usr/include/SDL/SDL_mutex.h: 61
def SDL_LockMutex(m):
    return (SDL_mutexP (m))

# /usr/include/SDL/SDL_mutex.h: 67
def SDL_UnlockMutex(m):
    return (SDL_mutexV (m))

# /usr/include/SDL/SDL_rwops.h: 115
try:
    RW_SEEK_SET = 0
except:
    pass

# /usr/include/SDL/SDL_rwops.h: 116
try:
    RW_SEEK_CUR = 1
except:
    pass

# /usr/include/SDL/SDL_rwops.h: 117
try:
    RW_SEEK_END = 2
except:
    pass

# /usr/include/SDL/SDL_rwops.h: 122
def SDL_RWseek(ctx, offset, whence):
    return ((ctx.contents.seek) (ctx, offset, whence))

# /usr/include/SDL/SDL_rwops.h: 123
def SDL_RWtell(ctx):
    return ((ctx.contents.seek) (ctx, 0, RW_SEEK_CUR))

# /usr/include/SDL/SDL_rwops.h: 124
def SDL_RWread(ctx, ptr, size, n):
    return ((ctx.contents.read) (ctx, ptr, size, n))

# /usr/include/SDL/SDL_rwops.h: 125
def SDL_RWwrite(ctx, ptr, size, n):
    return ((ctx.contents.write) (ctx, ptr, size, n))

# /usr/include/SDL/SDL_rwops.h: 126
def SDL_RWclose(ctx):
    return ((ctx.contents.close) (ctx))

# /usr/include/SDL/SDL_audio.h: 100
try:
    AUDIO_U8 = 8
except:
    pass

# /usr/include/SDL/SDL_audio.h: 101
try:
    AUDIO_S8 = 32776
except:
    pass

# /usr/include/SDL/SDL_audio.h: 102
try:
    AUDIO_U16LSB = 16
except:
    pass

# /usr/include/SDL/SDL_audio.h: 103
try:
    AUDIO_S16LSB = 32784
except:
    pass

# /usr/include/SDL/SDL_audio.h: 104
try:
    AUDIO_U16MSB = 4112
except:
    pass

# /usr/include/SDL/SDL_audio.h: 105
try:
    AUDIO_S16MSB = 36880
except:
    pass

# /usr/include/SDL/SDL_audio.h: 106
try:
    AUDIO_U16 = AUDIO_U16LSB
except:
    pass

# /usr/include/SDL/SDL_audio.h: 107
try:
    AUDIO_S16 = AUDIO_S16LSB
except:
    pass

# /usr/include/SDL/SDL_audio.h: 114
try:
    AUDIO_U16SYS = AUDIO_U16LSB
except:
    pass

# /usr/include/SDL/SDL_audio.h: 115
try:
    AUDIO_S16SYS = AUDIO_S16LSB
except:
    pass

# /usr/include/SDL/SDL_audio.h: 218
def SDL_LoadWAV(file, spec, audio_buf, audio_len):
    return (SDL_LoadWAV_RW ((SDL_RWFromFile (file, 'rb')), 1, spec, audio_buf, audio_len))

# /usr/include/SDL/SDL_audio.h: 250
try:
    SDL_MIX_MAXVOLUME = 128
except:
    pass

# /usr/include/SDL/SDL_cdrom.h: 48
try:
    SDL_MAX_TRACKS = 99
except:
    pass

# /usr/include/SDL/SDL_cdrom.h: 54
try:
    SDL_AUDIO_TRACK = 0
except:
    pass

# /usr/include/SDL/SDL_cdrom.h: 55
try:
    SDL_DATA_TRACK = 4
except:
    pass

# /usr/include/SDL/SDL_cdrom.h: 68
def CD_INDRIVE(status):
    return (status > 0)

# /usr/include/SDL/SDL_cdrom.h: 96
try:
    CD_FPS = 75
except:
    pass

# /usr/include/SDL/SDL_cdrom.h: 105
def MSF_TO_FRAMES(M, S, F):
    return ((((M * 60) * CD_FPS) + (S * CD_FPS)) + F)

# /usr/include/SDL/SDL_keysym.h: 321
try:
    KMOD_CTRL = (KMOD_LCTRL | KMOD_RCTRL)
except:
    pass

# /usr/include/SDL/SDL_keysym.h: 322
try:
    KMOD_SHIFT = (KMOD_LSHIFT | KMOD_RSHIFT)
except:
    pass

# /usr/include/SDL/SDL_keysym.h: 323
try:
    KMOD_ALT = (KMOD_LALT | KMOD_RALT)
except:
    pass

# /usr/include/SDL/SDL_keysym.h: 324
try:
    KMOD_META = (KMOD_LMETA | KMOD_RMETA)
except:
    pass

# /usr/include/SDL/SDL_keyboard.h: 67
try:
    SDL_ALL_HOTKEYS = 4294967295
except:
    pass

# /usr/include/SDL/SDL_keyboard.h: 84
try:
    SDL_DEFAULT_REPEAT_DELAY = 500
except:
    pass

# /usr/include/SDL/SDL_keyboard.h: 85
try:
    SDL_DEFAULT_REPEAT_INTERVAL = 30
except:
    pass

# /usr/include/SDL/SDL_video.h: 44
try:
    SDL_ALPHA_OPAQUE = 255
except:
    pass

# /usr/include/SDL/SDL_video.h: 45
try:
    SDL_ALPHA_TRANSPARENT = 0
except:
    pass

SDL_Colour = SDL_Color # /usr/include/SDL/SDL_video.h: 61

# /usr/include/SDL/SDL_video.h: 131
try:
    SDL_SWSURFACE = 0
except:
    pass

# /usr/include/SDL/SDL_video.h: 132
try:
    SDL_HWSURFACE = 1
except:
    pass

# /usr/include/SDL/SDL_video.h: 133
try:
    SDL_ASYNCBLIT = 4
except:
    pass

# /usr/include/SDL/SDL_video.h: 138
try:
    SDL_ANYFORMAT = 268435456
except:
    pass

# /usr/include/SDL/SDL_video.h: 139
try:
    SDL_HWPALETTE = 536870912
except:
    pass

# /usr/include/SDL/SDL_video.h: 140
try:
    SDL_DOUBLEBUF = 1073741824
except:
    pass

# /usr/include/SDL/SDL_video.h: 141
try:
    SDL_FULLSCREEN = 2147483648
except:
    pass

# /usr/include/SDL/SDL_video.h: 142
try:
    SDL_OPENGL = 2
except:
    pass

# /usr/include/SDL/SDL_video.h: 143
try:
    SDL_OPENGLBLIT = 10
except:
    pass

# /usr/include/SDL/SDL_video.h: 144
try:
    SDL_RESIZABLE = 16
except:
    pass

# /usr/include/SDL/SDL_video.h: 145
try:
    SDL_NOFRAME = 32
except:
    pass

# /usr/include/SDL/SDL_video.h: 150
try:
    SDL_HWACCEL = 256
except:
    pass

# /usr/include/SDL/SDL_video.h: 151
try:
    SDL_SRCCOLORKEY = 4096
except:
    pass

# /usr/include/SDL/SDL_video.h: 152
try:
    SDL_RLEACCELOK = 8192
except:
    pass

# /usr/include/SDL/SDL_video.h: 153
try:
    SDL_RLEACCEL = 16384
except:
    pass

# /usr/include/SDL/SDL_video.h: 154
try:
    SDL_SRCALPHA = 65536
except:
    pass

# /usr/include/SDL/SDL_video.h: 155
try:
    SDL_PREALLOC = 16777216
except:
    pass

# /usr/include/SDL/SDL_video.h: 161
def SDL_MUSTLOCK(surface):
    return ((surface.contents.offset) or (((surface.contents.flags) & ((SDL_HWSURFACE | SDL_ASYNCBLIT) | SDL_RLEACCEL)) != 0))

# /usr/include/SDL/SDL_video.h: 200
try:
    SDL_YV12_OVERLAY = 842094169
except:
    pass

# /usr/include/SDL/SDL_video.h: 201
try:
    SDL_IYUV_OVERLAY = 1448433993
except:
    pass

# /usr/include/SDL/SDL_video.h: 202
try:
    SDL_YUY2_OVERLAY = 844715353
except:
    pass

# /usr/include/SDL/SDL_video.h: 203
try:
    SDL_UYVY_OVERLAY = 1498831189
except:
    pass

# /usr/include/SDL/SDL_video.h: 204
try:
    SDL_YVYU_OVERLAY = 1431918169
except:
    pass

# /usr/include/SDL/SDL_video.h: 252
try:
    SDL_LOGPAL = 1
except:
    pass

# /usr/include/SDL/SDL_video.h: 253
try:
    SDL_PHYSPAL = 2
except:
    pass

# /usr/include/SDL/SDL_video.h: 518
try:
    SDL_AllocSurface = SDL_CreateRGBSurface
except:
    pass

# /usr/include/SDL/SDL_video.h: 592
def SDL_LoadBMP(file):
    return (SDL_LoadBMP_RW ((SDL_RWFromFile (file, 'rb')), 1))

# /usr/include/SDL/SDL_video.h: 603
def SDL_SaveBMP(surface, file):
    return (SDL_SaveBMP_RW (surface, (SDL_RWFromFile (file, 'wb')), 1))

# /usr/include/SDL/SDL_video.h: 743
try:
    SDL_BlitSurface = SDL_UpperBlit
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 122
def SDL_BUTTON(X):
    return (1 << (X - 1))

# /usr/include/SDL/SDL_mouse.h: 123
try:
    SDL_BUTTON_LEFT = 1
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 124
try:
    SDL_BUTTON_MIDDLE = 2
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 125
try:
    SDL_BUTTON_RIGHT = 3
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 126
try:
    SDL_BUTTON_WHEELUP = 4
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 127
try:
    SDL_BUTTON_WHEELDOWN = 5
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 128
try:
    SDL_BUTTON_X1 = 6
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 129
try:
    SDL_BUTTON_X2 = 7
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 130
try:
    SDL_BUTTON_LMASK = (SDL_BUTTON (SDL_BUTTON_LEFT))
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 131
try:
    SDL_BUTTON_MMASK = (SDL_BUTTON (SDL_BUTTON_MIDDLE))
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 132
try:
    SDL_BUTTON_RMASK = (SDL_BUTTON (SDL_BUTTON_RIGHT))
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 133
try:
    SDL_BUTTON_X1MASK = (SDL_BUTTON (SDL_BUTTON_X1))
except:
    pass

# /usr/include/SDL/SDL_mouse.h: 134
try:
    SDL_BUTTON_X2MASK = (SDL_BUTTON (SDL_BUTTON_X2))
except:
    pass

# /usr/include/SDL/SDL_joystick.h: 141
try:
    SDL_HAT_CENTERED = 0
except:
    pass

# /usr/include/SDL/SDL_joystick.h: 142
try:
    SDL_HAT_UP = 1
except:
    pass

# /usr/include/SDL/SDL_joystick.h: 143
try:
    SDL_HAT_RIGHT = 2
except:
    pass

# /usr/include/SDL/SDL_joystick.h: 144
try:
    SDL_HAT_DOWN = 4
except:
    pass

# /usr/include/SDL/SDL_joystick.h: 145
try:
    SDL_HAT_LEFT = 8
except:
    pass

# /usr/include/SDL/SDL_joystick.h: 146
try:
    SDL_HAT_RIGHTUP = (SDL_HAT_RIGHT | SDL_HAT_UP)
except:
    pass

# /usr/include/SDL/SDL_joystick.h: 147
try:
    SDL_HAT_RIGHTDOWN = (SDL_HAT_RIGHT | SDL_HAT_DOWN)
except:
    pass

# /usr/include/SDL/SDL_joystick.h: 148
try:
    SDL_HAT_LEFTUP = (SDL_HAT_LEFT | SDL_HAT_UP)
except:
    pass

# /usr/include/SDL/SDL_joystick.h: 149
try:
    SDL_HAT_LEFTDOWN = (SDL_HAT_LEFT | SDL_HAT_DOWN)
except:
    pass

# /usr/include/SDL/SDL_quit.h: 52
try:
    SDL_QuitRequested = (SDL_PumpEvents ())
except:
    pass

# /usr/include/SDL/SDL_events.h: 47
try:
    SDL_RELEASED = 0
except:
    pass

# /usr/include/SDL/SDL_events.h: 48
try:
    SDL_PRESSED = 1
except:
    pass

# /usr/include/SDL/SDL_events.h: 87
def SDL_EVENTMASK(X):
    return (1 << X)

# /usr/include/SDL/SDL_events.h: 115
try:
    SDL_ALLEVENTS = 4294967295
except:
    pass

# /usr/include/SDL/SDL_events.h: 334
try:
    SDL_QUERY = (-1)
except:
    pass

# /usr/include/SDL/SDL_events.h: 335
try:
    SDL_IGNORE = 0
except:
    pass

# /usr/include/SDL/SDL_events.h: 336
try:
    SDL_DISABLE = 0
except:
    pass

# /usr/include/SDL/SDL_events.h: 337
try:
    SDL_ENABLE = 1
except:
    pass

# /usr/include/SDL/SDL_timer.h: 40
try:
    SDL_TIMESLICE = 10
except:
    pass

# /usr/include/SDL/SDL_timer.h: 43
try:
    TIMER_RESOLUTION = 10
except:
    pass

# /usr/include/SDL/SDL_version.h: 42
try:
    SDL_MAJOR_VERSION = 1
except:
    pass

# /usr/include/SDL/SDL_version.h: 43
try:
    SDL_MINOR_VERSION = 2
except:
    pass

# /usr/include/SDL/SDL_version.h: 44
try:
    SDL_PATCHLEVEL = 14
except:
    pass

# /usr/include/SDL/SDL_version.h: 68
def SDL_VERSIONNUM(X, Y, Z):
    return (((X * 1000) + (Y * 100)) + Z)

# /usr/include/SDL/SDL_version.h: 72
try:
    SDL_COMPILEDVERSION = (SDL_VERSIONNUM (SDL_MAJOR_VERSION, SDL_MINOR_VERSION, SDL_PATCHLEVEL))
except:
    pass

# /usr/include/SDL/SDL_version.h: 76
def SDL_VERSION_ATLEAST(X, Y, Z):
    return (SDL_COMPILEDVERSION >= ((SDL_VERSIONNUM (X, Y, Z)).value))

# /usr/include/SDL/SDL.h: 61
try:
    SDL_INIT_TIMER = 1
except:
    pass

# /usr/include/SDL/SDL.h: 62
try:
    SDL_INIT_AUDIO = 16
except:
    pass

# /usr/include/SDL/SDL.h: 63
try:
    SDL_INIT_VIDEO = 32
except:
    pass

# /usr/include/SDL/SDL.h: 64
try:
    SDL_INIT_CDROM = 256
except:
    pass

# /usr/include/SDL/SDL.h: 65
try:
    SDL_INIT_JOYSTICK = 512
except:
    pass

# /usr/include/SDL/SDL.h: 66
try:
    SDL_INIT_NOPARACHUTE = 1048576
except:
    pass

# /usr/include/SDL/SDL.h: 67
try:
    SDL_INIT_EVENTTHREAD = 16777216
except:
    pass

# /usr/include/SDL/SDL.h: 68
try:
    SDL_INIT_EVERYTHING = 65535
except:
    pass

# /usr/include/SDL/SDL_framerate.h: 27
try:
    FPS_UPPER_LIMIT = 200
except:
    pass

# /usr/include/SDL/SDL_framerate.h: 32
try:
    FPS_LOWER_LIMIT = 1
except:
    pass

# /usr/include/SDL/SDL_framerate.h: 37
try:
    FPS_DEFAULT = 30
except:
    pass

# /usr/include/SDL/SDL_gfxPrimitives_font.h: 6
try:
    GFX_FONTDATAMAX = (8 * 256)
except:
    pass

# /usr/include/SDL/SDL_gfxPrimitives.h: 26
try:
    SDL_GFXPRIMITIVES_MAJOR = 2
except:
    pass

# /usr/include/SDL/SDL_gfxPrimitives.h: 27
try:
    SDL_GFXPRIMITIVES_MINOR = 0
except:
    pass

# /usr/include/SDL/SDL_gfxPrimitives.h: 28
try:
    SDL_GFXPRIMITIVES_MICRO = 22
except:
    pass

# /usr/include/SDL/SDL_image.h: 39
try:
    SDL_IMAGE_MAJOR_VERSION = 1
except:
    pass

# /usr/include/SDL/SDL_image.h: 40
try:
    SDL_IMAGE_MINOR_VERSION = 2
except:
    pass

# /usr/include/SDL/SDL_image.h: 41
try:
    SDL_IMAGE_PATCHLEVEL = 10
except:
    pass

# /usr/include/SDL/SDL_image.h: 127
try:
    IMG_SetError = SDL_SetError
except:
    pass

# /usr/include/SDL/SDL_image.h: 128
try:
    IMG_GetError = SDL_GetError
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 42
try:
    SDL_MIXER_MAJOR_VERSION = 1
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 43
try:
    SDL_MIXER_MINOR_VERSION = 2
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 44
try:
    SDL_MIXER_PATCHLEVEL = 11
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 57
try:
    MIX_MAJOR_VERSION = SDL_MIXER_MAJOR_VERSION
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 58
try:
    MIX_MINOR_VERSION = SDL_MIXER_MINOR_VERSION
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 59
try:
    MIX_PATCHLEVEL = SDL_MIXER_PATCHLEVEL
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 88
try:
    MIX_CHANNELS = 8
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 92
try:
    MIX_DEFAULT_FREQUENCY = 22050
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 94
try:
    MIX_DEFAULT_FORMAT = AUDIO_S16LSB
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 98
try:
    MIX_DEFAULT_CHANNELS = 2
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 99
try:
    MIX_MAX_VOLUME = 128
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 149
def Mix_LoadWAV(file):
    return (Mix_LoadWAV_RW ((SDL_RWFromFile (file, 'rb')), 1))

# /usr/include/SDL/SDL_mixer.h: 229
try:
    MIX_CHANNEL_POST = (-2)
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 337
try:
    MIX_EFFECTSMAXSPEED = 'MIX_EFFECTSMAXSPEED'
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 532
def Mix_PlayChannel(channel, chunk, loops):
    return (Mix_PlayChannelTimed (channel, chunk, loops, (-1)))

# /usr/include/SDL/SDL_mixer.h: 540
def Mix_FadeInChannel(channel, chunk, loops, ms):
    return (Mix_FadeInChannelTimed (channel, chunk, loops, ms, (-1)))

# /usr/include/SDL/SDL_mixer.h: 616
try:
    Mix_SetError = SDL_SetError
except:
    pass

# /usr/include/SDL/SDL_mixer.h: 617
try:
    Mix_GetError = SDL_GetError
except:
    pass

# /usr/include/SDL/SDL_name.h: 6
try:
    NeedFunctionPrototypes = 1
except:
    pass

# /usr/include/SDL/SDL_net.h: 42
try:
    SDL_NET_MAJOR_VERSION = 1
except:
    pass

# /usr/include/SDL/SDL_net.h: 43
try:
    SDL_NET_MINOR_VERSION = 2
except:
    pass

# /usr/include/SDL/SDL_net.h: 44
try:
    SDL_NET_PATCHLEVEL = 7
except:
    pass

# /usr/include/SDL/SDL_net.h: 85
try:
    INADDR_ANY = 0
except:
    pass

# /usr/include/SDL/SDL_net.h: 88
try:
    INADDR_NONE = 4294967295
except:
    pass

# /usr/include/SDL/SDL_net.h: 91
try:
    INADDR_BROADCAST = 4294967295
except:
    pass

# /usr/include/SDL/SDL_net.h: 154
try:
    SDLNET_MAX_UDPCHANNELS = 32
except:
    pass

# /usr/include/SDL/SDL_net.h: 156
try:
    SDLNET_MAX_UDPADDRESSES = 4
except:
    pass

# /usr/include/SDL/SDL_net.h: 283
def SDLNet_TCP_AddSocket(set, sock):
    return (SDLNet_AddSocket (set, sock))

# /usr/include/SDL/SDL_net.h: 285
def SDLNet_UDP_AddSocket(set, sock):
    return (SDLNet_AddSocket (set, sock))

# /usr/include/SDL/SDL_net.h: 290
def SDLNet_TCP_DelSocket(set, sock):
    return (SDLNet_DelSocket (set, sock))

# /usr/include/SDL/SDL_net.h: 292
def SDLNet_UDP_DelSocket(set, sock):
    return (SDLNet_DelSocket (set, sock))

# /usr/include/SDL/SDL_net.h: 309
def SDLNet_SocketReady(sock):
    return ((sock != NULL) and (sock.contents.ready))

# /usr/include/SDL/SDL_net.h: 333
try:
    SDLNet_SetError = SDL_SetError
except:
    pass

# /usr/include/SDL/SDL_net.h: 334
try:
    SDLNet_GetError = SDL_GetError
except:
    pass

# /usr/include/SDL/SDL_net.h: 351
try:
    SDL_DATA_ALIGNED = 0
except:
    pass

# /usr/include/GL/gl.h: 250
try:
    GL_MODELVIEW = 5888
except:
    pass

# /usr/include/GL/gl.h: 543
try:
    GL_MODELVIEW_MATRIX = 2982
except:
    pass

# /usr/include/GL/gl.h: 544
try:
    GL_MODELVIEW_STACK_DEPTH = 2979
except:
    pass

# /usr/include/GL/gl.h: 1628
try:
    GL_BLEND_EQUATION = 32777
except:
    pass

# /usr/include/GL/gl.h: 1834
try:
    GL_SOURCE0_RGB = 34176
except:
    pass

# /usr/include/GL/gl.h: 1835
try:
    GL_SOURCE1_RGB = 34177
except:
    pass

# /usr/include/GL/gl.h: 1836
try:
    GL_SOURCE2_RGB = 34178
except:
    pass

# /usr/include/GL/gl.h: 1837
try:
    GL_SOURCE0_ALPHA = 34184
except:
    pass

# /usr/include/GL/gl.h: 1838
try:
    GL_SOURCE1_ALPHA = 34185
except:
    pass

# /usr/include/GL/gl.h: 1839
try:
    GL_SOURCE2_ALPHA = 34186
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 116
try:
    GL_GLEXT_VERSION = 29
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 340
try:
    GL_BLEND_DST_RGB = 32968
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 341
try:
    GL_BLEND_SRC_RGB = 32969
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 342
try:
    GL_BLEND_DST_ALPHA = 32970
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 343
try:
    GL_BLEND_SRC_ALPHA = 32971
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 344
try:
    GL_POINT_SIZE_MIN = 33062
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 345
try:
    GL_POINT_SIZE_MAX = 33063
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 346
try:
    GL_POINT_FADE_THRESHOLD_SIZE = 33064
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 347
try:
    GL_POINT_DISTANCE_ATTENUATION = 33065
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 348
try:
    GL_GENERATE_MIPMAP = 33169
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 349
try:
    GL_GENERATE_MIPMAP_HINT = 33170
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 350
try:
    GL_DEPTH_COMPONENT16 = 33189
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 351
try:
    GL_DEPTH_COMPONENT24 = 33190
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 352
try:
    GL_DEPTH_COMPONENT32 = 33191
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 353
try:
    GL_MIRRORED_REPEAT = 33648
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 354
try:
    GL_FOG_COORDINATE_SOURCE = 33872
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 355
try:
    GL_FOG_COORDINATE = 33873
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 356
try:
    GL_FRAGMENT_DEPTH = 33874
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 357
try:
    GL_CURRENT_FOG_COORDINATE = 33875
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 358
try:
    GL_FOG_COORDINATE_ARRAY_TYPE = 33876
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 359
try:
    GL_FOG_COORDINATE_ARRAY_STRIDE = 33877
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 360
try:
    GL_FOG_COORDINATE_ARRAY_POINTER = 33878
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 361
try:
    GL_FOG_COORDINATE_ARRAY = 33879
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 362
try:
    GL_COLOR_SUM = 33880
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 363
try:
    GL_CURRENT_SECONDARY_COLOR = 33881
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 364
try:
    GL_SECONDARY_COLOR_ARRAY_SIZE = 33882
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 365
try:
    GL_SECONDARY_COLOR_ARRAY_TYPE = 33883
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 366
try:
    GL_SECONDARY_COLOR_ARRAY_STRIDE = 33884
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 367
try:
    GL_SECONDARY_COLOR_ARRAY_POINTER = 33885
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 368
try:
    GL_SECONDARY_COLOR_ARRAY = 33886
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 369
try:
    GL_MAX_TEXTURE_LOD_BIAS = 34045
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 370
try:
    GL_TEXTURE_FILTER_CONTROL = 34048
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 371
try:
    GL_TEXTURE_LOD_BIAS = 34049
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 372
try:
    GL_INCR_WRAP = 34055
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 373
try:
    GL_DECR_WRAP = 34056
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 374
try:
    GL_TEXTURE_DEPTH_SIZE = 34890
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 375
try:
    GL_DEPTH_TEXTURE_MODE = 34891
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 376
try:
    GL_TEXTURE_COMPARE_MODE = 34892
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 377
try:
    GL_TEXTURE_COMPARE_FUNC = 34893
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 378
try:
    GL_COMPARE_R_TO_TEXTURE = 34894
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 382
try:
    GL_BUFFER_SIZE = 34660
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 383
try:
    GL_BUFFER_USAGE = 34661
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 384
try:
    GL_QUERY_COUNTER_BITS = 34916
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 385
try:
    GL_CURRENT_QUERY = 34917
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 386
try:
    GL_QUERY_RESULT = 34918
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 387
try:
    GL_QUERY_RESULT_AVAILABLE = 34919
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 388
try:
    GL_ARRAY_BUFFER = 34962
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 389
try:
    GL_ELEMENT_ARRAY_BUFFER = 34963
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 390
try:
    GL_ARRAY_BUFFER_BINDING = 34964
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 391
try:
    GL_ELEMENT_ARRAY_BUFFER_BINDING = 34965
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 392
try:
    GL_VERTEX_ARRAY_BUFFER_BINDING = 34966
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 393
try:
    GL_NORMAL_ARRAY_BUFFER_BINDING = 34967
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 394
try:
    GL_COLOR_ARRAY_BUFFER_BINDING = 34968
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 395
try:
    GL_INDEX_ARRAY_BUFFER_BINDING = 34969
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 396
try:
    GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = 34970
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 397
try:
    GL_EDGE_FLAG_ARRAY_BUFFER_BINDING = 34971
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 398
try:
    GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING = 34972
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 399
try:
    GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING = 34973
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 400
try:
    GL_WEIGHT_ARRAY_BUFFER_BINDING = 34974
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 401
try:
    GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 34975
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 402
try:
    GL_READ_ONLY = 35000
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 403
try:
    GL_WRITE_ONLY = 35001
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 404
try:
    GL_READ_WRITE = 35002
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 405
try:
    GL_BUFFER_ACCESS = 35003
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 406
try:
    GL_BUFFER_MAPPED = 35004
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 407
try:
    GL_BUFFER_MAP_POINTER = 35005
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 408
try:
    GL_STREAM_DRAW = 35040
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 409
try:
    GL_STREAM_READ = 35041
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 410
try:
    GL_STREAM_COPY = 35042
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 411
try:
    GL_STATIC_DRAW = 35044
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 412
try:
    GL_STATIC_READ = 35045
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 413
try:
    GL_STATIC_COPY = 35046
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 414
try:
    GL_DYNAMIC_DRAW = 35048
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 415
try:
    GL_DYNAMIC_READ = 35049
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 416
try:
    GL_DYNAMIC_COPY = 35050
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 417
try:
    GL_SAMPLES_PASSED = 35092
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 418
try:
    GL_FOG_COORD_SRC = GL_FOG_COORDINATE_SOURCE
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 419
try:
    GL_FOG_COORD = GL_FOG_COORDINATE
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 420
try:
    GL_CURRENT_FOG_COORD = GL_CURRENT_FOG_COORDINATE
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 421
try:
    GL_FOG_COORD_ARRAY_TYPE = GL_FOG_COORDINATE_ARRAY_TYPE
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 422
try:
    GL_FOG_COORD_ARRAY_STRIDE = GL_FOG_COORDINATE_ARRAY_STRIDE
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 423
try:
    GL_FOG_COORD_ARRAY_POINTER = GL_FOG_COORDINATE_ARRAY_POINTER
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 424
try:
    GL_FOG_COORD_ARRAY = GL_FOG_COORDINATE_ARRAY
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 425
try:
    GL_FOG_COORD_ARRAY_BUFFER_BINDING = GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 426
try:
    GL_SRC0_RGB = GL_SOURCE0_RGB
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 427
try:
    GL_SRC1_RGB = GL_SOURCE1_RGB
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 428
try:
    GL_SRC2_RGB = GL_SOURCE2_RGB
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 429
try:
    GL_SRC0_ALPHA = GL_SOURCE0_ALPHA
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 430
try:
    GL_SRC1_ALPHA = GL_SOURCE1_ALPHA
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 431
try:
    GL_SRC2_ALPHA = GL_SOURCE2_ALPHA
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 435
try:
    GL_BLEND_EQUATION_RGB = GL_BLEND_EQUATION
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 436
try:
    GL_VERTEX_ATTRIB_ARRAY_ENABLED = 34338
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 437
try:
    GL_VERTEX_ATTRIB_ARRAY_SIZE = 34339
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 438
try:
    GL_VERTEX_ATTRIB_ARRAY_STRIDE = 34340
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 439
try:
    GL_VERTEX_ATTRIB_ARRAY_TYPE = 34341
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 440
try:
    GL_CURRENT_VERTEX_ATTRIB = 34342
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 441
try:
    GL_VERTEX_PROGRAM_POINT_SIZE = 34370
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 442
try:
    GL_VERTEX_PROGRAM_TWO_SIDE = 34371
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 443
try:
    GL_VERTEX_ATTRIB_ARRAY_POINTER = 34373
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 444
try:
    GL_STENCIL_BACK_FUNC = 34816
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 445
try:
    GL_STENCIL_BACK_FAIL = 34817
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 446
try:
    GL_STENCIL_BACK_PASS_DEPTH_FAIL = 34818
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 447
try:
    GL_STENCIL_BACK_PASS_DEPTH_PASS = 34819
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 448
try:
    GL_MAX_DRAW_BUFFERS = 34852
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 449
try:
    GL_DRAW_BUFFER0 = 34853
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 450
try:
    GL_DRAW_BUFFER1 = 34854
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 451
try:
    GL_DRAW_BUFFER2 = 34855
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 452
try:
    GL_DRAW_BUFFER3 = 34856
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 453
try:
    GL_DRAW_BUFFER4 = 34857
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 454
try:
    GL_DRAW_BUFFER5 = 34858
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 455
try:
    GL_DRAW_BUFFER6 = 34859
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 456
try:
    GL_DRAW_BUFFER7 = 34860
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 457
try:
    GL_DRAW_BUFFER8 = 34861
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 458
try:
    GL_DRAW_BUFFER9 = 34862
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 459
try:
    GL_DRAW_BUFFER10 = 34863
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 460
try:
    GL_DRAW_BUFFER11 = 34864
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 461
try:
    GL_DRAW_BUFFER12 = 34865
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 462
try:
    GL_DRAW_BUFFER13 = 34866
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 463
try:
    GL_DRAW_BUFFER14 = 34867
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 464
try:
    GL_DRAW_BUFFER15 = 34868
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 465
try:
    GL_BLEND_EQUATION_ALPHA = 34877
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 466
try:
    GL_POINT_SPRITE = 34913
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 467
try:
    GL_COORD_REPLACE = 34914
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 468
try:
    GL_MAX_VERTEX_ATTRIBS = 34921
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 469
try:
    GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 34922
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 470
try:
    GL_MAX_TEXTURE_COORDS = 34929
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 471
try:
    GL_MAX_TEXTURE_IMAGE_UNITS = 34930
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 472
try:
    GL_FRAGMENT_SHADER = 35632
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 473
try:
    GL_VERTEX_SHADER = 35633
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 474
try:
    GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = 35657
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 475
try:
    GL_MAX_VERTEX_UNIFORM_COMPONENTS = 35658
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 476
try:
    GL_MAX_VARYING_FLOATS = 35659
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 477
try:
    GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 35660
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 478
try:
    GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 35661
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 479
try:
    GL_SHADER_TYPE = 35663
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 480
try:
    GL_FLOAT_VEC2 = 35664
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 481
try:
    GL_FLOAT_VEC3 = 35665
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 482
try:
    GL_FLOAT_VEC4 = 35666
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 483
try:
    GL_INT_VEC2 = 35667
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 484
try:
    GL_INT_VEC3 = 35668
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 485
try:
    GL_INT_VEC4 = 35669
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 486
try:
    GL_BOOL = 35670
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 487
try:
    GL_BOOL_VEC2 = 35671
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 488
try:
    GL_BOOL_VEC3 = 35672
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 489
try:
    GL_BOOL_VEC4 = 35673
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 490
try:
    GL_FLOAT_MAT2 = 35674
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 491
try:
    GL_FLOAT_MAT3 = 35675
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 492
try:
    GL_FLOAT_MAT4 = 35676
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 493
try:
    GL_SAMPLER_1D = 35677
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 494
try:
    GL_SAMPLER_2D = 35678
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 495
try:
    GL_SAMPLER_3D = 35679
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 496
try:
    GL_SAMPLER_CUBE = 35680
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 497
try:
    GL_SAMPLER_1D_SHADOW = 35681
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 498
try:
    GL_SAMPLER_2D_SHADOW = 35682
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 499
try:
    GL_DELETE_STATUS = 35712
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 500
try:
    GL_COMPILE_STATUS = 35713
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 501
try:
    GL_LINK_STATUS = 35714
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 502
try:
    GL_VALIDATE_STATUS = 35715
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 503
try:
    GL_INFO_LOG_LENGTH = 35716
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 504
try:
    GL_ATTACHED_SHADERS = 35717
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 505
try:
    GL_ACTIVE_UNIFORMS = 35718
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 506
try:
    GL_ACTIVE_UNIFORM_MAX_LENGTH = 35719
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 507
try:
    GL_SHADER_SOURCE_LENGTH = 35720
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 508
try:
    GL_ACTIVE_ATTRIBUTES = 35721
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 509
try:
    GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 35722
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 510
try:
    GL_FRAGMENT_SHADER_DERIVATIVE_HINT = 35723
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 511
try:
    GL_SHADING_LANGUAGE_VERSION = 35724
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 512
try:
    GL_CURRENT_PROGRAM = 35725
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 513
try:
    GL_POINT_SPRITE_COORD_ORIGIN = 36000
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 514
try:
    GL_LOWER_LEFT = 36001
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 515
try:
    GL_UPPER_LEFT = 36002
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 516
try:
    GL_STENCIL_BACK_REF = 36003
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 517
try:
    GL_STENCIL_BACK_VALUE_MASK = 36004
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 518
try:
    GL_STENCIL_BACK_WRITEMASK = 36005
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 560
try:
    GL_TRANSPOSE_MODELVIEW_MATRIX_ARB = 34019
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 561
try:
    GL_TRANSPOSE_PROJECTION_MATRIX_ARB = 34020
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 562
try:
    GL_TRANSPOSE_TEXTURE_MATRIX_ARB = 34021
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 563
try:
    GL_TRANSPOSE_COLOR_MATRIX_ARB = 34022
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 567
try:
    GL_MULTISAMPLE_ARB = 32925
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 568
try:
    GL_SAMPLE_ALPHA_TO_COVERAGE_ARB = 32926
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 569
try:
    GL_SAMPLE_ALPHA_TO_ONE_ARB = 32927
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 570
try:
    GL_SAMPLE_COVERAGE_ARB = 32928
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 571
try:
    GL_SAMPLE_BUFFERS_ARB = 32936
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 572
try:
    GL_SAMPLES_ARB = 32937
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 573
try:
    GL_SAMPLE_COVERAGE_VALUE_ARB = 32938
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 574
try:
    GL_SAMPLE_COVERAGE_INVERT_ARB = 32939
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 575
try:
    GL_MULTISAMPLE_BIT_ARB = 536870912
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 582
try:
    GL_NORMAL_MAP_ARB = 34065
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 583
try:
    GL_REFLECTION_MAP_ARB = 34066
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 584
try:
    GL_TEXTURE_CUBE_MAP_ARB = 34067
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 585
try:
    GL_TEXTURE_BINDING_CUBE_MAP_ARB = 34068
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 586
try:
    GL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB = 34069
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 587
try:
    GL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB = 34070
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 588
try:
    GL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB = 34071
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 589
try:
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB = 34072
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 590
try:
    GL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB = 34073
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 591
try:
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB = 34074
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 592
try:
    GL_PROXY_TEXTURE_CUBE_MAP_ARB = 34075
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 593
try:
    GL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB = 34076
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 597
try:
    GL_COMPRESSED_ALPHA_ARB = 34025
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 598
try:
    GL_COMPRESSED_LUMINANCE_ARB = 34026
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 599
try:
    GL_COMPRESSED_LUMINANCE_ALPHA_ARB = 34027
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 600
try:
    GL_COMPRESSED_INTENSITY_ARB = 34028
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 601
try:
    GL_COMPRESSED_RGB_ARB = 34029
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 602
try:
    GL_COMPRESSED_RGBA_ARB = 34030
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 603
try:
    GL_TEXTURE_COMPRESSION_HINT_ARB = 34031
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 604
try:
    GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB = 34464
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 605
try:
    GL_TEXTURE_COMPRESSED_ARB = 34465
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 606
try:
    GL_NUM_COMPRESSED_TEXTURE_FORMATS_ARB = 34466
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 607
try:
    GL_COMPRESSED_TEXTURE_FORMATS_ARB = 34467
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 611
try:
    GL_CLAMP_TO_BORDER_ARB = 33069
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 615
try:
    GL_POINT_SIZE_MIN_ARB = 33062
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 616
try:
    GL_POINT_SIZE_MAX_ARB = 33063
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 617
try:
    GL_POINT_FADE_THRESHOLD_SIZE_ARB = 33064
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 618
try:
    GL_POINT_DISTANCE_ATTENUATION_ARB = 33065
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 622
try:
    GL_MAX_VERTEX_UNITS_ARB = 34468
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 623
try:
    GL_ACTIVE_VERTEX_UNITS_ARB = 34469
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 624
try:
    GL_WEIGHT_SUM_UNITY_ARB = 34470
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 625
try:
    GL_VERTEX_BLEND_ARB = 34471
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 626
try:
    GL_CURRENT_WEIGHT_ARB = 34472
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 627
try:
    GL_WEIGHT_ARRAY_TYPE_ARB = 34473
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 628
try:
    GL_WEIGHT_ARRAY_STRIDE_ARB = 34474
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 629
try:
    GL_WEIGHT_ARRAY_SIZE_ARB = 34475
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 630
try:
    GL_WEIGHT_ARRAY_POINTER_ARB = 34476
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 631
try:
    GL_WEIGHT_ARRAY_ARB = 34477
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 632
try:
    GL_MODELVIEW0_ARB = 5888
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 633
try:
    GL_MODELVIEW1_ARB = 34058
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 634
try:
    GL_MODELVIEW2_ARB = 34594
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 635
try:
    GL_MODELVIEW3_ARB = 34595
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 636
try:
    GL_MODELVIEW4_ARB = 34596
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 637
try:
    GL_MODELVIEW5_ARB = 34597
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 638
try:
    GL_MODELVIEW6_ARB = 34598
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 639
try:
    GL_MODELVIEW7_ARB = 34599
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 640
try:
    GL_MODELVIEW8_ARB = 34600
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 641
try:
    GL_MODELVIEW9_ARB = 34601
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 642
try:
    GL_MODELVIEW10_ARB = 34602
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 643
try:
    GL_MODELVIEW11_ARB = 34603
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 644
try:
    GL_MODELVIEW12_ARB = 34604
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 645
try:
    GL_MODELVIEW13_ARB = 34605
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 646
try:
    GL_MODELVIEW14_ARB = 34606
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 647
try:
    GL_MODELVIEW15_ARB = 34607
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 648
try:
    GL_MODELVIEW16_ARB = 34608
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 649
try:
    GL_MODELVIEW17_ARB = 34609
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 650
try:
    GL_MODELVIEW18_ARB = 34610
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 651
try:
    GL_MODELVIEW19_ARB = 34611
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 652
try:
    GL_MODELVIEW20_ARB = 34612
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 653
try:
    GL_MODELVIEW21_ARB = 34613
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 654
try:
    GL_MODELVIEW22_ARB = 34614
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 655
try:
    GL_MODELVIEW23_ARB = 34615
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 656
try:
    GL_MODELVIEW24_ARB = 34616
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 657
try:
    GL_MODELVIEW25_ARB = 34617
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 658
try:
    GL_MODELVIEW26_ARB = 34618
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 659
try:
    GL_MODELVIEW27_ARB = 34619
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 660
try:
    GL_MODELVIEW28_ARB = 34620
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 661
try:
    GL_MODELVIEW29_ARB = 34621
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 662
try:
    GL_MODELVIEW30_ARB = 34622
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 663
try:
    GL_MODELVIEW31_ARB = 34623
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 667
try:
    GL_MATRIX_PALETTE_ARB = 34880
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 668
try:
    GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB = 34881
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 669
try:
    GL_MAX_PALETTE_MATRICES_ARB = 34882
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 670
try:
    GL_CURRENT_PALETTE_MATRIX_ARB = 34883
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 671
try:
    GL_MATRIX_INDEX_ARRAY_ARB = 34884
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 672
try:
    GL_CURRENT_MATRIX_INDEX_ARB = 34885
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 673
try:
    GL_MATRIX_INDEX_ARRAY_SIZE_ARB = 34886
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 674
try:
    GL_MATRIX_INDEX_ARRAY_TYPE_ARB = 34887
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 675
try:
    GL_MATRIX_INDEX_ARRAY_STRIDE_ARB = 34888
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 676
try:
    GL_MATRIX_INDEX_ARRAY_POINTER_ARB = 34889
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 680
try:
    GL_COMBINE_ARB = 34160
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 681
try:
    GL_COMBINE_RGB_ARB = 34161
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 682
try:
    GL_COMBINE_ALPHA_ARB = 34162
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 683
try:
    GL_SOURCE0_RGB_ARB = 34176
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 684
try:
    GL_SOURCE1_RGB_ARB = 34177
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 685
try:
    GL_SOURCE2_RGB_ARB = 34178
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 686
try:
    GL_SOURCE0_ALPHA_ARB = 34184
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 687
try:
    GL_SOURCE1_ALPHA_ARB = 34185
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 688
try:
    GL_SOURCE2_ALPHA_ARB = 34186
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 689
try:
    GL_OPERAND0_RGB_ARB = 34192
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 690
try:
    GL_OPERAND1_RGB_ARB = 34193
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 691
try:
    GL_OPERAND2_RGB_ARB = 34194
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 692
try:
    GL_OPERAND0_ALPHA_ARB = 34200
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 693
try:
    GL_OPERAND1_ALPHA_ARB = 34201
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 694
try:
    GL_OPERAND2_ALPHA_ARB = 34202
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 695
try:
    GL_RGB_SCALE_ARB = 34163
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 696
try:
    GL_ADD_SIGNED_ARB = 34164
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 697
try:
    GL_INTERPOLATE_ARB = 34165
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 698
try:
    GL_SUBTRACT_ARB = 34023
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 699
try:
    GL_CONSTANT_ARB = 34166
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 700
try:
    GL_PRIMARY_COLOR_ARB = 34167
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 701
try:
    GL_PREVIOUS_ARB = 34168
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 708
try:
    GL_DOT3_RGB_ARB = 34478
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 709
try:
    GL_DOT3_RGBA_ARB = 34479
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 713
try:
    GL_MIRRORED_REPEAT_ARB = 33648
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 717
try:
    GL_DEPTH_COMPONENT16_ARB = 33189
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 718
try:
    GL_DEPTH_COMPONENT24_ARB = 33190
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 719
try:
    GL_DEPTH_COMPONENT32_ARB = 33191
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 720
try:
    GL_TEXTURE_DEPTH_SIZE_ARB = 34890
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 721
try:
    GL_DEPTH_TEXTURE_MODE_ARB = 34891
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 725
try:
    GL_TEXTURE_COMPARE_MODE_ARB = 34892
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 726
try:
    GL_TEXTURE_COMPARE_FUNC_ARB = 34893
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 727
try:
    GL_COMPARE_R_TO_TEXTURE_ARB = 34894
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 731
try:
    GL_TEXTURE_COMPARE_FAIL_VALUE_ARB = 32959
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 738
try:
    GL_COLOR_SUM_ARB = 33880
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 739
try:
    GL_VERTEX_PROGRAM_ARB = 34336
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 740
try:
    GL_VERTEX_ATTRIB_ARRAY_ENABLED_ARB = 34338
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 741
try:
    GL_VERTEX_ATTRIB_ARRAY_SIZE_ARB = 34339
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 742
try:
    GL_VERTEX_ATTRIB_ARRAY_STRIDE_ARB = 34340
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 743
try:
    GL_VERTEX_ATTRIB_ARRAY_TYPE_ARB = 34341
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 744
try:
    GL_CURRENT_VERTEX_ATTRIB_ARB = 34342
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 745
try:
    GL_PROGRAM_LENGTH_ARB = 34343
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 746
try:
    GL_PROGRAM_STRING_ARB = 34344
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 747
try:
    GL_MAX_PROGRAM_MATRIX_STACK_DEPTH_ARB = 34350
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 748
try:
    GL_MAX_PROGRAM_MATRICES_ARB = 34351
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 749
try:
    GL_CURRENT_MATRIX_STACK_DEPTH_ARB = 34368
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 750
try:
    GL_CURRENT_MATRIX_ARB = 34369
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 751
try:
    GL_VERTEX_PROGRAM_POINT_SIZE_ARB = 34370
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 752
try:
    GL_VERTEX_PROGRAM_TWO_SIDE_ARB = 34371
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 753
try:
    GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB = 34373
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 754
try:
    GL_PROGRAM_ERROR_POSITION_ARB = 34379
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 755
try:
    GL_PROGRAM_BINDING_ARB = 34423
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 756
try:
    GL_MAX_VERTEX_ATTRIBS_ARB = 34921
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 757
try:
    GL_VERTEX_ATTRIB_ARRAY_NORMALIZED_ARB = 34922
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 758
try:
    GL_PROGRAM_ERROR_STRING_ARB = 34932
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 759
try:
    GL_PROGRAM_FORMAT_ASCII_ARB = 34933
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 760
try:
    GL_PROGRAM_FORMAT_ARB = 34934
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 761
try:
    GL_PROGRAM_INSTRUCTIONS_ARB = 34976
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 762
try:
    GL_MAX_PROGRAM_INSTRUCTIONS_ARB = 34977
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 763
try:
    GL_PROGRAM_NATIVE_INSTRUCTIONS_ARB = 34978
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 764
try:
    GL_MAX_PROGRAM_NATIVE_INSTRUCTIONS_ARB = 34979
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 765
try:
    GL_PROGRAM_TEMPORARIES_ARB = 34980
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 766
try:
    GL_MAX_PROGRAM_TEMPORARIES_ARB = 34981
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 767
try:
    GL_PROGRAM_NATIVE_TEMPORARIES_ARB = 34982
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 768
try:
    GL_MAX_PROGRAM_NATIVE_TEMPORARIES_ARB = 34983
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 769
try:
    GL_PROGRAM_PARAMETERS_ARB = 34984
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 770
try:
    GL_MAX_PROGRAM_PARAMETERS_ARB = 34985
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 771
try:
    GL_PROGRAM_NATIVE_PARAMETERS_ARB = 34986
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 772
try:
    GL_MAX_PROGRAM_NATIVE_PARAMETERS_ARB = 34987
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 773
try:
    GL_PROGRAM_ATTRIBS_ARB = 34988
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 774
try:
    GL_MAX_PROGRAM_ATTRIBS_ARB = 34989
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 775
try:
    GL_PROGRAM_NATIVE_ATTRIBS_ARB = 34990
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 776
try:
    GL_MAX_PROGRAM_NATIVE_ATTRIBS_ARB = 34991
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 777
try:
    GL_PROGRAM_ADDRESS_REGISTERS_ARB = 34992
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 778
try:
    GL_MAX_PROGRAM_ADDRESS_REGISTERS_ARB = 34993
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 779
try:
    GL_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB = 34994
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 780
try:
    GL_MAX_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB = 34995
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 781
try:
    GL_MAX_PROGRAM_LOCAL_PARAMETERS_ARB = 34996
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 782
try:
    GL_MAX_PROGRAM_ENV_PARAMETERS_ARB = 34997
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 783
try:
    GL_PROGRAM_UNDER_NATIVE_LIMITS_ARB = 34998
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 784
try:
    GL_TRANSPOSE_CURRENT_MATRIX_ARB = 34999
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 785
try:
    GL_MATRIX0_ARB = 35008
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 786
try:
    GL_MATRIX1_ARB = 35009
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 787
try:
    GL_MATRIX2_ARB = 35010
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 788
try:
    GL_MATRIX3_ARB = 35011
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 789
try:
    GL_MATRIX4_ARB = 35012
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 790
try:
    GL_MATRIX5_ARB = 35013
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 791
try:
    GL_MATRIX6_ARB = 35014
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 792
try:
    GL_MATRIX7_ARB = 35015
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 793
try:
    GL_MATRIX8_ARB = 35016
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 794
try:
    GL_MATRIX9_ARB = 35017
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 795
try:
    GL_MATRIX10_ARB = 35018
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 796
try:
    GL_MATRIX11_ARB = 35019
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 797
try:
    GL_MATRIX12_ARB = 35020
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 798
try:
    GL_MATRIX13_ARB = 35021
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 799
try:
    GL_MATRIX14_ARB = 35022
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 800
try:
    GL_MATRIX15_ARB = 35023
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 801
try:
    GL_MATRIX16_ARB = 35024
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 802
try:
    GL_MATRIX17_ARB = 35025
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 803
try:
    GL_MATRIX18_ARB = 35026
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 804
try:
    GL_MATRIX19_ARB = 35027
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 805
try:
    GL_MATRIX20_ARB = 35028
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 806
try:
    GL_MATRIX21_ARB = 35029
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 807
try:
    GL_MATRIX22_ARB = 35030
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 808
try:
    GL_MATRIX23_ARB = 35031
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 809
try:
    GL_MATRIX24_ARB = 35032
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 810
try:
    GL_MATRIX25_ARB = 35033
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 811
try:
    GL_MATRIX26_ARB = 35034
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 812
try:
    GL_MATRIX27_ARB = 35035
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 813
try:
    GL_MATRIX28_ARB = 35036
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 814
try:
    GL_MATRIX29_ARB = 35037
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 815
try:
    GL_MATRIX30_ARB = 35038
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 816
try:
    GL_MATRIX31_ARB = 35039
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 820
try:
    GL_FRAGMENT_PROGRAM_ARB = 34820
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 821
try:
    GL_PROGRAM_ALU_INSTRUCTIONS_ARB = 34821
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 822
try:
    GL_PROGRAM_TEX_INSTRUCTIONS_ARB = 34822
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 823
try:
    GL_PROGRAM_TEX_INDIRECTIONS_ARB = 34823
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 824
try:
    GL_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = 34824
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 825
try:
    GL_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = 34825
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 826
try:
    GL_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = 34826
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 827
try:
    GL_MAX_PROGRAM_ALU_INSTRUCTIONS_ARB = 34827
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 828
try:
    GL_MAX_PROGRAM_TEX_INSTRUCTIONS_ARB = 34828
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 829
try:
    GL_MAX_PROGRAM_TEX_INDIRECTIONS_ARB = 34829
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 830
try:
    GL_MAX_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = 34830
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 831
try:
    GL_MAX_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = 34831
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 832
try:
    GL_MAX_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = 34832
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 833
try:
    GL_MAX_TEXTURE_COORDS_ARB = 34929
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 834
try:
    GL_MAX_TEXTURE_IMAGE_UNITS_ARB = 34930
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 838
try:
    GL_BUFFER_SIZE_ARB = 34660
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 839
try:
    GL_BUFFER_USAGE_ARB = 34661
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 840
try:
    GL_ARRAY_BUFFER_ARB = 34962
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 841
try:
    GL_ELEMENT_ARRAY_BUFFER_ARB = 34963
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 842
try:
    GL_ARRAY_BUFFER_BINDING_ARB = 34964
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 843
try:
    GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB = 34965
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 844
try:
    GL_VERTEX_ARRAY_BUFFER_BINDING_ARB = 34966
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 845
try:
    GL_NORMAL_ARRAY_BUFFER_BINDING_ARB = 34967
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 846
try:
    GL_COLOR_ARRAY_BUFFER_BINDING_ARB = 34968
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 847
try:
    GL_INDEX_ARRAY_BUFFER_BINDING_ARB = 34969
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 848
try:
    GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB = 34970
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 849
try:
    GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB = 34971
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 850
try:
    GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB = 34972
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 851
try:
    GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB = 34973
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 852
try:
    GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB = 34974
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 853
try:
    GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB = 34975
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 854
try:
    GL_READ_ONLY_ARB = 35000
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 855
try:
    GL_WRITE_ONLY_ARB = 35001
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 856
try:
    GL_READ_WRITE_ARB = 35002
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 857
try:
    GL_BUFFER_ACCESS_ARB = 35003
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 858
try:
    GL_BUFFER_MAPPED_ARB = 35004
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 859
try:
    GL_BUFFER_MAP_POINTER_ARB = 35005
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 860
try:
    GL_STREAM_DRAW_ARB = 35040
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 861
try:
    GL_STREAM_READ_ARB = 35041
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 862
try:
    GL_STREAM_COPY_ARB = 35042
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 863
try:
    GL_STATIC_DRAW_ARB = 35044
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 864
try:
    GL_STATIC_READ_ARB = 35045
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 865
try:
    GL_STATIC_COPY_ARB = 35046
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 866
try:
    GL_DYNAMIC_DRAW_ARB = 35048
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 867
try:
    GL_DYNAMIC_READ_ARB = 35049
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 868
try:
    GL_DYNAMIC_COPY_ARB = 35050
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 872
try:
    GL_QUERY_COUNTER_BITS_ARB = 34916
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 873
try:
    GL_CURRENT_QUERY_ARB = 34917
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 874
try:
    GL_QUERY_RESULT_ARB = 34918
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 875
try:
    GL_QUERY_RESULT_AVAILABLE_ARB = 34919
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 876
try:
    GL_SAMPLES_PASSED_ARB = 35092
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 880
try:
    GL_PROGRAM_OBJECT_ARB = 35648
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 881
try:
    GL_SHADER_OBJECT_ARB = 35656
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 882
try:
    GL_OBJECT_TYPE_ARB = 35662
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 883
try:
    GL_OBJECT_SUBTYPE_ARB = 35663
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 884
try:
    GL_FLOAT_VEC2_ARB = 35664
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 885
try:
    GL_FLOAT_VEC3_ARB = 35665
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 886
try:
    GL_FLOAT_VEC4_ARB = 35666
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 887
try:
    GL_INT_VEC2_ARB = 35667
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 888
try:
    GL_INT_VEC3_ARB = 35668
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 889
try:
    GL_INT_VEC4_ARB = 35669
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 890
try:
    GL_BOOL_ARB = 35670
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 891
try:
    GL_BOOL_VEC2_ARB = 35671
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 892
try:
    GL_BOOL_VEC3_ARB = 35672
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 893
try:
    GL_BOOL_VEC4_ARB = 35673
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 894
try:
    GL_FLOAT_MAT2_ARB = 35674
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 895
try:
    GL_FLOAT_MAT3_ARB = 35675
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 896
try:
    GL_FLOAT_MAT4_ARB = 35676
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 897
try:
    GL_SAMPLER_1D_ARB = 35677
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 898
try:
    GL_SAMPLER_2D_ARB = 35678
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 899
try:
    GL_SAMPLER_3D_ARB = 35679
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 900
try:
    GL_SAMPLER_CUBE_ARB = 35680
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 901
try:
    GL_SAMPLER_1D_SHADOW_ARB = 35681
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 902
try:
    GL_SAMPLER_2D_SHADOW_ARB = 35682
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 903
try:
    GL_SAMPLER_2D_RECT_ARB = 35683
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 904
try:
    GL_SAMPLER_2D_RECT_SHADOW_ARB = 35684
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 905
try:
    GL_OBJECT_DELETE_STATUS_ARB = 35712
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 906
try:
    GL_OBJECT_COMPILE_STATUS_ARB = 35713
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 907
try:
    GL_OBJECT_LINK_STATUS_ARB = 35714
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 908
try:
    GL_OBJECT_VALIDATE_STATUS_ARB = 35715
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 909
try:
    GL_OBJECT_INFO_LOG_LENGTH_ARB = 35716
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 910
try:
    GL_OBJECT_ATTACHED_OBJECTS_ARB = 35717
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 911
try:
    GL_OBJECT_ACTIVE_UNIFORMS_ARB = 35718
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 912
try:
    GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB = 35719
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 913
try:
    GL_OBJECT_SHADER_SOURCE_LENGTH_ARB = 35720
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 917
try:
    GL_VERTEX_SHADER_ARB = 35633
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 918
try:
    GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB = 35658
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 919
try:
    GL_MAX_VARYING_FLOATS_ARB = 35659
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 920
try:
    GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB = 35660
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 921
try:
    GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB = 35661
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 922
try:
    GL_OBJECT_ACTIVE_ATTRIBUTES_ARB = 35721
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 923
try:
    GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB = 35722
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 927
try:
    GL_FRAGMENT_SHADER_ARB = 35632
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 928
try:
    GL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB = 35657
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 929
try:
    GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB = 35723
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 933
try:
    GL_SHADING_LANGUAGE_VERSION_ARB = 35724
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 940
try:
    GL_POINT_SPRITE_ARB = 34913
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 941
try:
    GL_COORD_REPLACE_ARB = 34914
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 948
try:
    GL_MAX_DRAW_BUFFERS_ARB = 34852
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 949
try:
    GL_DRAW_BUFFER0_ARB = 34853
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 950
try:
    GL_DRAW_BUFFER1_ARB = 34854
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 951
try:
    GL_DRAW_BUFFER2_ARB = 34855
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 952
try:
    GL_DRAW_BUFFER3_ARB = 34856
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 953
try:
    GL_DRAW_BUFFER4_ARB = 34857
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 954
try:
    GL_DRAW_BUFFER5_ARB = 34858
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 955
try:
    GL_DRAW_BUFFER6_ARB = 34859
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 956
try:
    GL_DRAW_BUFFER7_ARB = 34860
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 957
try:
    GL_DRAW_BUFFER8_ARB = 34861
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 958
try:
    GL_DRAW_BUFFER9_ARB = 34862
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 959
try:
    GL_DRAW_BUFFER10_ARB = 34863
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 960
try:
    GL_DRAW_BUFFER11_ARB = 34864
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 961
try:
    GL_DRAW_BUFFER12_ARB = 34865
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 962
try:
    GL_DRAW_BUFFER13_ARB = 34866
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 963
try:
    GL_DRAW_BUFFER14_ARB = 34867
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 964
try:
    GL_DRAW_BUFFER15_ARB = 34868
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 968
try:
    GL_TEXTURE_RECTANGLE_ARB = 34037
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 969
try:
    GL_TEXTURE_BINDING_RECTANGLE_ARB = 34038
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 970
try:
    GL_PROXY_TEXTURE_RECTANGLE_ARB = 34039
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 971
try:
    GL_MAX_RECTANGLE_TEXTURE_SIZE_ARB = 34040
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 975
try:
    GL_RGBA_FLOAT_MODE_ARB = 34848
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 976
try:
    GL_CLAMP_VERTEX_COLOR_ARB = 35098
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 977
try:
    GL_CLAMP_FRAGMENT_COLOR_ARB = 35099
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 978
try:
    GL_CLAMP_READ_COLOR_ARB = 35100
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 979
try:
    GL_FIXED_ONLY_ARB = 35101
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 983
try:
    GL_HALF_FLOAT_ARB = 5131
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 987
try:
    GL_TEXTURE_RED_TYPE_ARB = 35856
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 988
try:
    GL_TEXTURE_GREEN_TYPE_ARB = 35857
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 989
try:
    GL_TEXTURE_BLUE_TYPE_ARB = 35858
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 990
try:
    GL_TEXTURE_ALPHA_TYPE_ARB = 35859
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 991
try:
    GL_TEXTURE_LUMINANCE_TYPE_ARB = 35860
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 992
try:
    GL_TEXTURE_INTENSITY_TYPE_ARB = 35861
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 993
try:
    GL_TEXTURE_DEPTH_TYPE_ARB = 35862
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 994
try:
    GL_UNSIGNED_NORMALIZED_ARB = 35863
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 995
try:
    GL_RGBA32F_ARB = 34836
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 996
try:
    GL_RGB32F_ARB = 34837
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 997
try:
    GL_ALPHA32F_ARB = 34838
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 998
try:
    GL_INTENSITY32F_ARB = 34839
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 999
try:
    GL_LUMINANCE32F_ARB = 34840
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1000
try:
    GL_LUMINANCE_ALPHA32F_ARB = 34841
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1001
try:
    GL_RGBA16F_ARB = 34842
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1002
try:
    GL_RGB16F_ARB = 34843
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1003
try:
    GL_ALPHA16F_ARB = 34844
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1004
try:
    GL_INTENSITY16F_ARB = 34845
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1005
try:
    GL_LUMINANCE16F_ARB = 34846
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1006
try:
    GL_LUMINANCE_ALPHA16F_ARB = 34847
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1010
try:
    GL_PIXEL_PACK_BUFFER_ARB = 35051
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1011
try:
    GL_PIXEL_UNPACK_BUFFER_ARB = 35052
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1012
try:
    GL_PIXEL_PACK_BUFFER_BINDING_ARB = 35053
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1013
try:
    GL_PIXEL_UNPACK_BUFFER_BINDING_ARB = 35055
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1017
try:
    GL_ABGR_EXT = 32768
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1021
try:
    GL_CONSTANT_COLOR_EXT = 32769
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1022
try:
    GL_ONE_MINUS_CONSTANT_COLOR_EXT = 32770
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1023
try:
    GL_CONSTANT_ALPHA_EXT = 32771
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1024
try:
    GL_ONE_MINUS_CONSTANT_ALPHA_EXT = 32772
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1025
try:
    GL_BLEND_COLOR_EXT = 32773
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1029
try:
    GL_POLYGON_OFFSET_EXT = 32823
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1030
try:
    GL_POLYGON_OFFSET_FACTOR_EXT = 32824
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1031
try:
    GL_POLYGON_OFFSET_BIAS_EXT = 32825
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1035
try:
    GL_ALPHA4_EXT = 32827
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1036
try:
    GL_ALPHA8_EXT = 32828
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1037
try:
    GL_ALPHA12_EXT = 32829
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1038
try:
    GL_ALPHA16_EXT = 32830
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1039
try:
    GL_LUMINANCE4_EXT = 32831
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1040
try:
    GL_LUMINANCE8_EXT = 32832
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1041
try:
    GL_LUMINANCE12_EXT = 32833
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1042
try:
    GL_LUMINANCE16_EXT = 32834
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1043
try:
    GL_LUMINANCE4_ALPHA4_EXT = 32835
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1044
try:
    GL_LUMINANCE6_ALPHA2_EXT = 32836
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1045
try:
    GL_LUMINANCE8_ALPHA8_EXT = 32837
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1046
try:
    GL_LUMINANCE12_ALPHA4_EXT = 32838
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1047
try:
    GL_LUMINANCE12_ALPHA12_EXT = 32839
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1048
try:
    GL_LUMINANCE16_ALPHA16_EXT = 32840
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1049
try:
    GL_INTENSITY_EXT = 32841
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1050
try:
    GL_INTENSITY4_EXT = 32842
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1051
try:
    GL_INTENSITY8_EXT = 32843
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1052
try:
    GL_INTENSITY12_EXT = 32844
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1053
try:
    GL_INTENSITY16_EXT = 32845
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1054
try:
    GL_RGB2_EXT = 32846
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1055
try:
    GL_RGB4_EXT = 32847
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1056
try:
    GL_RGB5_EXT = 32848
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1057
try:
    GL_RGB8_EXT = 32849
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1058
try:
    GL_RGB10_EXT = 32850
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1059
try:
    GL_RGB12_EXT = 32851
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1060
try:
    GL_RGB16_EXT = 32852
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1061
try:
    GL_RGBA2_EXT = 32853
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1062
try:
    GL_RGBA4_EXT = 32854
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1063
try:
    GL_RGB5_A1_EXT = 32855
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1064
try:
    GL_RGBA8_EXT = 32856
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1065
try:
    GL_RGB10_A2_EXT = 32857
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1066
try:
    GL_RGBA12_EXT = 32858
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1067
try:
    GL_RGBA16_EXT = 32859
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1068
try:
    GL_TEXTURE_RED_SIZE_EXT = 32860
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1069
try:
    GL_TEXTURE_GREEN_SIZE_EXT = 32861
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1070
try:
    GL_TEXTURE_BLUE_SIZE_EXT = 32862
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1071
try:
    GL_TEXTURE_ALPHA_SIZE_EXT = 32863
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1072
try:
    GL_TEXTURE_LUMINANCE_SIZE_EXT = 32864
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1073
try:
    GL_TEXTURE_INTENSITY_SIZE_EXT = 32865
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1074
try:
    GL_REPLACE_EXT = 32866
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1075
try:
    GL_PROXY_TEXTURE_1D_EXT = 32867
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1076
try:
    GL_PROXY_TEXTURE_2D_EXT = 32868
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1077
try:
    GL_TEXTURE_TOO_LARGE_EXT = 32869
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1081
try:
    GL_PACK_SKIP_IMAGES_EXT = 32875
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1082
try:
    GL_PACK_IMAGE_HEIGHT_EXT = 32876
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1083
try:
    GL_UNPACK_SKIP_IMAGES_EXT = 32877
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1084
try:
    GL_UNPACK_IMAGE_HEIGHT_EXT = 32878
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1085
try:
    GL_TEXTURE_3D_EXT = 32879
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1086
try:
    GL_PROXY_TEXTURE_3D_EXT = 32880
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1087
try:
    GL_TEXTURE_DEPTH_EXT = 32881
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1088
try:
    GL_TEXTURE_WRAP_R_EXT = 32882
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1089
try:
    GL_MAX_3D_TEXTURE_SIZE_EXT = 32883
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1093
try:
    GL_FILTER4_SGIS = 33094
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1094
try:
    GL_TEXTURE_FILTER4_SIZE_SGIS = 33095
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1104
try:
    GL_HISTOGRAM_EXT = 32804
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1105
try:
    GL_PROXY_HISTOGRAM_EXT = 32805
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1106
try:
    GL_HISTOGRAM_WIDTH_EXT = 32806
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1107
try:
    GL_HISTOGRAM_FORMAT_EXT = 32807
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1108
try:
    GL_HISTOGRAM_RED_SIZE_EXT = 32808
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1109
try:
    GL_HISTOGRAM_GREEN_SIZE_EXT = 32809
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1110
try:
    GL_HISTOGRAM_BLUE_SIZE_EXT = 32810
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1111
try:
    GL_HISTOGRAM_ALPHA_SIZE_EXT = 32811
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1112
try:
    GL_HISTOGRAM_LUMINANCE_SIZE_EXT = 32812
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1113
try:
    GL_HISTOGRAM_SINK_EXT = 32813
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1114
try:
    GL_MINMAX_EXT = 32814
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1115
try:
    GL_MINMAX_FORMAT_EXT = 32815
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1116
try:
    GL_MINMAX_SINK_EXT = 32816
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1117
try:
    GL_TABLE_TOO_LARGE_EXT = 32817
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1121
try:
    GL_CONVOLUTION_1D_EXT = 32784
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1122
try:
    GL_CONVOLUTION_2D_EXT = 32785
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1123
try:
    GL_SEPARABLE_2D_EXT = 32786
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1124
try:
    GL_CONVOLUTION_BORDER_MODE_EXT = 32787
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1125
try:
    GL_CONVOLUTION_FILTER_SCALE_EXT = 32788
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1126
try:
    GL_CONVOLUTION_FILTER_BIAS_EXT = 32789
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1127
try:
    GL_REDUCE_EXT = 32790
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1128
try:
    GL_CONVOLUTION_FORMAT_EXT = 32791
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1129
try:
    GL_CONVOLUTION_WIDTH_EXT = 32792
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1130
try:
    GL_CONVOLUTION_HEIGHT_EXT = 32793
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1131
try:
    GL_MAX_CONVOLUTION_WIDTH_EXT = 32794
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1132
try:
    GL_MAX_CONVOLUTION_HEIGHT_EXT = 32795
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1133
try:
    GL_POST_CONVOLUTION_RED_SCALE_EXT = 32796
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1134
try:
    GL_POST_CONVOLUTION_GREEN_SCALE_EXT = 32797
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1135
try:
    GL_POST_CONVOLUTION_BLUE_SCALE_EXT = 32798
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1136
try:
    GL_POST_CONVOLUTION_ALPHA_SCALE_EXT = 32799
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1137
try:
    GL_POST_CONVOLUTION_RED_BIAS_EXT = 32800
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1138
try:
    GL_POST_CONVOLUTION_GREEN_BIAS_EXT = 32801
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1139
try:
    GL_POST_CONVOLUTION_BLUE_BIAS_EXT = 32802
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1140
try:
    GL_POST_CONVOLUTION_ALPHA_BIAS_EXT = 32803
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1144
try:
    GL_COLOR_MATRIX_SGI = 32945
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1145
try:
    GL_COLOR_MATRIX_STACK_DEPTH_SGI = 32946
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1146
try:
    GL_MAX_COLOR_MATRIX_STACK_DEPTH_SGI = 32947
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1147
try:
    GL_POST_COLOR_MATRIX_RED_SCALE_SGI = 32948
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1148
try:
    GL_POST_COLOR_MATRIX_GREEN_SCALE_SGI = 32949
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1149
try:
    GL_POST_COLOR_MATRIX_BLUE_SCALE_SGI = 32950
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1150
try:
    GL_POST_COLOR_MATRIX_ALPHA_SCALE_SGI = 32951
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1151
try:
    GL_POST_COLOR_MATRIX_RED_BIAS_SGI = 32952
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1152
try:
    GL_POST_COLOR_MATRIX_GREEN_BIAS_SGI = 32953
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1153
try:
    GL_POST_COLOR_MATRIX_BLUE_BIAS_SGI = 32954
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1154
try:
    GL_POST_COLOR_MATRIX_ALPHA_BIAS_SGI = 32955
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1158
try:
    GL_COLOR_TABLE_SGI = 32976
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1159
try:
    GL_POST_CONVOLUTION_COLOR_TABLE_SGI = 32977
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1160
try:
    GL_POST_COLOR_MATRIX_COLOR_TABLE_SGI = 32978
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1161
try:
    GL_PROXY_COLOR_TABLE_SGI = 32979
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1162
try:
    GL_PROXY_POST_CONVOLUTION_COLOR_TABLE_SGI = 32980
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1163
try:
    GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE_SGI = 32981
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1164
try:
    GL_COLOR_TABLE_SCALE_SGI = 32982
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1165
try:
    GL_COLOR_TABLE_BIAS_SGI = 32983
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1166
try:
    GL_COLOR_TABLE_FORMAT_SGI = 32984
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1167
try:
    GL_COLOR_TABLE_WIDTH_SGI = 32985
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1168
try:
    GL_COLOR_TABLE_RED_SIZE_SGI = 32986
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1169
try:
    GL_COLOR_TABLE_GREEN_SIZE_SGI = 32987
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1170
try:
    GL_COLOR_TABLE_BLUE_SIZE_SGI = 32988
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1171
try:
    GL_COLOR_TABLE_ALPHA_SIZE_SGI = 32989
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1172
try:
    GL_COLOR_TABLE_LUMINANCE_SIZE_SGI = 32990
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1173
try:
    GL_COLOR_TABLE_INTENSITY_SIZE_SGI = 32991
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1177
try:
    GL_PIXEL_TEXTURE_SGIS = 33619
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1178
try:
    GL_PIXEL_FRAGMENT_RGB_SOURCE_SGIS = 33620
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1179
try:
    GL_PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS = 33621
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1180
try:
    GL_PIXEL_GROUP_COLOR_SGIS = 33622
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1184
try:
    GL_PIXEL_TEX_GEN_SGIX = 33081
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1185
try:
    GL_PIXEL_TEX_GEN_MODE_SGIX = 33579
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1189
try:
    GL_PACK_SKIP_VOLUMES_SGIS = 33072
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1190
try:
    GL_PACK_IMAGE_DEPTH_SGIS = 33073
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1191
try:
    GL_UNPACK_SKIP_VOLUMES_SGIS = 33074
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1192
try:
    GL_UNPACK_IMAGE_DEPTH_SGIS = 33075
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1193
try:
    GL_TEXTURE_4D_SGIS = 33076
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1194
try:
    GL_PROXY_TEXTURE_4D_SGIS = 33077
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1195
try:
    GL_TEXTURE_4DSIZE_SGIS = 33078
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1196
try:
    GL_TEXTURE_WRAP_Q_SGIS = 33079
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1197
try:
    GL_MAX_4D_TEXTURE_SIZE_SGIS = 33080
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1198
try:
    GL_TEXTURE_4D_BINDING_SGIS = 33103
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1202
try:
    GL_TEXTURE_COLOR_TABLE_SGI = 32956
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1203
try:
    GL_PROXY_TEXTURE_COLOR_TABLE_SGI = 32957
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1207
try:
    GL_CMYK_EXT = 32780
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1208
try:
    GL_CMYKA_EXT = 32781
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1209
try:
    GL_PACK_CMYK_HINT_EXT = 32782
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1210
try:
    GL_UNPACK_CMYK_HINT_EXT = 32783
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1214
try:
    GL_TEXTURE_PRIORITY_EXT = 32870
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1215
try:
    GL_TEXTURE_RESIDENT_EXT = 32871
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1216
try:
    GL_TEXTURE_1D_BINDING_EXT = 32872
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1217
try:
    GL_TEXTURE_2D_BINDING_EXT = 32873
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1218
try:
    GL_TEXTURE_3D_BINDING_EXT = 32874
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1222
try:
    GL_DETAIL_TEXTURE_2D_SGIS = 32917
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1223
try:
    GL_DETAIL_TEXTURE_2D_BINDING_SGIS = 32918
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1224
try:
    GL_LINEAR_DETAIL_SGIS = 32919
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1225
try:
    GL_LINEAR_DETAIL_ALPHA_SGIS = 32920
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1226
try:
    GL_LINEAR_DETAIL_COLOR_SGIS = 32921
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1227
try:
    GL_DETAIL_TEXTURE_LEVEL_SGIS = 32922
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1228
try:
    GL_DETAIL_TEXTURE_MODE_SGIS = 32923
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1229
try:
    GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS = 32924
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1233
try:
    GL_LINEAR_SHARPEN_SGIS = 32941
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1234
try:
    GL_LINEAR_SHARPEN_ALPHA_SGIS = 32942
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1235
try:
    GL_LINEAR_SHARPEN_COLOR_SGIS = 32943
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1236
try:
    GL_SHARPEN_TEXTURE_FUNC_POINTS_SGIS = 32944
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1240
try:
    GL_UNSIGNED_BYTE_3_3_2_EXT = 32818
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1241
try:
    GL_UNSIGNED_SHORT_4_4_4_4_EXT = 32819
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1242
try:
    GL_UNSIGNED_SHORT_5_5_5_1_EXT = 32820
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1243
try:
    GL_UNSIGNED_INT_8_8_8_8_EXT = 32821
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1244
try:
    GL_UNSIGNED_INT_10_10_10_2_EXT = 32822
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1248
try:
    GL_TEXTURE_MIN_LOD_SGIS = 33082
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1249
try:
    GL_TEXTURE_MAX_LOD_SGIS = 33083
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1250
try:
    GL_TEXTURE_BASE_LEVEL_SGIS = 33084
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1251
try:
    GL_TEXTURE_MAX_LEVEL_SGIS = 33085
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1255
try:
    GL_MULTISAMPLE_SGIS = 32925
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1256
try:
    GL_SAMPLE_ALPHA_TO_MASK_SGIS = 32926
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1257
try:
    GL_SAMPLE_ALPHA_TO_ONE_SGIS = 32927
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1258
try:
    GL_SAMPLE_MASK_SGIS = 32928
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1259
try:
    GL_1PASS_SGIS = 32929
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1260
try:
    GL_2PASS_0_SGIS = 32930
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1261
try:
    GL_2PASS_1_SGIS = 32931
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1262
try:
    GL_4PASS_0_SGIS = 32932
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1263
try:
    GL_4PASS_1_SGIS = 32933
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1264
try:
    GL_4PASS_2_SGIS = 32934
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1265
try:
    GL_4PASS_3_SGIS = 32935
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1266
try:
    GL_SAMPLE_BUFFERS_SGIS = 32936
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1267
try:
    GL_SAMPLES_SGIS = 32937
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1268
try:
    GL_SAMPLE_MASK_VALUE_SGIS = 32938
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1269
try:
    GL_SAMPLE_MASK_INVERT_SGIS = 32939
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1270
try:
    GL_SAMPLE_PATTERN_SGIS = 32940
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1274
try:
    GL_RESCALE_NORMAL_EXT = 32826
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1278
try:
    GL_VERTEX_ARRAY_EXT = 32884
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1279
try:
    GL_NORMAL_ARRAY_EXT = 32885
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1280
try:
    GL_COLOR_ARRAY_EXT = 32886
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1281
try:
    GL_INDEX_ARRAY_EXT = 32887
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1282
try:
    GL_TEXTURE_COORD_ARRAY_EXT = 32888
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1283
try:
    GL_EDGE_FLAG_ARRAY_EXT = 32889
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1284
try:
    GL_VERTEX_ARRAY_SIZE_EXT = 32890
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1285
try:
    GL_VERTEX_ARRAY_TYPE_EXT = 32891
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1286
try:
    GL_VERTEX_ARRAY_STRIDE_EXT = 32892
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1287
try:
    GL_VERTEX_ARRAY_COUNT_EXT = 32893
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1288
try:
    GL_NORMAL_ARRAY_TYPE_EXT = 32894
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1289
try:
    GL_NORMAL_ARRAY_STRIDE_EXT = 32895
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1290
try:
    GL_NORMAL_ARRAY_COUNT_EXT = 32896
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1291
try:
    GL_COLOR_ARRAY_SIZE_EXT = 32897
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1292
try:
    GL_COLOR_ARRAY_TYPE_EXT = 32898
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1293
try:
    GL_COLOR_ARRAY_STRIDE_EXT = 32899
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1294
try:
    GL_COLOR_ARRAY_COUNT_EXT = 32900
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1295
try:
    GL_INDEX_ARRAY_TYPE_EXT = 32901
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1296
try:
    GL_INDEX_ARRAY_STRIDE_EXT = 32902
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1297
try:
    GL_INDEX_ARRAY_COUNT_EXT = 32903
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1298
try:
    GL_TEXTURE_COORD_ARRAY_SIZE_EXT = 32904
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1299
try:
    GL_TEXTURE_COORD_ARRAY_TYPE_EXT = 32905
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1300
try:
    GL_TEXTURE_COORD_ARRAY_STRIDE_EXT = 32906
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1301
try:
    GL_TEXTURE_COORD_ARRAY_COUNT_EXT = 32907
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1302
try:
    GL_EDGE_FLAG_ARRAY_STRIDE_EXT = 32908
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1303
try:
    GL_EDGE_FLAG_ARRAY_COUNT_EXT = 32909
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1304
try:
    GL_VERTEX_ARRAY_POINTER_EXT = 32910
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1305
try:
    GL_NORMAL_ARRAY_POINTER_EXT = 32911
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1306
try:
    GL_COLOR_ARRAY_POINTER_EXT = 32912
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1307
try:
    GL_INDEX_ARRAY_POINTER_EXT = 32913
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1308
try:
    GL_TEXTURE_COORD_ARRAY_POINTER_EXT = 32914
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1309
try:
    GL_EDGE_FLAG_ARRAY_POINTER_EXT = 32915
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1316
try:
    GL_GENERATE_MIPMAP_SGIS = 33169
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1317
try:
    GL_GENERATE_MIPMAP_HINT_SGIS = 33170
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1321
try:
    GL_LINEAR_CLIPMAP_LINEAR_SGIX = 33136
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1322
try:
    GL_TEXTURE_CLIPMAP_CENTER_SGIX = 33137
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1323
try:
    GL_TEXTURE_CLIPMAP_FRAME_SGIX = 33138
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1324
try:
    GL_TEXTURE_CLIPMAP_OFFSET_SGIX = 33139
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1325
try:
    GL_TEXTURE_CLIPMAP_VIRTUAL_DEPTH_SGIX = 33140
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1326
try:
    GL_TEXTURE_CLIPMAP_LOD_OFFSET_SGIX = 33141
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1327
try:
    GL_TEXTURE_CLIPMAP_DEPTH_SGIX = 33142
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1328
try:
    GL_MAX_CLIPMAP_DEPTH_SGIX = 33143
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1329
try:
    GL_MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX = 33144
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1330
try:
    GL_NEAREST_CLIPMAP_NEAREST_SGIX = 33869
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1331
try:
    GL_NEAREST_CLIPMAP_LINEAR_SGIX = 33870
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1332
try:
    GL_LINEAR_CLIPMAP_NEAREST_SGIX = 33871
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1336
try:
    GL_TEXTURE_COMPARE_SGIX = 33178
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1337
try:
    GL_TEXTURE_COMPARE_OPERATOR_SGIX = 33179
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1338
try:
    GL_TEXTURE_LEQUAL_R_SGIX = 33180
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1339
try:
    GL_TEXTURE_GEQUAL_R_SGIX = 33181
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1343
try:
    GL_CLAMP_TO_EDGE_SGIS = 33071
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1347
try:
    GL_CLAMP_TO_BORDER_SGIS = 33069
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1351
try:
    GL_FUNC_ADD_EXT = 32774
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1352
try:
    GL_MIN_EXT = 32775
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1353
try:
    GL_MAX_EXT = 32776
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1354
try:
    GL_BLEND_EQUATION_EXT = 32777
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1358
try:
    GL_FUNC_SUBTRACT_EXT = 32778
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1359
try:
    GL_FUNC_REVERSE_SUBTRACT_EXT = 32779
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1366
try:
    GL_INTERLACE_SGIX = 32916
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1370
try:
    GL_PIXEL_TILE_BEST_ALIGNMENT_SGIX = 33086
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1371
try:
    GL_PIXEL_TILE_CACHE_INCREMENT_SGIX = 33087
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1372
try:
    GL_PIXEL_TILE_WIDTH_SGIX = 33088
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1373
try:
    GL_PIXEL_TILE_HEIGHT_SGIX = 33089
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1374
try:
    GL_PIXEL_TILE_GRID_WIDTH_SGIX = 33090
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1375
try:
    GL_PIXEL_TILE_GRID_HEIGHT_SGIX = 33091
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1376
try:
    GL_PIXEL_TILE_GRID_DEPTH_SGIX = 33092
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1377
try:
    GL_PIXEL_TILE_CACHE_SIZE_SGIX = 33093
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1381
try:
    GL_DUAL_ALPHA4_SGIS = 33040
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1382
try:
    GL_DUAL_ALPHA8_SGIS = 33041
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1383
try:
    GL_DUAL_ALPHA12_SGIS = 33042
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1384
try:
    GL_DUAL_ALPHA16_SGIS = 33043
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1385
try:
    GL_DUAL_LUMINANCE4_SGIS = 33044
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1386
try:
    GL_DUAL_LUMINANCE8_SGIS = 33045
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1387
try:
    GL_DUAL_LUMINANCE12_SGIS = 33046
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1388
try:
    GL_DUAL_LUMINANCE16_SGIS = 33047
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1389
try:
    GL_DUAL_INTENSITY4_SGIS = 33048
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1390
try:
    GL_DUAL_INTENSITY8_SGIS = 33049
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1391
try:
    GL_DUAL_INTENSITY12_SGIS = 33050
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1392
try:
    GL_DUAL_INTENSITY16_SGIS = 33051
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1393
try:
    GL_DUAL_LUMINANCE_ALPHA4_SGIS = 33052
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1394
try:
    GL_DUAL_LUMINANCE_ALPHA8_SGIS = 33053
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1395
try:
    GL_QUAD_ALPHA4_SGIS = 33054
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1396
try:
    GL_QUAD_ALPHA8_SGIS = 33055
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1397
try:
    GL_QUAD_LUMINANCE4_SGIS = 33056
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1398
try:
    GL_QUAD_LUMINANCE8_SGIS = 33057
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1399
try:
    GL_QUAD_INTENSITY4_SGIS = 33058
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1400
try:
    GL_QUAD_INTENSITY8_SGIS = 33059
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1401
try:
    GL_DUAL_TEXTURE_SELECT_SGIS = 33060
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1402
try:
    GL_QUAD_TEXTURE_SELECT_SGIS = 33061
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1406
try:
    GL_SPRITE_SGIX = 33096
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1407
try:
    GL_SPRITE_MODE_SGIX = 33097
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1408
try:
    GL_SPRITE_AXIS_SGIX = 33098
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1409
try:
    GL_SPRITE_TRANSLATION_SGIX = 33099
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1410
try:
    GL_SPRITE_AXIAL_SGIX = 33100
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1411
try:
    GL_SPRITE_OBJECT_ALIGNED_SGIX = 33101
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1412
try:
    GL_SPRITE_EYE_ALIGNED_SGIX = 33102
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1416
try:
    GL_TEXTURE_MULTI_BUFFER_HINT_SGIX = 33070
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1420
try:
    GL_POINT_SIZE_MIN_EXT = 33062
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1421
try:
    GL_POINT_SIZE_MAX_EXT = 33063
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1422
try:
    GL_POINT_FADE_THRESHOLD_SIZE_EXT = 33064
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1423
try:
    GL_DISTANCE_ATTENUATION_EXT = 33065
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1427
try:
    GL_POINT_SIZE_MIN_SGIS = 33062
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1428
try:
    GL_POINT_SIZE_MAX_SGIS = 33063
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1429
try:
    GL_POINT_FADE_THRESHOLD_SIZE_SGIS = 33064
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1430
try:
    GL_DISTANCE_ATTENUATION_SGIS = 33065
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1434
try:
    GL_INSTRUMENT_BUFFER_POINTER_SGIX = 33152
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1435
try:
    GL_INSTRUMENT_MEASUREMENTS_SGIX = 33153
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1439
try:
    GL_POST_TEXTURE_FILTER_BIAS_SGIX = 33145
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1440
try:
    GL_POST_TEXTURE_FILTER_SCALE_SGIX = 33146
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1441
try:
    GL_POST_TEXTURE_FILTER_BIAS_RANGE_SGIX = 33147
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1442
try:
    GL_POST_TEXTURE_FILTER_SCALE_RANGE_SGIX = 33148
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1446
try:
    GL_FRAMEZOOM_SGIX = 33163
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1447
try:
    GL_FRAMEZOOM_FACTOR_SGIX = 33164
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1448
try:
    GL_MAX_FRAMEZOOM_FACTOR_SGIX = 33165
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1455
try:
    GL_TEXTURE_DEFORMATION_BIT_SGIX = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1456
try:
    GL_GEOMETRY_DEFORMATION_BIT_SGIX = 2
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1460
try:
    GL_GEOMETRY_DEFORMATION_SGIX = 33172
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1461
try:
    GL_TEXTURE_DEFORMATION_SGIX = 33173
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1462
try:
    GL_DEFORMATIONS_MASK_SGIX = 33174
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1463
try:
    GL_MAX_DEFORMATION_ORDER_SGIX = 33175
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1467
try:
    GL_REFERENCE_PLANE_SGIX = 33149
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1468
try:
    GL_REFERENCE_PLANE_EQUATION_SGIX = 33150
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1475
try:
    GL_DEPTH_COMPONENT16_SGIX = 33189
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1476
try:
    GL_DEPTH_COMPONENT24_SGIX = 33190
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1477
try:
    GL_DEPTH_COMPONENT32_SGIX = 33191
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1481
try:
    GL_FOG_FUNC_SGIS = 33066
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1482
try:
    GL_FOG_FUNC_POINTS_SGIS = 33067
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1483
try:
    GL_MAX_FOG_FUNC_POINTS_SGIS = 33068
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1487
try:
    GL_FOG_OFFSET_SGIX = 33176
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1488
try:
    GL_FOG_OFFSET_VALUE_SGIX = 33177
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1492
try:
    GL_IMAGE_SCALE_X_HP = 33109
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1493
try:
    GL_IMAGE_SCALE_Y_HP = 33110
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1494
try:
    GL_IMAGE_TRANSLATE_X_HP = 33111
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1495
try:
    GL_IMAGE_TRANSLATE_Y_HP = 33112
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1496
try:
    GL_IMAGE_ROTATE_ANGLE_HP = 33113
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1497
try:
    GL_IMAGE_ROTATE_ORIGIN_X_HP = 33114
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1498
try:
    GL_IMAGE_ROTATE_ORIGIN_Y_HP = 33115
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1499
try:
    GL_IMAGE_MAG_FILTER_HP = 33116
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1500
try:
    GL_IMAGE_MIN_FILTER_HP = 33117
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1501
try:
    GL_IMAGE_CUBIC_WEIGHT_HP = 33118
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1502
try:
    GL_CUBIC_HP = 33119
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1503
try:
    GL_AVERAGE_HP = 33120
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1504
try:
    GL_IMAGE_TRANSFORM_2D_HP = 33121
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1505
try:
    GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP = 33122
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1506
try:
    GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP = 33123
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1510
try:
    GL_IGNORE_BORDER_HP = 33104
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1511
try:
    GL_CONSTANT_BORDER_HP = 33105
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1512
try:
    GL_REPLICATE_BORDER_HP = 33107
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1513
try:
    GL_CONVOLUTION_BORDER_COLOR_HP = 33108
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1520
try:
    GL_TEXTURE_ENV_BIAS_SGIX = 32958
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1527
try:
    GL_VERTEX_DATA_HINT_PGI = 107050
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1528
try:
    GL_VERTEX_CONSISTENT_HINT_PGI = 107051
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1529
try:
    GL_MATERIAL_SIDE_HINT_PGI = 107052
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1530
try:
    GL_MAX_VERTEX_HINT_PGI = 107053
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1531
try:
    GL_COLOR3_BIT_PGI = 65536
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1532
try:
    GL_COLOR4_BIT_PGI = 131072
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1533
try:
    GL_EDGEFLAG_BIT_PGI = 262144
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1534
try:
    GL_INDEX_BIT_PGI = 524288
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1535
try:
    GL_MAT_AMBIENT_BIT_PGI = 1048576
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1536
try:
    GL_MAT_AMBIENT_AND_DIFFUSE_BIT_PGI = 2097152
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1537
try:
    GL_MAT_DIFFUSE_BIT_PGI = 4194304
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1538
try:
    GL_MAT_EMISSION_BIT_PGI = 8388608
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1539
try:
    GL_MAT_COLOR_INDEXES_BIT_PGI = 16777216
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1540
try:
    GL_MAT_SHININESS_BIT_PGI = 33554432
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1541
try:
    GL_MAT_SPECULAR_BIT_PGI = 67108864
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1542
try:
    GL_NORMAL_BIT_PGI = 134217728
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1543
try:
    GL_TEXCOORD1_BIT_PGI = 268435456
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1544
try:
    GL_TEXCOORD2_BIT_PGI = 536870912
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1545
try:
    GL_TEXCOORD3_BIT_PGI = 1073741824
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1546
try:
    GL_TEXCOORD4_BIT_PGI = 2147483648
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1547
try:
    GL_VERTEX23_BIT_PGI = 4
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1548
try:
    GL_VERTEX4_BIT_PGI = 8
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1552
try:
    GL_PREFER_DOUBLEBUFFER_HINT_PGI = 107000
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1553
try:
    GL_CONSERVE_MEMORY_HINT_PGI = 107005
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1554
try:
    GL_RECLAIM_MEMORY_HINT_PGI = 107006
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1555
try:
    GL_NATIVE_GRAPHICS_HANDLE_PGI = 107010
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1556
try:
    GL_NATIVE_GRAPHICS_BEGIN_HINT_PGI = 107011
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1557
try:
    GL_NATIVE_GRAPHICS_END_HINT_PGI = 107012
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1558
try:
    GL_ALWAYS_FAST_HINT_PGI = 107020
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1559
try:
    GL_ALWAYS_SOFT_HINT_PGI = 107021
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1560
try:
    GL_ALLOW_DRAW_OBJ_HINT_PGI = 107022
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1561
try:
    GL_ALLOW_DRAW_WIN_HINT_PGI = 107023
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1562
try:
    GL_ALLOW_DRAW_FRG_HINT_PGI = 107024
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1563
try:
    GL_ALLOW_DRAW_MEM_HINT_PGI = 107025
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1564
try:
    GL_STRICT_DEPTHFUNC_HINT_PGI = 107030
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1565
try:
    GL_STRICT_LIGHTING_HINT_PGI = 107031
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1566
try:
    GL_STRICT_SCISSOR_HINT_PGI = 107032
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1567
try:
    GL_FULL_STIPPLE_HINT_PGI = 107033
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1568
try:
    GL_CLIP_NEAR_HINT_PGI = 107040
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1569
try:
    GL_CLIP_FAR_HINT_PGI = 107041
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1570
try:
    GL_WIDE_LINE_HINT_PGI = 107042
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1571
try:
    GL_BACK_NORMALS_HINT_PGI = 107043
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1575
try:
    GL_COLOR_INDEX1_EXT = 32994
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1576
try:
    GL_COLOR_INDEX2_EXT = 32995
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1577
try:
    GL_COLOR_INDEX4_EXT = 32996
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1578
try:
    GL_COLOR_INDEX8_EXT = 32997
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1579
try:
    GL_COLOR_INDEX12_EXT = 32998
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1580
try:
    GL_COLOR_INDEX16_EXT = 32999
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1581
try:
    GL_TEXTURE_INDEX_SIZE_EXT = 33005
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1585
try:
    GL_CLIP_VOLUME_CLIPPING_HINT_EXT = 33008
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1589
try:
    GL_LIST_PRIORITY_SGIX = 33154
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1593
try:
    GL_IR_INSTRUMENT1_SGIX = 33151
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1597
try:
    GL_CALLIGRAPHIC_FRAGMENT_SGIX = 33155
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1601
try:
    GL_TEXTURE_LOD_BIAS_S_SGIX = 33166
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1602
try:
    GL_TEXTURE_LOD_BIAS_T_SGIX = 33167
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1603
try:
    GL_TEXTURE_LOD_BIAS_R_SGIX = 33168
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1607
try:
    GL_SHADOW_AMBIENT_SGIX = 32959
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1614
try:
    GL_INDEX_MATERIAL_EXT = 33208
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1615
try:
    GL_INDEX_MATERIAL_PARAMETER_EXT = 33209
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1616
try:
    GL_INDEX_MATERIAL_FACE_EXT = 33210
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1620
try:
    GL_INDEX_TEST_EXT = 33205
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1621
try:
    GL_INDEX_TEST_FUNC_EXT = 33206
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1622
try:
    GL_INDEX_TEST_REF_EXT = 33207
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1626
try:
    GL_IUI_V2F_EXT = 33197
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1627
try:
    GL_IUI_V3F_EXT = 33198
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1628
try:
    GL_IUI_N3F_V2F_EXT = 33199
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1629
try:
    GL_IUI_N3F_V3F_EXT = 33200
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1630
try:
    GL_T2F_IUI_V2F_EXT = 33201
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1631
try:
    GL_T2F_IUI_V3F_EXT = 33202
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1632
try:
    GL_T2F_IUI_N3F_V2F_EXT = 33203
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1633
try:
    GL_T2F_IUI_N3F_V3F_EXT = 33204
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1637
try:
    GL_ARRAY_ELEMENT_LOCK_FIRST_EXT = 33192
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1638
try:
    GL_ARRAY_ELEMENT_LOCK_COUNT_EXT = 33193
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1642
try:
    GL_CULL_VERTEX_EXT = 33194
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1643
try:
    GL_CULL_VERTEX_EYE_POSITION_EXT = 33195
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1644
try:
    GL_CULL_VERTEX_OBJECT_POSITION_EXT = 33196
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1648
try:
    GL_YCRCB_422_SGIX = 33211
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1649
try:
    GL_YCRCB_444_SGIX = 33212
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1653
try:
    GL_FRAGMENT_LIGHTING_SGIX = 33792
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1654
try:
    GL_FRAGMENT_COLOR_MATERIAL_SGIX = 33793
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1655
try:
    GL_FRAGMENT_COLOR_MATERIAL_FACE_SGIX = 33794
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1656
try:
    GL_FRAGMENT_COLOR_MATERIAL_PARAMETER_SGIX = 33795
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1657
try:
    GL_MAX_FRAGMENT_LIGHTS_SGIX = 33796
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1658
try:
    GL_MAX_ACTIVE_LIGHTS_SGIX = 33797
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1659
try:
    GL_CURRENT_RASTER_NORMAL_SGIX = 33798
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1660
try:
    GL_LIGHT_ENV_MODE_SGIX = 33799
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1661
try:
    GL_FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_SGIX = 33800
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1662
try:
    GL_FRAGMENT_LIGHT_MODEL_TWO_SIDE_SGIX = 33801
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1663
try:
    GL_FRAGMENT_LIGHT_MODEL_AMBIENT_SGIX = 33802
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1664
try:
    GL_FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_SGIX = 33803
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1665
try:
    GL_FRAGMENT_LIGHT0_SGIX = 33804
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1666
try:
    GL_FRAGMENT_LIGHT1_SGIX = 33805
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1667
try:
    GL_FRAGMENT_LIGHT2_SGIX = 33806
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1668
try:
    GL_FRAGMENT_LIGHT3_SGIX = 33807
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1669
try:
    GL_FRAGMENT_LIGHT4_SGIX = 33808
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1670
try:
    GL_FRAGMENT_LIGHT5_SGIX = 33809
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1671
try:
    GL_FRAGMENT_LIGHT6_SGIX = 33810
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1672
try:
    GL_FRAGMENT_LIGHT7_SGIX = 33811
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1676
try:
    GL_RASTER_POSITION_UNCLIPPED_IBM = 103010
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1680
try:
    GL_TEXTURE_LIGHTING_MODE_HP = 33127
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1681
try:
    GL_TEXTURE_POST_SPECULAR_HP = 33128
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1682
try:
    GL_TEXTURE_PRE_SPECULAR_HP = 33129
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1686
try:
    GL_MAX_ELEMENTS_VERTICES_EXT = 33000
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1687
try:
    GL_MAX_ELEMENTS_INDICES_EXT = 33001
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1691
try:
    GL_PHONG_WIN = 33002
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1692
try:
    GL_PHONG_HINT_WIN = 33003
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1696
try:
    GL_FOG_SPECULAR_TEXTURE_WIN = 33004
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1700
try:
    GL_FRAGMENT_MATERIAL_EXT = 33609
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1701
try:
    GL_FRAGMENT_NORMAL_EXT = 33610
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1702
try:
    GL_FRAGMENT_COLOR_EXT = 33612
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1703
try:
    GL_ATTENUATION_EXT = 33613
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1704
try:
    GL_SHADOW_ATTENUATION_EXT = 33614
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1705
try:
    GL_TEXTURE_APPLICATION_MODE_EXT = 33615
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1706
try:
    GL_TEXTURE_LIGHT_EXT = 33616
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1707
try:
    GL_TEXTURE_MATERIAL_FACE_EXT = 33617
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1708
try:
    GL_TEXTURE_MATERIAL_PARAMETER_EXT = 33618
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1713
try:
    GL_ALPHA_MIN_SGIX = 33568
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1714
try:
    GL_ALPHA_MAX_SGIX = 33569
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1718
try:
    GL_PIXEL_TEX_GEN_Q_CEILING_SGIX = 33156
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1719
try:
    GL_PIXEL_TEX_GEN_Q_ROUND_SGIX = 33157
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1720
try:
    GL_PIXEL_TEX_GEN_Q_FLOOR_SGIX = 33158
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1721
try:
    GL_PIXEL_TEX_GEN_ALPHA_REPLACE_SGIX = 33159
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1722
try:
    GL_PIXEL_TEX_GEN_ALPHA_NO_REPLACE_SGIX = 33160
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1723
try:
    GL_PIXEL_TEX_GEN_ALPHA_LS_SGIX = 33161
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1724
try:
    GL_PIXEL_TEX_GEN_ALPHA_MS_SGIX = 33162
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1728
try:
    GL_BGR_EXT = 32992
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1729
try:
    GL_BGRA_EXT = 32993
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1733
try:
    GL_ASYNC_MARKER_SGIX = 33577
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1737
try:
    GL_ASYNC_TEX_IMAGE_SGIX = 33628
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1738
try:
    GL_ASYNC_DRAW_PIXELS_SGIX = 33629
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1739
try:
    GL_ASYNC_READ_PIXELS_SGIX = 33630
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1740
try:
    GL_MAX_ASYNC_TEX_IMAGE_SGIX = 33631
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1741
try:
    GL_MAX_ASYNC_DRAW_PIXELS_SGIX = 33632
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1742
try:
    GL_MAX_ASYNC_READ_PIXELS_SGIX = 33633
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1746
try:
    GL_ASYNC_HISTOGRAM_SGIX = 33580
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1747
try:
    GL_MAX_ASYNC_HISTOGRAM_SGIX = 33581
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1754
try:
    GL_PARALLEL_ARRAYS_INTEL = 33780
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1755
try:
    GL_VERTEX_ARRAY_PARALLEL_POINTERS_INTEL = 33781
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1756
try:
    GL_NORMAL_ARRAY_PARALLEL_POINTERS_INTEL = 33782
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1757
try:
    GL_COLOR_ARRAY_PARALLEL_POINTERS_INTEL = 33783
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1758
try:
    GL_TEXTURE_COORD_ARRAY_PARALLEL_POINTERS_INTEL = 33784
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1762
try:
    GL_OCCLUSION_TEST_HP = 33125
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1763
try:
    GL_OCCLUSION_TEST_RESULT_HP = 33126
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1767
try:
    GL_PIXEL_TRANSFORM_2D_EXT = 33584
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1768
try:
    GL_PIXEL_MAG_FILTER_EXT = 33585
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1769
try:
    GL_PIXEL_MIN_FILTER_EXT = 33586
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1770
try:
    GL_PIXEL_CUBIC_WEIGHT_EXT = 33587
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1771
try:
    GL_CUBIC_EXT = 33588
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1772
try:
    GL_AVERAGE_EXT = 33589
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1773
try:
    GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT = 33590
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1774
try:
    GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT = 33591
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1775
try:
    GL_PIXEL_TRANSFORM_2D_MATRIX_EXT = 33592
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1782
try:
    GL_SHARED_TEXTURE_PALETTE_EXT = 33275
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1786
try:
    GL_LIGHT_MODEL_COLOR_CONTROL_EXT = 33272
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1787
try:
    GL_SINGLE_COLOR_EXT = 33273
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1788
try:
    GL_SEPARATE_SPECULAR_COLOR_EXT = 33274
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1792
try:
    GL_COLOR_SUM_EXT = 33880
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1793
try:
    GL_CURRENT_SECONDARY_COLOR_EXT = 33881
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1794
try:
    GL_SECONDARY_COLOR_ARRAY_SIZE_EXT = 33882
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1795
try:
    GL_SECONDARY_COLOR_ARRAY_TYPE_EXT = 33883
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1796
try:
    GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT = 33884
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1797
try:
    GL_SECONDARY_COLOR_ARRAY_POINTER_EXT = 33885
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1798
try:
    GL_SECONDARY_COLOR_ARRAY_EXT = 33886
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1802
try:
    GL_PERTURB_EXT = 34222
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1803
try:
    GL_TEXTURE_NORMAL_EXT = 34223
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1810
try:
    GL_FOG_COORDINATE_SOURCE_EXT = 33872
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1811
try:
    GL_FOG_COORDINATE_EXT = 33873
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1812
try:
    GL_FRAGMENT_DEPTH_EXT = 33874
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1813
try:
    GL_CURRENT_FOG_COORDINATE_EXT = 33875
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1814
try:
    GL_FOG_COORDINATE_ARRAY_TYPE_EXT = 33876
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1815
try:
    GL_FOG_COORDINATE_ARRAY_STRIDE_EXT = 33877
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1816
try:
    GL_FOG_COORDINATE_ARRAY_POINTER_EXT = 33878
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1817
try:
    GL_FOG_COORDINATE_ARRAY_EXT = 33879
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1821
try:
    GL_SCREEN_COORDINATES_REND = 33936
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1822
try:
    GL_INVERTED_SCREEN_W_REND = 33937
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1826
try:
    GL_TANGENT_ARRAY_EXT = 33849
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1827
try:
    GL_BINORMAL_ARRAY_EXT = 33850
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1828
try:
    GL_CURRENT_TANGENT_EXT = 33851
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1829
try:
    GL_CURRENT_BINORMAL_EXT = 33852
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1830
try:
    GL_TANGENT_ARRAY_TYPE_EXT = 33854
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1831
try:
    GL_TANGENT_ARRAY_STRIDE_EXT = 33855
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1832
try:
    GL_BINORMAL_ARRAY_TYPE_EXT = 33856
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1833
try:
    GL_BINORMAL_ARRAY_STRIDE_EXT = 33857
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1834
try:
    GL_TANGENT_ARRAY_POINTER_EXT = 33858
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1835
try:
    GL_BINORMAL_ARRAY_POINTER_EXT = 33859
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1836
try:
    GL_MAP1_TANGENT_EXT = 33860
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1837
try:
    GL_MAP2_TANGENT_EXT = 33861
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1838
try:
    GL_MAP1_BINORMAL_EXT = 33862
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1839
try:
    GL_MAP2_BINORMAL_EXT = 33863
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1843
try:
    GL_COMBINE_EXT = 34160
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1844
try:
    GL_COMBINE_RGB_EXT = 34161
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1845
try:
    GL_COMBINE_ALPHA_EXT = 34162
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1846
try:
    GL_RGB_SCALE_EXT = 34163
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1847
try:
    GL_ADD_SIGNED_EXT = 34164
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1848
try:
    GL_INTERPOLATE_EXT = 34165
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1849
try:
    GL_CONSTANT_EXT = 34166
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1850
try:
    GL_PRIMARY_COLOR_EXT = 34167
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1851
try:
    GL_PREVIOUS_EXT = 34168
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1852
try:
    GL_SOURCE0_RGB_EXT = 34176
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1853
try:
    GL_SOURCE1_RGB_EXT = 34177
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1854
try:
    GL_SOURCE2_RGB_EXT = 34178
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1855
try:
    GL_SOURCE0_ALPHA_EXT = 34184
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1856
try:
    GL_SOURCE1_ALPHA_EXT = 34185
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1857
try:
    GL_SOURCE2_ALPHA_EXT = 34186
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1858
try:
    GL_OPERAND0_RGB_EXT = 34192
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1859
try:
    GL_OPERAND1_RGB_EXT = 34193
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1860
try:
    GL_OPERAND2_RGB_EXT = 34194
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1861
try:
    GL_OPERAND0_ALPHA_EXT = 34200
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1862
try:
    GL_OPERAND1_ALPHA_EXT = 34201
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1863
try:
    GL_OPERAND2_ALPHA_EXT = 34202
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1867
try:
    GL_LIGHT_MODEL_SPECULAR_VECTOR_APPLE = 34224
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1871
try:
    GL_TRANSFORM_HINT_APPLE = 34225
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1875
try:
    GL_FOG_SCALE_SGIX = 33276
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1876
try:
    GL_FOG_SCALE_VALUE_SGIX = 33277
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1880
try:
    GL_UNPACK_CONSTANT_DATA_SUNX = 33237
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1881
try:
    GL_TEXTURE_CONSTANT_DATA_SUNX = 33238
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1885
try:
    GL_GLOBAL_ALPHA_SUN = 33241
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1886
try:
    GL_GLOBAL_ALPHA_FACTOR_SUN = 33242
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1890
try:
    GL_RESTART_SUN = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1891
try:
    GL_REPLACE_MIDDLE_SUN = 2
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1892
try:
    GL_REPLACE_OLDEST_SUN = 3
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1893
try:
    GL_TRIANGLE_LIST_SUN = 33239
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1894
try:
    GL_REPLACEMENT_CODE_SUN = 33240
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1895
try:
    GL_REPLACEMENT_CODE_ARRAY_SUN = 34240
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1896
try:
    GL_REPLACEMENT_CODE_ARRAY_TYPE_SUN = 34241
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1897
try:
    GL_REPLACEMENT_CODE_ARRAY_STRIDE_SUN = 34242
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1898
try:
    GL_REPLACEMENT_CODE_ARRAY_POINTER_SUN = 34243
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1899
try:
    GL_R1UI_V3F_SUN = 34244
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1900
try:
    GL_R1UI_C4UB_V3F_SUN = 34245
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1901
try:
    GL_R1UI_C3F_V3F_SUN = 34246
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1902
try:
    GL_R1UI_N3F_V3F_SUN = 34247
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1903
try:
    GL_R1UI_C4F_N3F_V3F_SUN = 34248
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1904
try:
    GL_R1UI_T2F_V3F_SUN = 34249
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1905
try:
    GL_R1UI_T2F_N3F_V3F_SUN = 34250
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1906
try:
    GL_R1UI_T2F_C4F_N3F_V3F_SUN = 34251
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1913
try:
    GL_BLEND_DST_RGB_EXT = 32968
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1914
try:
    GL_BLEND_SRC_RGB_EXT = 32969
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1915
try:
    GL_BLEND_DST_ALPHA_EXT = 32970
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1916
try:
    GL_BLEND_SRC_ALPHA_EXT = 32971
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1920
try:
    GL_RED_MIN_CLAMP_INGR = 34144
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1921
try:
    GL_GREEN_MIN_CLAMP_INGR = 34145
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1922
try:
    GL_BLUE_MIN_CLAMP_INGR = 34146
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1923
try:
    GL_ALPHA_MIN_CLAMP_INGR = 34147
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1924
try:
    GL_RED_MAX_CLAMP_INGR = 34148
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1925
try:
    GL_GREEN_MAX_CLAMP_INGR = 34149
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1926
try:
    GL_BLUE_MAX_CLAMP_INGR = 34150
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1927
try:
    GL_ALPHA_MAX_CLAMP_INGR = 34151
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1931
try:
    GL_INTERLACE_READ_INGR = 34152
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1935
try:
    GL_INCR_WRAP_EXT = 34055
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1936
try:
    GL_DECR_WRAP_EXT = 34056
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1940
try:
    GL_422_EXT = 32972
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1941
try:
    GL_422_REV_EXT = 32973
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1942
try:
    GL_422_AVERAGE_EXT = 32974
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1943
try:
    GL_422_REV_AVERAGE_EXT = 32975
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1947
try:
    GL_NORMAL_MAP_NV = 34065
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1948
try:
    GL_REFLECTION_MAP_NV = 34066
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1952
try:
    GL_NORMAL_MAP_EXT = 34065
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1953
try:
    GL_REFLECTION_MAP_EXT = 34066
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1954
try:
    GL_TEXTURE_CUBE_MAP_EXT = 34067
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1955
try:
    GL_TEXTURE_BINDING_CUBE_MAP_EXT = 34068
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1956
try:
    GL_TEXTURE_CUBE_MAP_POSITIVE_X_EXT = 34069
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1957
try:
    GL_TEXTURE_CUBE_MAP_NEGATIVE_X_EXT = 34070
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1958
try:
    GL_TEXTURE_CUBE_MAP_POSITIVE_Y_EXT = 34071
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1959
try:
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_EXT = 34072
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1960
try:
    GL_TEXTURE_CUBE_MAP_POSITIVE_Z_EXT = 34073
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1961
try:
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_EXT = 34074
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1962
try:
    GL_PROXY_TEXTURE_CUBE_MAP_EXT = 34075
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1963
try:
    GL_MAX_CUBE_MAP_TEXTURE_SIZE_EXT = 34076
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1967
try:
    GL_WRAP_BORDER_SUN = 33236
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1974
try:
    GL_MAX_TEXTURE_LOD_BIAS_EXT = 34045
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1975
try:
    GL_TEXTURE_FILTER_CONTROL_EXT = 34048
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1976
try:
    GL_TEXTURE_LOD_BIAS_EXT = 34049
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1980
try:
    GL_TEXTURE_MAX_ANISOTROPY_EXT = 34046
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1981
try:
    GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT = 34047
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1985
try:
    GL_MODELVIEW0_STACK_DEPTH_EXT = GL_MODELVIEW_STACK_DEPTH
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1986
try:
    GL_MODELVIEW1_STACK_DEPTH_EXT = 34050
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1987
try:
    GL_MODELVIEW0_MATRIX_EXT = GL_MODELVIEW_MATRIX
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1988
try:
    GL_MODELVIEW1_MATRIX_EXT = 34054
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1989
try:
    GL_VERTEX_WEIGHTING_EXT = 34057
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1990
try:
    GL_MODELVIEW0_EXT = GL_MODELVIEW
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1991
try:
    GL_MODELVIEW1_EXT = 34058
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1992
try:
    GL_CURRENT_VERTEX_WEIGHT_EXT = 34059
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1993
try:
    GL_VERTEX_WEIGHT_ARRAY_EXT = 34060
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1994
try:
    GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT = 34061
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1995
try:
    GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT = 34062
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1996
try:
    GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT = 34063
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 1997
try:
    GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT = 34064
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2001
try:
    GL_MAX_SHININESS_NV = 34052
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2002
try:
    GL_MAX_SPOT_EXPONENT_NV = 34053
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2006
try:
    GL_VERTEX_ARRAY_RANGE_NV = 34077
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2007
try:
    GL_VERTEX_ARRAY_RANGE_LENGTH_NV = 34078
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2008
try:
    GL_VERTEX_ARRAY_RANGE_VALID_NV = 34079
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2009
try:
    GL_MAX_VERTEX_ARRAY_RANGE_ELEMENT_NV = 34080
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2010
try:
    GL_VERTEX_ARRAY_RANGE_POINTER_NV = 34081
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2014
try:
    GL_REGISTER_COMBINERS_NV = 34082
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2015
try:
    GL_VARIABLE_A_NV = 34083
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2016
try:
    GL_VARIABLE_B_NV = 34084
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2017
try:
    GL_VARIABLE_C_NV = 34085
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2018
try:
    GL_VARIABLE_D_NV = 34086
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2019
try:
    GL_VARIABLE_E_NV = 34087
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2020
try:
    GL_VARIABLE_F_NV = 34088
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2021
try:
    GL_VARIABLE_G_NV = 34089
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2022
try:
    GL_CONSTANT_COLOR0_NV = 34090
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2023
try:
    GL_CONSTANT_COLOR1_NV = 34091
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2024
try:
    GL_PRIMARY_COLOR_NV = 34092
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2025
try:
    GL_SECONDARY_COLOR_NV = 34093
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2026
try:
    GL_SPARE0_NV = 34094
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2027
try:
    GL_SPARE1_NV = 34095
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2028
try:
    GL_DISCARD_NV = 34096
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2029
try:
    GL_E_TIMES_F_NV = 34097
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2030
try:
    GL_SPARE0_PLUS_SECONDARY_COLOR_NV = 34098
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2031
try:
    GL_UNSIGNED_IDENTITY_NV = 34102
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2032
try:
    GL_UNSIGNED_INVERT_NV = 34103
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2033
try:
    GL_EXPAND_NORMAL_NV = 34104
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2034
try:
    GL_EXPAND_NEGATE_NV = 34105
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2035
try:
    GL_HALF_BIAS_NORMAL_NV = 34106
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2036
try:
    GL_HALF_BIAS_NEGATE_NV = 34107
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2037
try:
    GL_SIGNED_IDENTITY_NV = 34108
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2038
try:
    GL_SIGNED_NEGATE_NV = 34109
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2039
try:
    GL_SCALE_BY_TWO_NV = 34110
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2040
try:
    GL_SCALE_BY_FOUR_NV = 34111
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2041
try:
    GL_SCALE_BY_ONE_HALF_NV = 34112
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2042
try:
    GL_BIAS_BY_NEGATIVE_ONE_HALF_NV = 34113
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2043
try:
    GL_COMBINER_INPUT_NV = 34114
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2044
try:
    GL_COMBINER_MAPPING_NV = 34115
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2045
try:
    GL_COMBINER_COMPONENT_USAGE_NV = 34116
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2046
try:
    GL_COMBINER_AB_DOT_PRODUCT_NV = 34117
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2047
try:
    GL_COMBINER_CD_DOT_PRODUCT_NV = 34118
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2048
try:
    GL_COMBINER_MUX_SUM_NV = 34119
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2049
try:
    GL_COMBINER_SCALE_NV = 34120
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2050
try:
    GL_COMBINER_BIAS_NV = 34121
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2051
try:
    GL_COMBINER_AB_OUTPUT_NV = 34122
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2052
try:
    GL_COMBINER_CD_OUTPUT_NV = 34123
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2053
try:
    GL_COMBINER_SUM_OUTPUT_NV = 34124
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2054
try:
    GL_MAX_GENERAL_COMBINERS_NV = 34125
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2055
try:
    GL_NUM_GENERAL_COMBINERS_NV = 34126
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2056
try:
    GL_COLOR_SUM_CLAMP_NV = 34127
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2057
try:
    GL_COMBINER0_NV = 34128
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2058
try:
    GL_COMBINER1_NV = 34129
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2059
try:
    GL_COMBINER2_NV = 34130
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2060
try:
    GL_COMBINER3_NV = 34131
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2061
try:
    GL_COMBINER4_NV = 34132
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2062
try:
    GL_COMBINER5_NV = 34133
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2063
try:
    GL_COMBINER6_NV = 34134
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2064
try:
    GL_COMBINER7_NV = 34135
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2073
try:
    GL_FOG_DISTANCE_MODE_NV = 34138
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2074
try:
    GL_EYE_RADIAL_NV = 34139
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2075
try:
    GL_EYE_PLANE_ABSOLUTE_NV = 34140
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2080
try:
    GL_EMBOSS_LIGHT_NV = 34141
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2081
try:
    GL_EMBOSS_CONSTANT_NV = 34142
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2082
try:
    GL_EMBOSS_MAP_NV = 34143
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2089
try:
    GL_COMBINE4_NV = 34051
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2090
try:
    GL_SOURCE3_RGB_NV = 34179
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2091
try:
    GL_SOURCE3_ALPHA_NV = 34187
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2092
try:
    GL_OPERAND3_RGB_NV = 34195
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2093
try:
    GL_OPERAND3_ALPHA_NV = 34203
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2103
try:
    GL_COMPRESSED_RGB_S3TC_DXT1_EXT = 33776
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2104
try:
    GL_COMPRESSED_RGBA_S3TC_DXT1_EXT = 33777
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2105
try:
    GL_COMPRESSED_RGBA_S3TC_DXT3_EXT = 33778
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2106
try:
    GL_COMPRESSED_RGBA_S3TC_DXT5_EXT = 33779
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2110
try:
    GL_CULL_VERTEX_IBM = 103050
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2117
try:
    GL_VERTEX_ARRAY_LIST_IBM = 103070
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2118
try:
    GL_NORMAL_ARRAY_LIST_IBM = 103071
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2119
try:
    GL_COLOR_ARRAY_LIST_IBM = 103072
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2120
try:
    GL_INDEX_ARRAY_LIST_IBM = 103073
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2121
try:
    GL_TEXTURE_COORD_ARRAY_LIST_IBM = 103074
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2122
try:
    GL_EDGE_FLAG_ARRAY_LIST_IBM = 103075
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2123
try:
    GL_FOG_COORDINATE_ARRAY_LIST_IBM = 103076
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2124
try:
    GL_SECONDARY_COLOR_ARRAY_LIST_IBM = 103077
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2125
try:
    GL_VERTEX_ARRAY_LIST_STRIDE_IBM = 103080
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2126
try:
    GL_NORMAL_ARRAY_LIST_STRIDE_IBM = 103081
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2127
try:
    GL_COLOR_ARRAY_LIST_STRIDE_IBM = 103082
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2128
try:
    GL_INDEX_ARRAY_LIST_STRIDE_IBM = 103083
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2129
try:
    GL_TEXTURE_COORD_ARRAY_LIST_STRIDE_IBM = 103084
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2130
try:
    GL_EDGE_FLAG_ARRAY_LIST_STRIDE_IBM = 103085
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2131
try:
    GL_FOG_COORDINATE_ARRAY_LIST_STRIDE_IBM = 103086
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2132
try:
    GL_SECONDARY_COLOR_ARRAY_LIST_STRIDE_IBM = 103087
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2136
try:
    GL_PACK_SUBSAMPLE_RATE_SGIX = 34208
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2137
try:
    GL_UNPACK_SUBSAMPLE_RATE_SGIX = 34209
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2138
try:
    GL_PIXEL_SUBSAMPLE_4444_SGIX = 34210
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2139
try:
    GL_PIXEL_SUBSAMPLE_2424_SGIX = 34211
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2140
try:
    GL_PIXEL_SUBSAMPLE_4242_SGIX = 34212
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2147
try:
    GL_YCRCB_SGIX = 33560
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2148
try:
    GL_YCRCBA_SGIX = 33561
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2152
try:
    GL_DEPTH_PASS_INSTRUMENT_SGIX = 33552
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2153
try:
    GL_DEPTH_PASS_INSTRUMENT_COUNTERS_SGIX = 33553
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2154
try:
    GL_DEPTH_PASS_INSTRUMENT_MAX_SGIX = 33554
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2158
try:
    GL_COMPRESSED_RGB_FXT1_3DFX = 34480
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2159
try:
    GL_COMPRESSED_RGBA_FXT1_3DFX = 34481
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2163
try:
    GL_MULTISAMPLE_3DFX = 34482
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2164
try:
    GL_SAMPLE_BUFFERS_3DFX = 34483
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2165
try:
    GL_SAMPLES_3DFX = 34484
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2166
try:
    GL_MULTISAMPLE_BIT_3DFX = 536870912
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2173
try:
    GL_MULTISAMPLE_EXT = 32925
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2174
try:
    GL_SAMPLE_ALPHA_TO_MASK_EXT = 32926
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2175
try:
    GL_SAMPLE_ALPHA_TO_ONE_EXT = 32927
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2176
try:
    GL_SAMPLE_MASK_EXT = 32928
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2177
try:
    GL_1PASS_EXT = 32929
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2178
try:
    GL_2PASS_0_EXT = 32930
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2179
try:
    GL_2PASS_1_EXT = 32931
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2180
try:
    GL_4PASS_0_EXT = 32932
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2181
try:
    GL_4PASS_1_EXT = 32933
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2182
try:
    GL_4PASS_2_EXT = 32934
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2183
try:
    GL_4PASS_3_EXT = 32935
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2184
try:
    GL_SAMPLE_BUFFERS_EXT = 32936
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2185
try:
    GL_SAMPLES_EXT = 32937
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2186
try:
    GL_SAMPLE_MASK_VALUE_EXT = 32938
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2187
try:
    GL_SAMPLE_MASK_INVERT_EXT = 32939
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2188
try:
    GL_SAMPLE_PATTERN_EXT = 32940
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2189
try:
    GL_MULTISAMPLE_BIT_EXT = 536870912
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2193
try:
    GL_VERTEX_PRECLIP_SGIX = 33774
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2194
try:
    GL_VERTEX_PRECLIP_HINT_SGIX = 33775
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2198
try:
    GL_CONVOLUTION_HINT_SGIX = 33558
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2202
try:
    GL_PACK_RESAMPLE_SGIX = 33836
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2203
try:
    GL_UNPACK_RESAMPLE_SGIX = 33837
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2204
try:
    GL_RESAMPLE_REPLICATE_SGIX = 33838
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2205
try:
    GL_RESAMPLE_ZERO_FILL_SGIX = 33839
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2206
try:
    GL_RESAMPLE_DECIMATE_SGIX = 33840
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2210
try:
    GL_EYE_DISTANCE_TO_POINT_SGIS = 33264
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2211
try:
    GL_OBJECT_DISTANCE_TO_POINT_SGIS = 33265
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2212
try:
    GL_EYE_DISTANCE_TO_LINE_SGIS = 33266
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2213
try:
    GL_OBJECT_DISTANCE_TO_LINE_SGIS = 33267
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2214
try:
    GL_EYE_POINT_SGIS = 33268
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2215
try:
    GL_OBJECT_POINT_SGIS = 33269
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2216
try:
    GL_EYE_LINE_SGIS = 33270
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2217
try:
    GL_OBJECT_LINE_SGIS = 33271
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2221
try:
    GL_TEXTURE_COLOR_WRITEMASK_SGIS = 33263
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2225
try:
    GL_DOT3_RGB_EXT = 34624
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2226
try:
    GL_DOT3_RGBA_EXT = 34625
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2230
try:
    GL_MIRROR_CLAMP_ATI = 34626
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2231
try:
    GL_MIRROR_CLAMP_TO_EDGE_ATI = 34627
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2235
try:
    GL_ALL_COMPLETED_NV = 34034
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2236
try:
    GL_FENCE_STATUS_NV = 34035
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2237
try:
    GL_FENCE_CONDITION_NV = 34036
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2241
try:
    GL_MIRRORED_REPEAT_IBM = 33648
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2245
try:
    GL_EVAL_2D_NV = 34496
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2246
try:
    GL_EVAL_TRIANGULAR_2D_NV = 34497
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2247
try:
    GL_MAP_TESSELLATION_NV = 34498
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2248
try:
    GL_MAP_ATTRIB_U_ORDER_NV = 34499
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2249
try:
    GL_MAP_ATTRIB_V_ORDER_NV = 34500
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2250
try:
    GL_EVAL_FRACTIONAL_TESSELLATION_NV = 34501
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2251
try:
    GL_EVAL_VERTEX_ATTRIB0_NV = 34502
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2252
try:
    GL_EVAL_VERTEX_ATTRIB1_NV = 34503
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2253
try:
    GL_EVAL_VERTEX_ATTRIB2_NV = 34504
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2254
try:
    GL_EVAL_VERTEX_ATTRIB3_NV = 34505
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2255
try:
    GL_EVAL_VERTEX_ATTRIB4_NV = 34506
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2256
try:
    GL_EVAL_VERTEX_ATTRIB5_NV = 34507
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2257
try:
    GL_EVAL_VERTEX_ATTRIB6_NV = 34508
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2258
try:
    GL_EVAL_VERTEX_ATTRIB7_NV = 34509
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2259
try:
    GL_EVAL_VERTEX_ATTRIB8_NV = 34510
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2260
try:
    GL_EVAL_VERTEX_ATTRIB9_NV = 34511
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2261
try:
    GL_EVAL_VERTEX_ATTRIB10_NV = 34512
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2262
try:
    GL_EVAL_VERTEX_ATTRIB11_NV = 34513
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2263
try:
    GL_EVAL_VERTEX_ATTRIB12_NV = 34514
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2264
try:
    GL_EVAL_VERTEX_ATTRIB13_NV = 34515
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2265
try:
    GL_EVAL_VERTEX_ATTRIB14_NV = 34516
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2266
try:
    GL_EVAL_VERTEX_ATTRIB15_NV = 34517
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2267
try:
    GL_MAX_MAP_TESSELLATION_NV = 34518
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2268
try:
    GL_MAX_RATIONAL_EVAL_ORDER_NV = 34519
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2272
try:
    GL_DEPTH_STENCIL_NV = 34041
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2273
try:
    GL_UNSIGNED_INT_24_8_NV = 34042
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2277
try:
    GL_PER_STAGE_CONSTANTS_NV = 34101
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2284
try:
    GL_TEXTURE_RECTANGLE_NV = 34037
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2285
try:
    GL_TEXTURE_BINDING_RECTANGLE_NV = 34038
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2286
try:
    GL_PROXY_TEXTURE_RECTANGLE_NV = 34039
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2287
try:
    GL_MAX_RECTANGLE_TEXTURE_SIZE_NV = 34040
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2291
try:
    GL_OFFSET_TEXTURE_RECTANGLE_NV = 34380
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2292
try:
    GL_OFFSET_TEXTURE_RECTANGLE_SCALE_NV = 34381
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2293
try:
    GL_DOT_PRODUCT_TEXTURE_RECTANGLE_NV = 34382
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2294
try:
    GL_RGBA_UNSIGNED_DOT_PRODUCT_MAPPING_NV = 34521
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2295
try:
    GL_UNSIGNED_INT_S8_S8_8_8_NV = 34522
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2296
try:
    GL_UNSIGNED_INT_8_8_S8_S8_REV_NV = 34523
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2297
try:
    GL_DSDT_MAG_INTENSITY_NV = 34524
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2298
try:
    GL_SHADER_CONSISTENT_NV = 34525
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2299
try:
    GL_TEXTURE_SHADER_NV = 34526
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2300
try:
    GL_SHADER_OPERATION_NV = 34527
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2301
try:
    GL_CULL_MODES_NV = 34528
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2302
try:
    GL_OFFSET_TEXTURE_MATRIX_NV = 34529
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2303
try:
    GL_OFFSET_TEXTURE_SCALE_NV = 34530
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2304
try:
    GL_OFFSET_TEXTURE_BIAS_NV = 34531
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2305
try:
    GL_OFFSET_TEXTURE_2D_MATRIX_NV = GL_OFFSET_TEXTURE_MATRIX_NV
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2306
try:
    GL_OFFSET_TEXTURE_2D_SCALE_NV = GL_OFFSET_TEXTURE_SCALE_NV
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2307
try:
    GL_OFFSET_TEXTURE_2D_BIAS_NV = GL_OFFSET_TEXTURE_BIAS_NV
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2308
try:
    GL_PREVIOUS_TEXTURE_INPUT_NV = 34532
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2309
try:
    GL_CONST_EYE_NV = 34533
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2310
try:
    GL_PASS_THROUGH_NV = 34534
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2311
try:
    GL_CULL_FRAGMENT_NV = 34535
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2312
try:
    GL_OFFSET_TEXTURE_2D_NV = 34536
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2313
try:
    GL_DEPENDENT_AR_TEXTURE_2D_NV = 34537
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2314
try:
    GL_DEPENDENT_GB_TEXTURE_2D_NV = 34538
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2315
try:
    GL_DOT_PRODUCT_NV = 34540
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2316
try:
    GL_DOT_PRODUCT_DEPTH_REPLACE_NV = 34541
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2317
try:
    GL_DOT_PRODUCT_TEXTURE_2D_NV = 34542
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2318
try:
    GL_DOT_PRODUCT_TEXTURE_CUBE_MAP_NV = 34544
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2319
try:
    GL_DOT_PRODUCT_DIFFUSE_CUBE_MAP_NV = 34545
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2320
try:
    GL_DOT_PRODUCT_REFLECT_CUBE_MAP_NV = 34546
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2321
try:
    GL_DOT_PRODUCT_CONST_EYE_REFLECT_CUBE_MAP_NV = 34547
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2322
try:
    GL_HILO_NV = 34548
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2323
try:
    GL_DSDT_NV = 34549
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2324
try:
    GL_DSDT_MAG_NV = 34550
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2325
try:
    GL_DSDT_MAG_VIB_NV = 34551
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2326
try:
    GL_HILO16_NV = 34552
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2327
try:
    GL_SIGNED_HILO_NV = 34553
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2328
try:
    GL_SIGNED_HILO16_NV = 34554
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2329
try:
    GL_SIGNED_RGBA_NV = 34555
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2330
try:
    GL_SIGNED_RGBA8_NV = 34556
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2331
try:
    GL_SIGNED_RGB_NV = 34558
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2332
try:
    GL_SIGNED_RGB8_NV = 34559
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2333
try:
    GL_SIGNED_LUMINANCE_NV = 34561
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2334
try:
    GL_SIGNED_LUMINANCE8_NV = 34562
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2335
try:
    GL_SIGNED_LUMINANCE_ALPHA_NV = 34563
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2336
try:
    GL_SIGNED_LUMINANCE8_ALPHA8_NV = 34564
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2337
try:
    GL_SIGNED_ALPHA_NV = 34565
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2338
try:
    GL_SIGNED_ALPHA8_NV = 34566
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2339
try:
    GL_SIGNED_INTENSITY_NV = 34567
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2340
try:
    GL_SIGNED_INTENSITY8_NV = 34568
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2341
try:
    GL_DSDT8_NV = 34569
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2342
try:
    GL_DSDT8_MAG8_NV = 34570
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2343
try:
    GL_DSDT8_MAG8_INTENSITY8_NV = 34571
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2344
try:
    GL_SIGNED_RGB_UNSIGNED_ALPHA_NV = 34572
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2345
try:
    GL_SIGNED_RGB8_UNSIGNED_ALPHA8_NV = 34573
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2346
try:
    GL_HI_SCALE_NV = 34574
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2347
try:
    GL_LO_SCALE_NV = 34575
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2348
try:
    GL_DS_SCALE_NV = 34576
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2349
try:
    GL_DT_SCALE_NV = 34577
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2350
try:
    GL_MAGNITUDE_SCALE_NV = 34578
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2351
try:
    GL_VIBRANCE_SCALE_NV = 34579
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2352
try:
    GL_HI_BIAS_NV = 34580
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2353
try:
    GL_LO_BIAS_NV = 34581
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2354
try:
    GL_DS_BIAS_NV = 34582
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2355
try:
    GL_DT_BIAS_NV = 34583
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2356
try:
    GL_MAGNITUDE_BIAS_NV = 34584
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2357
try:
    GL_VIBRANCE_BIAS_NV = 34585
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2358
try:
    GL_TEXTURE_BORDER_VALUES_NV = 34586
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2359
try:
    GL_TEXTURE_HI_SIZE_NV = 34587
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2360
try:
    GL_TEXTURE_LO_SIZE_NV = 34588
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2361
try:
    GL_TEXTURE_DS_SIZE_NV = 34589
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2362
try:
    GL_TEXTURE_DT_SIZE_NV = 34590
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2363
try:
    GL_TEXTURE_MAG_SIZE_NV = 34591
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2367
try:
    GL_DOT_PRODUCT_TEXTURE_3D_NV = 34543
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2371
try:
    GL_VERTEX_ARRAY_RANGE_WITHOUT_FLUSH_NV = 34099
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2375
try:
    GL_VERTEX_PROGRAM_NV = 34336
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2376
try:
    GL_VERTEX_STATE_PROGRAM_NV = 34337
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2377
try:
    GL_ATTRIB_ARRAY_SIZE_NV = 34339
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2378
try:
    GL_ATTRIB_ARRAY_STRIDE_NV = 34340
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2379
try:
    GL_ATTRIB_ARRAY_TYPE_NV = 34341
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2380
try:
    GL_CURRENT_ATTRIB_NV = 34342
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2381
try:
    GL_PROGRAM_LENGTH_NV = 34343
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2382
try:
    GL_PROGRAM_STRING_NV = 34344
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2383
try:
    GL_MODELVIEW_PROJECTION_NV = 34345
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2384
try:
    GL_IDENTITY_NV = 34346
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2385
try:
    GL_INVERSE_NV = 34347
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2386
try:
    GL_TRANSPOSE_NV = 34348
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2387
try:
    GL_INVERSE_TRANSPOSE_NV = 34349
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2388
try:
    GL_MAX_TRACK_MATRIX_STACK_DEPTH_NV = 34350
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2389
try:
    GL_MAX_TRACK_MATRICES_NV = 34351
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2390
try:
    GL_MATRIX0_NV = 34352
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2391
try:
    GL_MATRIX1_NV = 34353
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2392
try:
    GL_MATRIX2_NV = 34354
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2393
try:
    GL_MATRIX3_NV = 34355
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2394
try:
    GL_MATRIX4_NV = 34356
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2395
try:
    GL_MATRIX5_NV = 34357
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2396
try:
    GL_MATRIX6_NV = 34358
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2397
try:
    GL_MATRIX7_NV = 34359
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2398
try:
    GL_CURRENT_MATRIX_STACK_DEPTH_NV = 34368
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2399
try:
    GL_CURRENT_MATRIX_NV = 34369
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2400
try:
    GL_VERTEX_PROGRAM_POINT_SIZE_NV = 34370
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2401
try:
    GL_VERTEX_PROGRAM_TWO_SIDE_NV = 34371
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2402
try:
    GL_PROGRAM_PARAMETER_NV = 34372
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2403
try:
    GL_ATTRIB_ARRAY_POINTER_NV = 34373
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2404
try:
    GL_PROGRAM_TARGET_NV = 34374
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2405
try:
    GL_PROGRAM_RESIDENT_NV = 34375
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2406
try:
    GL_TRACK_MATRIX_NV = 34376
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2407
try:
    GL_TRACK_MATRIX_TRANSFORM_NV = 34377
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2408
try:
    GL_VERTEX_PROGRAM_BINDING_NV = 34378
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2409
try:
    GL_PROGRAM_ERROR_POSITION_NV = 34379
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2410
try:
    GL_VERTEX_ATTRIB_ARRAY0_NV = 34384
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2411
try:
    GL_VERTEX_ATTRIB_ARRAY1_NV = 34385
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2412
try:
    GL_VERTEX_ATTRIB_ARRAY2_NV = 34386
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2413
try:
    GL_VERTEX_ATTRIB_ARRAY3_NV = 34387
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2414
try:
    GL_VERTEX_ATTRIB_ARRAY4_NV = 34388
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2415
try:
    GL_VERTEX_ATTRIB_ARRAY5_NV = 34389
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2416
try:
    GL_VERTEX_ATTRIB_ARRAY6_NV = 34390
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2417
try:
    GL_VERTEX_ATTRIB_ARRAY7_NV = 34391
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2418
try:
    GL_VERTEX_ATTRIB_ARRAY8_NV = 34392
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2419
try:
    GL_VERTEX_ATTRIB_ARRAY9_NV = 34393
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2420
try:
    GL_VERTEX_ATTRIB_ARRAY10_NV = 34394
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2421
try:
    GL_VERTEX_ATTRIB_ARRAY11_NV = 34395
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2422
try:
    GL_VERTEX_ATTRIB_ARRAY12_NV = 34396
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2423
try:
    GL_VERTEX_ATTRIB_ARRAY13_NV = 34397
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2424
try:
    GL_VERTEX_ATTRIB_ARRAY14_NV = 34398
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2425
try:
    GL_VERTEX_ATTRIB_ARRAY15_NV = 34399
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2426
try:
    GL_MAP1_VERTEX_ATTRIB0_4_NV = 34400
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2427
try:
    GL_MAP1_VERTEX_ATTRIB1_4_NV = 34401
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2428
try:
    GL_MAP1_VERTEX_ATTRIB2_4_NV = 34402
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2429
try:
    GL_MAP1_VERTEX_ATTRIB3_4_NV = 34403
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2430
try:
    GL_MAP1_VERTEX_ATTRIB4_4_NV = 34404
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2431
try:
    GL_MAP1_VERTEX_ATTRIB5_4_NV = 34405
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2432
try:
    GL_MAP1_VERTEX_ATTRIB6_4_NV = 34406
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2433
try:
    GL_MAP1_VERTEX_ATTRIB7_4_NV = 34407
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2434
try:
    GL_MAP1_VERTEX_ATTRIB8_4_NV = 34408
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2435
try:
    GL_MAP1_VERTEX_ATTRIB9_4_NV = 34409
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2436
try:
    GL_MAP1_VERTEX_ATTRIB10_4_NV = 34410
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2437
try:
    GL_MAP1_VERTEX_ATTRIB11_4_NV = 34411
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2438
try:
    GL_MAP1_VERTEX_ATTRIB12_4_NV = 34412
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2439
try:
    GL_MAP1_VERTEX_ATTRIB13_4_NV = 34413
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2440
try:
    GL_MAP1_VERTEX_ATTRIB14_4_NV = 34414
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2441
try:
    GL_MAP1_VERTEX_ATTRIB15_4_NV = 34415
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2442
try:
    GL_MAP2_VERTEX_ATTRIB0_4_NV = 34416
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2443
try:
    GL_MAP2_VERTEX_ATTRIB1_4_NV = 34417
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2444
try:
    GL_MAP2_VERTEX_ATTRIB2_4_NV = 34418
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2445
try:
    GL_MAP2_VERTEX_ATTRIB3_4_NV = 34419
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2446
try:
    GL_MAP2_VERTEX_ATTRIB4_4_NV = 34420
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2447
try:
    GL_MAP2_VERTEX_ATTRIB5_4_NV = 34421
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2448
try:
    GL_MAP2_VERTEX_ATTRIB6_4_NV = 34422
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2449
try:
    GL_MAP2_VERTEX_ATTRIB7_4_NV = 34423
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2450
try:
    GL_MAP2_VERTEX_ATTRIB8_4_NV = 34424
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2451
try:
    GL_MAP2_VERTEX_ATTRIB9_4_NV = 34425
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2452
try:
    GL_MAP2_VERTEX_ATTRIB10_4_NV = 34426
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2453
try:
    GL_MAP2_VERTEX_ATTRIB11_4_NV = 34427
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2454
try:
    GL_MAP2_VERTEX_ATTRIB12_4_NV = 34428
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2455
try:
    GL_MAP2_VERTEX_ATTRIB13_4_NV = 34429
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2456
try:
    GL_MAP2_VERTEX_ATTRIB14_4_NV = 34430
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2457
try:
    GL_MAP2_VERTEX_ATTRIB15_4_NV = 34431
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2461
try:
    GL_TEXTURE_MAX_CLAMP_S_SGIX = 33641
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2462
try:
    GL_TEXTURE_MAX_CLAMP_T_SGIX = 33642
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2463
try:
    GL_TEXTURE_MAX_CLAMP_R_SGIX = 33643
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2467
try:
    GL_SCALEBIAS_HINT_SGIX = 33570
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2471
try:
    GL_INTERLACE_OML = 35200
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2472
try:
    GL_INTERLACE_READ_OML = 35201
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2476
try:
    GL_FORMAT_SUBSAMPLE_24_24_OML = 35202
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2477
try:
    GL_FORMAT_SUBSAMPLE_244_244_OML = 35203
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2481
try:
    GL_PACK_RESAMPLE_OML = 35204
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2482
try:
    GL_UNPACK_RESAMPLE_OML = 35205
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2483
try:
    GL_RESAMPLE_REPLICATE_OML = 35206
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2484
try:
    GL_RESAMPLE_ZERO_FILL_OML = 35207
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2485
try:
    GL_RESAMPLE_AVERAGE_OML = 35208
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2486
try:
    GL_RESAMPLE_DECIMATE_OML = 35209
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2490
try:
    GL_DEPTH_STENCIL_TO_RGBA_NV = 34926
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2491
try:
    GL_DEPTH_STENCIL_TO_BGRA_NV = 34927
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2495
try:
    GL_BUMP_ROT_MATRIX_ATI = 34677
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2496
try:
    GL_BUMP_ROT_MATRIX_SIZE_ATI = 34678
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2497
try:
    GL_BUMP_NUM_TEX_UNITS_ATI = 34679
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2498
try:
    GL_BUMP_TEX_UNITS_ATI = 34680
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2499
try:
    GL_DUDV_ATI = 34681
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2500
try:
    GL_DU8DV8_ATI = 34682
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2501
try:
    GL_BUMP_ENVMAP_ATI = 34683
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2502
try:
    GL_BUMP_TARGET_ATI = 34684
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2506
try:
    GL_FRAGMENT_SHADER_ATI = 35104
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2507
try:
    GL_REG_0_ATI = 35105
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2508
try:
    GL_REG_1_ATI = 35106
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2509
try:
    GL_REG_2_ATI = 35107
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2510
try:
    GL_REG_3_ATI = 35108
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2511
try:
    GL_REG_4_ATI = 35109
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2512
try:
    GL_REG_5_ATI = 35110
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2513
try:
    GL_REG_6_ATI = 35111
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2514
try:
    GL_REG_7_ATI = 35112
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2515
try:
    GL_REG_8_ATI = 35113
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2516
try:
    GL_REG_9_ATI = 35114
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2517
try:
    GL_REG_10_ATI = 35115
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2518
try:
    GL_REG_11_ATI = 35116
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2519
try:
    GL_REG_12_ATI = 35117
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2520
try:
    GL_REG_13_ATI = 35118
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2521
try:
    GL_REG_14_ATI = 35119
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2522
try:
    GL_REG_15_ATI = 35120
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2523
try:
    GL_REG_16_ATI = 35121
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2524
try:
    GL_REG_17_ATI = 35122
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2525
try:
    GL_REG_18_ATI = 35123
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2526
try:
    GL_REG_19_ATI = 35124
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2527
try:
    GL_REG_20_ATI = 35125
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2528
try:
    GL_REG_21_ATI = 35126
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2529
try:
    GL_REG_22_ATI = 35127
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2530
try:
    GL_REG_23_ATI = 35128
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2531
try:
    GL_REG_24_ATI = 35129
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2532
try:
    GL_REG_25_ATI = 35130
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2533
try:
    GL_REG_26_ATI = 35131
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2534
try:
    GL_REG_27_ATI = 35132
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2535
try:
    GL_REG_28_ATI = 35133
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2536
try:
    GL_REG_29_ATI = 35134
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2537
try:
    GL_REG_30_ATI = 35135
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2538
try:
    GL_REG_31_ATI = 35136
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2539
try:
    GL_CON_0_ATI = 35137
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2540
try:
    GL_CON_1_ATI = 35138
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2541
try:
    GL_CON_2_ATI = 35139
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2542
try:
    GL_CON_3_ATI = 35140
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2543
try:
    GL_CON_4_ATI = 35141
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2544
try:
    GL_CON_5_ATI = 35142
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2545
try:
    GL_CON_6_ATI = 35143
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2546
try:
    GL_CON_7_ATI = 35144
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2547
try:
    GL_CON_8_ATI = 35145
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2548
try:
    GL_CON_9_ATI = 35146
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2549
try:
    GL_CON_10_ATI = 35147
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2550
try:
    GL_CON_11_ATI = 35148
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2551
try:
    GL_CON_12_ATI = 35149
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2552
try:
    GL_CON_13_ATI = 35150
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2553
try:
    GL_CON_14_ATI = 35151
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2554
try:
    GL_CON_15_ATI = 35152
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2555
try:
    GL_CON_16_ATI = 35153
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2556
try:
    GL_CON_17_ATI = 35154
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2557
try:
    GL_CON_18_ATI = 35155
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2558
try:
    GL_CON_19_ATI = 35156
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2559
try:
    GL_CON_20_ATI = 35157
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2560
try:
    GL_CON_21_ATI = 35158
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2561
try:
    GL_CON_22_ATI = 35159
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2562
try:
    GL_CON_23_ATI = 35160
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2563
try:
    GL_CON_24_ATI = 35161
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2564
try:
    GL_CON_25_ATI = 35162
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2565
try:
    GL_CON_26_ATI = 35163
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2566
try:
    GL_CON_27_ATI = 35164
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2567
try:
    GL_CON_28_ATI = 35165
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2568
try:
    GL_CON_29_ATI = 35166
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2569
try:
    GL_CON_30_ATI = 35167
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2570
try:
    GL_CON_31_ATI = 35168
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2571
try:
    GL_MOV_ATI = 35169
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2572
try:
    GL_ADD_ATI = 35171
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2573
try:
    GL_MUL_ATI = 35172
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2574
try:
    GL_SUB_ATI = 35173
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2575
try:
    GL_DOT3_ATI = 35174
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2576
try:
    GL_DOT4_ATI = 35175
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2577
try:
    GL_MAD_ATI = 35176
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2578
try:
    GL_LERP_ATI = 35177
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2579
try:
    GL_CND_ATI = 35178
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2580
try:
    GL_CND0_ATI = 35179
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2581
try:
    GL_DOT2_ADD_ATI = 35180
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2582
try:
    GL_SECONDARY_INTERPOLATOR_ATI = 35181
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2583
try:
    GL_NUM_FRAGMENT_REGISTERS_ATI = 35182
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2584
try:
    GL_NUM_FRAGMENT_CONSTANTS_ATI = 35183
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2585
try:
    GL_NUM_PASSES_ATI = 35184
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2586
try:
    GL_NUM_INSTRUCTIONS_PER_PASS_ATI = 35185
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2587
try:
    GL_NUM_INSTRUCTIONS_TOTAL_ATI = 35186
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2588
try:
    GL_NUM_INPUT_INTERPOLATOR_COMPONENTS_ATI = 35187
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2589
try:
    GL_NUM_LOOPBACK_COMPONENTS_ATI = 35188
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2590
try:
    GL_COLOR_ALPHA_PAIRING_ATI = 35189
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2591
try:
    GL_SWIZZLE_STR_ATI = 35190
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2592
try:
    GL_SWIZZLE_STQ_ATI = 35191
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2593
try:
    GL_SWIZZLE_STR_DR_ATI = 35192
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2594
try:
    GL_SWIZZLE_STQ_DQ_ATI = 35193
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2595
try:
    GL_SWIZZLE_STRQ_ATI = 35194
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2596
try:
    GL_SWIZZLE_STRQ_DQ_ATI = 35195
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2597
try:
    GL_RED_BIT_ATI = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2598
try:
    GL_GREEN_BIT_ATI = 2
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2599
try:
    GL_BLUE_BIT_ATI = 4
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2600
try:
    GL_2X_BIT_ATI = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2601
try:
    GL_4X_BIT_ATI = 2
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2602
try:
    GL_8X_BIT_ATI = 4
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2603
try:
    GL_HALF_BIT_ATI = 8
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2604
try:
    GL_QUARTER_BIT_ATI = 16
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2605
try:
    GL_EIGHTH_BIT_ATI = 32
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2606
try:
    GL_SATURATE_BIT_ATI = 64
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2607
try:
    GL_COMP_BIT_ATI = 2
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2608
try:
    GL_NEGATE_BIT_ATI = 4
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2609
try:
    GL_BIAS_BIT_ATI = 8
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2613
try:
    GL_PN_TRIANGLES_ATI = 34800
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2614
try:
    GL_MAX_PN_TRIANGLES_TESSELATION_LEVEL_ATI = 34801
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2615
try:
    GL_PN_TRIANGLES_POINT_MODE_ATI = 34802
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2616
try:
    GL_PN_TRIANGLES_NORMAL_MODE_ATI = 34803
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2617
try:
    GL_PN_TRIANGLES_TESSELATION_LEVEL_ATI = 34804
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2618
try:
    GL_PN_TRIANGLES_POINT_MODE_LINEAR_ATI = 34805
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2619
try:
    GL_PN_TRIANGLES_POINT_MODE_CUBIC_ATI = 34806
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2620
try:
    GL_PN_TRIANGLES_NORMAL_MODE_LINEAR_ATI = 34807
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2621
try:
    GL_PN_TRIANGLES_NORMAL_MODE_QUADRATIC_ATI = 34808
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2625
try:
    GL_STATIC_ATI = 34656
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2626
try:
    GL_DYNAMIC_ATI = 34657
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2627
try:
    GL_PRESERVE_ATI = 34658
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2628
try:
    GL_DISCARD_ATI = 34659
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2629
try:
    GL_OBJECT_BUFFER_SIZE_ATI = 34660
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2630
try:
    GL_OBJECT_BUFFER_USAGE_ATI = 34661
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2631
try:
    GL_ARRAY_OBJECT_BUFFER_ATI = 34662
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2632
try:
    GL_ARRAY_OBJECT_OFFSET_ATI = 34663
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2636
try:
    GL_VERTEX_SHADER_EXT = 34688
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2637
try:
    GL_VERTEX_SHADER_BINDING_EXT = 34689
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2638
try:
    GL_OP_INDEX_EXT = 34690
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2639
try:
    GL_OP_NEGATE_EXT = 34691
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2640
try:
    GL_OP_DOT3_EXT = 34692
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2641
try:
    GL_OP_DOT4_EXT = 34693
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2642
try:
    GL_OP_MUL_EXT = 34694
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2643
try:
    GL_OP_ADD_EXT = 34695
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2644
try:
    GL_OP_MADD_EXT = 34696
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2645
try:
    GL_OP_FRAC_EXT = 34697
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2646
try:
    GL_OP_MAX_EXT = 34698
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2647
try:
    GL_OP_MIN_EXT = 34699
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2648
try:
    GL_OP_SET_GE_EXT = 34700
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2649
try:
    GL_OP_SET_LT_EXT = 34701
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2650
try:
    GL_OP_CLAMP_EXT = 34702
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2651
try:
    GL_OP_FLOOR_EXT = 34703
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2652
try:
    GL_OP_ROUND_EXT = 34704
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2653
try:
    GL_OP_EXP_BASE_2_EXT = 34705
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2654
try:
    GL_OP_LOG_BASE_2_EXT = 34706
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2655
try:
    GL_OP_POWER_EXT = 34707
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2656
try:
    GL_OP_RECIP_EXT = 34708
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2657
try:
    GL_OP_RECIP_SQRT_EXT = 34709
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2658
try:
    GL_OP_SUB_EXT = 34710
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2659
try:
    GL_OP_CROSS_PRODUCT_EXT = 34711
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2660
try:
    GL_OP_MULTIPLY_MATRIX_EXT = 34712
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2661
try:
    GL_OP_MOV_EXT = 34713
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2662
try:
    GL_OUTPUT_VERTEX_EXT = 34714
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2663
try:
    GL_OUTPUT_COLOR0_EXT = 34715
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2664
try:
    GL_OUTPUT_COLOR1_EXT = 34716
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2665
try:
    GL_OUTPUT_TEXTURE_COORD0_EXT = 34717
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2666
try:
    GL_OUTPUT_TEXTURE_COORD1_EXT = 34718
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2667
try:
    GL_OUTPUT_TEXTURE_COORD2_EXT = 34719
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2668
try:
    GL_OUTPUT_TEXTURE_COORD3_EXT = 34720
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2669
try:
    GL_OUTPUT_TEXTURE_COORD4_EXT = 34721
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2670
try:
    GL_OUTPUT_TEXTURE_COORD5_EXT = 34722
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2671
try:
    GL_OUTPUT_TEXTURE_COORD6_EXT = 34723
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2672
try:
    GL_OUTPUT_TEXTURE_COORD7_EXT = 34724
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2673
try:
    GL_OUTPUT_TEXTURE_COORD8_EXT = 34725
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2674
try:
    GL_OUTPUT_TEXTURE_COORD9_EXT = 34726
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2675
try:
    GL_OUTPUT_TEXTURE_COORD10_EXT = 34727
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2676
try:
    GL_OUTPUT_TEXTURE_COORD11_EXT = 34728
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2677
try:
    GL_OUTPUT_TEXTURE_COORD12_EXT = 34729
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2678
try:
    GL_OUTPUT_TEXTURE_COORD13_EXT = 34730
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2679
try:
    GL_OUTPUT_TEXTURE_COORD14_EXT = 34731
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2680
try:
    GL_OUTPUT_TEXTURE_COORD15_EXT = 34732
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2681
try:
    GL_OUTPUT_TEXTURE_COORD16_EXT = 34733
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2682
try:
    GL_OUTPUT_TEXTURE_COORD17_EXT = 34734
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2683
try:
    GL_OUTPUT_TEXTURE_COORD18_EXT = 34735
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2684
try:
    GL_OUTPUT_TEXTURE_COORD19_EXT = 34736
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2685
try:
    GL_OUTPUT_TEXTURE_COORD20_EXT = 34737
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2686
try:
    GL_OUTPUT_TEXTURE_COORD21_EXT = 34738
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2687
try:
    GL_OUTPUT_TEXTURE_COORD22_EXT = 34739
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2688
try:
    GL_OUTPUT_TEXTURE_COORD23_EXT = 34740
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2689
try:
    GL_OUTPUT_TEXTURE_COORD24_EXT = 34741
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2690
try:
    GL_OUTPUT_TEXTURE_COORD25_EXT = 34742
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2691
try:
    GL_OUTPUT_TEXTURE_COORD26_EXT = 34743
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2692
try:
    GL_OUTPUT_TEXTURE_COORD27_EXT = 34744
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2693
try:
    GL_OUTPUT_TEXTURE_COORD28_EXT = 34745
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2694
try:
    GL_OUTPUT_TEXTURE_COORD29_EXT = 34746
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2695
try:
    GL_OUTPUT_TEXTURE_COORD30_EXT = 34747
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2696
try:
    GL_OUTPUT_TEXTURE_COORD31_EXT = 34748
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2697
try:
    GL_OUTPUT_FOG_EXT = 34749
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2698
try:
    GL_SCALAR_EXT = 34750
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2699
try:
    GL_VECTOR_EXT = 34751
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2700
try:
    GL_MATRIX_EXT = 34752
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2701
try:
    GL_VARIANT_EXT = 34753
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2702
try:
    GL_INVARIANT_EXT = 34754
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2703
try:
    GL_LOCAL_CONSTANT_EXT = 34755
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2704
try:
    GL_LOCAL_EXT = 34756
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2705
try:
    GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT = 34757
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2706
try:
    GL_MAX_VERTEX_SHADER_VARIANTS_EXT = 34758
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2707
try:
    GL_MAX_VERTEX_SHADER_INVARIANTS_EXT = 34759
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2708
try:
    GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 34760
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2709
try:
    GL_MAX_VERTEX_SHADER_LOCALS_EXT = 34761
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2710
try:
    GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT = 34762
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2711
try:
    GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT = 34763
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2712
try:
    GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 34764
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2713
try:
    GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT = 34765
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2714
try:
    GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT = 34766
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2715
try:
    GL_VERTEX_SHADER_INSTRUCTIONS_EXT = 34767
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2716
try:
    GL_VERTEX_SHADER_VARIANTS_EXT = 34768
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2717
try:
    GL_VERTEX_SHADER_INVARIANTS_EXT = 34769
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2718
try:
    GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 34770
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2719
try:
    GL_VERTEX_SHADER_LOCALS_EXT = 34771
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2720
try:
    GL_VERTEX_SHADER_OPTIMIZED_EXT = 34772
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2721
try:
    GL_X_EXT = 34773
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2722
try:
    GL_Y_EXT = 34774
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2723
try:
    GL_Z_EXT = 34775
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2724
try:
    GL_W_EXT = 34776
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2725
try:
    GL_NEGATIVE_X_EXT = 34777
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2726
try:
    GL_NEGATIVE_Y_EXT = 34778
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2727
try:
    GL_NEGATIVE_Z_EXT = 34779
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2728
try:
    GL_NEGATIVE_W_EXT = 34780
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2729
try:
    GL_ZERO_EXT = 34781
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2730
try:
    GL_ONE_EXT = 34782
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2731
try:
    GL_NEGATIVE_ONE_EXT = 34783
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2732
try:
    GL_NORMALIZED_RANGE_EXT = 34784
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2733
try:
    GL_FULL_RANGE_EXT = 34785
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2734
try:
    GL_CURRENT_VERTEX_EXT = 34786
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2735
try:
    GL_MVP_MATRIX_EXT = 34787
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2736
try:
    GL_VARIANT_VALUE_EXT = 34788
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2737
try:
    GL_VARIANT_DATATYPE_EXT = 34789
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2738
try:
    GL_VARIANT_ARRAY_STRIDE_EXT = 34790
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2739
try:
    GL_VARIANT_ARRAY_TYPE_EXT = 34791
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2740
try:
    GL_VARIANT_ARRAY_EXT = 34792
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2741
try:
    GL_VARIANT_ARRAY_POINTER_EXT = 34793
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2742
try:
    GL_INVARIANT_VALUE_EXT = 34794
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2743
try:
    GL_INVARIANT_DATATYPE_EXT = 34795
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2744
try:
    GL_LOCAL_CONSTANT_VALUE_EXT = 34796
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2745
try:
    GL_LOCAL_CONSTANT_DATATYPE_EXT = 34797
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2749
try:
    GL_MAX_VERTEX_STREAMS_ATI = 34667
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2750
try:
    GL_VERTEX_STREAM0_ATI = 34668
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2751
try:
    GL_VERTEX_STREAM1_ATI = 34669
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2752
try:
    GL_VERTEX_STREAM2_ATI = 34670
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2753
try:
    GL_VERTEX_STREAM3_ATI = 34671
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2754
try:
    GL_VERTEX_STREAM4_ATI = 34672
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2755
try:
    GL_VERTEX_STREAM5_ATI = 34673
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2756
try:
    GL_VERTEX_STREAM6_ATI = 34674
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2757
try:
    GL_VERTEX_STREAM7_ATI = 34675
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2758
try:
    GL_VERTEX_SOURCE_ATI = 34676
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2762
try:
    GL_ELEMENT_ARRAY_ATI = 34664
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2763
try:
    GL_ELEMENT_ARRAY_TYPE_ATI = 34665
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2764
try:
    GL_ELEMENT_ARRAY_POINTER_ATI = 34666
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2768
try:
    GL_QUAD_MESH_SUN = 34324
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2769
try:
    GL_TRIANGLE_MESH_SUN = 34325
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2773
try:
    GL_SLICE_ACCUM_SUN = 34252
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2777
try:
    GL_MULTISAMPLE_FILTER_HINT_NV = 34100
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2781
try:
    GL_DEPTH_CLAMP_NV = 34383
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2785
try:
    GL_PIXEL_COUNTER_BITS_NV = 34916
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2786
try:
    GL_CURRENT_OCCLUSION_QUERY_ID_NV = 34917
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2787
try:
    GL_PIXEL_COUNT_NV = 34918
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2788
try:
    GL_PIXEL_COUNT_AVAILABLE_NV = 34919
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2792
try:
    GL_POINT_SPRITE_NV = 34913
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2793
try:
    GL_COORD_REPLACE_NV = 34914
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2794
try:
    GL_POINT_SPRITE_R_MODE_NV = 34915
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2798
try:
    GL_OFFSET_PROJECTIVE_TEXTURE_2D_NV = 34896
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2799
try:
    GL_OFFSET_PROJECTIVE_TEXTURE_2D_SCALE_NV = 34897
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2800
try:
    GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_NV = 34898
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2801
try:
    GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_SCALE_NV = 34899
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2802
try:
    GL_OFFSET_HILO_TEXTURE_2D_NV = 34900
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2803
try:
    GL_OFFSET_HILO_TEXTURE_RECTANGLE_NV = 34901
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2804
try:
    GL_OFFSET_HILO_PROJECTIVE_TEXTURE_2D_NV = 34902
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2805
try:
    GL_OFFSET_HILO_PROJECTIVE_TEXTURE_RECTANGLE_NV = 34903
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2806
try:
    GL_DEPENDENT_HILO_TEXTURE_2D_NV = 34904
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2807
try:
    GL_DEPENDENT_RGB_TEXTURE_3D_NV = 34905
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2808
try:
    GL_DEPENDENT_RGB_TEXTURE_CUBE_MAP_NV = 34906
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2809
try:
    GL_DOT_PRODUCT_PASS_THROUGH_NV = 34907
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2810
try:
    GL_DOT_PRODUCT_TEXTURE_1D_NV = 34908
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2811
try:
    GL_DOT_PRODUCT_AFFINE_DEPTH_REPLACE_NV = 34909
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2812
try:
    GL_HILO8_NV = 34910
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2813
try:
    GL_SIGNED_HILO8_NV = 34911
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2814
try:
    GL_FORCE_BLUE_TO_ONE_NV = 34912
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2824
try:
    GL_STENCIL_TEST_TWO_SIDE_EXT = 35088
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2825
try:
    GL_ACTIVE_STENCIL_FACE_EXT = 35089
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2829
try:
    GL_TEXT_FRAGMENT_SHADER_ATI = 33280
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2833
try:
    GL_UNPACK_CLIENT_STORAGE_APPLE = 34226
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2837
try:
    GL_ELEMENT_ARRAY_APPLE = 34664
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2838
try:
    GL_ELEMENT_ARRAY_TYPE_APPLE = 34665
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2839
try:
    GL_ELEMENT_ARRAY_POINTER_APPLE = 34666
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2843
try:
    GL_DRAW_PIXELS_APPLE = 35338
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2844
try:
    GL_FENCE_APPLE = 35339
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2848
try:
    GL_VERTEX_ARRAY_BINDING_APPLE = 34229
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2852
try:
    GL_VERTEX_ARRAY_RANGE_APPLE = 34077
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2853
try:
    GL_VERTEX_ARRAY_RANGE_LENGTH_APPLE = 34078
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2854
try:
    GL_VERTEX_ARRAY_STORAGE_HINT_APPLE = 34079
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2855
try:
    GL_VERTEX_ARRAY_RANGE_POINTER_APPLE = 34081
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2856
try:
    GL_STORAGE_CACHED_APPLE = 34238
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2857
try:
    GL_STORAGE_SHARED_APPLE = 34239
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2861
try:
    GL_YCBCR_422_APPLE = 34233
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2862
try:
    GL_UNSIGNED_SHORT_8_8_APPLE = 34234
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2863
try:
    GL_UNSIGNED_SHORT_8_8_REV_APPLE = 34235
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2867
try:
    GL_RGB_S3TC = 33696
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2868
try:
    GL_RGB4_S3TC = 33697
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2869
try:
    GL_RGBA_S3TC = 33698
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2870
try:
    GL_RGBA4_S3TC = 33699
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2874
try:
    GL_MAX_DRAW_BUFFERS_ATI = 34852
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2875
try:
    GL_DRAW_BUFFER0_ATI = 34853
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2876
try:
    GL_DRAW_BUFFER1_ATI = 34854
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2877
try:
    GL_DRAW_BUFFER2_ATI = 34855
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2878
try:
    GL_DRAW_BUFFER3_ATI = 34856
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2879
try:
    GL_DRAW_BUFFER4_ATI = 34857
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2880
try:
    GL_DRAW_BUFFER5_ATI = 34858
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2881
try:
    GL_DRAW_BUFFER6_ATI = 34859
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2882
try:
    GL_DRAW_BUFFER7_ATI = 34860
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2883
try:
    GL_DRAW_BUFFER8_ATI = 34861
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2884
try:
    GL_DRAW_BUFFER9_ATI = 34862
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2885
try:
    GL_DRAW_BUFFER10_ATI = 34863
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2886
try:
    GL_DRAW_BUFFER11_ATI = 34864
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2887
try:
    GL_DRAW_BUFFER12_ATI = 34865
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2888
try:
    GL_DRAW_BUFFER13_ATI = 34866
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2889
try:
    GL_DRAW_BUFFER14_ATI = 34867
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2890
try:
    GL_DRAW_BUFFER15_ATI = 34868
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2894
try:
    GL_TYPE_RGBA_FLOAT_ATI = 34848
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2895
try:
    GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI = 34869
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2899
try:
    GL_MODULATE_ADD_ATI = 34628
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2900
try:
    GL_MODULATE_SIGNED_ADD_ATI = 34629
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2901
try:
    GL_MODULATE_SUBTRACT_ATI = 34630
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2905
try:
    GL_RGBA_FLOAT32_ATI = 34836
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2906
try:
    GL_RGB_FLOAT32_ATI = 34837
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2907
try:
    GL_ALPHA_FLOAT32_ATI = 34838
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2908
try:
    GL_INTENSITY_FLOAT32_ATI = 34839
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2909
try:
    GL_LUMINANCE_FLOAT32_ATI = 34840
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2910
try:
    GL_LUMINANCE_ALPHA_FLOAT32_ATI = 34841
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2911
try:
    GL_RGBA_FLOAT16_ATI = 34842
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2912
try:
    GL_RGB_FLOAT16_ATI = 34843
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2913
try:
    GL_ALPHA_FLOAT16_ATI = 34844
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2914
try:
    GL_INTENSITY_FLOAT16_ATI = 34845
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2915
try:
    GL_LUMINANCE_FLOAT16_ATI = 34846
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2916
try:
    GL_LUMINANCE_ALPHA_FLOAT16_ATI = 34847
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2920
try:
    GL_FLOAT_R_NV = 34944
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2921
try:
    GL_FLOAT_RG_NV = 34945
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2922
try:
    GL_FLOAT_RGB_NV = 34946
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2923
try:
    GL_FLOAT_RGBA_NV = 34947
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2924
try:
    GL_FLOAT_R16_NV = 34948
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2925
try:
    GL_FLOAT_R32_NV = 34949
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2926
try:
    GL_FLOAT_RG16_NV = 34950
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2927
try:
    GL_FLOAT_RG32_NV = 34951
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2928
try:
    GL_FLOAT_RGB16_NV = 34952
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2929
try:
    GL_FLOAT_RGB32_NV = 34953
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2930
try:
    GL_FLOAT_RGBA16_NV = 34954
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2931
try:
    GL_FLOAT_RGBA32_NV = 34955
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2932
try:
    GL_TEXTURE_FLOAT_COMPONENTS_NV = 34956
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2933
try:
    GL_FLOAT_CLEAR_COLOR_VALUE_NV = 34957
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2934
try:
    GL_FLOAT_RGBA_MODE_NV = 34958
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2938
try:
    GL_MAX_FRAGMENT_PROGRAM_LOCAL_PARAMETERS_NV = 34920
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2939
try:
    GL_FRAGMENT_PROGRAM_NV = 34928
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2940
try:
    GL_MAX_TEXTURE_COORDS_NV = 34929
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2941
try:
    GL_MAX_TEXTURE_IMAGE_UNITS_NV = 34930
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2942
try:
    GL_FRAGMENT_PROGRAM_BINDING_NV = 34931
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2943
try:
    GL_PROGRAM_ERROR_STRING_NV = 34932
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2947
try:
    GL_HALF_FLOAT_NV = 5131
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2951
try:
    GL_WRITE_PIXEL_DATA_RANGE_NV = 34936
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2952
try:
    GL_READ_PIXEL_DATA_RANGE_NV = 34937
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2953
try:
    GL_WRITE_PIXEL_DATA_RANGE_LENGTH_NV = 34938
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2954
try:
    GL_READ_PIXEL_DATA_RANGE_LENGTH_NV = 34939
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2955
try:
    GL_WRITE_PIXEL_DATA_RANGE_POINTER_NV = 34940
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2956
try:
    GL_READ_PIXEL_DATA_RANGE_POINTER_NV = 34941
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2960
try:
    GL_PRIMITIVE_RESTART_NV = 34136
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2961
try:
    GL_PRIMITIVE_RESTART_INDEX_NV = 34137
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2965
try:
    GL_TEXTURE_UNSIGNED_REMAP_MODE_NV = 34959
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2975
try:
    GL_STENCIL_BACK_FUNC_ATI = 34816
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2976
try:
    GL_STENCIL_BACK_FAIL_ATI = 34817
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2977
try:
    GL_STENCIL_BACK_PASS_DEPTH_FAIL_ATI = 34818
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2978
try:
    GL_STENCIL_BACK_PASS_DEPTH_PASS_ATI = 34819
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2985
try:
    GL_IMPLEMENTATION_COLOR_READ_TYPE_OES = 35738
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2986
try:
    GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES = 35739
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2990
try:
    GL_DEPTH_BOUNDS_TEST_EXT = 34960
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2991
try:
    GL_DEPTH_BOUNDS_EXT = 34961
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2995
try:
    GL_MIRROR_CLAMP_EXT = 34626
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2996
try:
    GL_MIRROR_CLAMP_TO_EDGE_EXT = 34627
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 2997
try:
    GL_MIRROR_CLAMP_TO_BORDER_EXT = 35090
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3001
try:
    GL_BLEND_EQUATION_RGB_EXT = GL_BLEND_EQUATION
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3002
try:
    GL_BLEND_EQUATION_ALPHA_EXT = 34877
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3006
try:
    GL_PACK_INVERT_MESA = 34648
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3010
try:
    GL_UNSIGNED_SHORT_8_8_MESA = 34234
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3011
try:
    GL_UNSIGNED_SHORT_8_8_REV_MESA = 34235
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3012
try:
    GL_YCBCR_MESA = 34647
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3016
try:
    GL_PIXEL_PACK_BUFFER_EXT = 35051
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3017
try:
    GL_PIXEL_UNPACK_BUFFER_EXT = 35052
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3018
try:
    GL_PIXEL_PACK_BUFFER_BINDING_EXT = 35053
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3019
try:
    GL_PIXEL_UNPACK_BUFFER_BINDING_EXT = 35055
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3026
try:
    GL_MAX_PROGRAM_EXEC_INSTRUCTIONS_NV = 35060
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3027
try:
    GL_MAX_PROGRAM_CALL_DEPTH_NV = 35061
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3028
try:
    GL_MAX_PROGRAM_IF_DEPTH_NV = 35062
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3029
try:
    GL_MAX_PROGRAM_LOOP_DEPTH_NV = 35063
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3030
try:
    GL_MAX_PROGRAM_LOOP_COUNT_NV = 35064
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3043
try:
    GL_INVALID_FRAMEBUFFER_OPERATION_EXT = 1286
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3044
try:
    GL_MAX_RENDERBUFFER_SIZE_EXT = 34024
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3045
try:
    GL_FRAMEBUFFER_BINDING_EXT = 36006
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3046
try:
    GL_RENDERBUFFER_BINDING_EXT = 36007
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3047
try:
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT = 36048
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3048
try:
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT = 36049
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3049
try:
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT = 36050
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3050
try:
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT = 36051
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3051
try:
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT = 36052
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3052
try:
    GL_FRAMEBUFFER_COMPLETE_EXT = 36053
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3053
try:
    GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT = 36054
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3054
try:
    GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT = 36055
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3055
try:
    GL_FRAMEBUFFER_INCOMPLETE_DUPLICATE_ATTACHMENT_EXT = 36056
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3056
try:
    GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT = 36057
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3057
try:
    GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT = 36058
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3058
try:
    GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT = 36059
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3059
try:
    GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT = 36060
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3060
try:
    GL_FRAMEBUFFER_UNSUPPORTED_EXT = 36061
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3061
try:
    GL_MAX_COLOR_ATTACHMENTS_EXT = 36063
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3062
try:
    GL_COLOR_ATTACHMENT0_EXT = 36064
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3063
try:
    GL_COLOR_ATTACHMENT1_EXT = 36065
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3064
try:
    GL_COLOR_ATTACHMENT2_EXT = 36066
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3065
try:
    GL_COLOR_ATTACHMENT3_EXT = 36067
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3066
try:
    GL_COLOR_ATTACHMENT4_EXT = 36068
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3067
try:
    GL_COLOR_ATTACHMENT5_EXT = 36069
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3068
try:
    GL_COLOR_ATTACHMENT6_EXT = 36070
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3069
try:
    GL_COLOR_ATTACHMENT7_EXT = 36071
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3070
try:
    GL_COLOR_ATTACHMENT8_EXT = 36072
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3071
try:
    GL_COLOR_ATTACHMENT9_EXT = 36073
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3072
try:
    GL_COLOR_ATTACHMENT10_EXT = 36074
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3073
try:
    GL_COLOR_ATTACHMENT11_EXT = 36075
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3074
try:
    GL_COLOR_ATTACHMENT12_EXT = 36076
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3075
try:
    GL_COLOR_ATTACHMENT13_EXT = 36077
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3076
try:
    GL_COLOR_ATTACHMENT14_EXT = 36078
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3077
try:
    GL_COLOR_ATTACHMENT15_EXT = 36079
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3078
try:
    GL_DEPTH_ATTACHMENT_EXT = 36096
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3079
try:
    GL_STENCIL_ATTACHMENT_EXT = 36128
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3080
try:
    GL_FRAMEBUFFER_EXT = 36160
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3081
try:
    GL_RENDERBUFFER_EXT = 36161
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3082
try:
    GL_RENDERBUFFER_WIDTH_EXT = 36162
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3083
try:
    GL_RENDERBUFFER_HEIGHT_EXT = 36163
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3084
try:
    GL_RENDERBUFFER_INTERNAL_FORMAT_EXT = 36164
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3085
try:
    GL_STENCIL_INDEX1_EXT = 36166
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3086
try:
    GL_STENCIL_INDEX4_EXT = 36167
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3087
try:
    GL_STENCIL_INDEX8_EXT = 36168
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3088
try:
    GL_STENCIL_INDEX16_EXT = 36169
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3089
try:
    GL_RENDERBUFFER_RED_SIZE_EXT = 36176
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3090
try:
    GL_RENDERBUFFER_GREEN_SIZE_EXT = 36177
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3091
try:
    GL_RENDERBUFFER_BLUE_SIZE_EXT = 36178
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3092
try:
    GL_RENDERBUFFER_ALPHA_SIZE_EXT = 36179
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3093
try:
    GL_RENDERBUFFER_DEPTH_SIZE_EXT = 36180
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3094
try:
    GL_RENDERBUFFER_STENCIL_SIZE_EXT = 36181
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3317
try:
    GL_VERSION_1_4 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3413
try:
    GL_VERSION_1_5 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3457
try:
    GL_VERSION_2_0 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3723
try:
    GL_ARB_transpose_matrix = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3737
try:
    GL_ARB_multisample = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3745
try:
    GL_ARB_texture_env_add = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3749
try:
    GL_ARB_texture_cube_map = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3753
try:
    GL_ARB_texture_compression = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3773
try:
    GL_ARB_texture_border_clamp = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3777
try:
    GL_ARB_point_parameters = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3787
try:
    GL_ARB_vertex_blend = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3813
try:
    GL_ARB_matrix_palette = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3829
try:
    GL_ARB_texture_env_combine = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3833
try:
    GL_ARB_texture_env_crossbar = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3837
try:
    GL_ARB_texture_env_dot3 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3841
try:
    GL_ARB_texture_mirrored_repeat = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3845
try:
    GL_ARB_depth_texture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3849
try:
    GL_ARB_shadow = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3853
try:
    GL_ARB_shadow_ambient = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3857
try:
    GL_ARB_window_pos = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 3895
try:
    GL_ARB_vertex_program = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4025
try:
    GL_ARB_fragment_program = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4030
try:
    GL_ARB_vertex_buffer_object = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4058
try:
    GL_ARB_occlusion_query = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4080
try:
    GL_ARB_shader_objects = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4164
try:
    GL_ARB_vertex_shader = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4176
try:
    GL_ARB_fragment_shader = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4180
try:
    GL_ARB_shading_language_100 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4184
try:
    GL_ARB_texture_non_power_of_two = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4188
try:
    GL_ARB_point_sprite = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4192
try:
    GL_ARB_fragment_program_shadow = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4196
try:
    GL_ARB_draw_buffers = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4204
try:
    GL_ARB_texture_rectangle = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4208
try:
    GL_ARB_color_buffer_float = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4216
try:
    GL_ARB_half_float_pixel = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4220
try:
    GL_ARB_texture_float = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4224
try:
    GL_ARB_pixel_buffer_object = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4228
try:
    GL_EXT_abgr = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4232
try:
    GL_EXT_blend_color = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4240
try:
    GL_EXT_polygon_offset = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4248
try:
    GL_EXT_texture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4252
try:
    GL_EXT_texture3D = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4262
try:
    GL_SGIS_texture_filter4 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4272
try:
    GL_EXT_subtexture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4282
try:
    GL_EXT_copy_texture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4298
try:
    GL_EXT_histogram = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4324
try:
    GL_EXT_convolution = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4356
try:
    GL_EXT_color_matrix = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4360
try:
    GL_SGI_color_table = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4380
try:
    GL_SGIX_pixel_texture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4388
try:
    GL_SGIS_pixel_texture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4406
try:
    GL_SGIS_texture4D = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4416
try:
    GL_SGI_texture_color_table = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4420
try:
    GL_EXT_cmyka = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4424
try:
    GL_EXT_texture_object = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4442
try:
    GL_SGIS_detail_texture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4452
try:
    GL_SGIS_sharpen_texture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4462
try:
    GL_EXT_packed_pixels = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4466
try:
    GL_SGIS_texture_lod = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4470
try:
    GL_SGIS_multisample = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4480
try:
    GL_EXT_rescale_normal = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4484
try:
    GL_EXT_vertex_array = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4508
try:
    GL_EXT_misc_attribute = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4512
try:
    GL_SGIS_generate_mipmap = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4516
try:
    GL_SGIX_clipmap = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4520
try:
    GL_SGIX_shadow = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4524
try:
    GL_SGIS_texture_edge_clamp = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4528
try:
    GL_SGIS_texture_border_clamp = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4532
try:
    GL_EXT_blend_minmax = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4540
try:
    GL_EXT_blend_subtract = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4544
try:
    GL_EXT_blend_logic_op = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4548
try:
    GL_SGIX_interlace = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4552
try:
    GL_SGIX_pixel_tiles = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4556
try:
    GL_SGIX_texture_select = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4560
try:
    GL_SGIX_sprite = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4574
try:
    GL_SGIX_texture_multi_buffer = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4578
try:
    GL_EXT_point_parameters = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4588
try:
    GL_SGIS_point_parameters = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4598
try:
    GL_SGIX_instruments = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4616
try:
    GL_SGIX_texture_scale_bias = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4620
try:
    GL_SGIX_framezoom = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4628
try:
    GL_SGIX_tag_sample_buffer = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4636
try:
    GL_SGIX_polynomial_ffd = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4650
try:
    GL_SGIX_reference_plane = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4658
try:
    GL_SGIX_flush_raster = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4666
try:
    GL_SGIX_depth_texture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4670
try:
    GL_SGIS_fog_function = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4680
try:
    GL_SGIX_fog_offset = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4684
try:
    GL_HP_image_transform = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4702
try:
    GL_HP_convolution_border_modes = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4706
try:
    GL_SGIX_texture_add_env = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4710
try:
    GL_EXT_color_subtable = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4720
try:
    GL_PGI_vertex_hints = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4724
try:
    GL_PGI_misc_hints = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4732
try:
    GL_EXT_paletted_texture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4746
try:
    GL_EXT_clip_volume_hint = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4750
try:
    GL_SGIX_list_priority = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4768
try:
    GL_SGIX_ir_instrument1 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4772
try:
    GL_SGIX_calligraphic_fragment = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4776
try:
    GL_SGIX_texture_lod_bias = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4780
try:
    GL_SGIX_shadow_ambient = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4784
try:
    GL_EXT_index_texture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4788
try:
    GL_EXT_index_material = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4796
try:
    GL_EXT_index_func = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4804
try:
    GL_EXT_index_array_formats = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4808
try:
    GL_EXT_compiled_vertex_array = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4818
try:
    GL_EXT_cull_vertex = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4828
try:
    GL_SGIX_ycrcb = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4832
try:
    GL_SGIX_fragment_lighting = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4874
try:
    GL_IBM_rasterpos_clip = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4878
try:
    GL_HP_texture_lighting = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4882
try:
    GL_EXT_draw_range_elements = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4890
try:
    GL_WIN_phong_shading = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4894
try:
    GL_WIN_specular_fog = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4898
try:
    GL_EXT_light_texture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4910
try:
    GL_SGIX_blend_alpha_minmax = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4914
try:
    GL_EXT_bgra = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4918
try:
    GL_SGIX_async = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4936
try:
    GL_SGIX_async_pixel = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4940
try:
    GL_SGIX_async_histogram = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4944
try:
    GL_INTEL_parallel_arrays = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4958
try:
    GL_HP_occlusion_test = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4962
try:
    GL_EXT_pixel_transform = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4976
try:
    GL_EXT_pixel_transform_color_table = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4980
try:
    GL_EXT_shared_texture_palette = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4984
try:
    GL_EXT_separate_specular_color = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 4988
try:
    GL_EXT_secondary_color = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5028
try:
    GL_EXT_texture_perturb_normal = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5036
try:
    GL_EXT_multi_draw_arrays = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5046
try:
    GL_EXT_fog_coord = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5062
try:
    GL_REND_screen_coordinates = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5066
try:
    GL_EXT_coordinate_frame = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5116
try:
    GL_EXT_texture_env_combine = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5120
try:
    GL_APPLE_specular_vector = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5124
try:
    GL_APPLE_transform_hint = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5128
try:
    GL_SGIX_fog_scale = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5132
try:
    GL_SUNX_constant_data = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5140
try:
    GL_SUN_global_alpha = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5162
try:
    GL_SUN_triangle_list = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5182
try:
    GL_SUN_vertex = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5268
try:
    GL_EXT_blend_func_separate = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5276
try:
    GL_INGR_blend_func_separate = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5284
try:
    GL_INGR_color_clamp = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5288
try:
    GL_INGR_interlace_read = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5292
try:
    GL_EXT_stencil_wrap = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5296
try:
    GL_EXT_422_pixels = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5300
try:
    GL_NV_texgen_reflection = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5304
try:
    GL_SUN_convolution_border_modes = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5308
try:
    GL_EXT_texture_env_add = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5312
try:
    GL_EXT_texture_lod_bias = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5316
try:
    GL_EXT_texture_filter_anisotropic = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5320
try:
    GL_EXT_vertex_weighting = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5332
try:
    GL_NV_light_max_exponent = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5336
try:
    GL_NV_vertex_array_range = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5346
try:
    GL_NV_register_combiners = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5378
try:
    GL_NV_fog_distance = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5382
try:
    GL_NV_texgen_emboss = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5386
try:
    GL_NV_blend_square = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5390
try:
    GL_NV_texture_env_combine4 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5394
try:
    GL_MESA_resize_buffers = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5402
try:
    GL_MESA_window_pos = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5456
try:
    GL_IBM_cull_vertex = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5460
try:
    GL_IBM_multimode_draw_arrays = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5470
try:
    GL_IBM_vertex_array_lists = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5492
try:
    GL_SGIX_subsample = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5496
try:
    GL_SGIX_ycrcba = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5500
try:
    GL_SGIX_ycrcb_subsample = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5504
try:
    GL_SGIX_depth_pass_instrument = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5508
try:
    GL_3DFX_texture_compression_FXT1 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5512
try:
    GL_3DFX_multisample = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5516
try:
    GL_3DFX_tbuffer = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5524
try:
    GL_EXT_multisample = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5534
try:
    GL_SGIX_vertex_preclip = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5538
try:
    GL_SGIX_convolution_accuracy = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5542
try:
    GL_SGIX_resample = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5546
try:
    GL_SGIS_point_line_texgen = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5550
try:
    GL_SGIS_texture_color_mask = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5558
try:
    GL_SGIX_igloo_interface = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5566
try:
    GL_EXT_texture_env_dot3 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5570
try:
    GL_ATI_texture_mirror_once = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5574
try:
    GL_NV_fence = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5594
try:
    GL_NV_evaluators = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5618
try:
    GL_NV_packed_depth_stencil = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5622
try:
    GL_NV_register_combiners2 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5632
try:
    GL_NV_texture_compression_vtc = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5636
try:
    GL_NV_texture_rectangle = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5640
try:
    GL_NV_texture_shader = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5644
try:
    GL_NV_texture_shader2 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5648
try:
    GL_NV_vertex_array_range2 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5652
try:
    GL_NV_vertex_program = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5786
try:
    GL_SGIX_texture_coordinate_clamp = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5790
try:
    GL_SGIX_scalebias_hint = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5794
try:
    GL_OML_interlace = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5798
try:
    GL_OML_subsample = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5802
try:
    GL_OML_resample = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5806
try:
    GL_NV_copy_depth_to_color = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5810
try:
    GL_ATI_envmap_bumpmap = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5824
try:
    GL_ATI_fragment_shader = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5858
try:
    GL_ATI_pn_triangles = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5868
try:
    GL_ATI_vertex_array_object = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5898
try:
    GL_EXT_vertex_shader = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 5988
try:
    GL_ATI_vertex_streams = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6084
try:
    GL_ATI_element_array = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6096
try:
    GL_SUN_mesh_array = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6104
try:
    GL_SUN_slice_accum = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6108
try:
    GL_NV_multisample_filter_hint = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6112
try:
    GL_NV_depth_clamp = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6116
try:
    GL_NV_occlusion_query = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6136
try:
    GL_NV_point_sprite = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6146
try:
    GL_NV_texture_shader3 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6150
try:
    GL_NV_vertex_program1_1 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6154
try:
    GL_EXT_shadow_funcs = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6158
try:
    GL_EXT_stencil_two_side = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6166
try:
    GL_ATI_text_fragment_shader = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6170
try:
    GL_APPLE_client_storage = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6174
try:
    GL_APPLE_element_array = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6190
try:
    GL_APPLE_fence = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6212
try:
    GL_APPLE_vertex_array_object = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6226
try:
    GL_APPLE_vertex_array_range = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6238
try:
    GL_APPLE_ycbcr_422 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6242
try:
    GL_S3_s3tc = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6246
try:
    GL_ATI_draw_buffers = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6254
try:
    GL_ATI_pixel_format_float = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6261
try:
    GL_ATI_texture_env_combine3 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6265
try:
    GL_ATI_texture_float = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6269
try:
    GL_NV_float_buffer = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6273
try:
    GL_NV_fragment_program = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6292
try:
    GL_NV_half_float = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6390
try:
    GL_NV_pixel_data_range = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6400
try:
    GL_NV_primitive_restart = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6410
try:
    GL_NV_texture_expand_normal = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6414
try:
    GL_NV_vertex_program2 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6418
try:
    GL_ATI_map_object_buffer = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6428
try:
    GL_ATI_separate_stencil = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6438
try:
    GL_ATI_vertex_attrib_array_object = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6450
try:
    GL_OES_read_format = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6454
try:
    GL_EXT_depth_bounds_test = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6462
try:
    GL_EXT_texture_mirror_clamp = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6466
try:
    GL_EXT_blend_equation_separate = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6474
try:
    GL_MESA_pack_invert = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6478
try:
    GL_MESA_ycbcr_texture = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6482
try:
    GL_EXT_pixel_buffer_object = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6486
try:
    GL_NV_fragment_program_option = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6490
try:
    GL_NV_fragment_program2 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6494
try:
    GL_NV_vertex_program2_option = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6498
try:
    GL_NV_vertex_program3 = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6502
try:
    GL_EXT_framebuffer_object = 1
except:
    pass

# /usr/include/SDL/SDL_opengl.h: 6542
try:
    GL_GREMEDY_string_marker = 1
except:
    pass

# /usr/include/SDL/SDL_rotozoom.h: 31
try:
    SMOOTHING_OFF = 0
except:
    pass

# /usr/include/SDL/SDL_rotozoom.h: 36
try:
    SMOOTHING_ON = 1
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 40
try:
    SDL_TTF_MAJOR_VERSION = 2
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 41
try:
    SDL_TTF_MINOR_VERSION = 0
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 42
try:
    SDL_TTF_PATCHLEVEL = 11
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 55
try:
    TTF_MAJOR_VERSION = SDL_TTF_MAJOR_VERSION
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 56
try:
    TTF_MINOR_VERSION = SDL_TTF_MINOR_VERSION
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 57
try:
    TTF_PATCHLEVEL = SDL_TTF_PATCHLEVEL
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 67
try:
    UNICODE_BOM_NATIVE = 65279
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 68
try:
    UNICODE_BOM_SWAPPED = 65534
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 92
try:
    TTF_STYLE_NORMAL = 0
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 93
try:
    TTF_STYLE_BOLD = 1
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 94
try:
    TTF_STYLE_ITALIC = 2
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 95
try:
    TTF_STYLE_UNDERLINE = 4
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 96
try:
    TTF_STYLE_STRIKETHROUGH = 8
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 103
try:
    TTF_HINTING_NORMAL = 0
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 104
try:
    TTF_HINTING_LIGHT = 1
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 105
try:
    TTF_HINTING_MONO = 2
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 106
try:
    TTF_HINTING_NONE = 3
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 220
def TTF_RenderText(font, text, fg, bg):
    return (TTF_RenderText_Shaded (font, text, fg, bg))

# /usr/include/SDL/SDL_ttf.h: 222
def TTF_RenderUTF8(font, text, fg, bg):
    return (TTF_RenderUTF8_Shaded (font, text, fg, bg))

# /usr/include/SDL/SDL_ttf.h: 224
def TTF_RenderUNICODE(font, text, fg, bg):
    return (TTF_RenderUNICODE_Shaded (font, text, fg, bg))

# /usr/include/SDL/SDL_ttf.h: 240
try:
    TTF_SetError = SDL_SetError
except:
    pass

# /usr/include/SDL/SDL_ttf.h: 241
try:
    TTF_GetError = SDL_GetError
except:
    pass

SDL_mutex = struct_SDL_mutex # /usr/include/SDL/SDL_mutex.h: 55

SDL_semaphore = struct_SDL_semaphore # /usr/include/SDL/SDL_mutex.h: 86

SDL_cond = struct_SDL_cond # /usr/include/SDL/SDL_mutex.h: 133

SDL_Thread = struct_SDL_Thread # /usr/include/SDL/SDL_thread.h: 45

SDL_RWops = struct_SDL_RWops # /usr/include/SDL/SDL_rwops.h: 42

SDL_AudioSpec = struct_SDL_AudioSpec # /usr/include/SDL/SDL_audio.h: 93

SDL_AudioCVT = struct_SDL_AudioCVT # /usr/include/SDL/SDL_audio.h: 126

SDL_CDtrack = struct_SDL_CDtrack # /usr/include/SDL/SDL_cdrom.h: 76

SDL_CD = struct_SDL_CD # /usr/include/SDL/SDL_cdrom.h: 90

SDL_keysym = struct_SDL_keysym # /usr/include/SDL/SDL_keyboard.h: 64

SDL_Rect = struct_SDL_Rect # /usr/include/SDL/SDL_video.h: 53

SDL_Color = struct_SDL_Color # /usr/include/SDL/SDL_video.h: 60

SDL_Palette = struct_SDL_Palette # /usr/include/SDL/SDL_video.h: 66

SDL_PixelFormat = struct_SDL_PixelFormat # /usr/include/SDL/SDL_video.h: 91

private_hwdata = struct_private_hwdata # /usr/include/SDL/SDL_video.h: 105

SDL_BlitMap = struct_SDL_BlitMap # /usr/include/SDL/SDL_video.h: 115

SDL_Surface = struct_SDL_Surface # /usr/include/SDL/SDL_video.h: 122

SDL_VideoInfo = struct_SDL_VideoInfo # /usr/include/SDL/SDL_video.h: 188

private_yuvhwfuncs = struct_private_yuvhwfuncs # /usr/include/SDL/SDL_video.h: 217

private_yuvhwdata = struct_private_yuvhwdata # /usr/include/SDL/SDL_video.h: 218

SDL_Overlay = struct_SDL_Overlay # /usr/include/SDL/SDL_video.h: 226

WMcursor = struct_WMcursor # /usr/include/SDL/SDL_mouse.h: 40

SDL_Cursor = struct_SDL_Cursor # /usr/include/SDL/SDL_mouse.h: 48

_SDL_Joystick = struct__SDL_Joystick # /usr/include/SDL/SDL_joystick.h: 46

SDL_ActiveEvent = struct_SDL_ActiveEvent # /usr/include/SDL/SDL_events.h: 123

SDL_KeyboardEvent = struct_SDL_KeyboardEvent # /usr/include/SDL/SDL_events.h: 131

SDL_MouseMotionEvent = struct_SDL_MouseMotionEvent # /usr/include/SDL/SDL_events.h: 141

SDL_MouseButtonEvent = struct_SDL_MouseButtonEvent # /usr/include/SDL/SDL_events.h: 150

SDL_JoyAxisEvent = struct_SDL_JoyAxisEvent # /usr/include/SDL/SDL_events.h: 158

SDL_JoyBallEvent = struct_SDL_JoyBallEvent # /usr/include/SDL/SDL_events.h: 167

SDL_JoyHatEvent = struct_SDL_JoyHatEvent # /usr/include/SDL/SDL_events.h: 180

SDL_JoyButtonEvent = struct_SDL_JoyButtonEvent # /usr/include/SDL/SDL_events.h: 188

SDL_ResizeEvent = struct_SDL_ResizeEvent # /usr/include/SDL/SDL_events.h: 198

SDL_ExposeEvent = struct_SDL_ExposeEvent # /usr/include/SDL/SDL_events.h: 203

SDL_QuitEvent = struct_SDL_QuitEvent # /usr/include/SDL/SDL_events.h: 208

SDL_UserEvent = struct_SDL_UserEvent # /usr/include/SDL/SDL_events.h: 216

SDL_SysWMmsg = struct_SDL_SysWMmsg # /usr/include/SDL/SDL_syswm.h: 72

SDL_SysWMEvent = struct_SDL_SysWMEvent # /usr/include/SDL/SDL_events.h: 224

SDL_Event = union_SDL_Event # /usr/include/SDL/SDL_events.h: 242

_SDL_TimerID = struct__SDL_TimerID # /usr/include/SDL/SDL_timer.h: 104

SDL_version = struct_SDL_version # /usr/include/SDL/SDL_version.h: 51

Mix_Chunk = struct_Mix_Chunk # /usr/include/SDL/SDL_mixer.h: 107

_Mix_Music = struct__Mix_Music # /usr/include/SDL/SDL_mixer.h: 129

_TCPsocket = struct__TCPsocket # /usr/include/SDL/SDL_net.h: 107

_UDPsocket = struct__UDPsocket # /usr/include/SDL/SDL_net.h: 158

_SDLNet_SocketSet = struct__SDLNet_SocketSet # /usr/include/SDL/SDL_net.h: 269

SDL_SysWMinfo = struct_SDL_SysWMinfo # /usr/include/SDL/SDL_syswm.h: 114

_TTF_Font = struct__TTF_Font # /usr/include/SDL/SDL_ttf.h: 77

# No inserted files

