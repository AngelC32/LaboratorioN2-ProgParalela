from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "draw_processing_parallel",
        ["draw_processing_parallel.pyx"],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],
    )
]

setup(
   name='parallel_draw_processing',
    ext_modules=cythonize(ext_modules),
)

