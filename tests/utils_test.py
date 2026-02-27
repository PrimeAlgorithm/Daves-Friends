"""
Tests the utilities.
"""

from utils.utils import mention


def test_mention():
    """
    Makes sure that formatting Discord mentions works correctly.
    """
    assert mention(20) == "<@20>"
