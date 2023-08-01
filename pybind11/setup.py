from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

ext_modules = [
    Pybind11Extension("pybind_example", ["src/main.cpp"]),
]

setup(
    name="pybind_example",
    version="0.0.1",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext}
)
