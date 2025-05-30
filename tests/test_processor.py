import unittest
from app.core.processor import process_data

class TestProcessor(unittest.TestCase):
    def test_process_data(self):
        data = {"A": 1, "B": 2}
        result = process_data(data)
        self.assertIn("components", result)
        self.assertEqual(result["components"], ["A", "B"])

if __name__ == "__main__":
    unittest.main()
