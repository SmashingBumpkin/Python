import testlib
import isrecursive
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, path, expected):
        try:
            isrecursive.decorate_module(program)
            program.ex9(path)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)
        
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.ex9(path)
        self.assertEqual(type(result), list, "Bisogna restituire una lista/The returned value is not a list")
        self.assertEqual(result, expected, "Il valore di ritorno {result} non e' quello atteso {expected}/The result should be {expected} instead of {result}")
    
    @data(  ('Informatica/Software', [('BasiDati', 0), ('SistemiOperativi', 287), ('Software', 10)]),
            ('Informatica/Hardware', [('Architetture', 12), ('Hardware', 0), ('Processori', 0), ('RISC', 5)]),
            ('Informatica', [('Architetture', 12), ('BasiDati', 0), ('Hardware', 0), ('Informatica', 23), ('Processori', 0), ('RISC', 5), ('SistemiOperativi', 287), ('Software', 10)])
    )
    @unpack
    def test(self, path, lista):
        return self.do_test(path, lista)
    

# The tests can be performed running program.py or calling pytest in the directory
if __name__ == "__main__":
    Test.main()
