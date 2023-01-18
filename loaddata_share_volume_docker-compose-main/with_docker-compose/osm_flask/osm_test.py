import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_get_row(self):
        # Make a GET request to the API to get a row with id 82a69eb5b7f8166a
        response = requests.get('http://localhost:5000/row/82a69eb5b7f8166a')
        # Assert that the request was successful (response code 200)
        self.assertEqual(response.status_code, 200)
        # Assert that the returned data contains the expected values
        self.assertEqual(response.json()[70], '82a69eb5b7f8166a')
        self.assertEqual(response.json()[0], 50.66396595000001)

if __name__ == '__main__':
    unittest.main()
