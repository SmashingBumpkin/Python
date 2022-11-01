import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, dictList, expected):
        '''Test implementation
            - dictList      : list of dictionaries
            - expected      : expected dictionary
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es36(dictList)
        self.assertEqual(type(result), dict,
                         "The result is not a dictionary")
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")


    @data(
        ([{'a': [1, 3, 5], 'b': [2, 3], 'd': [3]}, {'a': [5, 1, 2, 3], 'b': [2], 'd': [3]},
          {'a': [3, 5], 'c': [4, 1, 2], 'd': [4]}], {'a': [3, 5], 'd': []}),
        ([{'a': [1, 2, 3], 'b': [3, 1, 2], 'c': [2, 3, 1]},
          {'a': [3, 2, 1], 'b': [4, 3, 2], 'd': [1, 3, 2]}], {'a': [1, 2, 3], 'b': [2, 3]})
    )
    @unpack
    def test(self, dictList, expected):
        return self.do_test(dictList, expected)


# The tests are performed either by running program.py or by calling pytest from the directory
if __name__ == '__main__':
    Test.main()
