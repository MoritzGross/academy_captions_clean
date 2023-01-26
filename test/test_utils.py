"""
nice docstring
"""

from utils import format_float_to_time


def test_format_float_to_time():
    """test for utils"""

    assert format_float_to_time(81.34) == '00:01:21,340'
