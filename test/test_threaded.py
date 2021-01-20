import unittest

from interpreter.my_language import run

class TestMultiThreaded(unittest.TestCase):

    programms = {'test/sample_programms/test2.lang': [['b', 26.0]],
        'test/sample_programms/test3.lang': [['a', '15'], ['b', 18.0], ['c', '0']]
    }

    def test_upper(self):
        for i in self.programms.keys():
            f = open(i, 'r')
            file = f.read()
            f.close()

            self.assertEqual(self.programms[i], run(file, True))