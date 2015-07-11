import os
import sys

try:
    from .local import *
except ImportError:
    print("Loading development.py settings...", file=sys.stderr)
    from .development import *

