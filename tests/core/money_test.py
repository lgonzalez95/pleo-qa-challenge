import logging
import unittest
from flaskr.core import money
from tests.helpers.test_helper import TestHelper

logging.basicConfig(filename='logging.log',level=logging.DEBUG)


def test_format_int():
     expected_value = "2.00"
     test_value = 2
     assert money.format_money(test_value) == expected_value

def test_format_float():
     expected_value = "2.12"
     test_value = 2.12312
     assert money.format_money(test_value) == expected_value

def test_format_string():
     expected_value = "12 878 712.12"
     test_value = "12878712.12312"
     assert money.format_money(test_value) == expected_value

def test_format_random_string_with_alpha():
     test_random = TestHelper.random_string()
     assert money.format_money(test_random) == ""

def test_format_with_boundaries():
     tests = [(-1123.222,"-1 123.22"),(-1,"-1.00"),(0,"0.00"),(99999.99999,"100 000.00")]
     for test, expected in tests:
          assert money.format_money(test) == expected

def test_format_with_big_list_of_nasty_strings():    
     """This test validates that there are no exceptions thrown and all results are of type str"""
     list_of_strings= TestHelper.list_of_strings()
     results = set()
     try:
          for test_value in list_of_strings:        
               result = money.format_money(test_value)
               if type(result) != str:
                    result.add({"value":test_value, "result":result})
     except Exception:
        assert False

     if len(result) > 0:
          for res in results:
              print(f"Failed Value {res}")
          print(f"Fallo el test {res}")
          assert False
     
