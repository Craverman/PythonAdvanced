import sys

sys.path.append('../')
from Lesson4.utils import *
from Lesson4.variables import *
import unittest


class TestSocket:
    def __init__(self, test_dict):
        self.testdict = test_dict

    def send(self, message_to_send):
        json_test_message = json.dumps(self.testdict)
        self.encoded_message = json_test_message.encode(ENCODING)
        self.receved_message = message_to_send



class Tests(unittest.TestCase):
    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 1.1,
        USER: {
            ACCOUNT_NAME: 'test_test'
        }
    }

    def test_send_message(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoded_message, test_socket.receved_message)

    def test_send_message2(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertIn(b"action", test_socket.receved_message)


if __name__ == '__main__':
    unittest.main()
