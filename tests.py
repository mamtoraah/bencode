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

    def test_bencode_nested(self):
        data = {
            'string': 'Hello, World!',
            'integer': 42,
            'list': [1, 2, 3],
            'dict': {'key': 'value'},
        }
        encoded = bencode(data)
        encoded_val = "d4:dictd3:key5:valuee7:integeri42e4:listli1ei2ei3ee6:string13:Hello, World!e"
        self.assertEqual(encoded, encoded_val)

    def test_bdecode_nested(self):
        encoded_val = "d4:dictd3:key5:valuee7:integeri42e4:listli1ei2ei3ee6:string13:Hello, World!e"
        decoded = bdecode(encoded_val)
        data = {
            'string': 'Hello, World!',
            'integer': 42,
            'list': [1, 2, 3],
            'dict': {'key': 'value'},
        }
        self.assertEqual(decoded, data)

    def test_bdecode_list(self):
        encoded = 'li1ei2ei3ee'
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
        encoded = 'd4:key16:value14:key26:value2e'
        decoded = bdecode(encoded)
        self.assertEqual(decoded, {'key1': 'value1', 'key2': 'value2'})


if __name__ == '__main__':
    unittest.main()
