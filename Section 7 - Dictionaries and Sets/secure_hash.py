import hashlib

# All python distributions have these
print(sorted(hashlib.algorithms_guaranteed))
# These are all available to us, but might not be in all python versions
print(sorted(hashlib.algorithms_available))


python_programme = """for i in range(10):
print(i)
"""
print(python_programme)

#Use the encode bit to encode strings as a byte array, cant encode the string itself
# for b in python_programme.encode('utf8'):
#     print(b, chr(b))

original_hash = hashlib.sha256(python_programme.encode('utf8'))
print(f"SHA256: {original_hash.hexdigest()}")
python_programme += "print('code change')"
print(python_programme)

new_hash = hashlib.sha256(python_programme.encode('utf8'))
print()
print(f"SHA256: {new_hash.hexdigest()} ")

if new_hash.hexdigest() == original_hash.hexdigest():
    print("The code has not been modified")
else:
    print("The code has been modified")