import unittest

from bencode import bencode, bdecode

class BencodeBdecodeTests(unittest.TestCase):
    def test_bencode_list(self):
        data = [1, 2, 3]
        encoded = bencode(data)
        self.assertEqual(encoded, 'li1ei2ei3ee')

    def test_bencode_string(self):
        data = 'hello'
        encoded = bencode(data)
        self.assertEqual(encoded, '5:hello')

    def test_bencode_integer(self):
        data = 42
        encoded = bencode(data)
        self.assertEqual(encoded, 'i42e')

    def test_bencode_dict(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        encoded = bencode(data)
        self.assertEqual(encoded, 'd4:key16:value14:key26:value2e')

    def test_bdecode_list(self):
        encoded = 'l3:1i2ei3ee'
        decoded = bdecode(encoded)
        self.assertEqual(decoded, [1, 2, 3])

    def test_bdecode_string(self):
        encoded = '5:hello'
        decoded = bdecode(encoded)
        self.assertEqual(decoded, 'hello')

    def test_bdecode_integer(self):
        encoded = 'i42e'
        decoded = bdecode(encoded)
        self.assertEqual(decoded, 42)

    def test_bdecode_dict(self):
        encoded = 'd4:key15:value14:key25:value2e'
        decoded = bdecode(encoded)
        self.assertEqual(decoded, {'key1': 'value1', 'key2': 'value2'})

if __name__ == '__main__':
    unittest.main()