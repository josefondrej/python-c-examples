import ctypes
import os

os.add_dll_directory('C:/cygwin64/bin')  # This is where cygwin .dll files live
my_functions = ctypes.CDLL("./my_functions.so")

print(type(my_functions))
print(my_functions.square(8))
