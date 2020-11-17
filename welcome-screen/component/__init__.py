from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

for m in __all__:
    try:
        exec("from . import %s" %m)
        exec("reload(%s)" %m)
        exec("from .%s import *" %m)
        print("Importing %s" %m)
    except:
        print("Fail to import %s" %m)