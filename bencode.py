from typing import Union

BencodeType = Union[str, list, int, dict]

def bencode(obj: BencodeType) -> str:
  """
  Encode the given object into a bencoded string.

  Bencoding is a simple data serialization format used in BitTorrent.
  This function supports encoding integers, strings, lists, and dictionaries.

  Args:
    obj (BencodeType): The object to be encoded.

  Returns:
    str: A bencoded string representation of the object.

  Raises:
    TypeError: If the object type is not supported.

  """
  if isinstance(obj, int):
    return f"i{obj}e"
  elif isinstance(obj, str):
    return f"{len(obj)}:{obj}"
  elif isinstance(obj, list):
    return f"l{''.join(bencode(item) for item in obj)}e"
  elif isinstance(obj, dict):
    return f"d{''.join(bencode(key) + bencode(value) for key, value in obj.items())}e"
  else:
    raise TypeError(f"Unsupported type: {type(obj)}")


def bdecode(data: str) -> BencodeType:
  """
  Decode a bencoded string and return the corresponding Python object.

  Args:
    data (str): The bencoded string to decode.

  Returns:
    BencodeType: The decoded Python object.

  """
  def parse_integer(data, pos):
    pos += 1
    end = data.index("e", pos)
    num = int(data[pos:end])
    return num, end + 1

  def parse_string(data, pos):
    colon = data.index(":", pos)
    length = int(data[pos:colon])
    start = colon + 1
    end = start + length
    string = data[start:end]
    return string, end

  def parse_list(data, pos):
    pos += 1
    result = []
    while data[pos] != ord("e"):
      item, pos = parse_func.get(data[pos], parse_string)(data, pos)
      result.append(item)
    return result, pos + 1

  def parse_dict(data, pos):
    pos += 1
    result = {}
    while data[pos] != ord("e"):
      key, pos = parse_string(data, pos)
      print(f"{data=}, {pos=}")
      value, pos = parse_func.get(data[pos], parse_string)(data, pos)
      result[key] = value
    return result, pos + 1

  parse_func = {
    "i": parse_integer,
    "l": parse_list,
    "d": parse_dict,
  }

  return parse_func.get(data[0], parse_string)(data, 0)[0]


if __name__ == "__main__":
  data = {
    "string": "Hello, World!",
    "integer": 42,
    "list": [1, 2, 3],
    "dict": {"key": "value"},
  }

  encoded = bencode(data)
  print(encoded)

  decoded = bdecode(encoded.encode())
  print(decoded)