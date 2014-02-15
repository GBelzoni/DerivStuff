'''
Created on Feb 15, 2014

@author: phcostello
'''


from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# from Cython.Build import build_ext

ext_modules = [Extension("AnalyticFunctions2", ["AnalyticFunctions2.pyx"])]

setup(
      name = 'QDQuant App',
      cmdclass = {'build_ext': build_ext},
      ext_modules = ext_modules
#       ext_module = cythonize("AnalyticFunctions2.pyx"),
      )
