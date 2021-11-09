from unittest import TestCase
from main import parse_input, calculate


class TestMain(TestCase):

    def test_parse_input(self):

        checks = [
            {
                'str_input': '2 + m',
                'str_output': (None, None, None, 'Do you even know what numbers are? Stay focused!'),
            },
            {
                'str_input': '2 + m',
                'str_output': (None, None, None, 'Do you even know what numbers are? Stay focused!'),
            },
            {
                'str_input': '2 + m',
                'str_output': (None, None, None, 'Do you even know what numbers are? Stay focused!'),
            },
            {
                'str_input': '4.7 * 5.2',
                'str_output': (4.7, '*', 5.2, None),
            },
            {
                'str_input': '2 + 1.1',
                'str_output': (2.0, '+', 1.1, None),
            }
        ]

        for check in checks:
            with self.subTest(i=check):
                self.assertEqual(parse_input(check['str_input']), check['str_output'])

    def test_calculate(self):

        checks = [
            {
                'input': (4, '/', 0),
                'output': (None, 'Yeah... division by zero. Smart move...'),
            },
            {
                'input': (4 , '*', 5.2),
                'output': (20.8, None),
            },
            {
                'input': (411, '-', 211),
                'output': (200.0, None),
            },
        ]

        for check in checks:
            with self.subTest(i=check):
                self.assertEqual(calculate(*check['input']), check['output'])
