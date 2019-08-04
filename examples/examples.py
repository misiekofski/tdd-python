import sys
import unittest


class ExampleTests(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

    def test_expected_exception(self):
        with self.assertRaises(Exception):
            print (1/0)

if __name__ == '__main__':
    unittest.main()