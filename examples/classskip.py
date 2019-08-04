import unittest


@unittest.skip("showing class skipping")
class MySkippedClass(unittest.TestCase):
    def test_not_run(self):
        pass