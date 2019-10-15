from os.path import dirname, basename, isfile
from .person import Person
from .account import Account

__version__ = "1.0.0"

import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]