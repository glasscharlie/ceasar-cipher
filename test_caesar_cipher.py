from caesar_cipher import encrypt, decrypt

def test_encrypt():
    string = 'test string see how it goes'
    actual = encrypt(string, 3)
    expected = 'whvwqvwulqjqvhhqkrzqlwqjrhv'
    assert actual == expected

def test_decrypt():
    string = encrypt('teststringseehowitgoes', 3)
    actual = decrypt(string, 3)
    expected = 'teststringseehowitgoes'
    assert actual == expected