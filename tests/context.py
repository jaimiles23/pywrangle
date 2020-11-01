from __future__ import absolute_import

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pywrangle

try:    # imports for individual test scripts
    import create_df

except ModuleNotFoundError:     # pytest import needs to be relative
    from . import create_df