import importlib
import unittest

from subpy import detect


class TestStandardLibrary(unittest.TestCase):

    def test_fullstdlib(self):
        from subpy.stdlib import libraries

        for lib in libraries:
            mod = importlib.import_module(lib)
            detect(mod)

