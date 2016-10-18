
import unittest
import logging
import drone_client


class TestSomething(unittest.TestCase):


    def test_drone_client_subscribe(self):
        drone_client.subscribe()

    def test__update_command_id(self):
        command_dict = {"m1" : "1", "m2" : "2", "m_up" : "10", "time" : "100", "command_id" : "3"}
        expected_output = {"m1" : "1", "m2" : "2", "m_up" : "10", "time" : "100", "command_id" : "4"}
        self.assertEqual(expected_output, drone_client._update_command_id(command_dict))

    def test_average_of_latest_values(self):
        self.assertEqual(10, drone_client.average_of_latest_values("joku", "10"))

        for item in range(1, 15):
            print drone_client.average_of_latest_values("joku", item)
if __name__ == '__main__':
    unittest.main()
