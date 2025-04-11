import unittest

loader = unittest.TestLoader()
tests = loader.discover('tests')
test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(tests)
