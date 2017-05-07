from setuptools import setup, Extension
import numpy as np
from codecs import open
import os

# This file largely taken from https://github.com/Martinsos/edlib/blob/a77e81678abd9392f1e13ec8585831721a1f354a/bindings/python/setup.py

# Build directly from cython source file(s) if user wants so (probably for some experiments).
# Otherwise, pre-generated c source file(s) are used.
# User has to set environment variable LWS_USE_CYTHON.
# e.g.: LWS_USE_CYTHON=1 python setup.py install
cmdclass = {}
USE_CYTHON = os.getenv('LWS_USE_CYTHON', False)
if USE_CYTHON:
    from Cython.Build import build_ext
    edlib_module_src = "lws.pyx"
    cmdclass['build_ext'] = build_ext
else:
    edlib_module_src = "lws.bycython.c"


long_description = ""
# Load README into long description.
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Information
    name = "lws",
    description = "Fast spectrogram phase reconstruction using Local Weighted Sums",
    long_description = long_description,
    version = "1.0.0",
    url = "http://www.jonathanleroux.org/",
    author = "Jonathan Le Roux",
    author_email = "leroux@merl.com",
    license = "Apache 2.0",
    keywords = "phase reconstruction stft",
    # Build instructions
    ext_modules = [Extension("lws",
                             sources=["lws.bycython.cpp","lwslib/lwslib.cpp"],
                             include_dirs=["lwslib/",np.get_include()],
                             language="c++",
                             extra_compile_args=["-O3"])],
    cmdclass = cmdclass
)
