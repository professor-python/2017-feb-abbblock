
from unittest import TestCase, main


class SomeTest(TestCase):

    def test_1(self):
        # 'FOO'.lower() # --> foo

        self.assertEqual(
            'fooo',             # ожидаемое
            'FOO'.lower()       # то, что проверяем
        )

    def test_2(self):

        self.assertTrue(
            'fooo' == 'FOO'.lower()       # то, что проверяем
        )

        


if __name__=='__main__':
    main()

