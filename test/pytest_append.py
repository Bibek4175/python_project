import pytest
import json
from package.append import append_json
from tempfile import NamedTemporaryFile

@pytest.fixture
def test_json1():
    return {"name": "Ram", "age": 30}

@pytest.fixture
def test_json2():
    return {"name": "Shyam", "age": 25}

@pytest.fixture
def temp_file():
    # Create a temporary file
    temp_file = NamedTemporaryFile('w+t')
    yield temp_file.name
    temp_file.close()

def test_append_json(test_json1, test_json2, temp_file):
    # Append the first content to file
    append_json(temp_file, test_json1)
    
    # Append the second content to file
    append_json(temp_file, test_json2)


    with open(temp_file, 'r', encoding='utf-8') as file:
        content = file.readlines()

    # Convert each line back to JSON
    json_content = [json.loads(line) for line in content]

    
    assert json_content == [test_json1, test_json2]

if __name__ == "__main__":
    pytest.main()

