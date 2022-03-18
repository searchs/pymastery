import unittest
import unitty


class TestUnitty(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 15
        result = unitty.do_stuff(test_param)
        self.assertEqual(result, 20)

    def test_do_stuff_str(self):
        test_param = "Just Strings"
        result = unitty.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)


if __name__ == "__main__":
    unittest.main()
