from pathlib import Path

from cffi import FFI


def _load_h_file_contents(h_file_name):
    """Load the contents of a C header file"""
    with open(h_file_name, "r") as h_file:
        return h_file.read()


h_file_path = str(Path(__file__).parent / "my_functions.h")
h_file_contents = _load_h_file_contents(h_file_path)

ffibuilder = FFI()
ffibuilder.cdef(h_file_contents)
ffibuilder.set_source(
    "my_functions_module",  # name of the output C extension = name of the python module that will be generated
    '#include "my_functions.h"', # prepended to the generated my_functions_module.c file (doesn't have to be only the .h file link but general C source code)
    sources=["my_functions.c"]
)
ffibuilder.compile()
