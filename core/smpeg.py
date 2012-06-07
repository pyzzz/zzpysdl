'''Wrapper for smpeg.h

Generated with:
ctypesgen.py --cpp=g++ -E -L/usr/lib -L/usr/lib64 -lsmpeg -lSDL -I/usr/include/SDL/ /usr/include/smpeg/smpeg.h -o smpeg.py

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

_libs["smpeg"] = load_library("smpeg")
_libs["SDL"] = load_library("SDL")

# 2 libraries
# End libraries

# No modules

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

Uint8 = c_uint8 # /usr/include/SDL/SDL_stdinc.h: 99

Sint16 = c_int16 # /usr/include/SDL/SDL_stdinc.h: 100

Uint16 = c_uint16 # /usr/include/SDL/SDL_stdinc.h: 101

Uint32 = c_uint32 # /usr/include/SDL/SDL_stdinc.h: 103

# /usr/include/SDL/SDL_mutex.h: 55
class struct_SDL_mutex(Structure):
    pass

SDL_mutex = struct_SDL_mutex # /usr/include/SDL/SDL_mutex.h: 56

# /usr/include/SDL/SDL_rwops.h: 42
class struct_SDL_RWops(Structure):
    pass

# /usr/include/SDL/SDL_rwops.h: 78
class struct_anon_30(Structure):
    pass

struct_anon_30.__slots__ = [
    'autoclose',
    'fp',
]
struct_anon_30._fields_ = [
    ('autoclose', c_int),
    ('fp', POINTER(FILE)),
]

# /usr/include/SDL/SDL_rwops.h: 83
class struct_anon_31(Structure):
    pass

struct_anon_31.__slots__ = [
    'base',
    'here',
    'stop',
]
struct_anon_31._fields_ = [
    ('base', POINTER(Uint8)),
    ('here', POINTER(Uint8)),
    ('stop', POINTER(Uint8)),
]

# /usr/include/SDL/SDL_rwops.h: 88
class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'data1',
]
struct_anon_32._fields_ = [
    ('data1', POINTER(None)),
]

# /usr/include/SDL/SDL_rwops.h: 65
class union_anon_33(Union):
    pass

union_anon_33.__slots__ = [
    'stdio',
    'mem',
    'unknown',
]
union_anon_33._fields_ = [
    ('stdio', struct_anon_30),
    ('mem', struct_anon_31),
    ('unknown', struct_anon_32),
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
    ('hidden', union_anon_33),
]

SDL_RWops = struct_SDL_RWops # /usr/include/SDL/SDL_rwops.h: 93

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

# /usr/include/smpeg/MPEGfilter.h: 33
class struct_SMPEG_FilterInfo(Structure):
    pass

struct_SMPEG_FilterInfo.__slots__ = [
    'yuv_mb_square_error',
    'yuv_pixel_square_error',
]
struct_SMPEG_FilterInfo._fields_ = [
    ('yuv_mb_square_error', POINTER(Uint16)),
    ('yuv_pixel_square_error', POINTER(Uint16)),
]

SMPEG_FilterInfo = struct_SMPEG_FilterInfo # /usr/include/smpeg/MPEGfilter.h: 33

# /usr/include/smpeg/MPEGfilter.h: 43
class struct_SMPEG_Filter(Structure):
    pass

SMPEG_FilterCallback = CFUNCTYPE(UNCHECKED(None), POINTER(SDL_Overlay), POINTER(SDL_Overlay), POINTER(SDL_Rect), POINTER(SMPEG_FilterInfo), POINTER(None)) # /usr/include/smpeg/MPEGfilter.h: 39

SMPEG_FilterDestroy = CFUNCTYPE(UNCHECKED(None), POINTER(struct_SMPEG_Filter)) # /usr/include/smpeg/MPEGfilter.h: 40

struct_SMPEG_Filter.__slots__ = [
    'flags',
    'data',
    'callback',
    'destroy',
]
struct_SMPEG_Filter._fields_ = [
    ('flags', Uint32),
    ('data', POINTER(None)),
    ('callback', SMPEG_FilterCallback),
    ('destroy', SMPEG_FilterDestroy),
]

SMPEG_Filter = struct_SMPEG_Filter # /usr/include/smpeg/MPEGfilter.h: 48

# /usr/include/smpeg/smpeg.h: 43
class struct_anon_43(Structure):
    pass

struct_anon_43.__slots__ = [
    'major',
    'minor',
    'patch',
]
struct_anon_43._fields_ = [
    ('major', Uint8),
    ('minor', Uint8),
    ('patch', Uint8),
]

SMPEG_version = struct_anon_43 # /usr/include/smpeg/smpeg.h: 43

# /usr/include/smpeg/smpeg.h: 56
class struct__SMPEG(Structure):
    pass

SMPEG = struct__SMPEG # /usr/include/smpeg/smpeg.h: 56

# /usr/include/smpeg/smpeg.h: 72
class struct__SMPEG_Info(Structure):
    pass

struct__SMPEG_Info.__slots__ = [
    'has_audio',
    'has_video',
    'width',
    'height',
    'current_frame',
    'current_fps',
    'audio_string',
    'audio_current_frame',
    'current_offset',
    'total_size',
    'current_time',
    'total_time',
]
struct__SMPEG_Info._fields_ = [
    ('has_audio', c_int),
    ('has_video', c_int),
    ('width', c_int),
    ('height', c_int),
    ('current_frame', c_int),
    ('current_fps', c_double),
    ('audio_string', c_char * 80),
    ('audio_current_frame', c_int),
    ('current_offset', Uint32),
    ('total_size', Uint32),
    ('current_time', c_double),
    ('total_time', c_double),
]

SMPEG_Info = struct__SMPEG_Info # /usr/include/smpeg/smpeg.h: 72

enum_anon_44 = c_int # /usr/include/smpeg/smpeg.h: 79

SMPEG_ERROR = (-1) # /usr/include/smpeg/smpeg.h: 79

SMPEG_STOPPED = (SMPEG_ERROR + 1) # /usr/include/smpeg/smpeg.h: 79

SMPEG_PLAYING = (SMPEG_STOPPED + 1) # /usr/include/smpeg/smpeg.h: 79

SMPEGstatus = enum_anon_44 # /usr/include/smpeg/smpeg.h: 79

SMPEG_DisplayCallback = CFUNCTYPE(UNCHECKED(None), POINTER(SDL_Surface), c_int, c_int, c_uint, c_uint) # /usr/include/smpeg/smpeg.h: 83

# /usr/include/smpeg/smpeg.h: 95
if hasattr(_libs['smpeg'], 'SMPEG_new'):
    SMPEG_new = _libs['smpeg'].SMPEG_new
    SMPEG_new.argtypes = [String, POINTER(SMPEG_Info), c_int]
    SMPEG_new.restype = POINTER(SMPEG)

# /usr/include/smpeg/smpeg.h: 98
if hasattr(_libs['smpeg'], 'SMPEG_new_descr'):
    SMPEG_new_descr = _libs['smpeg'].SMPEG_new_descr
    SMPEG_new_descr.argtypes = [c_int, POINTER(SMPEG_Info), c_int]
    SMPEG_new_descr.restype = POINTER(SMPEG)

# /usr/include/smpeg/smpeg.h: 105
if hasattr(_libs['smpeg'], 'SMPEG_new_data'):
    SMPEG_new_data = _libs['smpeg'].SMPEG_new_data
    SMPEG_new_data.argtypes = [POINTER(None), c_int, POINTER(SMPEG_Info), c_int]
    SMPEG_new_data.restype = POINTER(SMPEG)

# /usr/include/smpeg/smpeg.h: 108
if hasattr(_libs['smpeg'], 'SMPEG_new_rwops'):
    SMPEG_new_rwops = _libs['smpeg'].SMPEG_new_rwops
    SMPEG_new_rwops.argtypes = [POINTER(SDL_RWops), POINTER(SMPEG_Info), c_int]
    SMPEG_new_rwops.restype = POINTER(SMPEG)

# /usr/include/smpeg/smpeg.h: 111
if hasattr(_libs['smpeg'], 'SMPEG_getinfo'):
    SMPEG_getinfo = _libs['smpeg'].SMPEG_getinfo
    SMPEG_getinfo.argtypes = [POINTER(SMPEG), POINTER(SMPEG_Info)]
    SMPEG_getinfo.restype = None

# /usr/include/smpeg/smpeg.h: 114
if hasattr(_libs['smpeg'], 'SMPEG_enableaudio'):
    SMPEG_enableaudio = _libs['smpeg'].SMPEG_enableaudio
    SMPEG_enableaudio.argtypes = [POINTER(SMPEG), c_int]
    SMPEG_enableaudio.restype = None

# /usr/include/smpeg/smpeg.h: 117
if hasattr(_libs['smpeg'], 'SMPEG_enablevideo'):
    SMPEG_enablevideo = _libs['smpeg'].SMPEG_enablevideo
    SMPEG_enablevideo.argtypes = [POINTER(SMPEG), c_int]
    SMPEG_enablevideo.restype = None

# /usr/include/smpeg/smpeg.h: 120
if hasattr(_libs['smpeg'], 'SMPEG_delete'):
    SMPEG_delete = _libs['smpeg'].SMPEG_delete
    SMPEG_delete.argtypes = [POINTER(SMPEG)]
    SMPEG_delete.restype = None

# /usr/include/smpeg/smpeg.h: 123
if hasattr(_libs['smpeg'], 'SMPEG_status'):
    SMPEG_status = _libs['smpeg'].SMPEG_status
    SMPEG_status.argtypes = [POINTER(SMPEG)]
    SMPEG_status.restype = SMPEGstatus

# /usr/include/smpeg/smpeg.h: 126
if hasattr(_libs['smpeg'], 'SMPEG_setvolume'):
    SMPEG_setvolume = _libs['smpeg'].SMPEG_setvolume
    SMPEG_setvolume.argtypes = [POINTER(SMPEG), c_int]
    SMPEG_setvolume.restype = None

# /usr/include/smpeg/smpeg.h: 133
if hasattr(_libs['smpeg'], 'SMPEG_setdisplay'):
    SMPEG_setdisplay = _libs['smpeg'].SMPEG_setdisplay
    SMPEG_setdisplay.argtypes = [POINTER(SMPEG), POINTER(SDL_Surface), POINTER(SDL_mutex), SMPEG_DisplayCallback]
    SMPEG_setdisplay.restype = None

# /usr/include/smpeg/smpeg.h: 137
if hasattr(_libs['smpeg'], 'SMPEG_loop'):
    SMPEG_loop = _libs['smpeg'].SMPEG_loop
    SMPEG_loop.argtypes = [POINTER(SMPEG), c_int]
    SMPEG_loop.restype = None

# /usr/include/smpeg/smpeg.h: 140
if hasattr(_libs['smpeg'], 'SMPEG_scaleXY'):
    SMPEG_scaleXY = _libs['smpeg'].SMPEG_scaleXY
    SMPEG_scaleXY.argtypes = [POINTER(SMPEG), c_int, c_int]
    SMPEG_scaleXY.restype = None

# /usr/include/smpeg/smpeg.h: 141
if hasattr(_libs['smpeg'], 'SMPEG_scale'):
    SMPEG_scale = _libs['smpeg'].SMPEG_scale
    SMPEG_scale.argtypes = [POINTER(SMPEG), c_int]
    SMPEG_scale.restype = None

# /usr/include/smpeg/smpeg.h: 147
if hasattr(_libs['smpeg'], 'SMPEG_move'):
    SMPEG_move = _libs['smpeg'].SMPEG_move
    SMPEG_move.argtypes = [POINTER(SMPEG), c_int, c_int]
    SMPEG_move.restype = None

# /usr/include/smpeg/smpeg.h: 150
if hasattr(_libs['smpeg'], 'SMPEG_setdisplayregion'):
    SMPEG_setdisplayregion = _libs['smpeg'].SMPEG_setdisplayregion
    SMPEG_setdisplayregion.argtypes = [POINTER(SMPEG), c_int, c_int, c_int, c_int]
    SMPEG_setdisplayregion.restype = None

# /usr/include/smpeg/smpeg.h: 153
if hasattr(_libs['smpeg'], 'SMPEG_play'):
    SMPEG_play = _libs['smpeg'].SMPEG_play
    SMPEG_play.argtypes = [POINTER(SMPEG)]
    SMPEG_play.restype = None

# /usr/include/smpeg/smpeg.h: 156
if hasattr(_libs['smpeg'], 'SMPEG_pause'):
    SMPEG_pause = _libs['smpeg'].SMPEG_pause
    SMPEG_pause.argtypes = [POINTER(SMPEG)]
    SMPEG_pause.restype = None

# /usr/include/smpeg/smpeg.h: 159
if hasattr(_libs['smpeg'], 'SMPEG_stop'):
    SMPEG_stop = _libs['smpeg'].SMPEG_stop
    SMPEG_stop.argtypes = [POINTER(SMPEG)]
    SMPEG_stop.restype = None

# /usr/include/smpeg/smpeg.h: 162
if hasattr(_libs['smpeg'], 'SMPEG_rewind'):
    SMPEG_rewind = _libs['smpeg'].SMPEG_rewind
    SMPEG_rewind.argtypes = [POINTER(SMPEG)]
    SMPEG_rewind.restype = None

# /usr/include/smpeg/smpeg.h: 165
if hasattr(_libs['smpeg'], 'SMPEG_seek'):
    SMPEG_seek = _libs['smpeg'].SMPEG_seek
    SMPEG_seek.argtypes = [POINTER(SMPEG), c_int]
    SMPEG_seek.restype = None

# /usr/include/smpeg/smpeg.h: 168
if hasattr(_libs['smpeg'], 'SMPEG_skip'):
    SMPEG_skip = _libs['smpeg'].SMPEG_skip
    SMPEG_skip.argtypes = [POINTER(SMPEG), c_float]
    SMPEG_skip.restype = None

# /usr/include/smpeg/smpeg.h: 174
if hasattr(_libs['smpeg'], 'SMPEG_renderFrame'):
    SMPEG_renderFrame = _libs['smpeg'].SMPEG_renderFrame
    SMPEG_renderFrame.argtypes = [POINTER(SMPEG), c_int]
    SMPEG_renderFrame.restype = None

# /usr/include/smpeg/smpeg.h: 177
if hasattr(_libs['smpeg'], 'SMPEG_renderFinal'):
    SMPEG_renderFinal = _libs['smpeg'].SMPEG_renderFinal
    SMPEG_renderFinal.argtypes = [POINTER(SMPEG), POINTER(SDL_Surface), c_int, c_int]
    SMPEG_renderFinal.restype = None

# /usr/include/smpeg/smpeg.h: 180
if hasattr(_libs['smpeg'], 'SMPEG_filter'):
    SMPEG_filter = _libs['smpeg'].SMPEG_filter
    SMPEG_filter.argtypes = [POINTER(SMPEG), POINTER(SMPEG_Filter)]
    SMPEG_filter.restype = POINTER(SMPEG_Filter)

# /usr/include/smpeg/smpeg.h: 185
if hasattr(_libs['smpeg'], 'SMPEG_error'):
    SMPEG_error = _libs['smpeg'].SMPEG_error
    SMPEG_error.argtypes = [POINTER(SMPEG)]
    if sizeof(c_int) == sizeof(c_void_p):
        SMPEG_error.restype = ReturnString
    else:
        SMPEG_error.restype = String
        SMPEG_error.errcheck = ReturnString

# /usr/include/smpeg/smpeg.h: 192
if hasattr(_libs['smpeg'], 'SMPEG_playAudio'):
    SMPEG_playAudio = _libs['smpeg'].SMPEG_playAudio
    SMPEG_playAudio.argtypes = [POINTER(SMPEG), POINTER(Uint8), c_int]
    SMPEG_playAudio.restype = c_int

# /usr/include/smpeg/smpeg.h: 196
if hasattr(_libs['smpeg'], 'SMPEG_playAudioSDL'):
    SMPEG_playAudioSDL = _libs['smpeg'].SMPEG_playAudioSDL
    SMPEG_playAudioSDL.argtypes = [POINTER(None), POINTER(Uint8), c_int]
    SMPEG_playAudioSDL.restype = None

# /usr/include/smpeg/smpeg.h: 199
if hasattr(_libs['smpeg'], 'SMPEG_wantedSpec'):
    SMPEG_wantedSpec = _libs['smpeg'].SMPEG_wantedSpec
    SMPEG_wantedSpec.argtypes = [POINTER(SMPEG), POINTER(SDL_AudioSpec)]
    SMPEG_wantedSpec.restype = c_int

# /usr/include/smpeg/smpeg.h: 202
if hasattr(_libs['smpeg'], 'SMPEG_actualSpec'):
    SMPEG_actualSpec = _libs['smpeg'].SMPEG_actualSpec
    SMPEG_actualSpec.argtypes = [POINTER(SMPEG), POINTER(SDL_AudioSpec)]
    SMPEG_actualSpec.restype = None

# /usr/include/smpeg/smpeg.h: 35
try:
    SMPEG_MAJOR_VERSION = 0
except:
    pass

# /usr/include/smpeg/smpeg.h: 36
try:
    SMPEG_MINOR_VERSION = 4
except:
    pass

# /usr/include/smpeg/smpeg.h: 37
try:
    SMPEG_PATCHLEVEL = 5
except:
    pass

# /usr/include/smpeg/smpeg.h: 143
def SMPEG_double(mpeg, on):
    return (SMPEG_scale (mpeg, on and 2 or 1))

_SMPEG = struct__SMPEG # /usr/include/smpeg/smpeg.h: 56

_SMPEG_Info = struct__SMPEG_Info # /usr/include/smpeg/smpeg.h: 72

# No inserted files

