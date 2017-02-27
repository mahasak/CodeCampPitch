from nose import with_setup
from sample_math import multiply

def setup():
    pass
 
def teardown():
    pass
 
@with_setup(setup, teardown)
def test_numbers_3_4_pass():
    assert multiply(3,4) == 12 

@with_setup(setup, teardown)
def test_numbers_3_4_failed():
    assert multiply(3,4) == 13