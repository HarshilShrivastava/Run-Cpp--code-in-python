import sys, platform
import ctypes, ctypes.util

if platform.system() == "Windows":
    path_libc = ctypes.util.find_library("msvcrt")
else:
    path_libc = ctypes.util.find_library("c")
try:
    libc = ctypes.CDLL(path_libc)
except OSError:
    print("Unable to load the system C library")
    sys.exit()
print(path_libc)
libc.puts(b"Hello from Python to C")