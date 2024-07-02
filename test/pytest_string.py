#pytest_string.py
import pytest
from package.calculate_string import calculate_string

@pytest.mark.parametrize("name_string,expected_result" , [
        ("Hello",5),
        ("Bye",3),
        ("123rt",5),
        ])
      
def test_len_string(name_string,expected_result):
    assert calculate_string(name_string)==expected_result
