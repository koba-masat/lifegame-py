import pytest
import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))
from app.app import Sample

def test_sample():
    sample = Sample()
    assert 3 == sample.calcAdd(1, 2)
