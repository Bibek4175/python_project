import pytest
from tempfile import NamedTemporaryFile
import json
from package.append import append_json


@pytest.fixture

def temp_file():
    temp_file = NamedTemporaryFile('w+t')
    yield temp_file.name
    temp_file.close()


def test_append_json(temp_file):
    key = "u1"
    initial_data = {key:[1,2,3]}
    new_value = 6
    with open(temp_file,"w",encoding='utf-8') as file:
        json.dump(initial_data,file)
    
    append_json(temp_file,new_value,key)

    with open(temp_file,"r", encoding='utf-8') as file:
        updated_data = json.load(file)

    assert updated_data=={key:[1,2,3,6]}       

if __name__ == "__main__":
    pytest.main()
