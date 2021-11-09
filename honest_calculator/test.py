from unittest import TestCase
from .main import check_input


class TestMain(TestCase):

    def test_input(self):

        checks = [
            {
                'str_input': '2 + m',
                'str_output': 'Do you even know what numbers are? Stay focused!'
            },
            {
                'str_input': '2 + m',
                'str_output': 'Do you even know what numbers are? Stay focused!'
            },
            {
                'str_input': '2 + m',
                'str_output': 'Do you even know what numbers are? Stay focused!'
            },
            {
                'str_input': '4.7 * 5.2',
                'str_output': None,
            },
            {
                'str_input': '2 + 1.1',
                'str_output': None,
            }
        ]

        for check in checks:
            with self.subTest(i=check):
                print(check)
                self.assertEqual(check_input(check['str_input']), check['str_output'])
