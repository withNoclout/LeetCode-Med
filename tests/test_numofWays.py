import os
import importlib.util
import unittest

MODULE_PATH = os.path.join(os.path.dirname(__file__), "..", "numofWays_2417.py")
MODULE_PATH = os.path.abspath(MODULE_PATH)

spec = importlib.util.spec_from_file_location("numofWays_2417", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestNumberOfWays(unittest.TestCase):
    def test_basic(self):
        sol = Solution()
        self.assertEqual(sol.numberOfWays("SS"), 1)
        self.assertEqual(sol.numberOfWays("SPS"), 1)
        self.assertEqual(sol.numberOfWays("SSPSS"), 2)
        self.assertEqual(sol.numberOfWays("PPP"), 0)


if __name__ == "__main__":
    unittest.main()
