# Python - C examples

Examples on how to call C code from Python.

## Useful links

- https://realpython.com/python-bindings-overview/

## Pre-requisites

- Install [Cygwin](https://www.cygwin.com/) with the following packages:
    - `gcc-core`
    - `gcc-g++`
    - `python3-devel`

- Add the path to the Cygwin bin (e.g. `C:/cygwin64/bin`) folder to the Windows PATH environment variable.
- Create new python 3.10 environment and install requirements by running `pip install -r requirements.txt`

## Ctypes

Based on this tutorial: https://www.digitalocean.com/community/tutorials/calling-c-functions-from-python

### Pre-requisites

Create a shared library from C code by running

```bash
gcc -fPIC -shared -o my_functions.so my_functions.c
```

this should generate file `my_functions.so` in the current directory.

### Run

Run the Python script by running

```bash
python ctypes_example.py
```

You should see the following output:

```
<class 'ctypes.CDLL'>
64
```

## CFFI

