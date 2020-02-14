import pytest
from caesar_cipher import encrypt, decrypt
import random

def test_encryption():
    sent = 'The rain in Spain falls mainly on the plain.'
    expected = 'vjg tckp kp urckp hcnnu ockpna qp vjg rnckp.'
    assert encrypt(sent, 2) == expected

def test_decryption_known():
    expected = 'the rain in spain falls mainly on the plain.'
    encrypted = 'vjg tckp kp urckp hcnnu ockpna qp vjg rnckp.'
    assert decrypt(encrypted) == expected

def test_decrypt_random():
    sent = 'Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much'
    encrypted = encrypt(sent, random.randint(1,26))
    assert sent == decrypt(encrypted)