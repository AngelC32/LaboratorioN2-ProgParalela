from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        #"in_circle_opt_parallel",
        #["in_circle_opt_parallel.pyx"],
        "in_circle_parallel",
        ["in_circle_parallel.pyx"],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],
    )
]

setup(
    #name='parallel_circle_opt',
   name='parallel_circle',
    ext_modules=cythonize(ext_modules),
)

