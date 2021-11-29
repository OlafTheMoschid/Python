import unittest
import datetime
from unittest.mock import patch
import date_past


class DateTest(unittest.TestCase):
    @patch('date_past.PastDate.is_past_date', return_value=True)
    def test_wrongMock(self, is_past_date):
        self.assertEqual(is_past_date(datetime.date(2022, 10, 10)), False)

    @patch('date_past.PastDate.is_past_date', return_value=True)
    def test_wrongInputMock(self, is_past_date):
        self.assertEqual(is_past_date(datetime.date(2022, 10, 10)), True)

    @patch('date_past.PastDate.is_past_date', return_value=False)
    def test_rightInputMock(self, is_past_date):
        self.assertEqual(is_past_date(datetime.date(2022, 10, 10)), False)


if __name__ == '__main__':
    unittest.main()
