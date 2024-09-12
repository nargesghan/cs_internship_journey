import unittest
import os
from zip_extractor import extract_zip
from uaingzipfile import extract_zipfile

class TestZipExtractor(unittest.TestCase):

    def setUp(self):
        self.test_zip = 'test.zip'
        self.test_output_dir = 'test_output'
        self.test_file_content = b'This is a test file.'

        # Create a test zip file
        with open('test_file.txt', 'wb') as f:
            f.write(self.test_file_content)
        with zipfile.ZipFile(self.test_zip, 'w') as zipf:
            zipf.write('test_file.txt')

    def tearDown(self):
        # Clean up the test files and directories
        os.remove('test_file.txt')
        os.remove(self.test_zip)
        if os.path.exists(self.test_output_dir):
            for root, dirs, files in os.walk(self.test_output_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.test_output_dir)

    def test_extract_zip(self):
        extract_zip(self.test_zip, self.test_output_dir)
        extracted_file_path = os.path.join(self.test_output_dir, 'test_file.txt')
        self.assertTrue(os.path.exists(extracted_file_path))
        with open(extracted_file_path, 'rb') as f:
            content = f.read()
        self.assertEqual(content, self.test_file_content)

    def test_extract_zipfile(self):
        extract_zipfile(self.test_zip, self.test_output_dir)
        extracted_file_path = os.path.join(self.test_output_dir, 'test_file.txt')
        self.assertTrue(os.path.exists(extracted_file_path))
        with open(extracted_file_path, 'rb') as f:
            content = f.read()
        self.assertEqual(content, self.test_file_content)

if __name__ == '__main__':
    unittest.main()
