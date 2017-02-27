from sample_math import multiply

def test_numbers_3_4_pass():
    assert multiply(3,4) == 12 

def test_numbers_3_4_failed():
    assert multiply(3,4) == 13