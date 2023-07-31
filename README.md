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

## CFFI

Has 2 modes -- API and ABI. API uses C compiler to generate full python module, ABI loads the shared library (.so?) and
interacts with it directly. **API is the preffered way.**

Has 2 ways when to compile the bindings -- `in-line` mode compiles every time you run the python script. 
`out-of-line` mode compiles once and then uses the compiled module = faster. That is what we will use.

= C Foreign Function Interface for Python.

### Pre-requisites

- Install [Visual Studio Build Tools](https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst)
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