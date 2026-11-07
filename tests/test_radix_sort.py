import importlib.util
from pathlib import Path
import sys
import types
import unittest

# Isolate the pure algorithm from optional package-level plotting dependencies.
for name in ('sandbox_pkg', 'sandbox_pkg.sorting', 'sandbox_pkg.factory', 'sandbox_pkg.factory.registry'):
    module = types.ModuleType(name)
    module.__path__ = []
    sys.modules[name] = module
sys.modules['sandbox_pkg.factory.registry'].register_algo = lambda name: lambda fn: fn
spec = importlib.util.spec_from_file_location(
    'sandbox_pkg.sorting.linear_sort',
    str(Path(__file__).resolve().parents[1] / 'datastructure_factory' / 'sorting' / 'linear_sort.py'),
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class RadixTests(unittest.TestCase):
    def test_regular_and_duplicates(self):
        self.assertEqual(mod.radix_sort([91, 3, 10, 3, 0]), [0, 3, 3, 10, 91])
        self.assertEqual(mod.radix_sort([15, 1, 2, 0], base=2), [0, 1, 2, 15])

    def test_empty_and_zero(self):
        self.assertEqual(mod.radix_sort([]), [])
        self.assertEqual(mod.radix_sort([0, 0]), [0, 0])

    def test_negative_rejected(self):
        with self.assertRaises(ValueError):
            mod.radix_sort([-1, 2])

    def test_invalid_base_rejected(self):
        for base in (0, 1, -2):
            with self.subTest(base=base), self.assertRaises(ValueError):
                mod.radix_sort([1, 2], base=base)

    def test_empty_invalid_base_rejected(self):
        with self.assertRaises(ValueError):
            mod.radix_sort([], base=1)


if __name__ == '__main__':
    unittest.main()
