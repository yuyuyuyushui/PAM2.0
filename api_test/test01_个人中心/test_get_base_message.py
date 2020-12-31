import pytest
tenantId='e72bb65093868065a8b035ea984a4653'
def test_get_base_message(pam):
    result = pam.personnal.Get_basic_information('e72bb65093868065a8b035ea984a4653')
    print(result.response)
if __name__ == "__main__":
    pytest.main(["-s", "test_get_base_message.py"])