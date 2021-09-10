import sys

import pytest

sys.path.append('..')
print(sys.path)



@pytest.mark.parametrize('name',['阿里巴巴','腾讯企鹅'])
def test_encode(name):
    print(name)