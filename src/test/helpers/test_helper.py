
import string
import random

class TestHelper:
    
    @staticmethod
    def random_string(stringLength=10) -> str:
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    
    @staticmethod
    def list_of_strings():
        """ Returns an array with lots of extreme string cases"""
        file = "src/test/fixtures/extreme_cases.csv"
        with open(file,'r') as r:
            return [ln.replace('\n', '') for ln in r]