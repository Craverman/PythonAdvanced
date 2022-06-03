import sys

sys.path.append('../')
from Lesson4.client import create_presence
from Lesson4.variables import *
from Lesson4.client import process_ans
import unittest



# Класс с тестами
class TestClass(unittest.TestCase):


    # тест коректного запроса

    def test_def_presense_answer(self):
        test = create_presence('Vladislav')
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Vladislav'}})



    # тест корректтного разбора ответа 200
    def test_process_ans(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')


    def test_process_ans_400(self):
        self.assertIsNot(process_ans({RESPONSE: 200}), '400 : OK')




if __name__ == '__main__':
    unittest.main()
