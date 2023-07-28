import ctypes
import os

os.add_dll_directory('C:/cygwin64/bin')  # This is where cygwin .dll files live
my_functions = ctypes.CDLL("./my_functions.so")

print(type(my_functions))
my_functions.multiply.restype = ctypes.c_float
print(my_functions.multiply(ctypes.c_float(4.0), ctypes.c_float(16.0)))
