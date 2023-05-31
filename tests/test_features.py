import sys
import unittest

from subpy import detect
from subpy import features as f


class TestFeatureDetect(unittest.TestCase):

    def has(self, feature, fn):
        self.assertTrue(feature in detect(fn))

    def not_has(self, feature, fn):
        self.assertTrue(feature not in detect(fn))

    def test_implicit_casts(self):

        def fn():
            return 1 + 2.0

        self.has(f.ImplicitCasts, fn)

    def test_generators(self):

        def fn():
            yield 1

        self.has(f.Generators, fn)

    def test_delvar(self):

        def fn():
            x = 3
            del x

        self.has(f.DelVar, fn)

    def test_closure(self):

        def fn():
            x = 3

            def closure():
                print(x)

        self.has(f.Closures, fn)

    def test_classes(self):

        def fn():
            class Class:
                pass

        self.has(f.Classes, fn)

    def test_decorators(self):

        def fn():
            @f
            def g():
                pass

        self.has(f.Decorators, fn)

    def test_varargs1(self):

        def fn():
            def foo(*xs):
                pass

        self.has(f.VarArgs, fn)

    def test_varargs2(self):

        def fn():
            list(map(id, *xs))

        self.has(f.VarArgs, fn)

    def test_kwargs1(self):

        def fn():
            def foo(**kw):
                pass

        self.has(f.KeywordArgs, fn)

    def test_kwargs2(self):

        def fn():
            foo(x=3)

        self.has(f.KeywordArgs, fn)

    def test_kwargs3(self):

        def fn():
            foo(**kw)

        self.has(f.KeywordArgs, fn)

    def test_inheritance(self):

        def fn():
            class foo(int):
                pass

        self.has(f.Inheritance, fn)
        self.not_has(f.MInheritance, fn)

    def test_minheritance(self):

        def fn():
            class foo(int, bool):
                pass

        self.has(f.MInheritance, fn)
        self.has(f.Inheritance, fn)

    def test_class_decorators(self):

        def fn():
            @foo
            class foo(object):
                pass

        self.has(f.ClassDecorators, fn)

    def test_assertions(self):

        def fn():
            assert True

        self.has(f.Assertions, fn)

    def test_chain_comparisons(self):

        def fn():
            x > y > z

        self.has(f.ChainComparison, fn)

    def test_exceptions1(self):

        def fn():
            raise Exception

        self.has(f.Exceptions, fn)

    def test_exceptions2(self):

        def fn():
            try:
                foo()
            except Exception as e:
                pass

        self.has(f.Exceptions, fn)

    def test_exceptions3(self):

        def fn():
            try:
                foo()
            finally:
                pass

        self.has(f.Exceptions, fn)

    def test_lambda(self):

        def fn():
            S = lambda x: lambda y: lambda z: x(z)(y(z))
            K = lambda x: lambda y: x
            I = lambda x: x

        self.has(f.Lambda, fn)

    def test_relative_imports(self):

        def fn():
            from . import foo

        self.has(f.RelativeImports, fn)

    def test_importstar(self):

        fn = """from sys import *"""

        self.has(f.ImportStar, fn)

    def test_heterolist(self):

        def fn():
            [1, 2.0, None, 'guido']

        self.has(f.HeteroList, fn)

    def test_continue(self):

        def fn():
            while True:
                continue

        self.has(f.Continue, fn)

    def test_multiple_return(self):

        def fn():
            return 1, None

        self.has(f.MultipleReturn, fn)

    def test_dict_comp(self):

        def fn():
            {a: b for a, b in xs}

        self.has(f.DictComp, fn)

    def test_ellipsis1(self):

        def fn():
            xs[1:2, ..., 0]

        self.has(f.Ellipsi, fn)

    def test_ellipsis2(self):

        def fn():
            xs[...]

        self.has(f.Ellipsi, fn)

    def test_tuple_unpacking(self):

        def fn():
            x, y = [1, 2]

        self.has(f.TupleUnpacking, fn)

    def test_exec(self):

        def fn():
            exec('foo', {})

        self.has(f.Exec, fn)

    def test_fancy_indexing(self):

        def fn():
            A[1:, 20:10:-2, ...]

        self.has(f.FancyIndexing, fn)

    def test_globals(self):

        def fn():
            global x

        self.has(f.Globals, fn)

    def test_context_managers(self):

        def fn():
            with foo:
                pass

        self.has(f.ContextManagers, fn)

    def test_generator_exp1(self):

        def fn():
            (a for a in x)

        self.has(f.GeneratorExp, fn)

    def test_generator_exp2(self):

        def fn():
            f(a for a in x)

        self.has(f.GeneratorExp, fn)

    def test_ternary(self):

        def fn():
            a if True else b

        self.has(f.Ternary, fn)

    def test_listcomp(self):

        def fn():
            [a for a in x]

        self.has(f.ListComp, fn)

    def test_setcomp(self):

        def fn():
            {a for a in x}

        self.has(f.SetComp, fn)

    def test_custom_iterators1(self):

        def fn():
            for a in foo:
                pass

        self.has(f.CustomIterators, fn)

    def test_custom_iterators2(self):

        def fn():
            for a in set([1, 2, 3]):
                pass

        self.has(f.CustomIterators, fn)

    def test_custom_iterators3(self):

        def fn():
            for a in range(25):
                pass
            for a in range(25):
                pass

        self.not_has(f.CustomIterators, fn)

    def test_printing(self):

        def fn():
            print('hello world')

        self.has(f.Printing, fn)

    def test_metaclass(self):

        def fn():
            class Foo(object, metaclass=Bar):
                pass

        self.has(f.Metaclasses, fn)
