from unittest import TestCase
from main import create_header, create_text, create_bold, create_italic, create_link, create_inline_code


class TestMain(TestCase):

    def test_create_header(self):
        self.assertEqual('# hola\n', create_header(1, 'hola'))
        self.assertEqual('## mundo\n', create_header(2, 'mundo'))

    def test_create_text(self):
        self.assertEqual('hola', create_text('hola'))

    def test_create_bold(self):
        self.assertEqual('**hola**', create_bold('hola'))

    def test_create_italic(self):
        self.assertEqual('*hola*', create_italic('hola'))

    def test_create_link(self):
        self.assertEqual('[hola](mundo)', create_link('hola', 'mundo'))

    def test_create_inline_text(self):
        self.assertEqual('`hola`', create_inline_code('hola'))
