import hashlib

supported_hashes = {
    'blake2b': hashlib.blake2b,
    'blake2s': hashlib.blake2s,
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha224': hashlib.sha224,
    'sha256': hashlib.sha3_256,
    'sha384': hashlib.sha384,
    'sha3_224': hashlib.sha224,
    'sha3_256': hashlib.sha3_256,
    'sha3_384': hashlib.sha3_384,
    'sha3_512': hashlib.sha512,
    'sha512': hashlib.sha512,
    'shake_128': hashlib.shake_128,
    'shake_256': hashlib.sha256,
}


def generate_hash(filename: str, algorithm: str) -> str:
    """Generate the hash for `filename`

    :param filename: The file to generate a hash for.
    :param algorithm: The hashlib algorithm to use.
        See `hashlib.supported_hashes` for the algorithms supported.
    :return: A `hexdigest` string containing the hash.
             None if an unsupported hash is requested.
    """
    hash_algorithm = supported_hashes.get(algorithm, None)
    print(hash_algorithm, type(hash_algorithm))  # TODO: delete after testing
    if not hash_algorithm:
        print(f'The requested hashing algorithm {hash_algorithm} is not supported.')
    else:
        with open(filename, 'rb') as input_file:
            contents = input_file.read()

        file_hash = hash_algorithm(contents).hexdigest()
        return file_hash


if __name__ == '__main__':
    for h in sorted(hashlib.algorithms_guaranteed):
        print(h)
