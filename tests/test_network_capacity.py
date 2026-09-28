import pytest

from network_capacity import aws_usable_ipv4_addresses


def test_slash_24():
    assert aws_usable_ipv4_addresses(24) == 251

    
def test_slash_28():
    assert aws_usable_ipv4_addresses(28) == 11


def test_invalid_prefix():
    with pytest.raises(ValueError):
        aws_usable_ipv4_addresses(29)