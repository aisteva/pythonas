from distutils.core import setup
from distutils.core import Extension
MOD = "spam"
module = Extension(MOD, sources =["python.c"])
setup(name = MOD, ext_modules = [module])
setup(name="noddy", version="1.0",
      ext_modules=[
         Extension("noddy", ["noddy.c"]),
         Extension("noddy2", ["noddy2.c"]),
         ])