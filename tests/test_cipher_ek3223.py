from cipher_ek3223 import cipher_ek3223
import pytest

def test_cipher():
    example = 'broski'
    expected = 'csptlj'
    actual = cipher_ek3223.cipher(example, 1)
    assert actual == expected

def test_backwards_cipher():
    example = 'hubbabubba'
    expected = 'gtaaZataaZ'
    actual = cipher_ek3223.cipher(example, -1)
    assert actual == expected

def test_cipher_symbols():
    example = '!@#$%^&* *&^%$#@!'
    expected = '!@#$%^&* *&^%$#@!'
    actual = cipher_ek3223.cipher(example, 10)
    assert actual == expected
