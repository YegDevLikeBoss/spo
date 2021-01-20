import unittest

from interpreter.my_language import run

class TestSingleThreaded(unittest.TestCase):

    programms = {'test/sample_programms/test1.lang': [['a', 11.0], ['b', 62.0], ['c', 4.0], ['d', '9']],
        'test/sample_programms/test2.lang': [['b', 26.0]],
        'test/sample_programms/test3.lang': [['a', '15'], ['b', 18.0], ['c', '0']],
        'test/sample_programms/test4.lang': [['a', 0.0], ['b', 60.0], ['k', -20.0]],
        'test/sample_programms/test5.lang': [['a', 0.0], ['b', 65.0], ['k', '1']]
    }

    def test_upper(self):
        for i in self.programms.keys():
            f = open(i, 'r')
            file = f.read()
            f.close()

            self.assertEqual(self.programms[i], run(file, False))