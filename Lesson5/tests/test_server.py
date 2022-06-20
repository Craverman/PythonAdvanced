import sys

sys.path.append('../')
from variables import *
from Lesson4.client import process_ans
from Lesson4.server import process_client_message
import unittest

msg = {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}


class TestServerClass(unittest.TestCase):
    def test_process_client_message(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_process_client_message_400(self):
        self.assertEqual(process_client_message({21}), {'error': 'Bad Request', 'response': 400})

    def test_process_client_message_200(self):
        self.assertDictEqual(process_client_message(msg), {'response': 200})

    def test_process_client_message2(self):
        self.assertIn('response', process_client_message(msg))


