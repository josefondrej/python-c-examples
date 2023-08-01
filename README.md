# Python - C examples

Examples on how to call C code from Python. There are basically 4 options:

- ctypes
- CFFI
- PyBind11
- Cython

## Useful links

Based on:

- https://realpython.com/python-bindings-overview/

## Pre-requisites

- Install [Cygwin](https://www.cygwin.com/) with the following packages:
    - `gcc-core`
    - `gcc-g++`
    - `python3-devel`
    - `cmake`

- Add the path to the Cygwin bin (e.g. `C:/cygwin64/bin`) folder to the Windows PATH environment variable.
- Create new python 3.10 environment and install requirements by running `pip install -r requirements.txt`

## 1. Ctypes

Focuses on C (not C++)

Based on this tutorial: https://www.digitalocean.com/community/tutorials/calling-c-functions-from-python

### Pre-requisites

Create a shared library from C code by running (from the root of the project):

```bash
gcc -fPIC -shared -o ctypes/my_functions.so ctypes/my_functions.c
```

this should generate file `my_functions.so` in the `ctypes` directory.

### Run

Run the Python script by running

```bash
cd ctypes
python ctypes_example.py
```

You should see the following output:

```
<class 'ctypes.CDLL'>
64
```

## 2. CFFI

Focuses on C (not C++). Generates python module that can be used directly.

Has 2 modes -- API and ABI. API uses C compiler to generate full python module, ABI loads the shared library (.so?) and
interacts with it directly. **API is the preffered way.**

Has 2 ways when to compile the bindings -- `in-line` mode compiles every time you run the python script.
`out-of-line` mode compiles once and then uses the compiled module = faster. That is what we will use.

= C Foreign Function Interface for Python.

### Pre-requisites

-

Install [Visual Studio Build Tools](https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst)

- Build the shared library by running (from the root of the project):

  ```bash
  cd cffi
  python build.py
  ``` 
  which produces something like `my_functions_module.cp310-win_amd64.pyd` and `my_functions_module.c` files in
  the `cffi` directory.

### Run

From the root of the project, run:

```bash
cd cffi
python cffi_example.py
```

You should get `12.0` as output

## 3. PyBind11

Focuses on C++ 11 and newer (not C). Generates python module that can be used directly.

### Pre-requisities

Install Visual Studio with C++ and Python dev tools. Install pybind11 using pip.

### Run

First you need to compile and install the package by:

```
cd pybind11
pip install .
```

and then run the example by

```
cd pybind11
python pybind11_example.py
```

You should see the output 3.0.

### Useful links

- https://stackoverflow.com/questions/76323649/pybind11-compilation-errors-from-several-library-files
- https://learn.microsoft.com/en-us/visualstudio/python/working-with-c-cpp-python-in-visual-studio?view=vs-2022

## 4. Cython

Uses python-like language that generates C or C++ code that can be compiled into a python module.

https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html

### Pre-requisities

Install cython using pip.

### Run

From the root of the project, run:

```
cd cython
python setup.py build_ext --inplace
```

and then from the root of the project, run:

```
cd cython
python cython_example.py
```

You should see the output 5.0