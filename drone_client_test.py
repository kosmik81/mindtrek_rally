
import unittest
import logging
import drone_client


class TestSomething(unittest.TestCase):


    def test_drone_client_subscribe(self):
        drone_client.subscribe()


if __name__ == '__main__':
    unittest.main()
