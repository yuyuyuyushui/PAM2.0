import pytest
from pam import *
url = ''
token=''

@pytest.fixture(scope="session")
def pam():
    yield Pam(url,token=token)