from distutils.core import setup
from distutils.core import Extension
MOD = "spam"
module = Extension(MOD, sources =["python.c"])
setup(name = MOD, ext_modules = [module])
setup(name="dataType", version="1.0",
      ext_modules=[
         Extension("dataType", ["dataType.c"]),
         ])