import sys, platform
import ctypes, ctypes.util
import pathlib

mylib_path = pathlib.Path().absolute() / "mylib.dylib"
if not mylib_path:
    print("Unable to find the specified library.")
    sys.exit()

try:
    mylib = ctypes.CDLL(mylib_path)
except OSError:
    print("Unable to load the system C library")
    sys.exit()
mylib.test_empty()