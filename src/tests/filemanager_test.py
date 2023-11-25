import unittest
from file_manager import FileManager

class TestFileManager(unittest.TestCase):
    def setUp(self):
        with open("testfile.txt", "w") as file:
            file.write("one two three")
        self.manager=FileManager("testfile.txt")

    def test_file_manager_returns_text_with_existing_file(self):
        text=self.manager.read_file()
        self.assertEqual(text, "one two three")

    def test_file_manager_returns_none_with_non_existing_file(self):
        non_manager=FileManager("doesnotexist.txt")
        text=non_manager.read_file()
        self.assertEqual(text, None)

    def test_file_manager_writes_file(self):
        self.manager.write_file("four five six")
        text=self.manager.read_file()
        self.assertEqual(text, "four five six")
