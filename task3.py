import unittest
import os
from mail import filter_mail


class MailTest(unittest.TestCase):
    def test_emails(self):
        inputed_list = []
        inputed_filenames = []

        output_list = []
        output_filenames = []

        for name in os.listdir('input'):
            inputed_filenames.append('input/' + name)

        for name in os.listdir('output'):
            output_filenames.append('output/' + name)

        for item in inputed_filenames:
            with open(item) as f:
                inputed_list.append(f.readlines()[1::])

        for item in output_filenames:
            with open(item) as f:
                output_list.append(f.read())

        for i in range(len(inputed_list)):
            inputed_list[i] = list(
                map(lambda x: x.replace('\n', ''), inputed_list[i]))

        for i in range(len(inputed_list)):
            self.assertEqual(f'{filter_mail(inputed_list[i])}', output_list[i])


if __name__ == '__main__':
    unittest.main()
