import unittest


class TestToplevel(unittest.TestCase):

    def test_detect(self):
        from subpy import detect, features

        def foo():
            lambda x:x
            x, y = (1,2)

        t1 = features.TupleUnpacking in detect(foo)
        t2 = features.Lambda in detect(foo)

        self.assertTrue(t1)
        self.assertTrue(t2)

    def test_checker(self):
        from subpy import checker
        from subpy.features import ListComp, SetComp

        def comps():
            return [x**2 for x in range(25)]

        my_subset = set([
            ListComp,
            SetComp,
        ])

        features = checker(comps)

        self.assertTrue(ListComp in features)

    def test_validator(self):

        from subpy import validator, FullPython, FeatureNotSupported
        from subpy.features import ListComp, SetComp

        def comps():
            return [x**2 for x in range(25)]

        my_features = FullPython - set([
            ListComp,
            SetComp,
        ])

        with self.assertRaises(FeatureNotSupported):
            validator(comps, features=my_features)
