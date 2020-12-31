import pytest
from pam import *
url = 'https://10.11.220.143'
token='a0e87043cbaa5923dcdc90a55b22fbbf'

@pytest.fixture(scope="session")
def pam():
    yield Pam(url,token=token)